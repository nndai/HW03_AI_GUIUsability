# Quy tắc làm việc HW03

- Chỉ biên tập nội dung đề bài yêu cầu. Báo cáo chính duy nhất là report.md; có 42 mục GUI-001–GUI-042, IA-01/02/03/04 = 11/11/9/11. GUI-042 do người dùng phát hiện AI bỏ sót, kiểm hiển thị an toàn họ tên chứa HTML theo SEC-04 + FR-04. Workbook chính thức GUI_Checklist.xlsx ở thư mục gốc.
- Giữ cấu trúc phẳng; không tạo thư mục con, docs hoặc phụ lục thành file riêng. AI Audit bắt buộc nằm trong report.md. README.md chỉ chứa danh mục file, summary và tự chấm theo đề.
- Không tự commit. Không tạo PDF hoặc ZIP cho đến khi người dùng yêu cầu nộp. Không xuất Git log trong lúc còn làm bài nếu chưa được yêu cầu.
- Giữ nguyên prompt/output tại prompt_log.md với số thứ tự, tool, thời gian prompt giờ Việt Nam. Chạy .git/hw3-tools/export_chat_log.py mỗi lượt và bật --follow nếu cần ghi câu trả lời cuối; không ghi system/developer/suy luận nội bộ.
- Không thêm lời nhắc quy trình, lịch sử biên tập, mapping ID cũ, bản nháp hoặc nội dung không bắt buộc vào báo cáo. Không tạo dữ liệu/participant/ảnh test hoặc Passed/Failed giả; phần chưa thực hiện chỉ ghi trạng thái ngắn.
- Bug report do sinh viên tự viết theo AI-01 §11. Không tự điền verdict/chữ ký hoặc coi AI tự sửa là SV bổ sung. Không sửa SUT để ép Passed.
- Khi cập nhật, giữ nội dung report.md và GUI_Checklist.xlsx đồng nhất; không ghi đè actual/kết quả người dùng đã điền. Không chạy các script dựng lại cấu trúc/PDF cũ. Công cụ nội bộ nằm trong .git, không thuộc hồ sơ nộp.
