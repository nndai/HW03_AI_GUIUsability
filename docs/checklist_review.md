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
