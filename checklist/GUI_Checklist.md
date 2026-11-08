# HW03 - GUI Checklist FR-04 và FR-11

Phiên bản 2.0 - ngày 08/11/2026. Có 41 mục chính thức, ID liên tục GUI-001 đến GUI-041. Chưa thực thi.

## 1. Phạm vi và cách ghi kết quả

Một trang /profile gồm hồ sơ FR-04, lịch sử đơn FR-11 và thành phần navbar liên quan. Không kiểm thao tác hủy đơn FR-10 hoặc checkout.

- IA-01: 11 mục; IA-02: 10 mục; IA-03: 9 mục; IA-04: 11 mục.
- Mọi mục đều có thao tác, dữ liệu, kết quả mong đợi và căn cứ. SRS là yêu cầu hệ thống; S13 là slide môn học; B01–B08 là quy ước kiểm tra của bài, không tự coi là điều khoản SRS.
- Chưa chạy thì để Chưa chạy. Chỉ ghi Passed khi mọi biến thể bắt buộc đã chạy và đạt; có biến thể lỗi thì Failed, nêu biến thể và actual trong Notes. Bị chặn bởi bước trước thì giữ Chưa chạy và ghi blocker.
- Failed phải có Notes và ảnh thật; bug report do sinh viên tự viết. Ảnh/Issue dùng đường dẫn trong gói nộp và ID/link GitHub tương ứng; không bắt chụp ảnh Passed.
- Chạy cùng 41 mục trên ít nhất 3 nền tảng. Workbook có 123 lượt dự kiến ở Execution, không tính thành 123 mục thiết kế khác nhau. Chốt browser/OS/device/version và lưu từng run riêng.
- Bảng Markdown là mẫu một run. Kết quả theo môi trường nhập tại Execution; sau kiểm thử cập nhật báo cáo và PDF từ dữ liệu thực.

## 2. Thông tin run

| Trường | Giá trị |
| --- | --- |
| Họ tên / MSSV / email sinh viên | Chưa cung cấp |
| Người thực thi / ngày giờ | Chưa thực hiện |
| Browser / version / OS / device | Chưa điền |
| URL frontend / backend | Ghi đúng môi trường thực tế; khảo sát trước dùng localhost:5175 / localhost:13000 |
| SUT commit | 85af3ba875c88283615e22cb108f13e2fccaf0e9; ghi thêm thay đổi cục bộ và port của run |
| Viewport / zoom / locale / timezone | Chưa điền |
| Baseline / fixture | Chưa chuẩn bị cho lần chạy chính thức |

## 3. Dữ liệu kiểm tra

| Fixture | Nội dung |
| --- | --- |
| A, B | Hai tài khoản thử có profile, email, role và đơn khác nhau; biết trước giá trị chuẩn; dùng thông tin giả |
| A0 | Tài khoản không có đơn; GET danh sách thành công trả [] |
| P | 091234567 / 0912345678 / 09123456789 / 091234567890; chỉ 10–11 chữ số đầu 0 hợp lệ |
| V | Nguyễn Văn Mẫu; phone 0912345678; địa chỉ 123 Đường Thử Nghiệm, Phường Mẫu / Thành phố Thử Nghiệm, nhập hai dòng để quan sát nội dung |
| O | Đơn đủ 5 status; tiền 0, 1234567, 123456789; ngày có ngày lớn hơn 12; có đơn của B không được thấy khi A login |
| Chậm/lỗi | Delay GET 3 giây, API 500 hoặc network offline trong môi trường thử riêng; ghi cách tạo và khôi phục |

## 4. Checklist chính thức

| ID | IA | Thành phần / trạng thái | Thao tác và dữ liệu | Kết quả mong đợi | Căn cứ | Kết quả | Notes | Ảnh / Issue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GUI-001 | IA-01 | Bố cục mặc định | Đăng nhập A, mở /profile tại 1366×768, zoom 100%; xem từ header đến footer. | Form và lịch sử tách thành hai vùng có tiêu đề; không chồng chữ/control; footer không che nội dung hay nút. | S13 tr.16; B01 | Chưa chạy |  |  |
| GUI-002 | IA-01 | Bố cục responsive | Mở cùng dữ liệu tại 390×844, 768×1024 và 1366×768; cuộn đến cuối form/bảng. | Mọi trường, nút và 4 cột dữ liệu đơn đều tiếp cận được; cho phép cuộn bảng ngang nhưng không có nội dung bị cắt không thể xem. | S13 tr.21–22; B01 | Chưa chạy |  |  |
| GUI-003 | IA-01 | Chữ và khả năng đọc | Xem các nhãn form, input và hàng bảng ở zoom 100%, dùng dữ liệu có dấu. | Chữ và nhãn đọc được, không mất dấu/ký tự hoặc cắt nét chữ; phân biệt được tiêu đề với nội dung. | S13 tr.16; B02 | Chưa chạy |  |  |
| GUI-004 | IA-01 | Ngôn ngữ | Đọc nhãn, tiêu đề, nút, message và trạng thái do SUT hiển thị trong các bước checklist. | Nội dung SUT dùng tiếng Việt có dấu nhất quán, trừ thuật ngữ kỹ thuật chuẩn và dữ liệu tài khoản do người dùng đặt; không chấm ngôn ngữ UI của browser. | SRS FR-21 | Chưa chạy |  |  |
| GUI-005 | IA-01 | Tiêu đề và hierarchy | Mở /profile; đối chiếu heading thấy trên trang với DOM chỉ đọc. | Có đúng 1 h1 mô tả trang; hai phần hồ sơ/lịch sử có heading phân biệt; không lấy tên tab browser thay cho h1. | SRS FR-21 | Chưa chạy |  |  |
| GUI-006 | IA-01 | Màu nút hành động | Xem Cập nhật và nút nguy hiểm nếu đang hiển thị, ở trạng thái idle. | Cập nhật có màu hành động xanh dương; nút nguy hiểm/hủy dùng đỏ; không bắt buộc mã hex cụ thể, không thực hiện hủy đơn. | SRS FR-21 | Chưa chạy |  |  |
| GUI-007 | IA-01 | Định dạng tổng tiền | Nạp fixture O; đối chiếu tiền từng đơn 0, 1234567, 123456789 với dữ liệu chuẩn. | Mỗi số tiền giữ đúng giá trị, có ký hiệu ₫ và phân cách nghìn. | SRS FR-11,FR-21 | Chưa chạy |  |  |
| GUI-008 | IA-01 | Ngày đặt | Nạp O với ngày 2026-03-14 12:00:00 và 2026-11-05 12:00:00; ghi locale/timezone của browser. | Ngày hiển thị đúng ngày/tháng/năm nguồn và theo cùng locale đã ghi; không hiển thị Invalid Date. SRS không bắt buộc dd/MM/yyyy. | SRS FR-11; S13 tr.12,16; B03 | Chưa chạy |  |  |
| GUI-009 | IA-01 | Nhãn và màu trạng thái đơn | Nạp O đủ pending/confirmed/shipping/delivered/canceled; so sánh từng badge. | Có nhãn tiếng Việt đúng nghĩa cho cả 5 trạng thái và màu phân biệt; vẫn đọc được trạng thái bằng chữ; không bắt bảng màu code hiện tại làm chuẩn duy nhất. | SRS FR-11 | Chưa chạy |  |  |
| GUI-010 | IA-01 | Focus nhìn thấy và khả năng đọc | Dùng Tab đến từng link/nút/input có thể tương tác; so sánh trước/sau focus ở zoom 100%. | Vị trí focus có thay đổi outline/border/background nhìn thấy được; chữ/nhãn vẫn đọc được trên nền thường và disabled. Đây là review định tính, chưa tuyên bố đạt tỷ lệ WCAG. | S13 tr.8,13,16; B04 | Chưa chạy |  |  |
| GUI-011 | IA-01 | Cấu trúc bảng và đúng cột | Nạp O; đối chiếu mỗi hàng với cặp ID/ngày/tổng/status trong fixture. | Có header nhận diện Mã đơn, Ngày đặt, Tổng tiền, Trạng thái; giá trị thuộc đúng cột và đúng cùng một đơn; không lệch hàng. | SRS FR-11; S13 tr.12,16 | Chưa chạy |  |  |
| GUI-012 | IA-02 | Giá trị ban đầu của form | Đăng nhập A có tên/phone/address đã biết; mở /profile mới. | Email, tên, điện thoại, địa chỉ đúng A và đúng trường; không lấy dữ liệu B hoặc placeholder làm giá trị thật. | SRS FR-04; S13 tr.11–12 | Chưa chạy |  |  |
| GUI-013 | IA-02 | Email chỉ đọc và đúng loại field | Thử click/gõ/paste vào email; xem thuộc tính type qua DOM chỉ đọc. | Email vẫn đúng tài khoản và không đổi qua GUI; field email có type=email theo FR-22 dù đang disabled/readonly. Không thử validate email nhập mới. | SRS FR-04,FR-22 | Chưa chạy |  |  |
| GUI-014 | IA-02 | Nhãn và tên truy cập của control | Xem nhãn Tên/Điện thoại/Địa chỉ và accessible name của từng control. | Nhãn diễn đạt đúng trường; control có tên truy cập đúng vai trò qua label/aria-label/aria-labelledby; placeholder không thay nhãn. | S13 tr.16,18; B05 | Chưa chạy |  |  |
| GUI-015 | IA-02 | Dấu trường bắt buộc | Ghi các trường đang được form khai báo required hoặc tài liệu đã chốt là bắt buộc; so sánh nhãn. | Mỗi trường được xác định bắt buộc đều có * cạnh nhãn. Mục này không tự kết luận phone/address bắt buộc hay tên toàn khoảng trắng hợp lệ. | SRS FR-22; S13 tr.11 | Chưa chạy |  |  |
| GUI-016 | IA-02 | Cập nhật tên tiếng Việt | Giữ phone hợp lệ; đổi tên A thành Nguyễn Văn Mẫu, lưu và mở lại. | Tên được cập nhật đúng dấu/ký tự và đúng tài khoản; không thay email/role. Không suy ra giới hạn tên dài từ dữ liệu mẫu. | SRS FR-04 | Chưa chạy |  |  |
| GUI-017 | IA-02 | Biên độ dài điện thoại | Lần lượt gửi P: 091234567 (9), 0912345678 (10), 09123456789 (11), 091234567890 (12); trường khác hợp lệ. | 10/11 chữ số đầu 0 được chấp nhận và giữ số 0 đầu; 9/12 chữ số bị từ chối, không thay dữ liệu đã lưu bằng giá trị sai. Ghi actual từng biến thể. | SRS FR-04; S13 tr.19 EP/BVA | Chưa chạy |  |  |
| GUI-018 | IA-02 | Phân lớp điện thoại sai | Gửi 1912345678, 09a2345678, 09123-5678, +84912345678; giữ trường khác hợp lệ. | Không lưu các chuỗi có đầu số khác 0 hoặc chứa ký tự không phải chữ số. Các quyết định trim khoảng trắng được tách khỏi mục này. | SRS FR-04; S13 tr.19 EP | Chưa chạy |  |  |
| GUI-019 | IA-02 | Nội dung địa chỉ | Giữ tên/phone hợp lệ; nhập địa chỉ V có tiếng Việt, 2 dòng và dấu phẩy; lưu rồi mở lại. | Địa chỉ mặc định sau tải lại còn đủ từ, chữ số và dấu; không bị chuyển sang trường khác. Không tự quy định maxLength. | SRS FR-04; S13 tr.12,20 | Chưa chạy |  |  |
| GUI-020 | IA-02 | Gửi đúng thay đổi hồ sơ bằng chuột | Từ baseline A, đổi tên/phone/address hợp lệ; click Cập nhật một lần; đối chiếu bản lưu và request chỉ đọc. | Ba trường cập nhật đúng A; email/role không thay đổi và hồ sơ B giữ nguyên. Không gửi payload sửa role hoặc kiểm sâu API trong checklist GUI. | SRS FR-04 | Chưa chạy |  |  |
| GUI-021 | IA-02 | Nội dung và vị trí lỗi nhập | Gửi 091234567 (9 số) rồi quan sát message và vùng trên Cập nhật. | Có lỗi nhận diện trường điện thoại và hướng dẫn quy tắc đầu 0, 10–11 số; lỗi hiển thị trong form phía trên submit theo FR-22; không chỉ kết luận từ alert ngoài form. | SRS FR-04,FR-22; S13 tr.16,18 | Chưa chạy |  |  |
| GUI-022 | IA-03 | Tìm và mở Profile | Bắt đầu ở Home đã đăng nhập A; dùng link tài khoản trên navbar. | Mở được /profile và nhận diện được hai phần hồ sơ/lịch sử của A; không cần tự gõ URL để hoàn thành đường đi này. | SRS FR-04; S13 tr.17 | Chưa chạy |  |  |
| GUI-023 | IA-03 | Navbar đang chọn | Từ Home vào /profile rồi trở lại Home; so sánh dấu chọn của link tài khoản. | Navbar có dấu highlight phân biệt trang hiện tại; không coi màu cố định giống nhau trên mọi route là bằng chứng active. | SRS FR-23 | Chưa chạy |  |  |
| GUI-024 | IA-03 | Logo về Home | Từ /profile đã login A, click EShop. | Đến đúng route /; phiên A vẫn còn, không tự đăng xuất hoặc sửa hồ sơ. | S13 tr.17–18; B06 | Chưa chạy |  |  |
| GUI-025 | IA-03 | Link và badge giỏ hàng chung | Chuẩn bị giỏ 0 rồi 3 sản phẩm khác nhau, mỗi loại số lượng 1; xem navbar tại Profile và mở Giỏ hàng. | Link đi đúng /cart; badge phản ánh 3 khi có 3 sản phẩm; với 0 cho phép ẩn hoặc hiển thị 0. Không đánh giá flow checkout. | SRS FR-23; B06 | Chưa chạy |  |  |
| GUI-026 | IA-03 | Nhãn và đường thoát | Tại Profile đã login A, xem nhãn nút và kích hoạt đăng xuất. | Nút mang nhãn Đăng xuất; sau click navbar trở về các lựa chọn chưa login. Bảo vệ dữ liệu kiểm tiếp tại GUI-031. | SRS FR-23; S13 tr.17 | Chưa chạy |  |  |
| GUI-027 | IA-03 | URL trực tiếp và reload | Khi phiên A hợp lệ, mở /profile trực tiếp rồi reload. | Route tải được, cuối quá trình hiển thị form/lịch sử của A, không lỗi 404 hoặc trắng trang; không dùng việc này thay test persistence GUI-034. | SRS FR-04; S13 tr.17 | Chưa chạy |  |  |
| GUI-028 | IA-03 | Thứ tự Tab và Shift+Tab | Từ đầu trang nhấn Tab qua navbar, form và control đang hiển thị; đi ngược bằng Shift+Tab. | Focus theo thứ tự trên xuống dưới/trái sang phải, không vòng kẹt; đến mọi control tương tác; skip email khi thực sự disabled, readonly được phép focus. | SRS FR-21; S13 tr.18 | Chưa chạy |  |  |
| GUI-029 | IA-03 | Kích hoạt bằng bàn phím | Dùng Enter trên link; Enter/Space trên nút; Enter trong textarea; gửi dữ liệu hợp lệ từ nút Cập nhật. | Link/nút thực hiện đúng hành động; Enter trong textarea thêm dòng, không gửi nhầm; có thể cập nhật qua keyboard. Không bắt Enter trong mọi input phải submit. | S13 tr.18; B06 | Chưa chạy |  |  |
| GUI-030 | IA-03 | Back và Forward | Lưu/không sửa form; điều hướng Profile → Home; Back rồi Forward. | Đến đúng các route trong lịch sử, phiên/tài khoản không đổi và dữ liệu đã lưu không bị thay bởi bản cũ. Không đánh giá bản nháp chưa lưu ở mục này. | S13 tr.17–18,20; B06 | Chưa chạy |  |  |
| GUI-031 | IA-04 | Bảo vệ khi thiếu hoặc hết hiệu lực phiên | Lần lượt dùng phiên không token và token không hợp lệ; mở Profile, thử Back sau đăng xuất. | Không lộ hồ sơ/đơn riêng, không báo thao tác thành công như đang login; có thông báo/đường đăng nhập lại. Ghi riêng kết quả từng điều kiện. | SRS FR-04,FR-11; S13 tr.11; B07 | Chưa chạy |  |  |
| GUI-032 | IA-04 | Đang khôi phục phiên | Reload khi token hợp lệ; làm chậm GET /users/me 3 giây trong môi trường thử. | Trong lúc chưa biết kết quả có dấu chờ trung tính, không khẳng định đã mất phiên; khi API thành công hiện đúng A. 3 giây là điều kiện gây chậm, không phải SLA. | S13 tr.13–14; B07 | Chưa chạy |  |  |
| GUI-033 | IA-04 | Phản hồi lưu thành công | Gửi dữ liệu hợp lệ và chờ phản hồi API thành công. | Chỉ sau khi request thành công mới có thông báo xác nhận đã cập nhật; không báo lỗi cho lần lưu đó. Cơ chế alert/toast/inline đều được ở nhánh success. | SRS FR-04; S13 tr.16,20 | Chưa chạy |  |  |
| GUI-034 | IA-04 | Đồng bộ và giữ dữ liệu sau lưu | Lưu tên/phone/address mới; xem form/navbar, rời Profile rồi mở lại và reload. | Tên trên navbar và dữ liệu form khớp bản đã lưu; các giá trị vẫn đúng sau mở lại/reload. Không dùng dữ liệu chỉ còn trong React state làm bằng chứng lưu. | SRS FR-04; S13 tr.12,14,20 | Chưa chạy |  |  |
| GUI-035 | IA-04 | Phản hồi lỗi lưu | Gây PUT trả 500 hoặc mất mạng trong môi trường thử, gửi dữ liệu hợp lệ. | Không có thông báo thành công; có lỗi cho biết chưa lưu hoặc chưa xác nhận được kết quả và hướng thử lại; có thể gửi lại sau phục hồi mạng. | S13 tr.11,16; B08 | Chưa chạy |  |  |
| GUI-036 | IA-04 | Focus sau đóng thông báo | Dùng keyboard gây validation, đóng thông báo nếu có, rồi tiếp tục Tab/nhập sửa phone. | Focus trở về trang, có thể tiếp cận trường lỗi và sửa/gửi lại bằng keyboard; không mắc kẹt trong dialog hoặc mất khả năng thao tác. | S13 tr.13,18; B04 | Chưa chạy |  |  |
| GUI-037 | IA-04 | Đang tải danh sách đơn | Làm chậm GET my-orders 3 giây, mở Profile với tài khoản có đơn. | Trong lúc chờ có loading/dấu đang lấy dữ liệu; chưa hiển thị khẳng định không có đơn; sau thành công chuyển sang bảng dữ liệu. | S13 tr.13–14; B07 | Chưa chạy |  |  |
| GUI-038 | IA-04 | Empty state thực sự | Dùng A0 không có đơn; chờ GET my-orders thành công trả []. | Có message thân thiện cho biết chưa có đơn và icon/hình minh họa; không hiển thị hàng đơn giả hoặc thông báo lỗi tải. | SRS FR-24; S13 tr.16 | Chưa chạy |  |  |
| GUI-039 | IA-04 | Lỗi tải lịch sử và phục hồi | Làm GET my-orders trả 500, rồi phục hồi API và reload/thử lại. | Khi lỗi có thông báo không tải được đơn, không đồng nhất với chưa có đơn; sau phục hồi có thể lấy và hiển thị dữ liệu thật. Không bắt buộc phải có nút Retry riêng. | S13 tr.11,16,20; B08 | Chưa chạy |  |  |
| GUI-040 | IA-04 | Chuyển tài khoản và cô lập dữ liệu | A và B có profile/đơn khác nhau; xem A, logout, login B, mở Profile rồi Back/Forward. | Chỉ profile và đơn của tài khoản hiện tại xuất hiện; không giữ flash/cache dữ liệu riêng A trong phiên B; mọi hàng khớp fixture theo chủ sở hữu. | SRS FR-04,FR-11; S13 tr.14 | Chưa chạy |  |  |
| GUI-041 | IA-04 | Trạng thái đơn thay đổi bên ngoài | Ghi baseline một đơn pending; đổi fixture riêng thành confirmed, không bấm Hủy đơn; mở lại/reload Profile. | Cùng mã đơn hiển thị nhãn/màu trạng thái confirmed mới; không làm thay đổi đơn khác. Không bắt buộc realtime/polling khi chưa reload. | SRS FR-11; S13 tr.12,14,20 | Chưa chạy |  |  |

## 5. Quy ước kiểm tra

- **B01:** Môi trường layout đề xuất: viewport CSS 390×844, 768×1024, 1366×768; zoom 100%. Cuộn bảng ngang hợp lệ nếu vẫn tiếp cận đủ nội dung. Đây là phạm vi kiểm thử, không phải số đo trong SRS.
- **B02:** Typography đề xuất: chữ và nhãn đọc được, không glyph thiếu/cắt; phân biệt tiêu đề và nội dung. Không yêu cầu font-family/font-size giống tuyệt đối hoặc tự đặt minimum 14/16 px.
- **B03:** Ghi locale và timezone cho mỗi run. Chấp nhận cách trình bày theo locale nếu giá trị ngày đúng và nhất quán; không tự bắt dd/MM/yyyy.
- **B04:** Focus/readability là review định tính theo slide: có dấu focus thấy được và thao tác tiếp được. Không dùng kết quả này chứng nhận accessibility hoặc tỷ lệ contrast.
- **B05:** Nhãn và accessible name phải diễn đạt đúng control; chấp nhận label/aria-label/aria-labelledby. Không yêu cầu click nhãn phải chuyển focus.
- **B06:** Quy ước thao tác GUI: link/nút đúng vai trò, giữ phiên trên điều hướng thường; giỏ 3 loại ×1 để không tranh luận badge đếm dòng hay số lượng. Không yêu cầu Enter trong mọi input submit.
- **B07:** Khôi phục phiên/loading phân biệt với logged-out/empty/error. Delay 3 giây chỉ để trạng thái đủ quan sát, không là yêu cầu tốc độ phản hồi.
- **B08:** Đề xuất phục hồi lỗi: message đúng loại lỗi, không báo thành công giả, thử lại được. Không bắt cụ thể HTTP error text hoặc nút Retry riêng.

## 6. Căn cứ

- SRS EShop, README.md: FR-04 dòng 62–68; FR-11 dòng 164–168; FR-21 dòng 242–248; FR-22 dòng 250–256; FR-23 dòng 258–263; FR-24 dòng 265–270. Bản đọc ngày 08/11/2026. Code nhận diện control/trạng thái, không thay SRS làm expected.
- Slide S13 GUI Testing & Usability Testing: trang 8, 11–14, 16–22; số trang theo PDF. Áp dụng checklist, navigation, EP/BVA, state transition và synchronization.
- HW03 §6 Task 1/3, §14: hơn 40 mục, đủ bốn IA, Passed/Failed, Notes/ảnh Failed, thực thi trên ít nhất 3 nền tảng; Excel và báo cáo Markdown/PDF.
- Chỉ 41 hàng tại mục 4 thuộc checklist chính thức. Bản nháp, mục bị loại và bảng đổi ID được lưu riêng trong phu_luc/AI_Review.md để audit, không tham gia execution hoặc mẫu số thống kê.

## 7. Test summary

| IA | Thiết kế | Lượt dự kiến | Đã chạy | Passed | Failed |
| --- | ---: | ---: | ---: | ---: | ---: |
| IA-01 | 11 | 33 | 0 | 0 | 0 |
| IA-02 | 10 | 30 | 0 | 0 | 0 |
| IA-03 | 9 | 27 | 0 | 0 | 0 |
| IA-04 | 11 | 33 | 0 | 0 | 0 |
| Tổng | 41 | 123 | 0 | 0 | 0 |

## 8. AI và thay đổi phiên bản

AI tạo bản nháp và biên tập theo góp ý của người dùng. Bản 2.0 bỏ hai mục GUI-004/GUI-038 của bản 1.1 và đánh lại ID; giữ nội dung 41 mục còn lại, chỉ sửa tham chiếu ID tương ứng. Quyết định này chưa thay thế kết quả thực thi hoặc verdict audit từng artifact. Prompt/output nguyên văn trong prompt_log.md; quá trình review và mapping trong phụ lục AI Review.
