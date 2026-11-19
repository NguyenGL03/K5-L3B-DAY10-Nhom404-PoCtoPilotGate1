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

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
