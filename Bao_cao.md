# HW03 - GUI & Usability

Báo cáo chính - cập nhật ngày 08/11/2026. Đã hoàn thành thiết kế checklist 41 mục; chưa thực thi checklist hoặc tổ chức usability. Các phần chưa có bằng chứng được ghi rõ bên dưới.

## 1. Thông tin bài làm

| Trường | Thông tin |
| --- | --- |
| Họ tên / MSSV / lớp / email sinh viên | Chưa cung cấp |
| Mã bài | HW03-AI |
| SUT | EShop - ứng dụng thương mại điện tử phục vụ kiểm thử |
| Phiên bản source đã khảo sát | 85af3ba875c88283615e22cb108f13e2fccaf0e9; có thay đổi cục bộ, không chỉ dựa vào SHA |
| Hạn nộp | Chưa lấy từ Moodle |
| Hình thức | Bài cá nhân, có AI hỗ trợ |

## 2. Phạm vi và căn cứ

Màn hình chính /profile là một trang có hai phần: hồ sơ FR-04 và lịch sử đơn hàng FR-11. Navbar dùng chung chỉ được kiểm trong mức liên quan. Không mở rộng sang hủy đơn FR-10, checkout hoặc CRUD admin.

Flow usability dự kiến: tài khoản đã đăng nhập → tìm hồ sơ → cập nhật thông tin liên hệ và địa chỉ → lưu → mở lại/tải lại để xác minh. Không coi hai phần của Profile là hai màn hình độc lập.

Căn cứ: SRS EShop FR-04, FR-11, FR-21–24; slide S13 GUI Testing & Usability Testing trang 8, 11–22; đề HW03 §6, §9–12, §14–15. Code Profile.jsx, AuthContext.jsx, App.jsx và API liên quan dùng nhận diện control/trạng thái, không thay SRS làm expected.

## 3. Task 1 - GUI checklist

### 3.1. Thiết kế và review

AI lập bản nháp 52 mục từ SRS/code/slide và khảo sát trang. Rà trùng/expected tạo bản 1.0 có 44 mục. Người dùng yêu cầu bỏ GUI-034 và bỏ năm điều kiện vượt căn cứ, còn 43 mục ở bản 1.1. Lượt chốt hiện tại bỏ thêm GUI-004 và GUI-038 theo ID bản 1.1, giữ 41 mục còn lại, đánh lại ID liên tục.

Checklist chính thức phiên bản 2.0 chỉ gồm GUI-001–GUI-041. Mục bị loại hoặc chưa đủ căn cứ không vào Execution hay mẫu số thống kê. Mapping ID và bản nháp phục vụ AI Audit nằm riêng tại phu_luc/AI_Review.md.

| IA | Nội dung | Số mục |
| --- | --- | ---: |
| IA-01 | Tiêu chuẩn giao diện chung | 11 |
| IA-02 | Form | 10 |
| IA-03 | Điều hướng | 9 |
| IA-04 | Phản hồi / trạng thái | 11 |
| Tổng | Bốn IA | 41 |

### 3.2. Checklist và phương pháp

Ba bản đầy đủ nằm tại checklist/GUI_Checklist.md, checklist/GUI_Checklist.xlsx, checklist/GUI_Checklist.pdf. Mỗi mục có ID, IA, thành phần, thao tác/dữ liệu, expected, căn cứ, kết quả, Notes và ảnh/Issue. Workbook có Summary, Checklist và Execution; Execution gồm 123 lượt dự kiến cho 41 mục × 3 nền tảng.

Áp dụng EP/BVA phone với đầu 0, độ dài 9/10/11/12; 10–11 chữ số hợp lệ theo FR-04. State transition phân biệt login, khôi phục phiên, validation, lưu thành công/lỗi, tải đơn/empty/error. Baseline đối chiếu form và đơn theo tài khoản, ngày, tiền, trạng thái.

### 3.3. Khảo sát ban đầu và môi trường

Đã xem trạng thái chưa login bằng Chrome/Windows, sau đó form và lịch sử trống/có năm trạng thái bằng trình duyệt tích hợp. Do cổng 3000 bị EACCES và backend drop/reseed khi khởi động, khảo sát dùng database thử riêng, web localhost:5175, API localhost:13000. Chỉ đổi port/kết nối của bản chạy thử, không sửa validation/nghiệp vụ để tạo kết quả.

Dữ liệu giả được khai báo gồm Test User, phone/address thử và năm đơn đủ status. Đây là setup/khảo sát, không phải dữ liệu participant hoặc chứng cứ đã chạy toàn bộ checklist. Hai ảnh thật tại evidence/survey chỉ là ảnh khảo sát; chưa có overlay danh tính/thông tin nền tảng theo đề để tính Task 3 chính thức.

### 3.4. Kết quả thực thi

Chưa thực thi checklist chính thức. Tất cả 41 mục và 123 lượt dự kiến vẫn Chưa chạy. Không suy ra Passed/Failed từ code hoặc ảnh khảo sát.

| Chỉ số | Hiện có |
| --- | ---: |
| Mục thiết kế | 41 |
| Lượt dự kiến trên ba nền tảng | 123 |
| Lượt đã chạy | 0 |
| Passed / Failed | 0 / 0 |
| Nền tảng đã hoàn thành Task 1 | 0 |

Mỗi Failed phải có actual/Notes và ảnh thật; mỗi run có browser/OS/device/version, URL, thời gian và baseline. Bị chặn bởi bước trước thì ghi blocker, không gán kết quả cho bước chưa đến được.

## 4. Bug report và GitHub Issues

Chưa có bug report chính thức. Theo AI-01 §11, sinh viên tự viết mô tả bug từ tái hiện thật; lưu Markdown cùng ảnh và GitHub Issue có ảnh. Truy vết GUI-ID → run → ảnh → bug → Issue. Nhiều Failed có thể cùng một nguyên nhân, không buộc số bug bằng số Failed.

## 5. Task 2 - Usability evaluation

### 5.1. Mục tiêu và scenario

Mục tiêu dự kiến: người dùng tự tìm nơi sửa hồ sơ, nhập thông tin, hiểu phản hồi và xác minh đã lưu. Scenario: “Bạn vừa thay đổi thông tin liên hệ và chuyển nơi ở. Hãy cập nhật tài khoản bằng thông tin thử nghiệm được cung cấp để chuẩn bị cho lần mua hàng tiếp theo, sau đó kiểm tra thông tin đã được lưu đúng.” Không đưa đường bấm cho participant.

### 5.2. Chuẩn bị và pilot

Dự kiến dùng SUS sau task và probe về độ rõ ràng, phục hồi lỗi, tốc độ, độ tin cậy. Cần chốt protocol, baseline, tiêu chí hoàn thành/dừng, môi trường và recording trước pilot. Chưa có pilot hoặc câu trả lời thật.

### 5.3. Participant và các phiên

Chưa tuyển participant; hiện có 0/7 phiên chính thức. Chỉ nhập người thật ngoài lớp và contact xác minh được sau khi có sự đồng ý; che bốn số giữa số điện thoại. Không tạo danh tính, contact, recording hoặc câu trả lời giả.

Mỗi phiên P01–P07 cần metadata/consent, ghi chú timestamp, completion/time/error/assistance, SUS hoặc UEQ-S, probe và recording khi có. Pilot lưu riêng, không trộn với bảy phiên chính thức.

### 5.4. Phân tích

Chưa có dữ liệu tính điểm, tỷ lệ hoàn thành, thời gian hoặc severity/tần suất pain point. Sau thu thập, phân biệt lỗi sản phẩm với lỗi nhập của participant; nhóm chủ đề, tính đúng thang đo, ưu tiên theo ảnh hưởng/tần suất và dẫn evidence. Không suy rộng từ mẫu 7 người thành kết luận dân số.

## 6. Task 3 - Cross-browser / cross-platform

| Nền tảng dự kiến | Phạm vi | Execution | Ảnh theo yêu cầu |
| --- | --- | --- | --- |
| P1 Chrome / Windows | 41 mục | Chưa chạy | Chưa có |
| P2 Firefox / Windows | 41 mục | Chưa chạy | Chưa có |
| P3 Safari / macOS hoặc Android Chrome | Chọn một phương án, 41 mục | Chưa chạy | Chưa có |

Ưu tiên BrowserStack/LambdaTest có localhost tunnel phù hợp. Ảnh phải có browser/OS/device, URL localhost, overlay email sinh viên và MSSV/họ tên theo đề. Ba viewport trong một browser không phải ba nền tảng.

## 7. Agent Skills và demo

Chưa có Agent Skill được áp dụng trọn màn hình/flow và chưa có demo YouTube. Công cụ xuất file/ghi log không tự được tính là hoàn thành phần skill 10 điểm.

## 8. AI Audit, Disclosure và AI Critique

AI Audit tại ai_audit.md/PDF; prompt/output nguyên văn có tool và thời gian tại prompt_log.md. Phụ lục AI Review giữ nháp và mapping ID. Góp ý cụ thể của người dùng được ghi nhận, không tự suy ra verdict/chữ ký hoặc review đầy đủ từng artifact.

### 8.1. Disclosure hiện tại

I use AI tools for the following tasks,

Đọc/tổng hợp yêu cầu, khảo sát cấu trúc SUT, lập/sửa checklist, xuất tài liệu, tổ chức hồ sơ và ghi log. Người dùng quyết định bỏ/sửa các nội dung trong phụ lục; AI thực hiện thay đổi file. Chưa có execution chính thức hoặc dữ liệu usability do AI thay thế.

AI Use Disclosure và Mandatory Disclosure có chữ ký/chỉ rõ phần sinh viên tự viết vẫn cần hoàn thiện; không tự ký hoặc tuyên bố đã review thay.

### 8.2. AI Critique bắt buộc 200–300 words

Chưa hoàn thiện đoạn critique. Khi viết, dùng tình huống thật trong AI Review: font tuyệt đối, label-click focus, newline/persistence hoặc kết luận server không đổi khi mất mạng thiếu căn cứ; phân tích nguyên nhân và nguyên tắc phối hợp. Không coi ghi chú này là đoạn critique đạt yêu cầu.

## 9. Tự đánh giá và phần còn thiếu

Bảng tự chấm trong README.md, chưa có điểm. Hồ sơ hoàn thành phần thiết kế checklist/tổ chức tài liệu, chưa phải bài hoàn chỉnh đủ điều kiện nộp.

Còn thiếu: thông tin sinh viên/deadline; execution ba nền tảng/ảnh đúng yêu cầu; bug report/Issues do sinh viên viết khi có bug; pilot và 7 phiên thật/phân tích; skill/demo; verdict audit, kết luận AI-02, Disclosure/critique; tự chấm, Git log cuối và ZIP đúng tên. Chưa xuất Git log/ZIP theo yêu cầu trước đó.

## 10. Tài liệu tham chiếu

- Đề 2026.HW03.GUI Usability_En §5–6, §9–12, §14–15; Assignment Policies.
- EShop SRS README.md FR-04/11/21–24 và code Profile/AuthContext/Header/API liên quan.
- Slide S13 GUI Testing & Usability Testing, checklist/navigation/state và quy trình usability.
- AI Templates AI-01/02/03/05; AI-04/06 áp dụng theo hướng dẫn môn học.
