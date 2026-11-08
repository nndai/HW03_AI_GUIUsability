# Yêu cầu đã đọc và cách áp dụng

Nguồn tại thư mục cha: `2026.HW03.GUI Usability_En.md` (bản chuyển từ PDF), `___2026.Homework.Policies.md`, `S13_GUI Testing & Usability Testing.md`, `HUONG_DAN_HW03.md`, sáu file `AI Templates` và README/setup guide của EShop. Đã đọc thêm mã trang Profile để hiểu cấu trúc; việc đọc mã không phải GUI execution.

## Đầu ra bắt buộc

| Hạng mục | Yêu cầu cần giữ |
| --- | --- |
| Task 1, 30 điểm | Ít nhất 41 mục có ý nghĩa, đủ IA-01 tiêu chuẩn chung, IA-02 form, IA-03 điều hướng, IA-04 phản hồi/trạng thái; AI nháp → người review/bổ sung và giải thích phần bỏ sót → chạy thật Passed/Failed; Failed có Notes và ảnh; checklist Excel và summary |
| Task 2, 40 điểm | Một flow end-to-end; mục tiêu, scenario theo mục tiêu, SUS/UEQ-S và probe clarity/error recovery/speed/trust; pilot trước; 7 người thật ngoài lớp, liên hệ xác minh được với số điện thoại che 4 số giữa; consent, think-aloud, quan sát trung lập, recording khi có; raw data, tính điểm và phân tích severity |
| Task 3, 20 điểm | Thực hiện Task 1 trên ≥3 nền tảng: Chrome, Firefox, Safari hoặc Android Chrome; Expo Go trên điện thoại thật có thể thay một nền tảng; ưu tiên cloud trial; ảnh rõ browser/OS/device và URL localhost, overlay email sinh viên; mục 11 còn yêu cầu MSSV và họ tên trong form |
| Agent Skills, 10 điểm | Đề khuyến khích skill tái sử dụng, kèm demo YouTube trọn màn hình/flow; chưa thực hiện |
| AI | AI Audit và Disclosure; mỗi tương tác có tool, ngày giờ, prompt/output nguyên văn; critique 200–300 words; thể hiện G9.3/G9.4 |
| Git | Một commit cho từng bước thực tế, gồm từng session; nộp git log text |
| Gói nộp | Main report Markdown + PDF, bug report/evidence/GitHub Issues có ảnh, AI Audit/Critique MD + PDF, Excel checklist + summary, session evidence và participant table, ảnh đa nền tảng, README có tự chấm và summary |

Tên ZIP theo đề cụ thể: `<StudentID>_HW03_AI_GUIUsability_<SelfAssessedGrade>.zip`, điểm ba chữ số 000–100. Nộp Moodle; deadline lấy tại Moodle. Policy chung: tối đa 20 file, mỗi file 20 MB; không chỉ nộp link thay nội dung.

## Trình tự kỹ thuật theo slide và hướng dẫn

GUI: xác định kỳ vọng → chuẩn bị môi trường/dữ liệu/checklist → thực thi → lưu actual/evidence → sinh viên viết bug. S13 đề cập màu/chữ/bố cục/nhãn/thông báo, navigation/focus, EP/BVA, state transition và compatibility. Với Profile, lấy SRS FR-04/FR-11 và các chuẩn giao diện làm căn cứ; không lấy hành vi hiện tại của code làm kỳ vọng đúng.

Usability: chuẩn bị purpose, problem statements, task/objective, user profile, method, environment, monitor role, measures và report. Thu cả performance (thành công, thời gian, lỗi, trợ giúp) lẫn preference (thang đo, ý kiến). Pilot để chốt protocol; sau đó 7 phiên; tổng hợp chủ đề và ưu tiên theo ảnh hưởng + tần suất. Không suy rộng mạnh từ mẫu 7 người.

Giữ phạm vi từ `HUONG_DAN_HW03.md`: FR-04 chính, FR-11 bổ trợ; không tự thêm hủy đơn hoặc chuyển checkout. Cần xác nhận flow không trùng nhóm. Một trang được phép nếu đủ hơn 40 mục độc lập; không nhân bản mục để tăng số lượng.

## Yêu cầu AI log và phần còn thiếu

- HW03 §9: khai “I use AI tools for the following tasks,” và ghi tool/date/time/prompt/output cho từng tương tác.
- AI-02 §2–3: prompt/output nguyên văn, 5 cột gồm prompt + tool, output, verdict VALID/INVALID/INCOMPLETE, lý do có căn cứ, bản sinh viên sửa có đánh dấu thay đổi. Phần người review vẫn để trống cho đến khi review thật.
- AI-02 §5: kết luận 80–150 chữ; khác với critique 200–300 words của HW03 §10. Không dùng một đoạn thay cho cả hai.
- AI-03 dẫn phụ lục `prompt_log.md`; AI-05 yêu cầu lưu mọi prompt + phản hồi có timestamp. Nhật ký hiện chỉ lấy dữ liệu gốc của chat này; không suy diễn nội dung các chat trước đã tạo hướng dẫn/PDF.
- AI-01 §11: sinh viên tự viết bug report. Danh sách người thật, ảnh thật, chữ ký và quyết định review không được AI xác nhận thay.
- Cần bổ sung trước khi nộp: thông tin SV, deadline, remote repo và Issues, các artifact kiểm thử thật, audit/review của SV, Disclosure/Mandatory Disclosure, critique, PDF và gói ZIP.
