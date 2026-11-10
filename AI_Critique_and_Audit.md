**Khoa Công nghệ Thông tin (FIT) – Trường Đại học Khoa học Tự nhiên (HCMUS)**

**CS423 / CSC13003 – Kiểm chứng Phần mềm (AI-augmented · 2026\)**

**CHÍNH SÁCH AI · BIỂU MẪU — 2026 v1.0**

# **AI Audit Report — Mẫu 5 mục cho mỗi Artifact**

*Phụ lục bắt buộc đính kèm cho mọi bài tập có dùng AI (HW\#01–HW\#06, Seminar).*

*Tài liệu được biên soạn lại từ Med Kharbach, PhD (2026) — Mẫu Chính sách Sử dụng AI cho Giáo dục Đại học. Giấy phép CC BY-NC-SA 4.0. Phiên bản này được FIT@HCMUS điều chỉnh cho môn CS423 / CSC15003 Kiểm chứng Phần mềm.*

## AI Critique

Trong HW03, AI hỗ trợ đọc yêu cầu, thiết kế checklist, chuẩn bị dữ liệu và tổng hợp báo cáo. Tuy nhiên, AI đã tạo ra quá nhiều thứ không cần thiết, khiến một bài kiểm thử có phạm vi khá rõ trở nên phức tạp. Bản nháp ban đầu có 52 mục, chứa nội dung trùng và những kỳ vọng chưa đủ căn cứ như yêu cầu font giống tuyệt đối. Việc thêm tài liệu, công cụ và diễn giải dài làm tăng công sức rà soát, đồng bộ và dọn hồ sơ, trong khi không trực tiếp cải thiện chất lượng kiểm thử.

Một thiếu sót đáng chú ý là AI bỏ qua việc hiển thị an toàn họ tên chứa HTML. Tôi đã yêu cầu bổ sung GUI-042 dựa trên SEC-04 và FR-04. Điều này cho thấy số lượng mục nhiều không bảo đảm bao phủ đủ rủi ro. AI cũng cần được điều chỉnh khi phân biệt hover với active, thao tác bàn phím với lưu thành công và Failed với Blocked. Nếu không đối chiếu actual, kết luận có thể vượt quá những gì thực sự quan sát được.

Bài học của tôi là giới hạn rõ đầu ra, yêu cầu căn cứ cho từng kỳ vọng và ưu tiên bằng chứng thật. Chỉ nên giữ tài liệu đề bài yêu cầu; công cụ thử đặt ngoài hồ sơ nộp. AI hữu ích khi hỗ trợ xử lý công việc lặp lại và tính SUS từ dữ liệu được cung cấp, nhưng không thay thế người tham gia, sự đồng ý ghi hình hoặc trách nhiệm đánh giá của sinh viên. Phần nhận xét và biểu mẫu cũng có AI hỗ trợ biên tập theo góp ý của tôi.

## **1\. Thông tin Sinh viên**

| Mục | Giá trị |
| :---- | :---- |
| **Họ tên sinh viên:** | NGUYỄN NGỌC ĐẠI |
| **MSSV:** | 23120226 |
| **Lớp / Khoá:** | Khóa 2023 |
| **Mã bài tập (ví dụ HW\#00, HW\#02):** | HW03-AI |
| **Ngày làm bài:** | 11/11/2026 |
| **Công cụ AI đã dùng:** | OpenAI Codex |
| **Công cụ AI đã dùng:** | \[ x ] Có  \[ \] Không |

## **3\. Bảng Audit — 1 hàng / artifact**

Bảng dưới tổng hợp artifact và căn cứ đã ghi nhận. Prompt/output **nguyên văn**, tool và thời gian: [prompt_log.md](prompt_log.md). Verdict dưới đây đánh giá đầu ra theo bằng chứng trong hồ sơ; cột chỉnh sửa phân biệt góp ý của người dùng và thao tác của AI.

| Prompt / công cụ / thời gian | Output AI | Verdict | Lý do / căn cứ review | Chỉnh sửa thực tế |
| --- | --- | --- | --- | --- |
| Đọc bài và thiết lập log; Codex; timestamp tại prompt_log.md | Tổng hợp yêu cầu và log | INCOMPLETE | HW03 §9 và AI Templates | Người dùng yêu cầu log đơn giản và chỉ xuất Git log cuối bài |
| Khảo sát FR-04/FR-11; Codex; timestamp tại prompt_log.md | Bản nháp 52 mục | INCOMPLETE | SRS FR-04/11/21–24, S13 | AI rà trùng và căn cứ; người dùng tiếp tục góp ý |
| Gộp checklist và thêm ID; Codex; timestamp tại prompt_log.md | Checklist hợp nhất | INCOMPLETE | Đối chiếu kỳ vọng, loại phần trùng và không có căn cứ | Gộp phone hợp lệ/biên; bỏ các điều kiện font, tiền thiếu, label-focus, newline và server không đổi khi mất mạng |
| Chốt 41 mục, đổi ID và dọn tài liệu; Codex; timestamp tại prompt_log.md | GUI-001–GUI-041 và workbook | INCOMPLETE | Phạm vi đã chọn; bốn IA 11/10/9/11 | Loại các mục người dùng chỉ định, đánh ID liên tục; giữ 41 mục hiện tại |
| `thêm vào report phần checklist ai bỏ sót kiểm tra hiển thị an toàn họ tên chứa html dựa sec-04 và fr-04, check xem cái tôi yêu cầu là đúng là thứ bạn bỏ sót không, nếu có thì thêm vào báo cáo đầy đủ theo đúng yêu cầu đề bào`; OpenAI Codex; 08/11/2026 23:55:05 (UTC+07:00) | GUI-042, dữ liệu H1/H2 và phần giải thích AI bỏ sót tại mục 2.1/2.3 | VALID | FR-04, SEC-04; bản nháp cũ thiếu kiểm HTML; App.jsx:27 dùng dangerouslySetInnerHTML với user.name | Người dùng phát hiện mục thiếu; AI xác minh và bổ sung. GUI-042 Chưa chạy |
| `đọc checklist mới nhất, chuẩn bị dữ liệu thử , không sửa logic sut hay checklist đã chốt, đưa ra kế hoặc viết test bằng playwright để test hết các checklist<br>`; OpenAI Codex; 2026-11-09T00:19:49.658000+07:00 | Dữ liệu tổng hợp và kế hoạch Playwright cho 42 mục | VALID | Checklist chốt và code SUT; chưa coi chuẩn bị dữ liệu là thực thi | Chuẩn bị SQLite riêng, xác định blocker phone và phần cần review giao diện. |
| `để các file vừa tạo ở ngoài thư mục work, có thể bỏ vào một folder ở ngoài phục vụ việc test, cái này không yêu cầu nộp, khi báo cáo sẽ nêu rõ mình sử dụng gì, chỉ những yêu cầu nộp mới để vào work, viết và chạy playwright trên chrome đầy đủ, lưu actual và ảnh failed, ko commit<br>`; OpenAI Codex; 2026-11-09T00:43:27.010000+07:00 | 42 ca Chrome đã thử; 19 Passed, 15 Failed, 8 bị chặn; 18 ảnh Failed | INCOMPLETE | Actual GUI/API/SQLite và ảnh thật; không sửa SUT hoặc định nghĩa checklist | Chuyển công cụ/dữ liệu ra ngoài work; sửa test phân biệt hover với active navbar và kiểm thêm focus thứ 11; giữ actual hai lần, khôi phục database gốc. |
| Sửa GUI-029/042 theo phạm vi keyboard và hiển thị fixture; Codex + Playwright; timestamp tại prompt_log.md | Test sửa và chạy lại Chrome: GUI-029 Passed, GUI-042 Failed với H1/H2; 2 ảnh lỗi mới | VALID | Checklist mới của người dùng, actual keyboard/DOM và ảnh sau reload; không PUT tên | Bỏ điều kiện lưu thành công ở GUI-029; GUI-042 chỉ dùng tài khoản fixture dựng sẵn để kiểm form/navbar sau reload. |
| Chốt Task 1 theo bằng chứng thực tế; Codex; timestamp tại prompt_log.md | 20 Passed, 19 Failed, 3 Blocked trên Chrome | VALID | Actual GUI/API và ảnh đã thu; không chạy lại hoặc sửa SUT | Người dùng chốt GUI-016/019/020 Failed; giữ GUI-033/034/035 Blocked; giữ kết quả chạy lại GUI-029/042. |
| Lập kế hoạch Task 3 và chạy Firefox cùng checklist, giữ Chrome; Codex + Playwright; timestamp tại prompt_log.md | Firefox: 20 Passed, 19 Failed, 3 Blocked; 23 ảnh Failed, Notes đủ 19 mục; kế hoạch Chrome Windows/Firefox Windows/Chrome Android | VALID | Actual Firefox độc lập; đối chiếu 42 ID và ảnh/DOM; hash/P1 Execution bảo toàn | Tách fixture P2 và cấu hình browser; kiểm lại GUI-010/028 từ focus xác định; không thay kết quả Chrome, không giả Android đã chạy. |
| Chạy checklist trên điện thoại Android qua ADB/Playwright, chụp scrcpy bằng Computer Use; Codex; timestamp tại prompt_log.md | P3: 18 Passed, 19 Failed, 5 Blocked; 42 actual, Notes và ảnh scrcpy; giữ P1/P2 | INCOMPLETE | Thiết bị/Chrome thật, API localhost và DOM/ảnh đo được; không giả lập Android trên Windows | Loại ảnh đen, kiểm lại header bảng/required; giữ Blocked cho viewport chưa đủ điều kiện và nhánh lưu chưa tới; khôi phục database gốc. |
| Chạy chụp lại toàn bộ ảnh Android bằng ADB theo yêu cầu; Codex + Playwright; timestamp tại prompt_log.md | 42 mục chạy lại, ảnh PNG ADB thay toàn bộ ảnh Android cũ; 18 Passed, 19 Failed, 5 Blocked | VALID | Actual lượt chạy lại và byte PNG trực tiếp từ thiết bị; không đổi P1/P2 | Đồng bộ liên kết ảnh và nguồn ảnh; giữ Notes cho Failed/Blocked; không sửa SUT hoặc commit. |
| Kiểm lại GUI-001/002 Android bằng viewport native và ảnh ADB; Codex + Playwright; timestamp tại prompt_log.md | Hai mục Passed; P3 20 Passed, 19 Failed, 3 Blocked | VALID | Đo đủ ba visualViewport scale=1, kiểm mọi control/cell sau cuộn và footer static; đối chiếu ảnh ADB/DOM | Đổi tạm display/density rồi khôi phục; không sửa SUT/checklist hoặc actual 40 ID khác/P1/P2. |
| Chuẩn bị Task 2 theo đề §6/§14, S13 và thang SUS; Codex; timestamp tại prompt_log.md | Kế hoạch, scenario, dữ liệu giả, protocol pilot/7 phiên, SUS/probe, biểu mẫu và cách phân tích; phần dữ liệu thật để trống | VALID | Đối chiếu từng phase, SRS FR-04, slide usability và tài liệu Brooke 1996/2013; kiểm định nghĩa chỉ số và trường dữ liệu | Tách dữ liệu hành vi/cảm nhận, lỗi người dùng/lỗi sản phẩm; không coi test tự động là pilot hoặc suy kết quả 7 người từ bug đã biết. |

## **4\. Tổng kết Độ chính xác AI**

Tổng hợp verdict từ Mục 3 và điền vào bảng dưới.

| Chỉ số | Số lượng | Tỉ lệ |
| :---- | :---- | :---- |
| **Tổng artifact AI sinh đã audit** | 14 | 100% |
| **VALID (đúng, dùng nguyên)** | 8 | 57,14% |
| **INVALID (sai; loại bỏ)** | 0 | 0% |
| **INCOMPLETE (chấp nhận sau khi sửa)** | 6 | 42,86% |

## **5\. Kết luận — Khi nào nên / không nên dùng AI?**

AI giúp tổ chức checklist, thực thi kiểm thử và tổng hợp số liệu, nhưng đầu ra ban đầu vừa dư thừa vừa bỏ sót rủi ro. Checklist 52 mục có kỳ vọng chưa đủ căn cứ, trong khi thiếu kiểm tra tên chứa HTML theo SEC-04. Việc tạo thêm tài liệu và công cụ khiến công việc phức tạp, tăng chi phí rà soát. Cách sử dụng phù hợp là giới hạn phạm vi, yêu cầu căn cứ SRS và đối chiếu ảnh, actual cùng dữ liệu thật. Không dùng AI để tạo người tham gia, consent hay kết quả chưa quan sát.

## **6\. Mandatory Disclosure (dán nguyên văn)**

Checklist, script và báo cáo có phiên bản đầu do OpenAI Codex hỗ trợ tạo. Tôi yêu cầu loại nội dung dư, điều chỉnh phạm vi và bổ sung ý tưởng GUI-042; AI thực hiện biên tập và kiểm tra kỹ thuật. Dữ liệu usability do người dùng cung cấp. Không coi phần AI biên tập là phần sinh viên tự viết độc lập. Chi tiết tại Phụ lục A của report.md.

## **Chữ ký**

| **Họ tên sinh viên:** | NGUYỄN NGỌC ĐẠI |
| :---- | :---- |
| **MSSV:** | 23120226 |
| **Lớp / Khoá:** | Khóa 2023 |
| **Môn học:** | CS423 / CSC13003 – Kiểm chứng Phần mềm |
| **Giảng viên:** | Theo phân công môn Kiểm chứng Phần mềm |
| **Ngày:** | 11/11/2026 |
| **Chữ ký:** | Nguyễn Ngọc Đại |

## **Tham khảo**

* Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.  
* ISTQB Foundation Level Syllabus (latest version).  
* Hardman, P. (2025). A Post-AI Learning Taxonomy.  
* Fuster Rabella, M. (2025). OECD Education Working Paper No. 338\.  
* Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.  
* Anthropic (2025). Building reliable AI test agents — engineering blog.  
* DeepEval & Promptfoo documentation — testing frameworks for LLM systems.
