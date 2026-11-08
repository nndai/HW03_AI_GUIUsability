# FR-04 và FR-11 — Thành phần, trạng thái và phạm vi kiểm tra GUI

Ngày khảo sát: 08/11/2026, giờ Việt Nam. Trang `/profile` là **một trang**, gồm form hồ sơ và lịch sử đơn hàng. Đây là danh mục phân tích để thiết kế checklist; 52 nội dung bên dưới chưa được thực thi đầy đủ và chưa có kết quả Passed/Failed hay review của sinh viên.

## 1. Căn cứ

| Nguồn | Nội dung áp dụng |
| --- | --- |
| [SRS FR-04](../../eshop-sut/README.md#fr-04-quản-lý-hồ-sơ-cá-nhân), dòng 62–68 | Người đã đăng nhập được cập nhật họ tên, điện thoại, địa chỉ mặc định; điện thoại bắt đầu bằng 0, dài 10–11 chữ số; email không đổi qua GUI; chỉ cập nhật bản thân, không đổi role |
| SRS FR-11, dòng 164–168 | Chỉ xem đơn của bản thân; hiển thị mã, ngày đặt, tổng tiền, trạng thái hiện tại; trạng thái tiếng Việt và phân biệt màu |
| SRS FR-21, dòng 242–248 | Tiếng Việt, màu hành động, ký hiệu ₫ và phân cách nghìn, đúng một h1, Tab theo thứ tự trên xuống dưới/trái sang phải |
| SRS FR-22, dòng 250–256 | Dấu * cho trường bắt buộc; type email; lỗi trên nút submit; password/step indicator chỉ khi có trường/luồng tương ứng |
| SRS FR-23, dòng 258–263 | Highlight trang đang chọn, badge giỏ hàng, nhãn Đăng xuất; breadcrumb bắt buộc chỉ nêu Giỏ hàng/Thanh toán/Chi tiết sản phẩm |
| SRS FR-24, dòng 265–270 | Empty state có icon/hình minh họa và thông điệp thân thiện; các quy định ảnh sản phẩm/thêm/xóa giỏ không tự áp vào form Profile |
| [Slide S13](../../S13_GUI%20Testing%20%26%20Usability%20Testing.md), trang 11–14 | Validation, default, server failure, tính cập nhật dữ liệu, đồng bộ nội dung và trạng thái control |
| Slide S13, trang 16–18 | Màu, typography, layout/alignment, label, error message; menu, link/nút và điều hướng form/focus |
| Slide S13, trang 19–22 | EP/BVA, state transition; client/server và synchronization; compatibility/platform |

Trong các bảng: **SRS** là yêu cầu đã nêu; **Slide** là vùng kiểm tra được slide hướng dẫn; **Bổ sung** là tiêu chí đề xuất cần chốt cách đánh giá trước execution. Code mô tả hiện trạng, không thay thế yêu cầu đúng.

Code đã đọc: [Profile.jsx](../../eshop-sut/frontend-web/src/pages/Profile.jsx) dòng 1–217; [AuthContext.jsx](../../eshop-sut/frontend-web/src/context/AuthContext.jsx) dòng 1–50; [App.jsx](../../eshop-sut/frontend-web/src/App.jsx) phần Header và route `/profile`; `src/index.css`, `src/main.jsx`, cấu hình Tailwind; [server.js](../../eshop-sut/backend/server.js) API `/api/users/me`, `/api/orders/my-orders` và phần hủy đơn để xác định ranh giới FR-10.

## 2. Thành phần giao diện

| Vùng | Thành phần | Trạng thái/biến thể cần tính đến | Cơ sở xác định |
| --- | --- | --- | --- |
| Khung trang | Header xanh, logo/link EShop, main, footer | Rộng/hẹp, zoom, nội dung dài, cuộn | Đã thấy trên web; App.jsx |
| Navbar | Giỏ hàng, link “Chào, {tên}”, nút “Thoát”; khi chưa login có Đăng nhập/Đăng ký | Có/không phiên; tên dài; trang đang chọn; giỏ rỗng/có sản phẩm | Đã thấy trên web; Header |
| Trạng thái chưa login | “Vui lòng đăng nhập” tại `/profile` | Chưa login, khôi phục phiên khi reload, token hết hạn | Đã thấy chưa login trên Chrome; Profile/AuthContext |
| Form hồ sơ | Tiêu đề “Hồ sơ của bạn” | Nhận diện trang và phân cấp heading | Đã thấy; code dùng h2 |
| Email | Nhãn “Email (Không đổi)”, input nền xám, disabled | Giá trị tài khoản hiện tại; không nhận chỉnh sửa; skip Tab | Đã thấy disabled; Profile |
| Họ tên | Nhãn “Họ Tên”, input text | Prefill, sửa, rỗng, khoảng trắng, Unicode/dài | Đã thấy; code có required |
| Điện thoại | Nhãn, input text, placeholder “VD: 0912345678” | Rỗng, hợp lệ theo SRS, sai ký tự/độ dài/đầu số; paste | Đã thấy; Profile.handleUpdate |
| Địa chỉ | Nhãn, textarea, placeholder “Nhập địa chỉ của bạn” | Chưa có địa chỉ, nhiều dòng, dài, Unicode, sửa/lưu lại | Đã thấy; Profile |
| Gửi form | Nút “Cập nhật” xanh dương | Idle, keyboard/chuột, submitting, lặp click, thành công/lỗi | Nút đã thấy; submitting là trạng thái cần khảo sát thêm |
| Phản hồi form | Native required của browser và JavaScript alert | Lỗi nhập, lỗi API, thành công, đóng thông báo/khôi phục focus | Code; thông báo validation được công cụ trình duyệt ghi nhận khi click |
| Lịch sử trống | Tiêu đề “Lịch sử đơn hàng”, “Bạn chưa có đơn hàng nào.” | Trống thật, đang tải, lỗi API cần phân biệt | Đã thấy trạng thái trống trên web |
| Lịch sử có dữ liệu | Table, hàng header và hàng dữ liệu | 1/nhiều đơn, số tiền/ngày khác nhau, nội dung dài, cuộn | Đã thấy 5 đơn thử |
| Cột thông tin | Mã ĐH, Ngày đặt, Tổng tiền, Trạng thái | Đúng tài khoản; dữ liệu đúng và cập nhật; định dạng | Đã thấy đầy đủ trên web |
| Trạng thái đơn | Badge có chữ và nền màu | pending, confirmed, shipping, delivered, canceled | Đã thấy đủ 5 bằng dữ liệu giả có khai báo |
| Cột thao tác | Header “Thao tác”, nút “Hủy đơn” theo từng hàng | Hiện/ẩn tùy trạng thái; thao tác thay đổi trạng thái thuộc FR-10 | Đã thấy nút; chưa click hủy, chưa mở rộng scope |

Không thấy control tìm kiếm/lọc/phân trang, link chi tiết đơn, reset form, đổi mật khẩu hay dark-mode switch trong trang này. Không tạo test cho control không tồn tại như thể đã có yêu cầu bắt buộc.

### Năm trạng thái đơn

| Giá trị | Nhãn trong code và đã thấy | Màu trong code | Việc cần kiểm tra theo FR-11 |
| --- | --- | --- | --- |
| pending | Chờ xác nhận | Vàng | Đúng đơn/nhãn/màu, dễ đọc |
| confirmed | Đã xác nhận | Indigo | Phân biệt với pending và shipping |
| shipping | Đang giao | Xanh dương | Trạng thái hiện tại, tránh chỉ dựa vào màu |
| delivered | Đã giao | Xanh lá | Đúng nhãn và dễ phân biệt trạng thái kết thúc |
| canceled | Đã hủy | Đỏ | Đúng nhãn; không nhầm với lỗi tải đơn |

Màu cụ thể theo code là hiện trạng; FR-11 yêu cầu phân biệt màu nhưng không quy định bảng màu cụ thể này. FR-10 chỉ dùng làm căn cứ nếu sau này quyết định kiểm **hủy đơn**: user chỉ hủy pending/confirmed; không hủy shipping hoặc trạng thái kết thúc. Lượt này không thực thi chuyển trạng thái.

## 3. Ma trận trạng thái cần kiểm tra

| Trạng thái | Điều kiện tạo/quan sát | Điều cần xác minh | Tình trạng khảo sát |
| --- | --- | --- | --- |
| Chưa đăng nhập | Vào URL trực tiếp không có phiên | Không lộ form/dữ liệu cá nhân; có đường đi login | Đã thấy lời nhắc, chưa kiểm hết điều hướng |
| Khôi phục phiên | Reload khi đã có token | Có thể phân biệt đang khôi phục với thực sự chưa login | Luồng AuthContext có request; chưa đo trạng thái thoáng qua |
| Phiên hết hạn | Token không hợp lệ hoặc API trả 401/403 | Thông báo và lối phục hồi; dữ liệu cũ không còn lộ | Chưa tạo |
| Hồ sơ chưa có phone/address | Tài khoản seed ban đầu | Prefill rỗng/placeholder đúng; email/name đúng | Đã thấy |
| Hồ sơ đã có dữ liệu | Seed dữ liệu giả rồi reload | Prefill đúng tên/phone/address | Đã thấy |
| Đang chỉnh sửa | Sửa một/nhiều trường, chưa gửi | Không thay dữ liệu bảng đơn; giữ dữ liệu người nhập | Chưa khảo sát đầy đủ |
| Validation họ tên | Gửi form có tên rỗng/khoảng trắng | Native validation, dấu bắt buộc và focus | Code có required; chưa thực hiện |
| Validation điện thoại | Các phân lớp/biên ở mục 5 | Kết quả theo SRS, thông điệp hướng dẫn thống nhất | Đã nhận alert khi click với mẫu 0912345678; chưa chạy bộ dữ liệu |
| Đang lưu | API chậm và click submit | Feedback chờ và chống thao tác lặp hợp lý | Chưa tạo; code chưa có biến loading riêng |
| Lưu thành công | API chấp nhận dữ liệu | Feedback, form/header đồng bộ, mở lại/reload còn đúng | Code có alert thành công; chưa thực thi |
| Lưu thất bại | Mạng/API lỗi | Lỗi có ích, không mất dữ liệu, có thể thử lại | Code có alert lỗi; chưa thực thi |
| Tải đơn | Mở trang với mạng chậm | Phân biệt pending request và rỗng thật | Chưa tạo; code khởi tạo orders=[] |
| Không có đơn thật | API trả danh sách rỗng | Message + hình/icon theo FR-24 | Đã thấy giao diện empty |
| Có đơn | API trả dữ liệu tài khoản | Đúng mã/ngày/tổng/status và các hàng | Đã thấy 5 hàng thử |
| Tải đơn thất bại | API lỗi/mất mạng | Không diễn đạt thành “chưa có đơn” nếu chưa biết | Chưa tạo; catch hiện setOrders([]), cần xác minh |
| Đơn thay đổi ngoài trang | Đổi trạng thái qua fixture riêng/API rồi mở lại | Dữ liệu mới và khả năng nhận biết cập nhật | Chưa tạo |
| Dữ liệu dài/nhiều | Tên/địa chỉ dài, nhiều đơn, số lớn | Bố cục, overflow, cuộn, performance quan sát | Chưa tạo |
| Rời trang/Back/Forward | Có thay đổi chưa lưu, điều hướng rồi quay lại | Hành vi nhất quán, tránh ngộ nhận đã lưu | Chưa tạo |

Các dòng “chưa tạo” là việc cần kiểm tra tiếp; không suy ra Passed/Failed từ code hoặc từ screenshot của trạng thái khác.

## 4. Nội dung kiểm tra theo IA-01 đến IA-04

Mỗi nội dung có một IA chính để tránh đếm trùng. Một bộ dữ liệu biên nằm trong cùng nội dung, không tách mỗi số điện thoại thành một mục để tăng số lượng.

### IA-01 — General UI standards: 12 nội dung

| STT | Thành phần / trạng thái | Nội dung cần kiểm tra | Căn cứ |
| --- | --- | --- | --- |
| 01 | Khung trang và hai vùng | Căn lề, khoảng cách, độ rộng form/bảng; không đè chồng hoặc bị footer che | Slide 16 |
| 02 | Viewport hẹp/rộng | Form và lịch sử thích ứng; bảng không làm mất cột hoặc thao tác không thể tiếp cận | Slide 21–22; cần chốt kích thước |
| 03 | Chữ trên form/bảng | Cỡ chữ, kiểu chữ, độ đậm và nhãn dễ đọc, nhất quán | Slide 16 |
| 04 | Nội dung dài/zoom | Tên, email, địa chỉ dài và zoom vẫn đọc/thao tác được; không che nút/cột | Slide 16, 22; bổ sung cách đo |
| 05 | Toàn trang | Tiếng Việt nhất quán và đúng dấu, kể cả nhãn/thông báo/state | SRS FR-21 |
| 06 | Tiêu đề trang | Đúng một h1 mô tả nội dung; hai phần có hierarchy phù hợp | SRS FR-21 |
| 07 | Nút hành động | “Cập nhật” dùng màu tích cực xanh; thao tác nguy hiểm đang hiển thị dùng màu phù hợp | SRS FR-21 |
| 08 | Tổng tiền | Có ₫, phân cách nghìn; không rớt chữ số hoặc sai giá trị khi trình bày | SRS FR-11, FR-21 |
| 09 | Ngày đặt | Giá trị đúng dữ liệu, cách trình bày nhất quán và không gây hiểu nhầm ngày/tháng | FR-11; Slide 12, 16; SRS chưa chốt locale |
| 10 | Badge trạng thái | Đủ 5 nhãn tiếng Việt và màu phân biệt; không chỉ có màu mà thiếu chữ | SRS FR-11 |
| 11 | Input/label/nút/badge | Tương phản và focus nhìn thấy được ở trạng thái thường/disabled/focus | Slide 8, 16; bổ sung tiêu chí accessibility cụ thể |
| 12 | Header bảng và dữ liệu | Tên cột dễ hiểu, cell thẳng hàng; phân biệt heading với dữ liệu, giá trị đúng cột | FR-11; Slide 12, 16 |

### IA-02 — Forms: 14 nội dung

| STT | Thành phần / trạng thái | Nội dung cần kiểm tra | Căn cứ |
| --- | --- | --- | --- |
| 01 | Prefill form | Tên/email/phone/address lấy đúng tài khoản và đúng trường | FR-04; Slide 11–12 |
| 02 | Email chỉ đọc | Không sửa được qua GUI hoặc thao tác bàn phím; giá trị nhận diện vẫn đọc được | FR-04 |
| 03 | Kiểu email | Đối chiếu type=email theo quy định chung, kể cả khi field disabled | FR-22; không coi đây là test nhập email |
| 04 | Nhãn và control | Nhãn gắn đúng ô để click/đọc bằng công nghệ hỗ trợ; không dùng placeholder thay nhãn | Slide 16, 18; bổ sung accessibility |
| 05 | Trường bắt buộc | Mọi trường thực sự bắt buộc có *; xác định rõ required trước khi chọn dữ liệu | FR-22; required tên hiện từ code |
| 06 | Họ tên rỗng/khoảng trắng | Xác minh quy tắc tên, required và thông báo; không coi chuỗi toàn khoảng trắng là tên hợp lệ chỉ do HTML chấp nhận | Slide 11, 19; SRS chưa quy định chi tiết |
| 07 | Họ tên có dấu/dài | Nhập và giữ nguyên Unicode; kiểm trình bày và lưu; không tự đặt giới hạn tối đa từ SRS | FR-04; Slide 16, 19 |
| 08 | Điện thoại hợp lệ | Chấp nhận chuỗi số đầu 0 dài 10 và 11; giữ số 0 đầu | FR-04; EP/BVA slide 19 |
| 09 | Biên độ dài điện thoại | Bộ 9/10/11/12 chữ số, cùng bắt đầu 0; đối chiếu ranh giới hợp lệ 10–11 | FR-04; BVA slide 19 |
| 10 | Ký tự/đầu số điện thoại | Không phải đầu 0, chữ, dấu +/gạch, khoảng trắng; làm rõ trim trước khi kết luận; không lấy regex code làm oracle | FR-04; EP slide 19 |
| 11 | Phone/address trống | Xác định optional/required với SRS/TA; kiểm không có dữ liệu ban đầu và khi xóa nội dung cũ | FR-04 chưa quy định bắt buộc; Slide 11 |
| 12 | Địa chỉ textarea | Unicode, nhiều dòng, địa chỉ dài, copy/paste; lưu đúng trường và không mất phần sau | FR-04; Slide 12, 16 |
| 13 | Submit/Enter | Chuột và Enter gửi đúng thay đổi, không đổi email/role; quan sát actual request khi execution | FR-04; Slide 18–19 |
| 14 | Cách sửa lỗi nhập | Message rõ trường/quy tắc, nằm trên submit theo SRS; có thể quay lại sửa và gửi lại | FR-22; Slide 16, 18 |

### IA-03 — Navigation: 10 nội dung

| STT | Thành phần / trạng thái | Nội dung cần kiểm tra | Căn cứ |
| --- | --- | --- | --- |
| 01 | Đường vào Profile | Người đã login tìm/mở được trang qua link tên trên navbar | FR-04; Slide 17 |
| 02 | Navbar active | Phân biệt Profile đang chọn với các trang khác; không chỉ cùng màu ở mọi route | FR-23 |
| 03 | Logo EShop | Quay về trang chủ đúng route và phiên được giữ | Slide 17–18 |
| 04 | Giỏ hàng trên header | Link đúng đích, badge đúng số lượng khi có dữ liệu; chỉ kiểm thành phần dùng chung | FR-23 |
| 05 | Đăng xuất | Nhãn “Đăng xuất”, thao tác thoát và đường đi tiếp dễ hiểu | FR-23; trạng thái bảo vệ sau thoát ở IA-04 |
| 06 | URL trực tiếp/reload | `/profile` truy cập được khi phiên hợp lệ, route không lỗi trắng/404 | FR-04; Slide 17 |
| 07 | Tab/Shift+Tab | Trên xuống dưới/trái sang phải; email disabled được skip; có thể đến mọi control tương tác | FR-21; Slide 18 |
| 08 | Keyboard link/nút | Enter kích hoạt đúng link/nút; textarea xuống dòng theo vai trò, không mắc kẹt focus | Slide 18 |
| 09 | Back/Forward | Trở lại Profile sau điều hướng vẫn đúng route/tài khoản và không gây nhầm dữ liệu cũ | Slide 17–18, 20 |
| 10 | Rời form chưa lưu | Khảo sát hành vi mất/giữ dữ liệu và dấu hiệu giúp người dùng biết chưa lưu | Slide 13–14; bổ sung, SRS không bắt dialog xác nhận |

### IA-04 — Feedback / state: 16 nội dung

| STT | Thành phần / trạng thái | Nội dung cần kiểm tra | Căn cứ |
| --- | --- | --- | --- |
| 01 | Chưa login | Lời nhắc rõ và không hiển thị dữ liệu hồ sơ/đơn riêng | FR-04, FR-11 |
| 02 | Đang khôi phục phiên | Không khiến người đã login hiểu nhầm đã mất phiên trong lúc chờ user API | Slide 13–14; bổ sung |
| 03 | Phiên hết hạn | Không tiếp tục hiển thị thành công hoặc dữ liệu riêng như thể phiên còn hợp lệ; có cách đăng nhập lại | FR-04, FR-11; Slide 11 |
| 04 | Đang lưu form | Có dấu hiệu đang xử lý trong điều kiện chậm, có thể biết thao tác đã được nhận | Slide 13–14; bổ sung |
| 05 | Submit liên tiếp | Hành vi bấm nhanh/lặp không tạo kết quả khó hiểu hoặc thông báo chồng nhau | Slide 13–14; bổ sung |
| 06 | Lưu thành công | Thông báo sau phản hồi API thành công, nội dung đủ rõ để người dùng biết đã lưu | FR-04; Slide 16, 20 |
| 07 | Dữ liệu sau lưu | Form/header và dữ liệu khi rời rồi mở lại/reload khớp giá trị đã lưu | FR-04; Slide 12, 14, 20 |
| 08 | Lưu thất bại | Không báo thành công; lỗi hữu ích và có thể thử lại | Slide 11, 16 |
| 09 | Giữ input khi lỗi | Không mất dữ liệu người vừa nhập sau validation/API failure | Slide 11, 14; bổ sung |
| 10 | Đóng alert/focus | Sau đóng thông báo vẫn biết cần sửa ở đâu, tiếp tục bằng keyboard được | Slide 13, 18; bổ sung |
| 11 | Đang tải lịch sử | Loading không bị diễn đạt như “không có đơn” trước khi request kết thúc | Slide 13–14; bổ sung |
| 12 | Empty thật | Có message thân thiện và icon/hình minh họa khi API trả rỗng | FR-24 |
| 13 | Lỗi tải lịch sử | Phân biệt lỗi tải với empty; có phản hồi giúp phục hồi/thử lại | Slide 11, 16; bổ sung |
| 14 | Đúng chủ sở hữu | Không trộn đơn hoặc hồ sơ khi đổi phiên/tài khoản; dữ liệu của phiên cũ được xử lý đúng | FR-04, FR-11; Slide 14 |
| 15 | Trạng thái đơn cập nhật | Hiển thị trạng thái hiện tại khi mở lại/tải lại và đúng dòng đơn | FR-11; Slide 12, 14, 20 |
| 16 | Dữ liệu bất thường/API chậm | Không trắng trang, không biến lỗi thành dữ liệu “đúng”; phản hồi hữu ích khi ngày/status/tổng thiếu hoặc response về chậm | Slide 11–14, 20; robustness bổ sung |

Tổng: **12 + 14 + 10 + 16 = 52 nội dung phân tích**. Đây là bản AI đề xuất trước human review; số checklist chính thức chỉ chốt sau khi loại trùng, chốt oracle, thêm bước thao tác và review của sinh viên. Chưa tính là 52 test đã chạy.

## 5. Dữ liệu và các điểm cần làm rõ trước execution

- **EP/BVA phone:** đầu 0 dài 9/10/11/12; thêm chuỗi số không đầu 0, có chữ, khoảng trắng và ký hiệu. 10/11 chữ số đầu 0 là expected hợp lệ theo FR-04. Không dùng regex `^[1-9][0-9]{8,9}$` hiện có làm kỳ vọng.
- **Hồ sơ:** chưa có/đã có phone/address; tên có dấu; tên rỗng/toàn khoảng trắng; địa chỉ nhiều dòng/dài. SRS chưa nói tên/address tối đa bao nhiêu hoặc phone/address bắt buộc; không tự đặt giới hạn rồi ghi Failed.
- **Đơn hàng:** 0, 1, nhiều đơn; đủ 5 trạng thái; đơn của tài khoản khác; tiền lớn/nhỏ và ngày khác nhau. ID giảm dần là hiện trạng query, FR-11 chưa bắt buộc thứ tự cụ thể.
- **State transition:** logged-out → logged-in → đang sửa → validation hoặc submitting → success/error → mở lại; orders loading → có dữ liệu/empty/error. Những state chưa có UI riêng vẫn cần thiết kế kiểm tra để nhận ra thiếu feedback.
- **Không áp cứng:** breadcrumb ở Profile, password field, step indicator, tìm/lọc/phân trang, dark mode/RTL. Chỉ thêm vào khi chốt yêu cầu/tiêu chí mở rộng, không mặc định là vi phạm FR-04/FR-11.
- **Giới hạn scope:** quyền cập nhật bản thân/không đổi role là yêu cầu FR-04; kiểm API bảo mật sâu là phần bổ trợ riêng, không biến nhiều payload API thành nhiều mục GUI. Tương tự, hủy đơn thuộc FR-10 và chưa đưa vào flow usability.

## 6. Ghi nhận khảo sát thực tế và giới hạn

- Đã dùng Chrome/Windows xem trực tiếp `/profile` khi chưa login. Điều khiển cửa sổ sau đó gặp lỗi “failed to activate captured window”; đã chuyển sang trình duyệt tích hợp để xem trang đã login.
- Backend gốc import `database.js` sẽ drop/reseed khi khởi động. Lượt này dùng bản sao `server.js`/`database.js` trong `.git/sut-runtime`, database riêng; không chạy seed lên database gốc.
- Cổng 3000 bị `EACCES`. Bản chạy khảo sát dùng API `http://localhost:13000` và web `http://localhost:5175`. Server chỉ đổi hằng PORT; [survey-vite.mjs](../scripts/survey-vite.mjs) chỉ thay URL API khi phục vụ JSX. Không sửa validation, UI hoặc nghiệp vụ để tạo kết quả.
- Sau quan sát empty, [seed_survey_data.py](../scripts/seed_survey_data.py) tạo **dữ liệu giả được khai báo**: phone/address thử, 5 đơn đủ status của Test User và 1 đơn của tài khoản khác. Đã reload và quan sát bảng. Đây là setup, không phải tạo đơn qua GUI hay dữ liệu participant.
- Click Cập nhật với phone `0912345678` nhận alert “Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.” Công cụ dừng tại alert; chụp ảnh alert và kết nối lại bị timeout. Chỉ có ghi nhận text từ công cụ, **không có ảnh validation**; không xem là đã hoàn thành execution cho bộ phone hoặc flow cập nhật.
- Ảnh thật đã lưu: [profile-empty.jpg](../evidence/survey/profile-empty.jpg), [profile-orders.jpg](../evidence/survey/profile-orders.jpg). Ảnh chỉ phục vụ khảo sát, chưa có overlay email/MSSV/họ tên theo đề nên không dùng làm bằng chứng Task 3 chính thức.
- Chưa kiểm màn hình hẹp/zoom, ba nền tảng, loading/network error, success/persistence, nhiều tài khoản qua GUI hoặc accessibility đầy đủ. Những nội dung đó vẫn để kế hoạch kiểm tra.
- Lượt này chưa viết bug report; phần này mô tả phạm vi và khả năng quan sát để sinh viên tiếp tục kiểm, tự viết report và review theo policy.
