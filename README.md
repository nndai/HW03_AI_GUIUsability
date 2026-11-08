# HW03 — GUI & Usability

Trạng thái ngày 08/11/2026: đã thiết lập repo/nhật ký AI và khảo sát sơ bộ trang Profile với lịch sử trống/có dữ liệu. Đã lập 52 nội dung cần kiểm tra theo IA-01–04, chờ review thành checklist. Chưa thực thi checklist chính thức hoặc tổ chức phiên usability trong repo này.

## Phạm vi theo hướng dẫn đã có

- Trang chính `/profile`: hồ sơ cá nhân (FR-04) và lịch sử đơn hàng (FR-11), là **một trang** có hai phần.
- Flow usability: đã đăng nhập → tìm hồ sơ → cập nhật liên hệ/địa chỉ → lưu → mở lại/tải lại để kiểm tra.
- Nền tảng dự kiến: Chrome/Windows, Firefox/Windows, Safari/macOS; thực tế chưa được xác minh trong lượt làm này.
- Source SUT nằm ngoài repo tại `../eshop-sut`; HEAD quan sát: `85af3ba875c88283615e22cb108f13e2fccaf0e9`. Có thay đổi cục bộ database và lockfile, backend có node_modules; HEAD không đại diện toàn bộ trạng thái làm việc.

## Tài liệu

- [Yêu cầu và đầu ra cần nộp](docs/requirements.md)
- [Thành phần, trạng thái và 52 nội dung kiểm tra FR-04/FR-11 theo IA](docs/profile_inventory.md)
- [Prompt và phản hồi AI nguyên văn](prompt_log.md)
- [Khung AI Audit — chờ sinh viên review](ai_audit.md)
- [Cách đồng bộ nhật ký](docs/chat_logging.md)
- Lịch sử commit dạng text: sẽ xuất `git_commit_log.txt` khi hoàn thiện bài.

## Test summary hiện tại

| Chỉ số trong repo này | Kết quả |
| --- | ---: |
| Màn hình / flow đã kiểm thử | 0 / 0 |
| Checklist đã thiết kế / thực thi | 0 / 0 |
| Passed / Failed | 0 / 0 |
| Bug đã xác minh và báo cáo | 0 |
| Phiên usability chính thức | 0 / 7 |
| Nền tảng đã chạy Task 1 | 0 / 3 |
| Video demo | Chưa có |

## Tự đánh giá — chưa chấm

| Tiêu chí | Điểm tối đa | Tự chấm |
| --- | ---: | --- |
| Task 1 — GUI checklist | 30 | Chưa chấm |
| Task 2 — Usability | 40 | Chưa chấm |
| Task 3 — Cross-platform | 20 | Chưa chấm |
| Agent Skills | 10 | Chưa chấm |
| Tổng | 100 | Chưa chấm |

Git hiện được quản lý cục bộ; chưa cấu hình remote vì chưa có địa chỉ repo cá nhân. MSSV, họ tên, email sinh viên và deadline Moodle chưa được cung cấp. Đây là hồ sơ khởi động, chưa phải gói nộp hoàn chỉnh.
