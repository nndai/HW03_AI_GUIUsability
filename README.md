# HW03 - GUI & Usability

**Nguyễn Ngọc Đại — MSSV 23120226 — Khóa 2023**

| Tệp | Nội dung |
| --- | --- |
| [report.md](report.md) | Báo cáo chính, checklist 42 mục, kết quả 7 phiên usability Task 2 và AI Audit |
| [Bug_Report.md](Bug_Report.md) | Chi tiết 19 issue Bug và 3 issue Blocked, kèm liên kết GitHub |
| [GUI_Checklist.xlsx](GUI_Checklist.xlsx) | Checklist, thực thi theo nền tảng và test summary |
| [AI_Critique_and_Audit.md](AI_Critique_and_Audit.md) | AI Critique và AI Audit theo AI-02 |
| [AI_Disclosure.md](AI_Disclosure.md) | Khai báo sử dụng AI theo AI-03 |
| [AI_Privacy_Checklist.md](AI_Privacy_Checklist.md) | Bảng kiểm riêng tư theo AI-05 |
| [prompt_log.md](prompt_log.md) | Prompt/output nguyên văn, tool và thời gian |
| [gui-usability-skill/SKILL.md](gui-usability-skill/SKILL.md) | Skill tái sử dụng cho thiết kế, review, thực thi GUI checklist và hỗ trợ usability |
| [screenshots/](screenshots/) | 23 ảnh [Chrome Windows](screenshots/chrome-windows/), 23 ảnh [Firefox Windows](screenshots/firefox-windows/); 28 ảnh [Failed Android](screenshots/chrome-android/) |

## Test summary

| Chỉ số | Kết quả |
| --- | ---: |
| Màn hình / flow trong phạm vi | 1 / 1 |
| Màn hình đã kiểm thử / phiên usability | 1 / 7 |
| Checklist thiết kế / có kết luận Chrome | 42 / 39 |
| Chrome: Passed / Failed / Blocked | 20 / 19 / 3 |
| Mục Chrome đã thử / bị chặn | 42 / 3 |
| Mục Firefox đã thử / Passed / Failed / Blocked | 42 / 20 / 19 / 3 |
| Mục Android đã thử / Passed / Failed / Blocked | 42 / 20 / 19 / 3 |
| Tổng lượt đã thử / có kết luận Passed hoặc Failed | 126 / 117 |
| Tổng Passed / Failed / Blocked | 60 / 57 / 9 |
| Nền tảng đã chạy trên Windows / Android thật | 3 / 3 |
| Bug report chính thức | 19 issue Bug / 3 issue Blocked |
| Participant đã tham gia | 7 / 7 theo hồ sơ cung cấp |
| Pilot usability thực tế | Đã ghi nhận trong hồ sơ Task 2 |
| Nền tảng đủ bằng chứng nộp Task 3 | 3 / 3 |
| Demo video Agent Skill | [Xem video demo](https://youtu.be/mtbgSK8GzcU) |

Task 1 đã chốt theo actual Chrome: 20 Passed, 19 Failed, 3 Blocked. Đã thử đủ 42 mục; 3 mục Blocked (GUI-033/034/035) vì chưa tới nhánh cần kiểm. Ảnh của ba nền tảng đã đủ thông tin danh tính và môi trường theo yêu cầu Task 3. Firefox đã chạy cùng 42 mục với actual/Notes/ảnh riêng, Chrome giữ nguyên. Chrome Android thật đã thử đủ 42 mục; ảnh đã chụp lại trực tiếp bằng ADB (PNG 1080×2340). GUI-001/002 Android đã kiểm lại đạt đúng viewport native và Passed. Còn 9 lượt Blocked ở các nhánh lưu; bằng chứng danh tính và môi trường đã đầy đủ. Actual kỹ thuật và công cụ thử nằm ngoài work.

Task 2 đã tích hợp hồ sơ pilot và bảy phiên D01–D07, bảy link video, đáp án SUS, phản hồi mở và findings xếp ưu tiên. SUS trung bình 30,71/100; hoàn tất nhiệm vụ 0/7 do validation phone. Hồ sơ phiên, đối tượng ngoài lớp, consent và liên kết video đã đầy đủ theo xác nhận của sinh viên; xem report.md §3. Đã đối chiếu [22 GitHub Issues](https://github.com/nndai/HW03_AI_GUIUsability/issues), gồm 19 Bug và 3 Blocked; nội dung chi tiết nằm tại Bug_Report.md.

## Agent Skill và video demo

Nộp kèm [skill GUI và usability](gui-usability-skill/SKILL.md). Skill nhận màn hình/flow, SRS/source, môi trường và thư mục output làm đầu vào, hướng dẫn thiết kế, review, thực thi checklist và tổng hợp báo cáo; phần usability yêu cầu dữ liệu người thật. Skill có thể tái sử dụng cho màn hình hoặc flow khác.

[Video demo Agent Skill trên trang Profile, phạm vi FR-04 và FR-11](https://youtu.be/mtbgSK8GzcU).

## Tự đánh giá

| STT | Tiêu chí | Điểm tối đa | Tự chấm |
| --- | --- | ---: | --- |
| 1 | Task 1 - GUI checklist | 30 | 30 |
| 2 | Task 2 - Usability evaluation | 40 | 40 |
| 3 | Task 3 - Cross-browser / cross-platform | 20 | 20 |
| 4 | Agent Skills | 10 | 10 |
| | Tổng | 100 | 100 |

Điểm tự đánh giá giữ theo bảng trên; hồ sơ phiên, consent và bằng chứng danh tính/môi trường đã được sinh viên xác nhận đầy đủ.
