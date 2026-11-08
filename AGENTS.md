# Quy tắc làm việc HW03

- Đọc README.md và Bao_cao.md. Checklist chính thức duy nhất là checklist/GUI_Checklist.md và Excel/PDF cùng thư mục, bản 2.0, 41 mục liên tục GUI-001–GUI-041; IA-01/02/03/04 = 11/10/9/11.
- ID đã đổi theo yêu cầu người dùng; tra mapping bản 1.1 → 2.0 tại phu_luc/AI_Review.md. Không dùng ID cũ để ghi execution. Không đưa mục bị loại/chưa đủ căn cứ trở lại checklist.
- Scope FR-04 + FR-11 trên /profile, một trang. SUT tại ../eshop-sut. Không sửa nghiệp vụ hoặc reset database để ép Passed.
- Prompt/output công khai lưu nguyên văn tại prompt_log.md, chỉ số/tool/thời gian prompt giờ Việt Nam/prompt/output. Không thêm session/ID kỹ thuật/ngữ cảnh tự động/suy luận nội bộ.
- Mỗi lượt chạy `python .git/hw3-tools/export_chat_log.py`; để ghi cả câu trả lời cuối, bật --follow nếu chưa có logger. Logger tự dừng sau 30 phút không có tin nhắn; state tại .git/chat-log, tool tại .git/hw3-tools. Không tạo lại ai/.local/scripts/output/outputs/docs trong cây nộp.
- Công cụ tạo file lưu nội bộ trong .git/hw3-tools. Khi sửa cập nhật đồng bộ MD/XLSX/PDF và báo cáo; không ghi đè kết quả người dùng đã nhập. Preview ở .git và dọn sau kiểm tra.
- Chưa chạy không gán Passed/Failed; bị blocker ghi Chưa chạy + Notes. Không tạo participant/feedback/recording/ảnh giả.
- Bug report do sinh viên viết 100%; AI không nháp theo AI-01 §11. Không tự điền verdict/chữ ký hay coi AI tự sửa là SV bổ sung.
- Commit từng bước thực. Cuối bài hoặc khi người dùng yêu cầu mới xuất git_commit_log.txt bằng .git/hw3-tools/export_git_log.py; không xuất sau từng commit.
- Giữ rõ phần chưa có bằng chứng trong README/Bao_cao, không đoán MSSV/họ tên/email/deadline, không đóng ZIP như bài hoàn tất khi chưa có dữ liệu thật. Loại AGENTS.md và .git khỏi ZIP.
