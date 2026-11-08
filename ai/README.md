# Nhật ký AI

`prompt_log.md` là bản đọc được; `messages.jsonl` giữ nguyên văn từng tin nhắn user/assistant đã xuất, role, timestamp UTC và giờ Việt Nam. Timestamp lấy trực tiếp từ bản ghi phiên, không gán giờ ước đoán cho prompt.

Log lấy mọi tin nhắn văn bản user và phản hồi công khai assistant trong **đúng chat đã chọn**. Các tin nhắn ngữ cảnh tự động của ứng dụng được giữ ở phần riêng. Không xuất system/developer, suy luận nội bộ, lệnh công cụ hoặc toàn bộ dữ liệu trả về từ công cụ; các file AI tạo được giữ bằng Git và dẫn trong audit. Không quét/xuất chat khác. Chưa nhập lịch sử từ chat cũ đã tạo hướng dẫn/chuyển PDF; cần dữ liệu gốc để bổ sung trung thực.

Đồng bộ thủ công từ thư mục work:

```powershell
python scripts/export_chat_log.py
python scripts/export_git_log.py
```

Lần đầu chỉ định `--session "đường dẫn bản ghi JSONL của đúng chat"`. Cấu hình đường dẫn máy nằm trong `.local/chat_log.json` và không đưa vào Git. Khi mở chat khác, truyền `--session` mới. Log các chat trước trong repo được giữ lại theo session ID.

Theo dõi tin nhắn mới, gồm cả câu trả lời cuối của lượt hiện tại:

```powershell
python scripts/export_chat_log.py --follow
```

Chỉ chạy một tiến trình cho repo. Tiến trình đọc cục bộ mỗi 2 giây, không gửi dữ liệu ra mạng; tự dừng sau 30 phút không có tin nhắn mới. Có thể dừng sớm bằng tạo `.local/stop-chat-log`, hoặc dừng PID trong `.local/chat_logger.pid`. Xóa file stop trước lần bật lại. Để chạy ẩn trên Windows, dùng `Start-Process` với `-WindowStyle Hidden` như đã thiết lập ở lượt khởi tạo.

Sau commit, xuất lại `git_commit_log.txt`; file ghi snapshot SHA cụ thể. Snapshot không thể tự chứa commit đang thêm chính nó. Phản hồi cuối có thể làm log thay đổi sau commit gần nhất; commit phần bổ sung ở bước tiếp theo, không lùi thời gian hoặc sửa lịch sử.

Trước nộp, review dữ liệu cá nhân/bí mật và tạo bản chia sẻ có che thông tin nếu cần, giữ bản gốc riêng; hoàn thiện AI Audit, Disclosure và PDF. Bộ log này chưa thay thế các phần sinh viên bắt buộc tự đánh giá.
