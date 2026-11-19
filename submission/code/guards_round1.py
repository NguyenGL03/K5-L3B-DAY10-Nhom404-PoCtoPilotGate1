"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Cổng 0: Ghim phiên bản chính sách có hiệu lực theo as_of (tránh drift do index_active cập nhật chậm)
    policies = ctx.tools.lookup_policies()
    policy = H.effective_policy(policies, ctx.as_of)
    if policy:
        return Verdict.allow(policy_id=policy["policy_id"])
    return Verdict.allow()


def write_gate(ctx, action):
    tool = action.get("tool")

    # Cổng 1: Chống tin lời khách đè database khi hoàn tiền (Fix T-002@55) & Giới hạn thiệt hại
    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if not order:
            return Verdict.escalate("Không tìm thấy đơn hàng trong hệ thống")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay_days = H.db_delay_days(parcel, ctx.as_of)
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        cause = parcel.get("delay_cause")
        entitled_vnd = H.entitlement_vnd(policy, order, delay_days, cause)

        # Nếu thực tế DB không đủ điều kiện hoàn mà agent đòi hoàn -> Từ chối lệnh hoàn
        if entitled_vnd == 0 and action.get("amount_vnd", 0) > 0:
            return Verdict.deny("Đơn hàng không đủ điều kiện hoàn tiền theo dữ liệu giao hàng thực tế")

        # Nếu agent hoàn vượt mức quyền lợi được hưởng theo DB -> Điều chỉnh lại số tiền đúng
        if action.get("amount_vnd", 0) > entitled_vnd > 0:
            return Verdict.modify(
                "Điều chỉnh số tiền hoàn về đúng mức quyền lợi theo độ trễ DB",
                amount_vnd=entitled_vnd,
            )

        # Kiểm tra trần ngân sách hoàn tự động trong ngày
        cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
        if cap is not None and not action.get("approval_id"):
            spent = ctx.tools.auto_refund_today_vnd()
            if spent + action.get("amount_vnd", 0) > cap:
                return Verdict.escalate("Vượt trần ngân sách hoàn tự động trong ngày, chờ người duyệt")

    # Cổng 2: Chống quy lỗi oan cho hãng vận chuyển (Fix T-002@55 & HAZOP B4)
    elif tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        if not order:
            return Verdict.escalate("Không tìm thấy đơn hàng khi ghi lỗi hãng")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay_days = H.db_delay_days(parcel, ctx.as_of)
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)

        # Kiểm tra căn cứ lỗi theo tracking DB
        if not H.carrier_at_fault(policy, parcel, delay_days):
            return Verdict.deny("Không đủ căn cứ quy lỗi cho hãng vận chuyển theo tracking database")

        # Đồng bộ đúng kiện hàng và hãng chịu trách nhiệm thực tế
        if (
            action.get("parcel_id") != parcel.get("parcel_id")
            or action.get("carrier_id") != parcel.get("carrier_id")
        ):
            return Verdict.modify(
                "Đồng bộ đúng kiện và hãng chịu trách nhiệm thực tế",
                parcel_id=parcel.get("parcel_id"),
                carrier_id=parcel.get("carrier_id"),
                driver_id=parcel.get("driver_id"),
                delay_days=delay_days,
            )

        # Chống ghi lỗi trùng cho cùng một kiện hàng
        if parcel.get("parcel_id") and ctx.tools.fault_rows(parcel_id=parcel["parcel_id"]):
            return Verdict.deny("Kiện hàng này đã được ghi lỗi hãng trước đó")

    # Cổng 3: Bảo vệ dữ liệu cá nhân (PII) khi gửi thông báo cho bên thứ ba (hãng)
    elif tool == "notify_carrier":
        payload = action.get("payload") or {}
        # Loại bỏ thông tin liên hệ người nhận nếu có trong payload gửi sang hãng
        if "recipient_contact" in payload:
            clean_payload = {k: v for k, v in payload.items() if k != "recipient_contact"}
            return Verdict.modify("Loại bỏ thông tin liên hệ người nhận khỏi thông báo gửi hãng", payload=clean_payload)

    return Verdict.allow()
