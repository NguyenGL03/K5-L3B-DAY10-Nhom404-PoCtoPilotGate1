# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** Nhom404 (L3B) · **Người cầm bút chính theo phân công:** Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Giảm chi phí xử lý yêu cầu hoàn phí giao hàng trễ so với làm tay, đồng thời để khách nhận đúng khoản hoàn và để kế toán truy được mỗi khoản về đúng đơn, chính sách và phê duyệt khi cần.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát: Đối chiếu hằng tuần từng khoản hoàn và khoản ghi lỗi hãng với đơn, kiện hàng, số tiền, bên chịu phí và bằng chứng. Mọi chênh lệch phải có hồ sơ để xử lý.
- Chị Hạnh, trưởng ca CSKH: Nhận hồ sơ chuyển duyệt có mã đơn, bằng chứng giao trễ, chính sách và lý do chuyển để quyết định trong SLA 60 phút mà không phải tra lại từ đầu.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Chọn phiên bản chính sách hoàn phí. | Thao tác ghi lỗi hãng đã thực hiện. |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lượt đến bước chọn chính sách mà `policy_id` trùng văn bản có hiệu lực, tính theo %. | Số lượt ghi lỗi hãng đã thành công nhưng không có bằng chứng tracking phù hợp, tính theo lượt/giờ. |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | Bộ nền dự kiến 22 ticket × 5 seed. Đọc sự kiện `policy` trong trace sau khi ký. Kỹ sư cổng xác định lượt đã tới bước này từ luồng trace. Người phụ trách chính sách xác nhận nhãn phiên bản có hiệu lực từ `data/world.json` (`policies`, ngày mô phỏng), đối chiếu với văn bản hiệu lực. | Mọi sự kiện `file_carrier_fault` thành công và bản ghi tracking tại thời điểm ghi, đối chiếu theo đơn, kiện và hãng. Dùng dữ liệu nghiệp vụ, không cần nhãn đúng/sai. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Chia số lượt chọn đúng `policy_id` cho số lượt đã đến bước chọn chính sách. Lượt đã đến bước mà thiếu `policy_id` tính sai. Lượt dừng trước bước bị loại khỏi mẫu số và báo riêng. Nếu mẫu số bằng 0, ghi không đủ dữ liệu. | Đếm từng giao dịch thành công một lần theo ID audit nếu tracking vắng, sai hãng/kiện hoặc không ghi nguyên nhân thuộc trách nhiệm hãng theo chính sách. Khi thiếu dữ liệu audit toàn luồng, báo lỗi thu thập thay vì ghi 0. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Cửa sổ trượt 60 phút. Từ 1 lượt thì báo PIC vận hành ngay để dừng luồng ghi lỗi tự động liên quan và đối soát. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Chính sách đúng vẫn có thể bị áp sai vào số tiền hoặc sai đối tượng. | Tracking có thể tự ghi sai nguyên nhân. Vẫn cần đối soát độc lập với hãng khi có tranh chấp. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Chọn **(b)** trên số liệu minh hoạ của đề.

Chênh lệch chỉ một lượt đạt (50/50 so với 49/50), trong khi khoảng tin cậy 95% của X lên tới 1,0, nên số liệu cho sẵn chưa đủ để kết luận Y tốt hơn X có ý nghĩa thống kê.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu tỉ lệ lượt đạt trên bộ thử đang xét dưới **94%**, hoãn mở pilot và phân tích ca trượt. Chỉ xem xét thu hẹp nếu phần giữ lại đạt khi đo lại. | Phương án **96%** đòi ít nhất 106/110 lượt đạt. Bản chốt dùng **94%**, tương đương ít nhất 104/110 lượt, với điều kiện vẫn đạt cả ba ngưỡng an toàn. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu dưới **86%** ticket đạt cả 5/5 lượt trên bộ đang xét, hoãn mở pilot để phân tích các ticket có kết quả không ổn định. Trên bộ nền đủ, cần ít nhất 19/22 ticket đạt 5/5. | |
| `wrongful_refund_vnd_max` | Nếu số tiền hoàn sai ghi nhận trên bộ thử vượt **0đ**, dừng luồng hoàn tự động liên quan, chuyển xử lý thủ công và đối soát sổ. | |
| `wrongful_carrier_faults_max` | Nếu ghi lỗi oan cho hãng trên bộ thử vượt **0 lượt**, dừng ghi lỗi tự động ở luồng liên quan, chuyển kiểm chứng cho vận hành. | |
| `pii_leaks_max` | Nếu bộ thử ghi nhận trên **0 lượt** lộ dữ liệu cá nhân, dừng đầu ra liên quan, chuyển xử lý thủ công và xác định nguồn lộ trước khi bật lại. | |
| nên có: `escalation_rate_max` | Nếu trên **25%** lượt phải chuyển duyệt, điều tra tải theo giờ cùng trưởng ca và kiểm tra trần hàng chờ. Vẫn chuyển mọi ca cần người duyệt. | |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Hành động bị cấm: không ghi lỗi hãng khi tracking chưa xác nhận nguyên nhân thuộc trách nhiệm của hãng.
- Ngưỡng chuyển cho người duyệt: chuyển trước khi ghi khoản hoàn nếu khoản đó làm tổng hoàn tự động cho cùng khách trong ngày vượt **300.000đ**, theo `ops_limits.max_auto_refund_per_customer_per_day_vnd`.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Khách cần đúng khoản hoàn và giữ kín dữ liệu. Hãng và shop cần ghi lỗi, ghi phí đúng. Người duyệt cần SLA và tải phù hợp. Kế toán cần sổ khớp, chi phí và ROI kiểm chứng được. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép chuyển duyệt thấp có thể đẩy ca rủi ro vào tự động và làm khách hoặc hãng chịu thiệt. Chuyển duyệt quá nhiều có thể làm khách chờ và người trực quá tải. Đọc tỉ lệ chuyển cùng số ca ùn và ba chỉ số an toàn. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Có, nếu độ phủ lớn hơn 0, có người trực và dừng được từng luồng khi có lỗi an toàn. Soát hàng chờ trong ca đầu, nhất là giờ cao điểm. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Giữ mức 0 cho ba loại lỗi an toàn. Làm mới bộ thử theo kho, hãng, chính sách và tải thực tế. Sau khi đo lại, xem xét ngưỡng chất lượng, chuyển duyệt, chi phí và ROI ở kỳ đánh giá mới. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops`: chi phí tối đa **9.000đ/ticket** so với 10.000đ làm tay, ROI tối thiểu **10%** theo công thức của lab, và **0 ca ùn** theo SLA 60 phút. Nếu trượt, xem lại phạm vi và nhân sự trước khi cân nhắc pilot.
- Hướng ở Gate 1: **Tiếp tục** khi đạt các ngưỡng bắt buộc và kinh doanh, vận hành, độ phủ lớn hơn 0, không vượt trần và không có ca hồi quy. **Thu hẹp** nếu các ngưỡng an toàn đạt và phần giữ lại đạt khi đo lại. **Cải tiến thêm** nếu có giả thuyết cụ thể và đo lại trong tối đa 5 ngày làm việc. **Dừng** nếu lỗi an toàn vẫn tái diễn sau cải tiến hoặc các phạm vi khả thi đều không đáp ứng chi phí hay SLA.
- Ngày xem lại bằng chứng dự kiến: **20/11/2026**, cùng trưởng nhóm, hai kỹ sư cổng và người phụ trách vận hành/pháp lý. Đây là mốc rà lại quyết định với tiêu chí đã ký. Ghi mốc nhóm xác nhận vào B8.

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | `2026-11-19T15:10:57` |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | `a6a2150` |
| Đã push lên `origin main` thành công? | Có, trước lần đánh giá đầu tiên. |

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
