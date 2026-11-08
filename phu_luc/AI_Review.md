# Phụ lục - AI Review và truy vết checklist

## 1. Phiên bản hiện tại 2.0

Người dùng chốt bỏ GUI-004 (nội dung dài/zoom) và GUI-038 (giữ nội dung khi lỗi) theo ID bản 1.1; giữ 41 mục còn lại, đánh lại ID liên tục. Có 41 mục chính thức và 123 lượt dự kiến, phân bổ IA-01/02/03/04 là 11/10/9/11. Checklist chính thức nằm tại checklist/GUI_Checklist.md.

Các phần lịch sử bên dưới chỉ phục vụ AI Audit. Không đưa các mục bị loại hoặc chưa đủ căn cứ vào checklist/Execution/test summary hiện tại. Không dùng ID của bản cũ để ghi kết quả mới.

## 2. Bảng đổi ID từ 1.1 sang 2.0

| ID bản 1.1 | ID bản 2.0 / quyết định | Thành phần |
| --- | --- | --- |
| GUI-001 | GUI-001 | Bố cục mặc định |
| GUI-002 | GUI-002 | Bố cục responsive |
| GUI-003 | GUI-003 | Chữ và khả năng đọc |
| GUI-004 | Loại theo yêu cầu người dùng | Nội dung dài và zoom |
| GUI-005 | GUI-004 | Ngôn ngữ |
| GUI-006 | GUI-005 | Tiêu đề và hierarchy |
| GUI-007 | GUI-006 | Màu nút hành động |
| GUI-008 | GUI-007 | Định dạng tổng tiền |
| GUI-009 | GUI-008 | Ngày đặt |
| GUI-010 | GUI-009 | Nhãn và màu trạng thái đơn |
| GUI-011 | GUI-010 | Focus nhìn thấy và khả năng đọc |
| GUI-012 | GUI-011 | Cấu trúc bảng và đúng cột |
| GUI-013 | GUI-012 | Giá trị ban đầu của form |
| GUI-014 | GUI-013 | Email chỉ đọc và đúng loại field |
| GUI-015 | GUI-014 | Nhãn và tên truy cập của control |
| GUI-016 | GUI-015 | Dấu trường bắt buộc |
| GUI-017 | GUI-016 | Cập nhật tên tiếng Việt |
| GUI-018 | GUI-017 | Biên độ dài điện thoại |
| GUI-019 | GUI-018 | Phân lớp điện thoại sai |
| GUI-020 | GUI-019 | Nội dung địa chỉ |
| GUI-021 | GUI-020 | Gửi đúng thay đổi hồ sơ bằng chuột |
| GUI-022 | GUI-021 | Nội dung và vị trí lỗi nhập |
| GUI-023 | GUI-022 | Tìm và mở Profile |
| GUI-024 | GUI-023 | Navbar đang chọn |
| GUI-025 | GUI-024 | Logo về Home |
| GUI-026 | GUI-025 | Link và badge giỏ hàng chung |
| GUI-027 | GUI-026 | Nhãn và đường thoát |
| GUI-028 | GUI-027 | URL trực tiếp và reload |
| GUI-029 | GUI-028 | Thứ tự Tab và Shift+Tab |
| GUI-030 | GUI-029 | Kích hoạt bằng bàn phím |
| GUI-031 | GUI-030 | Back và Forward |
| GUI-032 | GUI-031 | Bảo vệ khi thiếu hoặc hết hiệu lực phiên |
| GUI-033 | GUI-032 | Đang khôi phục phiên |
| GUI-035 | GUI-033 | Phản hồi lưu thành công |
| GUI-036 | GUI-034 | Đồng bộ và giữ dữ liệu sau lưu |
| GUI-037 | GUI-035 | Phản hồi lỗi lưu |
| GUI-038 | Loại theo yêu cầu người dùng | Giữ nội dung khi lỗi |
| GUI-039 | GUI-036 | Focus sau đóng thông báo |
| GUI-040 | GUI-037 | Đang tải danh sách đơn |
| GUI-041 | GUI-038 | Empty state thực sự |
| GUI-042 | GUI-039 | Lỗi tải lịch sử và phục hồi |
| GUI-043 | GUI-040 | Chuyển tài khoản và cô lập dữ liệu |
| GUI-044 | GUI-041 | Trạng thái đơn thay đổi bên ngoài |

## 3. Lịch sử review trước khi chốt bản 2.0

# Review bản nháp và truy vết checklist chuẩn

Ngày 08/11/2026. Người thực hiện review kỹ thuật: OpenAI Codex, theo yêu cầu của người dùng. Đây không phải chữ ký/verdict review của sinh viên. Giữ nguyên docs/profile_inventory.md làm bản AI nháp để so sánh.

## Bản 1.1 - góp ý của người dùng

Còn **43 mục**, IA-01: 12, IA-02: 10, IA-03: 9, IA-04: 12; dự kiến 129 lượt trên 3 nền tảng. Giữ nguyên ID; GUI-034 bị loại, B09 ngừng áp dụng. Quyết định dưới đây đến từ prompt người dùng ngày 08/11/2026, không phải AI tự gán là review của sinh viên.

| ID | Thay đổi | Lý do / căn cứ cập nhật |
| --- | --- | --- |
| GUI-034 | Bỏ toàn bộ mục đang lưu/click lặp và B09 | Theo yêu cầu trực tiếp của người dùng; không chuyển điều kiện chống lặp sang mục khác |
| GUI-003 | Bỏ khớp tuyệt đối font-family/font-size; giữ khả năng đọc và chữ không mất/cắt | SRS/slide không quy định mọi font phải trùng tuyệt đối; người dùng yêu cầu bỏ |
| GUI-008 | Bỏ điều kiện xử lý tiền thiếu/thay thiếu bằng 0 | Thu hẹp về tiền có dữ liệu và định dạng theo FR-11/21; không có oracle fallback cho thiếu dữ liệu |
| GUI-015 | Bỏ thao tác/expected click nhãn phải đưa focus | Giữ nhãn và accessible name đúng vai trò; người dùng yêu cầu không chấm label-click focus |
| GUI-020 | Bỏ yêu cầu giữ nguyên xuống dòng; giữ đầy đủ từ/chữ số/dấu | SRS không chốt chuẩn hóa whitespace/xuống dòng; người dùng yêu cầu bỏ điều kiện bảo toàn newline |
| GUI-037 | Bỏ assertion server không đổi khi mất mạng; message được phép nêu chưa xác nhận kết quả | Mất kết nối có thể xảy ra sau khi server đã xử lý; phía GUI không đủ căn cứ kết luận server chắc chắn không đổi |

## Lịch sử hợp nhất bản 1.0

52 mục nháp → gộp 4 cặp (giảm 4) → tách 4 mục chưa đủ oracle → **44 mục**. Phân bổ mới: IA-01 12, IA-02 10, IA-03 9, IA-04 13. Không thêm mục nhân tạo để bù số lượng. Các phần bàn phím/trình bày/persistence được chuyển đúng mục, tránh tính lại cùng assertion. Nội dung inventory được giữ nguyên; chỉ thêm ID nguồn để truy vết. Git giữ phiên bản trước khi thêm ID.

ID nguồn INV-IA01-01 nghĩa là mục 01 của IA-01 trong inventory, tương tự cho bốn nhóm; GUI-xxx là ID dùng thực thi. File chuẩn: outputs/HW03-01a1ba88/GUI_Checklist.md và workbook cùng tên; PDF ở output/pdf/GUI_Checklist.pdf.

## Lịch sử quyết định AI ở bản 1.0

Bảng sau ghi lại quá trình tạo bản 1.0; các quyết định bản 1.1 ở trên được ưu tiên khi khác nhau.

| Vấn đề | Mục nguồn | Sửa đề xuất / đích | Lý do |
| --- | --- | --- | --- |
| Trùng một phần hợp lệ/biên phone | IA-02.08 + .09 | Gộp GUI-018, bộ 9/10/11/12 trong một mục | Cả hai lặp dữ liệu hợp lệ 10/11; một bộ BVA chứa cả trong/ngoài biên, ghi actual từng biến thể |
| Phân mảnh một control email | IA-02.02 + .03 | Gộp GUI-014: readonly + type=email | Không phải hai assertion giống nhau; gộp vì cùng control/tác vụ kiểm, tránh dùng email disabled để tạo test validate nhập không thực hiện được |
| Hai trạng thái cùng nghĩa chưa được xác thực | IA-04.01 + .03 | Gộp GUI-032, giữ hai điều kiện thiếu/invalid token | Chung oracle không lộ dữ liệu và có đường login; vẫn ghi riêng actual từng điều kiện để không mất coverage |
| Chờ lưu và click lặp cùng một thời điểm | IA-04.04 + .05 | Gộp GUI-034: delay + ba click | Không phải trùng hoàn toàn; gộp một kịch bản có pending/feedback/chống lặp, công khai tiêu chí B09 do AI đề xuất |
| Submit/Enter bị kiểm ở form và navigation | IA-02.13 / IA-03.08 | GUI-021 chỉ click và đúng dữ liệu; GUI-030 sở hữu keyboard | Tách phương thức input khỏi tính đúng cập nhật; không tính cùng hành động Enter hai lần |
| Long name/layout/persistence bị gộp lẫn | IA-01.04 / IA-02.07 / IA-04.07 | GUI-004 chỉ trình bày fixture dài; GUI-017 tên Unicode ngắn; GUI-036 đồng bộ qua navigation/reload | Không yêu cầu form chấp nhận độ dài tùy ý khi SRS chưa chốt giới hạn; mỗi mục có quan sát riêng |
| Typography mơ hồ | IA-01.03 | GUI-003: không glyph thiếu/cắt và nhãn cùng vai trò có font-size/family nhất quán | Thay “đẹp/dễ đọc” bằng điều kiện có thể so sánh; không bịa ngưỡng cỡ chữ của slide |
| Responsive/zoom chưa có môi trường | IA-01.02 + .04 | GUI-002/004, B01: 390×844, 768×1024, 1366×768, zoom 100/200% | Cố định điều kiện để tái hiện; đây là test setting, không phải 3 nền tảng và không là thông số SRS |
| Ngày chưa có locale | IA-01.09 | GUI-009: đối chiếu giá trị với fixture, ghi locale/timezone | SRS chỉ yêu cầu Ngày đặt, không đủ căn cứ bắt dd/MM; dùng ngày >12 phát hiện nhầm tháng/ngày |
| Accessibility chưa có chuẩn đo | IA-01.11 / IA-02.04 / IA-04.10 | GUI-011 nhìn thấy focus; GUI-015 nhãn; GUI-039 phục hồi focus | Ba assertion khác nhau, giữ riêng; không tuyên bố WCAG 4.5:1 hoặc certification chỉ dựa slide |
| Dấu required bị dùng làm business oracle | IA-02.05 + .06 | GUI-016 kiểm dấu * cho field đã khai báo required; tách .06 chờ quy tắc | Code required không chứng minh SRS bắt tên không trắng, cũng không chứng minh blank hợp lệ |
| Lỗi chung và lỗi nhập lẫn nhau | IA-02.14 / IA-04.08 | GUI-022 lỗi phone + vị trí trên submit; GUI-037 lỗi API và phục hồi | Tránh bắt mọi success/error phải có cùng cơ chế; yêu cầu vị trí FR-22 áp vào lỗi form |
| Badge số lượng thiếu quy tắc đếm | IA-03.04 | GUI-026 dùng 3 loại ×1, cho phép ẩn hoặc 0 khi rỗng | Loại tranh luận đếm dòng hay tổng qty trong test này; không tự thêm quy tắc chưa đặc tả |
| Skip email khi Tab bị áp cứng | IA-03.07 | GUI-029 skip nếu disabled, readonly được focus | FR-04 chỉ đòi không sửa được, không bắt duy nhất disabled; chấp nhận implementation hợp lệ khác |
| Enter bị áp cứng mọi input | IA-02.13 / IA-03.08 | GUI-030 phân biệt link/nút/textarea | Tránh fail implementation không hỗ trợ implicit submit dù vẫn cập nhật hoàn toàn bằng keyboard |
| Reload route trùng persistence | IA-03.06 / IA-04.07 | GUI-028 route/phiên; GUI-036 so giá trị đã đổi sau lưu | Route tải được không chứng minh dữ liệu lưu; phân tách oracle |
| Loading/error thiếu dấu hiệu cụ thể | IA-04.02/.04/.11/.13 | B08–B10 + GUI-033/034/040/042 | Delay là test control, không SLA; chấp nhận feedback tương đương, không bắt spinner/Retry cụ thể |
| Snapshot đơn bị hiểu thành realtime | IA-04.15 | GUI-044 chỉ yêu cầu dữ liệu mới sau mở lại/reload | SRS chưa đòi polling/websocket, không ghi Failed vì không realtime |
| Các phần bảo mật API ngoài GUI | IA-02.13 / IA-04.14 | GUI-021 quan sát profile bản thân, GUI-043 đổi phiên qua GUI | Không gửi payload role hoặc xâm nhập ID khác rồi đếm như checklist UI; test API sâu là phụ lục riêng |

## Mục tách chờ làm rõ, không tính vào 43 mục hiện tại

| ID nguồn | Nội dung | Thiếu căn cứ/kỳ vọng | Đề xuất xử lý |
| --- | --- | --- | --- |
| INV-IA02-06 | Họ tên rỗng/toàn khoảng trắng | SRS FR-04 chưa chốt họ tên có bắt buộc hoặc trim không. required trong code chỉ là hiện trạng. | Giữ kiểm dấu * tại GUI-016. Xin quy tắc tên trước khi tạo test chấp nhận/từ chối tên rỗng; không tự ghi Failed chỉ vì thiếu quy tắc. |
| INV-IA02-11 | Phone/address trống | SRS chưa nói optional/required, cũng chưa phân biệt chưa khai báo và xóa giá trị đã có. | Tách khảo sát hành vi để hỏi TA/đặc tả; chưa tính là checklist có oracle đủ rõ. |
| INV-IA03-10 | Rời trang khi chưa lưu | Slide nêu đồng bộ/trạng thái nhưng SRS không bắt autosave, giữ draft hoặc dialog xác nhận. | Đưa vào probe usability; không bắt có dialog/giữ draft trong checklist chuẩn. |
| INV-IA04-16 | Payload thiếu/sai kiểu và response bất thường | Bản nháp gộp ngày/status/tổng lỗi với API chậm; thiếu hợp đồng schema và fallback. | Loading/error đã có GUI-040/042. Payload malformed giữ ở robustness bổ trợ sau khi chốt schema; không tạo hàng loạt Failed không có oracle. |

Các câu hỏi bổ sung: trim phone trước validation hay từ chối khoảng trắng; giới hạn tên/địa chỉ; bắt buộc breadcrumb tại Profile hay không. Chưa có câu trả lời thì không tạo expected bắt buộc. Dark mode/RTL chỉ là ý tưởng mở rộng, không thêm hàng Failed mặc định.

## Mapping toàn bộ 52 mục nháp

| ID nguồn | Đích / quyết định |
| --- | --- |
| INV-IA01-01 | GUI-001 |
| INV-IA01-02 | GUI-002 |
| INV-IA01-03 | GUI-003 |
| INV-IA01-04 | GUI-004 |
| INV-IA01-05 | GUI-005 |
| INV-IA01-06 | GUI-006 |
| INV-IA01-07 | GUI-007 |
| INV-IA01-08 | GUI-008 |
| INV-IA01-09 | GUI-009 |
| INV-IA01-10 | GUI-010 |
| INV-IA01-11 | GUI-011 |
| INV-IA01-12 | GUI-012 |
| INV-IA02-01 | GUI-013 |
| INV-IA02-02 | GUI-014 |
| INV-IA02-03 | GUI-014 |
| INV-IA02-04 | GUI-015 |
| INV-IA02-05 | GUI-016 |
| INV-IA02-06 | Tách chờ làm rõ |
| INV-IA02-07 | GUI-017 |
| INV-IA02-08 | GUI-018 |
| INV-IA02-09 | GUI-018 |
| INV-IA02-10 | GUI-019 |
| INV-IA02-11 | Tách chờ làm rõ |
| INV-IA02-12 | GUI-020 |
| INV-IA02-13 | GUI-021 |
| INV-IA02-14 | GUI-022 |
| INV-IA03-01 | GUI-023 |
| INV-IA03-02 | GUI-024 |
| INV-IA03-03 | GUI-025 |
| INV-IA03-04 | GUI-026 |
| INV-IA03-05 | GUI-027 |
| INV-IA03-06 | GUI-028 |
| INV-IA03-07 | GUI-029 |
| INV-IA03-08 | GUI-030 |
| INV-IA03-09 | GUI-031 |
| INV-IA03-10 | Tách chờ làm rõ |
| INV-IA04-01 | GUI-032 |
| INV-IA04-02 | GUI-033 |
| INV-IA04-03 | GUI-032 |
| INV-IA04-04 | Loại theo yêu cầu người dùng (GUI-034) |
| INV-IA04-05 | Loại theo yêu cầu người dùng (GUI-034) |
| INV-IA04-06 | GUI-035 |
| INV-IA04-07 | GUI-036 |
| INV-IA04-08 | GUI-037 |
| INV-IA04-09 | GUI-038 |
| INV-IA04-10 | GUI-039 |
| INV-IA04-11 | GUI-040 |
| INV-IA04-12 | GUI-041 |
| INV-IA04-13 | GUI-042 |
| INV-IA04-14 | GUI-043 |
| INV-IA04-15 | GUI-044 |
| INV-IA04-16 | Tách chờ làm rõ |

## Phần sinh viên cần thực hiện

- [ ] Rà 43 mục, các quy ước còn hiệu lực B01–B08, B10 và quyết định sửa; ghi ngày/người review thật.
- [ ] Chấp nhận/sửa/bỏ các tiêu chí bổ sung; cập nhật ID ổn định và số lượng thực nếu có thay đổi.
- [ ] Bổ sung mục AI bỏ sót dựa trên quan sát của chính sinh viên, giải thích vì sao AI bỏ sót. Các sửa do AI ở trên không được ghi là “SV tự bổ sung”.
- [ ] Điền verdict VALID/INVALID/INCOMPLETE, căn cứ và bản SV sửa trong AI Audit; chưa tự điền thay.
- [ ] Chốt 3 nền tảng, baseline và oracle còn phụ thuộc trước execution; không sửa SUT để ép Passed.
- [ ] Sau execution: cập nhật actual/Passed/Failed/Notes/ảnh thật, report và PDF; phần bị blocker phải được nêu, không báo hoàn tất giả.

Không có bước thực thi hoặc bug report mới trong lượt review này. Git commit log sẽ xuất ở cuối bài theo yêu cầu người dùng.

## 4. Bản nháp AI gốc để đối chiếu

Đây là 52 mục nháp, không phải checklist chính thức để thực thi.



Mỗi nội dung có một IA chính để tránh đếm trùng. Một bộ dữ liệu biên nằm trong cùng nội dung, không tách mỗi số điện thoại thành một mục để tăng số lượng.

### IA-01 — General UI standards: 12 nội dung

| ID nguồn | Thành phần / trạng thái | Nội dung cần kiểm tra | Căn cứ |
| --- | --- | --- | --- |
| INV-IA01-01 | Khung trang và hai vùng | Căn lề, khoảng cách, độ rộng form/bảng; không đè chồng hoặc bị footer che | Slide 16 |
| INV-IA01-02 | Viewport hẹp/rộng | Form và lịch sử thích ứng; bảng không làm mất cột hoặc thao tác không thể tiếp cận | Slide 21–22; cần chốt kích thước |
| INV-IA01-03 | Chữ trên form/bảng | Cỡ chữ, kiểu chữ, độ đậm và nhãn dễ đọc, nhất quán | Slide 16 |
| INV-IA01-04 | Nội dung dài/zoom | Tên, email, địa chỉ dài và zoom vẫn đọc/thao tác được; không che nút/cột | Slide 16, 22; bổ sung cách đo |
| INV-IA01-05 | Toàn trang | Tiếng Việt nhất quán và đúng dấu, kể cả nhãn/thông báo/state | SRS FR-21 |
| INV-IA01-06 | Tiêu đề trang | Đúng một h1 mô tả nội dung; hai phần có hierarchy phù hợp | SRS FR-21 |
| INV-IA01-07 | Nút hành động | “Cập nhật” dùng màu tích cực xanh; thao tác nguy hiểm đang hiển thị dùng màu phù hợp | SRS FR-21 |
| INV-IA01-08 | Tổng tiền | Có ₫, phân cách nghìn; không rớt chữ số hoặc sai giá trị khi trình bày | SRS FR-11, FR-21 |
| INV-IA01-09 | Ngày đặt | Giá trị đúng dữ liệu, cách trình bày nhất quán và không gây hiểu nhầm ngày/tháng | FR-11; Slide 12, 16; SRS chưa chốt locale |
| INV-IA01-10 | Badge trạng thái | Đủ 5 nhãn tiếng Việt và màu phân biệt; không chỉ có màu mà thiếu chữ | SRS FR-11 |
| INV-IA01-11 | Input/label/nút/badge | Tương phản và focus nhìn thấy được ở trạng thái thường/disabled/focus | Slide 8, 16; bổ sung tiêu chí accessibility cụ thể |
| INV-IA01-12 | Header bảng và dữ liệu | Tên cột dễ hiểu, cell thẳng hàng; phân biệt heading với dữ liệu, giá trị đúng cột | FR-11; Slide 12, 16 |

### IA-02 — Forms: 14 nội dung

| ID nguồn | Thành phần / trạng thái | Nội dung cần kiểm tra | Căn cứ |
| --- | --- | --- | --- |
| INV-IA02-01 | Prefill form | Tên/email/phone/address lấy đúng tài khoản và đúng trường | FR-04; Slide 11–12 |
| INV-IA02-02 | Email chỉ đọc | Không sửa được qua GUI hoặc thao tác bàn phím; giá trị nhận diện vẫn đọc được | FR-04 |
| INV-IA02-03 | Kiểu email | Đối chiếu type=email theo quy định chung, kể cả khi field disabled | FR-22; không coi đây là test nhập email |
| INV-IA02-04 | Nhãn và control | Nhãn gắn đúng ô để click/đọc bằng công nghệ hỗ trợ; không dùng placeholder thay nhãn | Slide 16, 18; bổ sung accessibility |
| INV-IA02-05 | Trường bắt buộc | Mọi trường thực sự bắt buộc có *; xác định rõ required trước khi chọn dữ liệu | FR-22; required tên hiện từ code |
| INV-IA02-06 | Họ tên rỗng/khoảng trắng | Xác minh quy tắc tên, required và thông báo; không coi chuỗi toàn khoảng trắng là tên hợp lệ chỉ do HTML chấp nhận | Slide 11, 19; SRS chưa quy định chi tiết |
| INV-IA02-07 | Họ tên có dấu/dài | Nhập và giữ nguyên Unicode; kiểm trình bày và lưu; không tự đặt giới hạn tối đa từ SRS | FR-04; Slide 16, 19 |
| INV-IA02-08 | Điện thoại hợp lệ | Chấp nhận chuỗi số đầu 0 dài 10 và 11; giữ số 0 đầu | FR-04; EP/BVA slide 19 |
| INV-IA02-09 | Biên độ dài điện thoại | Bộ 9/10/11/12 chữ số, cùng bắt đầu 0; đối chiếu ranh giới hợp lệ 10–11 | FR-04; BVA slide 19 |
| INV-IA02-10 | Ký tự/đầu số điện thoại | Không phải đầu 0, chữ, dấu +/gạch, khoảng trắng; làm rõ trim trước khi kết luận; không lấy regex code làm oracle | FR-04; EP slide 19 |
| INV-IA02-11 | Phone/address trống | Xác định optional/required với SRS/TA; kiểm không có dữ liệu ban đầu và khi xóa nội dung cũ | FR-04 chưa quy định bắt buộc; Slide 11 |
| INV-IA02-12 | Địa chỉ textarea | Unicode, nhiều dòng, địa chỉ dài, copy/paste; lưu đúng trường và không mất phần sau | FR-04; Slide 12, 16 |
| INV-IA02-13 | Submit/Enter | Chuột và Enter gửi đúng thay đổi, không đổi email/role; quan sát actual request khi execution | FR-04; Slide 18–19 |
| INV-IA02-14 | Cách sửa lỗi nhập | Message rõ trường/quy tắc, nằm trên submit theo SRS; có thể quay lại sửa và gửi lại | FR-22; Slide 16, 18 |

### IA-03 — Navigation: 10 nội dung

| ID nguồn | Thành phần / trạng thái | Nội dung cần kiểm tra | Căn cứ |
| --- | --- | --- | --- |
| INV-IA03-01 | Đường vào Profile | Người đã login tìm/mở được trang qua link tên trên navbar | FR-04; Slide 17 |
| INV-IA03-02 | Navbar active | Phân biệt Profile đang chọn với các trang khác; không chỉ cùng màu ở mọi route | FR-23 |
| INV-IA03-03 | Logo EShop | Quay về trang chủ đúng route và phiên được giữ | Slide 17–18 |
| INV-IA03-04 | Giỏ hàng trên header | Link đúng đích, badge đúng số lượng khi có dữ liệu; chỉ kiểm thành phần dùng chung | FR-23 |
| INV-IA03-05 | Đăng xuất | Nhãn “Đăng xuất”, thao tác thoát và đường đi tiếp dễ hiểu | FR-23; trạng thái bảo vệ sau thoát ở IA-04 |
| INV-IA03-06 | URL trực tiếp/reload | `/profile` truy cập được khi phiên hợp lệ, route không lỗi trắng/404 | FR-04; Slide 17 |
| INV-IA03-07 | Tab/Shift+Tab | Trên xuống dưới/trái sang phải; email disabled được skip; có thể đến mọi control tương tác | FR-21; Slide 18 |
| INV-IA03-08 | Keyboard link/nút | Enter kích hoạt đúng link/nút; textarea xuống dòng theo vai trò, không mắc kẹt focus | Slide 18 |
| INV-IA03-09 | Back/Forward | Trở lại Profile sau điều hướng vẫn đúng route/tài khoản và không gây nhầm dữ liệu cũ | Slide 17–18, 20 |
| INV-IA03-10 | Rời form chưa lưu | Khảo sát hành vi mất/giữ dữ liệu và dấu hiệu giúp người dùng biết chưa lưu | Slide 13–14; bổ sung, SRS không bắt dialog xác nhận |

### IA-04 — Feedback / state: 16 nội dung

| ID nguồn | Thành phần / trạng thái | Nội dung cần kiểm tra | Căn cứ |
| --- | --- | --- | --- |
| INV-IA04-01 | Chưa login | Lời nhắc rõ và không hiển thị dữ liệu hồ sơ/đơn riêng | FR-04, FR-11 |
| INV-IA04-02 | Đang khôi phục phiên | Không khiến người đã login hiểu nhầm đã mất phiên trong lúc chờ user API | Slide 13–14; bổ sung |
| INV-IA04-03 | Phiên hết hạn | Không tiếp tục hiển thị thành công hoặc dữ liệu riêng như thể phiên còn hợp lệ; có cách đăng nhập lại | FR-04, FR-11; Slide 11 |
| INV-IA04-04 | Đang lưu form | Có dấu hiệu đang xử lý trong điều kiện chậm, có thể biết thao tác đã được nhận | Slide 13–14; bổ sung |
| INV-IA04-05 | Submit liên tiếp | Hành vi bấm nhanh/lặp không tạo kết quả khó hiểu hoặc thông báo chồng nhau | Slide 13–14; bổ sung |
| INV-IA04-06 | Lưu thành công | Thông báo sau phản hồi API thành công, nội dung đủ rõ để người dùng biết đã lưu | FR-04; Slide 16, 20 |
| INV-IA04-07 | Dữ liệu sau lưu | Form/header và dữ liệu khi rời rồi mở lại/reload khớp giá trị đã lưu | FR-04; Slide 12, 14, 20 |
| INV-IA04-08 | Lưu thất bại | Không báo thành công; lỗi hữu ích và có thể thử lại | Slide 11, 16 |
| INV-IA04-09 | Giữ input khi lỗi | Không mất dữ liệu người vừa nhập sau validation/API failure | Slide 11, 14; bổ sung |
| INV-IA04-10 | Đóng alert/focus | Sau đóng thông báo vẫn biết cần sửa ở đâu, tiếp tục bằng keyboard được | Slide 13, 18; bổ sung |
| INV-IA04-11 | Đang tải lịch sử | Loading không bị diễn đạt như “không có đơn” trước khi request kết thúc | Slide 13–14; bổ sung |
| INV-IA04-12 | Empty thật | Có message thân thiện và icon/hình minh họa khi API trả rỗng | FR-24 |
| INV-IA04-13 | Lỗi tải lịch sử | Phân biệt lỗi tải với empty; có phản hồi giúp phục hồi/thử lại | Slide 11, 16; bổ sung |
| INV-IA04-14 | Đúng chủ sở hữu | Không trộn đơn hoặc hồ sơ khi đổi phiên/tài khoản; dữ liệu của phiên cũ được xử lý đúng | FR-04, FR-11; Slide 14 |
| INV-IA04-15 | Trạng thái đơn cập nhật | Hiển thị trạng thái hiện tại khi mở lại/tải lại và đúng dòng đơn | FR-11; Slide 12, 14, 20 |
| INV-IA04-16 | Dữ liệu bất thường/API chậm | Không trắng trang, không biến lỗi thành dữ liệu “đúng”; phản hồi hữu ích khi ngày/status/tổng thiếu hoặc response về chậm | Slide 11–14, 20; robustness bổ sung |

Tổng: **12 + 14 + 10 + 16 = 52 nội dung phân tích**. Đây là bản AI đề xuất trước human review; số checklist chính thức chỉ chốt sau khi loại trùng, chốt oracle, thêm bước thao tác và review của sinh viên. Chưa tính là 52 test đã chạy.

