# AI Audit Report — bản khởi tạo, chờ sinh viên review

I use AI tools for the following tasks,

- Đọc yêu cầu HW03 và thiết lập quản lý phiên bản.
- Xuất prompt/phản hồi nguyên văn từ bản ghi chat hiện tại, kèm timestamp.

| Thông tin | Giá trị |
| --- | --- |
| Họ tên / MSSV / lớp | Chưa cung cấp |
| Bài tập | HW03-AI — GUI & Usability |
| Ngày | 08/11/2026, Asia/Saigon (UTC+07:00) |
| Công cụ | OpenAI Codex; không suy đoán phiên bản model |
| Transcript gốc đã xuất | [prompt_log.md](prompt_log.md) |

## Audit theo AI-02

Các dòng dưới là danh mục artifact do AI lập, **chưa phải verdict của sinh viên**. Prompt và phản hồi hội thoại được dẫn nguyên văn qua log; đầu ra dạng file là chính các file trong Git, không thay bằng lời tóm tắt.

| (1) Prompt + công cụ | (2) Output AI | (3) Verdict | (4) Lý do có nguồn | (5) Bản SV sửa |
| --- | --- | --- | --- | --- |
| Mục 1 trong prompt_log.md; OpenAI Codex; timestamp tại log | README.md, docs/requirements.md | Chờ SV review | Đối chiếu HW03 §§5–6, 9–12, 14–15 và policy; SV điền nhận xét thực tế | Chưa có bản SV sửa |
| Cùng mục 1 | scripts/export_chat_log.py, scripts/export_git_log.py, prompt_log.md, git_commit_log.txt, AGENTS.md | Chờ SV review | Đối chiếu HW03 §9/§12, AI-02 §2–3, AI-03 §2.3, AI-05 §2; SV kiểm tra độ đầy đủ/nguyên văn | Chưa có bản SV sửa |
| Mục 5 trong prompt_log.md; OpenAI Codex; thời gian gửi prompt tại log | docs/profile_inventory.md: thành phần, ma trận trạng thái, 52 nội dung IA-01–04; scripts/survey-vite.mjs và scripts/seed_survey_data.py hỗ trợ môi trường khảo sát | Chờ SV review | Đối chiếu SRS FR-04/11/21–24 và slide S13 trang 11–22; kiểm nhãn yêu cầu/bổ sung, scope và các giới hạn execution | Chưa có bản SV sửa |
| Prompt “thêm id, gộp bốn nhóm thành checklist…” trong prompt_log.md; OpenAI Codex; thời gian gốc tại log | outputs/HW03-01a1ba88/GUI_Checklist.md và .xlsx; output/pdf/GUI_Checklist.pdf; docs/checklist_review.md; thêm ID nguồn vào inventory | Chờ SV review | AI tự rà kỹ thuật: 4 cặp được gộp, 4 mục thiếu oracle được tách; còn 44 mục. Mapping đủ 52 nguồn. Expected phân biệt SRS, slide và B01–B10 đề xuất; chưa tính đây là phần SV tự bổ sung/đã review | Chưa có bản SV sửa |

## Tổng kết độ chính xác AI

Góp ý trực tiếp tiếp theo của người dùng: bỏ GUI-034 và các điều kiện font tuyệt đối (GUI-003), tiền thiếu (GUI-008), click nhãn phải focus (GUI-015), giữ nguyên newline (GUI-020), server không đổi khi mất mạng (GUI-037). Đã áp dụng vào bản 1.1: còn 43 mục/129 lượt dự kiến, giữ ID. Đây là phản hồi thật từ người dùng; chưa suy ra verdict chung hoặc review toàn bộ các mục còn lại.

Chưa có artifact được sinh viên audit. Không tính tỷ lệ VALID/INVALID/INCOMPLETE khi chưa review. Sau review, điền nhãn thật và đánh dấu phần sửa bằng diff hoặc `<mark>…</mark>`.

## Kết luận và khai báo

Kết luận 80–150 chữ theo AI-02: chờ sinh viên viết sau audit. AI Critique 200–300 words theo HW03: chưa thực hiện. Disclosure/Mandatory Disclosure và chữ ký: chờ xác nhận phần AI/người đóng góp; không tự ký hoặc tuyên bố đã review.
