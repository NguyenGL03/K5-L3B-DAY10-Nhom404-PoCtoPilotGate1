# Phân công Lab 10 cho nhóm 4 người

Điền tên và MSSV thật vào `TEAM.md` trước khi làm bài. Bảng dưới dùng **Người 1–4** làm chỗ giữ chỗ; Người 1 là trưởng nhóm. Trong `TEAM.md`, ghi Người 2 và 3 cùng vai **Kỹ sư cổng**, kèm chuyên trách như dưới; Người 1 là **Sản phẩm và kinh doanh**, Người 4 là **Vận hành và pháp lý**.

| Người | Vai và trách nhiệm chính | Câu / phiếu | File, kết quả bàn giao |
|---|---|---|---|
| **1 — Trưởng nhóm (Khương Hoàng Nguyên)** | Tạo fork, mời cộng tác viên, kiểm tra repo; dẫn thảo luận chọn eval card và PRD; đặt tiêu chí, chi phí, phạm vi pilot; tổng hợp quyết định v1/v2 và điều phối commit/push | 1.1–1.6 / A1–A5; 2.3, 2.9 / B3, B7.4; 3.2, phần kinh doanh 3.5 / C5, C7; B8, C12 | `config/acceptance_criteria.json`, phần `business` trong `config/operating_gates.json`; bằng chứng ký và mã commit; quyết định có số liệu |
| **2 — Kỹ sư cổng (code)** | Thiết kế và viết 2–3 cổng vòng 1 từ pre-mortem/HAZOP; sửa cổng khi có thẻ sự cố; kiểm tra cổng không làm hỏng ca đúng | 2.6–2.7 / B7.1–B7.2; phần code 3.5 / C7 | `lab10/guards.py`; kết quả unit test, eval bộ nền và sự cố |
| **3 — Kỹ sư cổng (đo kiểm)** | Chạy baseline, gate và trace sau khi tiêu chí đã ký; phân loại lỗi, viết 2 ticket hiểm; theo dõi ba mốc; làm chỉ số mới ở vòng 2; phụ trách demo kỹ thuật | 2.1–2.2 / B0–B2; 2.8 / B7.3; trace 3.1 / C2; 3.6 / C8 | Mã `runs/<mã>` cho base/prepared/after, kết quả trace; `lab10/monitors.py` với hàm mới đăng ký trong `MONITORS` |
| **4 — Vận hành và pháp lý** | HAZOP, checklist có PIC thật, người trực, người duyệt, dữ liệu cá nhân, runbook; phân tích phần riêng của thẻ; gom bài và kiểm đủ thành phần | 2.4, 2.10 / B4–B5, B7.5–B7.6; 3.1, 3.3, 3.7 / C3–C4, C5, C9–C11 | Phần `operations`, `legal` trong `config/operating_gates.json`; runbook; `submission/submission.json`, `submission/manifest.json` |

## Trình tự và điểm giao việc

Đọc bảng từ trên xuống. Bốn cột theo người có thể làm song song trong mỗi hàng. Cột cuối ghi các bước phải chạy tuần tự và điểm cần bàn giao trước khi sang hàng tiếp theo.

| Mốc | Người 1 · Sản phẩm và kinh doanh | Người 2 · Kỹ sư cổng, code | Người 3 · Kỹ sư cổng, đo kiểm | Người 4 · Vận hành và pháp lý | Thứ tự và điểm bàn giao |
|---|---|---|---|---|---|
| **0–15 · CP1** | Chuẩn bị fork, quyền cộng tác và bảng `TEAM.md`. | Đọc `guards.py` và phạm vi file được sửa. | Chạy `python -m unittest discover -s tests`, kiểm tra `origin`. | Đọc rubric và xác nhận vai, thông tin thành viên. | Có repo nhóm → kiểm tra clone, danh tính Git, 13 test và bảng thành viên → cả nhóm thống nhất bộ tài liệu Day 09 trong `TEAM.md`. |
| **15–60 · CP2, Phiếu A** | Chủ trì A1–A4. Viết mục tiêu hệ thống (1.1), tiêu chí và quy tắc quyết định (1.6), cập nhật JSON. | Góp ý chọn bước cần đo và các ranh giới đầu ra. | Thiết kế thước đo offline (1.3) và rà công thức. | Viết mục tiêu của kế toán, trưởng ca (1.2) và telemetry (1.4). Rà điều kiện dừng. | Cả nhóm đọc ví dụ CI (1.5), soát Phiếu A và chốt ngưỡng trước khi xem kết quả Day 10. |
| **60–65 · CP2, ký** | Trên `main`, chạy `python -m lab10.criteria sign`. Commit hai tệp với message `Sign acceptance criteria`, push ngay rồi ghi giờ và mã commit vào A5. | Soát ngưỡng bắt buộc và ranh giới đầu ra. | Chờ xác nhận commit đã lên `origin/main`. | Soát ngưỡng vận hành và quy tắc dừng. | Chốt Phiếu A và JSON → ký → commit → push → ghi A5 → báo Người 3 chạy `base`. Giữ nguyên JSON đã ký. |
| **65–85 · CP3, Phiếu B** | Viết bản đồ dữ liệu và ví dụ drift (B3). | Cùng nhóm chọn các rủi ro có thể xử lý bằng cổng. | Chạy `base`, đọc `gate`, trace `T-002@55` và ghi mã lần chạy (B0–B2). | Viết HAZOP và checklist có tên PIC (B4–B5). | Làm phần riêng trước, rồi cả nhóm làm pre-mortem theo bốn lăng kính và chọn 2–3 rủi ro ưu tiên (B6). |
| **85–105 · CP3, cổng vòng 1** | Soạn mục `business` và lý do từng ngưỡng (B7.4). | Viết 2–3 cổng và mô tả cách tránh dùng tập chấm để chỉnh cổng (B7.1–B7.2). | Cùng một người không viết code tạo 2 ticket hiểm (B7.3). Sau khi ghép code và config, chạy thử và kiểm tra hồi quy. | Soạn `operations`, `legal`, runbook phần 1–3 và kịch bản giờ cao điểm (B7.5–B7.6). | Người 1 ghép ba mục của `config/operating_gates.json` sau khi nhận nội dung từ Người 4 → Người 3 kiểm tra bản đã ghép trên bộ nền và ticket hiểm. |
| **105–115 · CP3, quyết định v1** | Chạy `python -m lab10.checkpoint`, tổng hợp quyết định và commit/push. | Kiểm tra bản chụp cổng vòng 1. | Chạy mốc `prepared`, chạy `gate` và gửi mã lần chạy. | Đối chiếu PIC, runbook và ngưỡng vận hành với report. | Chốt bản chụp → chạy `prepared` → đọc `gate` → cả nhóm chốt v1 và ghi B8 → commit/push. Giữ nguyên bản chụp. |
| **125–155 · CP4, phân tích** | Điều phối nhận đúng thẻ Sx và viết specification (C5). | Xác định nguyên nhân kỹ thuật từ trace. | Chạy `grade --incident Sx` trước khi sửa (C0–C1), sau đó trace ít nhất hai kiểu lỗi (C2). | Viết phần riêng nếu thẻ yêu cầu, HAZOP và giả định môi trường (C3–C5). | Nhận đúng thẻ → đo `prepared` trước khi sửa → phân tích → cả nhóm vẽ fault tree với bằng chứng ở từng lá (C6). |
| **155–185 · CP4, sửa và đo lại** | Cập nhật mục `business` nếu cần, ghép config. | Sửa `guards.py` nếu nguyên nhân thuộc cổng, ghi thay đổi vào C7. | Thêm monitor và điền C8, sau đó đánh giá thẻ và bộ nền. | Sửa `operations` hoặc `legal` nếu cần. Dựa vào kết quả cập nhật cây lỗi, risk register, checklist, runbook phần 4–5 (C9–C11). | Ghép code, monitor và config → chạy `after` trên Sx → chạy lại bộ nền → chạy `grade` → cập nhật bằng chứng và rủi ro còn lại. |
| **185–200 · CP5, quyết định v2** | Chủ trì chốt v2 và điền C12, gồm ba dòng bắt buộc. | Đối chiếu biện pháp với nguyên nhân và báo ca còn hỏng. | Cung cấp mã và report của cả ba mốc. | Điền `submission/submission.json` và chạy `check_submission --collect`. | Chốt v2 theo tiêu chí đã ký → chép quyết định và ba dòng từ C12 vào JSON nộp bài → chạy lệnh gom đến khi báo `ĐỦ THÀNH PHẦN`. |
| **200–240 · CP5, demo và nộp** | Trình bày lý do giữ hoặc đổi quyết định, điều phối push cuối. | Giải thích cổng và hỗ trợ chạy ticket phản biện. | Trình bày `base`, `prepared`, `after` và chạy lại `grade` sau demo. | Trình bày runbook và gom lại bài sau demo. | Demo → khôi phục giá trị đã đổi thử → chạy lại `grade` và `check_submission --collect` → push → từng người nộp link repo trên LMS. |

## Việc chung bắt buộc

- Mỗi người tự viết mục `## HoVaTen-MSSV` trong `TEAM.md`: việc phụ trách, đóng góp cụ thể, bằng chứng commit/run/phiếu và exit ticket.
- Ba phiếu `templates/form-a-criteria.md`, `form-b-evaluation-gates.md`, `form-c-incident.md` phải khớp số câu và số liệu trong report; người phụ trách từng mục điền, cả nhóm soát lại.
- Quyết định v2 phải khớp tiêu chí đã ký và report. Khi còn vượt trần hoặc ngưỡng chưa đạt, không chọn **Tiếp tục**. Ghi đủ ba dòng bắt buộc ở C12 và chép đúng vào `submission/submission.json`.

Nguồn phân công: `README.md` (timeline và file được sửa), `problem-set.md` (câu và vai cầm bút), `RUBRIC.md` (điều kiện qua và điểm), `SUBMISSION.md` (nộp bài).
