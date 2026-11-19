# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): `Nhom404`
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Nhom404-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S4`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; bàn 3 người thì để trống dòng 4. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Khương Hoàng Nguyên   | 2A202603987  | Sản phẩm và kinh doanh    | x           |
|   2 | Vũ Đình Huy          |2A202603985      |Kỹ sư cổng(code)     |             |
|   3 | Cao Thanh Tùng     | 2A202603982  | Kỹ sư cổng (test)    |             |
|   4 | Nguyễn Quang Tiệp | 2A202603946 | Vận hành và pháp lý |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Tài liệu tham khảo chung từ Lab 9

- [Eval Card của trợ lý hoàn tiền LogiX-VN](docs/day09/eval_card.md)
- [PRD v1.1 của trợ lý hoàn tiền LogiX-VN](docs/day09/PRD_v1.1.md)

Nguồn chung là [bản Day 09 tại commit `a00a47e`](https://github.com/NguyenGL03/K5-DAY09-2A202603987-KhuongHoangNguyen-Evaluation-and-Failure-Analysis/tree/a00a47e6aee6078af573771ffcf511eabe850752/docs).

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## KhuongHoangNguyen-2A202603987

### Phần việc phụ trách

Trưởng nhóm, vai Sản phẩm và kinh doanh. Phụ trách Phiếu A và bản tiêu chí đã ký, câu 2.3 về dữ liệu, phần kinh doanh ở 2.9 và 3.5, specification ở 3.2 và quyết định Gate 1 ở B8/C12.

### Đóng góp cụ thể

- Lập bảng phân công, chọn bộ tài liệu Lab 9 dùng chung, chốt và ký tiêu chí trước lần đánh giá đầu tiên.
- Viết bản đồ dữ liệu và ví dụ thay đổi phiên bản chính sách ở B3. Chốt v1 ở B8 dựa trên report `prepared` và hai ticket hiểm.
- Sau S4, kiểm tra tác động của trần 300.000đ và phương án hai người duyệt. Ghi quyết định v2 **Cải tiến thêm** vì cần xác nhận ca trực thật trước khi mở toàn bộ phạm vi.
- Dùng AI để đọc đề, soạn và soát phiếu, đề xuất ngưỡng và phương án S4, tái lập hai lần chạy B0. Nhóm rà và chốt các ngưỡng, cấu hình và quyết định dựa trên report.

### Bằng chứng

- `a6a2150` ký tiêu chí, `d1714f0` hoàn thành Phiếu A, `54abd2f` cập nhật câu 2.3 và `330f323` chốt cổng vòng 1 cùng v1.
- `68b424b` cập nhật trần hoàn và năng lực duyệt cho S4. Phiếu C mục C12 dẫn report `R-S4-grade-20261119-175234-988b9c` và bảng đo ở C0.

### Exit ticket

- Điều học được: hạ trần ngân sách có thể chuyển thêm ca sang người duyệt. Trong S4, hạ trần giúp giảm hoàn tự động còn 292.000đ nhưng với một người trực vẫn có 5 ca ùn.
- Điều còn chưa chắc: hai người trực thật có giữ được SLA 60 phút khi lượng ticket dồn vào giờ sale hay không. Cần xác nhận lịch trực và đo thời gian chờ theo giờ trước khi mở phạm vi 100%.

## VuDinhHuy-2A202603985

### Phần việc phụ trách

Vai Kỹ sư cổng (code). Phụ trách thiết kế, viết và kiểm thử các cổng phòng ngừa cấp hệ thống độc lập ngoài prompt/model trong `lab10/guards.py`; câu 2.6 / Phiếu B mục B7.1 (bảng cổng phòng ngừa vòng 1); câu 2.7 / Phiếu B mục B7.2 (hai bước tránh rò rỉ dữ liệu); phối hợp câu 2.8 / B7.3 (behavioral testing qua `--adhoc`); câu 3.5 / Phiếu C mục C7 (hoàn thiện code xử lý sự cố S4 và tích hợp hệ thống).

### Đóng góp cụ thể

- Thiết kế và cài đặt 3 cổng phòng ngừa vòng 1 trong `lab10/guards.py`: ghim phiên bản chính sách hiệu lực theo ngày `as_of` trong `pre_guard`; kiểm tra quyền lợi theo tracking DB, chặn hoàn sai, hạ số tiền đúng chính sách và kiểm tra trần ngân sách ngày trong `write_gate` (`issue_refund`); chặn phạt oan hãng vận chuyển, đồng bộ kiện/hãng/ngày trễ và chống ghi trùng trong `write_gate` (`file_carrier_fault`); lọc dữ liệu cá nhân trong `write_gate` (`notify_carrier`). Khắc phục triệt để lỗi `T-002@55`.
- Soạn thảo câu trả lời 2 bước tránh rò rỉ dữ liệu ở B7.2; phối hợp chạy và đối chiếu 2 ticket hiểm ad-hoc ở B7.3.
- Xử lý sự cố S4 (vòng 2): phân tích trace vé lỗi khi LLM gặp sự cố 429 và fail-open; hoàn thiện code `guards.py` để khóa cứng bên chịu phí `payer = "LOGIX"` chống lách sang shop và đồng bộ số ngày trễ thực tế DB; bảo đảm hệ thống chặn 100% lệnh hoàn sai/phạt oan mà không gây hồi quy trên bộ nền.
- Hoàn thiện nội dung kỹ thuật nhánh [3] Bảng C7 và cập nhật nhật ký lượt chạy trong `templates/form-c-incident.md`.

### Bằng chứng

- Commit: `a7c4253` (hoàn thiện code `guards.py` và C7 cho sự cố S4), `330f323` (chốt cổng vòng 1).
- Mã lần chạy:
  + `R-base-after-20261119-160227-5b7827` (mốc after vòng 1, 110/110 đạt, pass rate 1.0).
  + `R-base-after-20261119-171837-988b9c` (kiểm tra hồi quy bộ nền sau khi hoàn thiện code, 110/110 đạt, 0 ca hỏng mới).
  + `R-S4-after-20261119-171842-988b9c` (mốc after S4, 205/205 đạt, 0 ca ùn, hoàn tự động 292.000đ ≤ 300.000đ, ROI 0.40).
  + `R-S4-grade-20261119-171849-988b9c` (kết quả tự kiểm tra toàn diện S4 đạt `PASS-VISIBLE`).
- Dòng trong phiếu: Phiếu B mục B7.1, B7.2, B7.3; Phiếu C mục C0 (lượt 6) và mục C7 (nhánh [3]).

### Exit ticket

- Điều học được: Cổng cấp hệ thống (system-level safety gate) nằm ngoài prompt/LLM là chốt chặn bắt buộc để bảo vệ các bất biến nghiệp vụ. Khi LLM gặp sự cố kỹ thuật (lỗi 429 fail-open) hoặc bị tấn công prompt injection, code guard dựa trên Ground Truth (tracking DB, bảng chính sách có hiệu lực) sẽ ngăn chặn hoàn toàn các lệnh xuất tiền sai hoặc phạt oan đối tác mà model/prompt không thể đảm bảo.
- Điều còn chưa chắc: Cơ chế chuyển duyệt (`Verdict.escalate`) khi chạm trần ngân sách ngày tuy bảo vệ an toàn dòng tiền nhưng lại chuyển rủi ro sang hàng chờ của con người. Nếu lượng vé tăng vọt trong giờ cao điểm mà không có cơ chế điều phối tải động, hàng chờ vận hành vẫn có nguy cơ vượt ngưỡng SLA 60 phút.

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
