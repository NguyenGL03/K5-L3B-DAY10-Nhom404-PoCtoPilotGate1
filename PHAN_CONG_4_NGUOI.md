# Phân công Lab 10 cho nhóm 4 người

Điền tên và MSSV thật vào `TEAM.md` trước khi làm bài. Bảng dưới dùng **Người 1–4** làm chỗ giữ chỗ; Người 1 là trưởng nhóm. Trong `TEAM.md`, ghi Người 2 và 3 cùng vai **Kỹ sư cổng**, kèm chuyên trách như dưới; Người 1 là **Sản phẩm và kinh doanh**, Người 4 là **Vận hành và pháp lý**.

| Người | Vai và trách nhiệm chính | Câu / phiếu | File, kết quả bàn giao |
|---|---|---|---|
| **1 — Trưởng nhóm (Khương Hoàng Nguyên)** | Tạo fork, mời cộng tác viên, kiểm tra repo; dẫn thảo luận chọn eval card và PRD; đặt tiêu chí, chi phí, phạm vi pilot; tổng hợp quyết định v1/v2 và điều phối commit/push | 1.1–1.6 / A1–A5; 2.3, 2.9 / B3, B7.4; 3.2, phần kinh doanh 3.5 / C5, C7; B8, C12 | `config/acceptance_criteria.json`, phần `business` trong `config/operating_gates.json`; bằng chứng ký và mã commit; quyết định có số liệu |
| **2 — Kỹ sư cổng (code)** | Thiết kế và viết 2–3 cổng vòng 1 từ pre-mortem/HAZOP; sửa cổng khi có thẻ sự cố; kiểm tra cổng không làm hỏng ca đúng | 2.6–2.7 / B7.1–B7.2; phần code 3.5 / C7 | `lab10/guards.py`; kết quả unit test, eval bộ nền và sự cố |
| **3 — Kỹ sư cổng (đo kiểm)** | Chạy baseline, gate và trace sau khi tiêu chí đã ký; phân loại lỗi, viết 2 ticket hiểm; theo dõi ba mốc; làm chỉ số mới ở vòng 2; phụ trách demo kỹ thuật | 2.1–2.2 / B0–B2; 2.8 / B7.3; trace 3.1 / C2; 3.6 / C8 | Mã `runs/<mã>` cho base/prepared/after, kết quả trace; `lab10/monitors.py` với hàm mới đăng ký trong `MONITORS` |
| **4 — Vận hành và pháp lý** | HAZOP, checklist có PIC thật, người trực, người duyệt, dữ liệu cá nhân, runbook; phân tích phần riêng của thẻ; gom bài và kiểm đủ thành phần | 2.4, 2.10 / B4–B5, B7.5–B7.6; 3.1, 3.3, 3.7 / C3–C4, C5, C9–C11 | Phần `operations`, `legal` trong `config/operating_gates.json`; runbook; `submission/submission.json`, `submission/manifest.json` |

## Trình tự và điểm giao việc

1. **Phút 0–15:** Người 1 tạo repo, mời cả nhóm và điền thông tin `TEAM.md`. Cả nhóm chạy unit test ban đầu, chọn eval card và PRD chung.
2. **Phút 15–65 — Phiếu A:** Người 1 chủ trì, cả nhóm góp ý ngưỡng và bốn quy tắc quyết định. Ký `config/acceptance_criteria.json`, commit và push **trước bất kỳ lần chạy đánh giá nào**. Ghi giờ ký và mã commit vào A5. Từ đó giữ nguyên file tiêu chí.
3. **Phút 65–85 — Phiếu B, phần tìm rủi ro:** Người 3 chạy base/gate/trace; Người 1 làm bản đồ dữ liệu; Người 4 làm HAZOP và checklist. Cả bốn cùng làm pre-mortem bốn lăng kính, chọn 2–3 rủi ro để chặn. Người 2 nhận các rủi ro đó làm đầu vào viết cổng.
4. **Phút 85–115 — Cổng vòng 1:** Người 2 viết cổng; Người 3 làm ticket hiểm và kiểm thử; Người 1 điền `business`; Người 4 điền `operations`, `legal` và runbook. Cả nhóm so kết quả với tiêu chí đã ký. Người 1 chạy `checkpoint`, Người 3 chạy mốc prepared/gate, cả nhóm thống nhất v1 rồi commit/push. Giữ nguyên hai bản chụp vòng 1.
5. **Phút 125–155 — Nhận và phân tích thẻ:** Một người nhận đúng thẻ Sx, push cho nhóm; Người 3 chạy `grade` **trước khi sửa**, trace ít nhất hai kiểu lỗi; Người 4 làm phần riêng thẻ và HAZOP; Người 1 viết specification; cả nhóm vẽ fault tree có bằng chứng ở từng lá.
6. **Phút 155–200 — Sửa và quyết định v2:** Người 2 sửa code nếu nguyên nhân nằm ở cổng; Người 1 chỉnh phạm vi/chi phí; Người 4 chỉnh người trực, quy trình, pháp lý; Người 3 thêm monitor và chạy lại thẻ lẫn bộ nền. Cả nhóm cập nhật risk register, runbook, checklist và quyết định v2 theo report. Người 4 điền `submission/submission.json` và chạy `check_submission --collect` đến khi báo `ĐỦ THÀNH PHẦN`.
7. **Phút 200–240 — Demo và nộp:** Người 3 trình bày ba mốc base/prepared/after; Người 2 giải thích cổng; Người 4 nói runbook và rủi ro còn lại; Người 1 bảo vệ quyết định. Sau demo, hoàn tác số liệu thay thử, chạy lại `grade` và `check_submission`, commit/push. **Mỗi thành viên tự nộp link repo trên LMS** đúng hạn.

## Việc chung bắt buộc

- Mỗi người tự viết mục `## HoVaTen-MSSV` trong `TEAM.md`: việc phụ trách, đóng góp cụ thể, bằng chứng commit/run/phiếu và exit ticket.
- Ba phiếu `templates/form-a-criteria.md`, `form-b-evaluation-gates.md`, `form-c-incident.md` phải khớp số câu và số liệu trong report; người phụ trách từng mục điền, cả nhóm soát lại.
- Quyết định v2 phải khớp tiêu chí đã ký và report. Khi còn vượt trần hoặc ngưỡng chưa đạt, không chọn **Tiếp tục**. Ghi đủ ba dòng bắt buộc ở C12 và chép đúng vào `submission/submission.json`.

Nguồn phân công: `README.md` (timeline và file được sửa), `problem-set.md` (câu và vai cầm bút), `RUBRIC.md` (điều kiện qua và điểm), `SUBMISSION.md` (nộp bài).
