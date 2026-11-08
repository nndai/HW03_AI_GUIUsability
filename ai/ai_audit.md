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
| Transcript gốc đã xuất | [prompt_log.md](prompt_log.md), [messages.jsonl](messages.jsonl) |

## Audit theo AI-02

Các dòng dưới là danh mục artifact do AI lập, **chưa phải verdict của sinh viên**. Prompt và phản hồi hội thoại được dẫn nguyên văn qua log; đầu ra dạng file là chính các file trong Git, không thay bằng lời tóm tắt.

| (1) Prompt + công cụ | (2) Output AI | (3) Verdict | (4) Lý do có nguồn | (5) Bản SV sửa |
| --- | --- | --- | --- | --- |
| Tương tác 001 trong prompt_log.md; OpenAI Codex; timestamp tại log | README.md, docs/requirements.md | Chờ SV review | Đối chiếu HW03 §§5–6, 9–12, 14–15 và policy; SV điền nhận xét thực tế | Chưa có bản SV sửa |
| Cùng tương tác 001 | scripts/export_chat_log.py, scripts/export_git_log.py, ai/prompt_log.md, ai/messages.jsonl, git_commit_log.txt, AGENTS.md | Chờ SV review | Đối chiếu HW03 §9/§12, AI-02 §2–3, AI-03 §2.3, AI-05 §2; SV kiểm tra độ đầy đủ/nguyên văn | Chưa có bản SV sửa |

## Tổng kết độ chính xác AI

Chưa có artifact được sinh viên audit. Không tính tỷ lệ VALID/INVALID/INCOMPLETE khi chưa review. Sau review, điền nhãn thật và đánh dấu phần sửa bằng diff hoặc `<mark>…</mark>`.

## Kết luận và khai báo

Kết luận 80–150 chữ theo AI-02: chờ sinh viên viết sau audit. AI Critique 200–300 words theo HW03: chưa thực hiện. Disclosure/Mandatory Disclosure và chữ ký: chờ xác nhận phần AI/người đóng góp; không tự ký hoặc tuyên bố đã review.
