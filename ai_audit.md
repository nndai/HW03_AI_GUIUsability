# AI Audit Report - HW03

I use AI tools for the following tasks,

Đọc yêu cầu/SRS/slide, khảo sát trang, thiết kế/sửa checklist, tạo tài liệu, ghi log và tổ chức hồ sơ. Chưa khai execution/usability chính thức là đã hoàn thành.

## 1. Thông tin

| Mục | Giá trị |
| --- | --- |
| Họ tên / MSSV / lớp | Chưa cung cấp |
| Bài tập | HW03-AI - GUI & Usability |
| Ngày | 08/11/2026, Asia/Saigon (UTC+07:00) |
| Công cụ | OpenAI Codex; không suy đoán model |
| Nhật ký nguyên văn | prompt_log.md có số, tool, timestamp, prompt/output |
| Artifact hiện tại | Bao_cao; checklist/GUI_Checklist; phu_luc/AI_Review, theo các định dạng đi kèm |

## 2. Audit năm cột AI-02

Prompt/output hội thoại nguyên văn tại prompt_log.md. Bản nháp và lịch sử quyết định giữ trong AI Review. Verdict và bản sửa của sinh viên chưa tự xác nhận thay.

| (1) Prompt + công cụ | (2) Output AI | (3) Verdict SV | (4) Lý do / căn cứ | (5) Góp ý thực / bản SV sửa |
| --- | --- | --- | --- | --- |
| Đọc folder, Git và log; OpenAI Codex; timestamp tại log | Tóm tắt yêu cầu, repo, nhật ký | Chưa điền | HW03 §9/12/14, AI-02/03/05 | Người dùng yêu cầu log đơn giản, bỏ ai/.local, xuất Git log cuối bài; AI đã thực hiện |
| Xem Profile FR-04/11 và phân IA; OpenAI Codex; timestamp tại log | Nháp 52 mục, thành phần/trạng thái, hai ảnh khảo sát | Chưa điền | SRS FR-04/11/21–24, S13 trang 8/11–22 | Chưa có verdict; không coi khảo sát là execution chính thức |
| Gộp, thêm ID, rà trùng/căn cứ/expected; OpenAI Codex; timestamp tại log | 44 mục bản 1.0 và review kỹ thuật | Chưa điền | Gộp 4 cặp, tách 4 mục thiếu oracle; SRS khác quy ước bổ sung | Người dùng tiếp tục chỉ rõ các điều kiện cần bỏ; AI tự sửa không tính SV bổ sung |
| Góp ý GUI-003/008/015/020/034/037 theo ID cũ; OpenAI Codex; timestamp tại log | 43 mục bản 1.1 | Chưa điền | Bỏ font tuyệt đối, tiền thiếu, label-click focus, newline, server không đổi khi mất mạng | Góp ý thật đã áp dụng; không suy ra chữ ký/verdict chung |
| Bỏ GUI-004/038, chốt 41 mục, đổi ID và dọn hồ sơ; OpenAI Codex; timestamp tại log | GUI-001–GUI-041 bản 2.0 và cấu trúc báo cáo | Chưa điền | Bốn IA 11/10/9/11; 123 lượt dự kiến; mục loại không vào Execution | Người dùng quyết định bỏ hai mục/giữ 41; AI đổi ID, lưu mapping và tạo file |

## 3. Phân chia đóng góp và giới hạn

AI tạo nháp, tự rà kỹ thuật, biên tập file. Người dùng chốt format/cấu trúc, bỏ/sửa điều kiện và giữ 41 mục. Chưa có mục do sinh viên tự bổ sung hoặc verdict VALID/INVALID/INCOMPLETE được ghi nhận.

Khảo sát SUT dùng dữ liệu thử có khai báo; không tạo participant/contact/recording/ảnh đa nền tảng hoặc Passed/Failed giả. Chưa nháp bug report, theo AI-01 §11.

## 4. Tổng kết độ chính xác và kết luận

Chưa tính tỷ lệ VALID/INVALID/INCOMPLETE khi chưa có verdict sinh viên. Kết luận 80–150 chữ theo AI-02 cần hoàn thiện sau audit; ghi chú này không thay kết luận.

AI Critique 200–300 words, AI Use Disclosure, Mandatory Disclosure và chữ ký chưa hoàn thiện, được ghi rõ trong Bao_cao.md. Không tự ký hoặc tuyên bố đã review toàn bộ bài.
