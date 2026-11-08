# HW03 — GUI & Usability

Trạng thái ngày 08/11/2026: đã khảo sát sơ bộ Profile, giữ 52 mục nháp có ID nguồn, rà kỹ thuật và hợp nhất thành checklist thiết kế 44 mục. Bản chuẩn đề xuất có Markdown, Excel và PDF, chờ sinh viên review. Chưa thực thi checklist chính thức hoặc tổ chức phiên usability.

## Phạm vi theo hướng dẫn đã có

- Trang chính `/profile`: hồ sơ cá nhân (FR-04) và lịch sử đơn hàng (FR-11), là **một trang** có hai phần.
- Flow usability: đã đăng nhập → tìm hồ sơ → cập nhật liên hệ/địa chỉ → lưu → mở lại/tải lại để kiểm tra.
- Nền tảng dự kiến: Chrome/Windows, Firefox/Windows, Safari/macOS; thực tế chưa được xác minh trong lượt làm này.
- Source SUT nằm ngoài repo tại `../eshop-sut`; HEAD quan sát: `85af3ba875c88283615e22cb108f13e2fccaf0e9`. Có thay đổi cục bộ database và lockfile, backend có node_modules; HEAD không đại diện toàn bộ trạng thái làm việc.

## Tài liệu

- [Yêu cầu và đầu ra cần nộp](docs/requirements.md)
- [Thành phần, trạng thái và 52 nội dung kiểm tra FR-04/FR-11 theo IA](docs/profile_inventory.md)
- [Checklist chuẩn đề xuất: 44 mục có ID, thao tác, expected và căn cứ](outputs/HW03-01a1ba88/GUI_Checklist.md)
- [Excel checklist, bảng thực thi ba nền tảng và test summary](outputs/HW03-01a1ba88/GUI_Checklist.xlsx)
- [Bản PDF của checklist](output/pdf/GUI_Checklist.pdf)
- [Review trùng/căn cứ/kỳ vọng và mapping 52 mục nháp](docs/checklist_review.md)
- [Prompt và phản hồi AI nguyên văn](prompt_log.md)
- [Khung AI Audit — chờ sinh viên review](ai_audit.md)
- [Cách đồng bộ nhật ký](docs/chat_logging.md)
- Lịch sử commit dạng text: sẽ xuất `git_commit_log.txt` khi hoàn thiện bài.

## Test summary hiện tại

| Chỉ số trong repo này | Kết quả |
| --- | ---: |
| Màn hình / flow đã kiểm thử | 0 / 0 |
| Checklist thiết kế đề xuất / đã thực thi | 44 / 0 |
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
