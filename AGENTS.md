# Quy tắc làm việc HW03

- Đọc `README.md`, `docs/requirements.md` và hướng dẫn `../HUONG_DAN_HW03.md` trước khi làm tiếp. Scope hiện có là FR-04 + FR-11 trên `/profile`; không tự chuyển sang flow mua hàng.
- Mọi prompt người dùng và phản hồi AI phải được lưu nguyên văn, kèm timestamp thật và tên công cụ, vào `ai/prompt_log.md`. Không ghi suy luận nội bộ hay chỉ dẫn hệ thống. Không dựng lại hội thoại chưa có dữ liệu gốc.
- Format log Markdown đơn giản: mỗi lượt chỉ có số thứ tự, Tool, thời gian gửi prompt (giờ Việt Nam), Prompt nguyên văn, Output nguyên văn. Gom các phản hồi công khai của AI vào Output của prompt tương ứng. Không thêm ID, session, dòng nguồn, thời gian từng output hay ngữ cảnh tự động vào Markdown.
- Mỗi lượt chat: chạy `python scripts/export_chat_log.py` để đồng bộ. Để lưu cả câu trả lời cuối sau khi gửi, bật `python scripts/export_chat_log.py --follow` bằng tiến trình ẩn nếu chưa có tiến trình tương ứng. Tiến trình tự dừng sau 30 phút không có tin nhắn mới; xem `ai/README.md`. Khi sang chat mới, dùng `--session` trỏ đúng bản ghi chat mới, không dùng nhầm chat cũ.
- Mỗi bước có sản phẩm thực phải có commit riêng, message mô tả chính xác việc đã làm. Không tạo lịch sử giả cho bước chưa chạy. Sau commit, chạy `python scripts/export_git_log.py`.
- Giữ source SUT tại `../eshop-sut`, tách khỏi repo bài nộp. Không sửa SUT để làm kết quả Passed. Không reset database tùy tiện.
- Chưa thực thi thì chưa được ghi Passed/Failed. Không tạo participant, phản hồi, recording hoặc ảnh chạy test giả.
- Theo AI-01 §11: bug report do sinh viên viết 100%; AI không nháp mô tả lỗi. Verdict, lý do và bản sửa của sinh viên trong audit phải do sinh viên review thật; không tự xác nhận thay.
- Chưa có MSSV, họ tên, email sinh viên, deadline hoặc remote Git thì ghi chưa cung cấp, không suy đoán. Trước nộp mới hoàn thiện PDF, Excel, evidence, chữ ký và ZIP theo đề.
