# HW03 - GUI & Usability

## 1. Thông tin và phạm vi

| Nội dung | Thông tin |
| --- | --- |
| Họ tên / MSSV / lớp / email sinh viên | Chưa cung cấp |
| Mã bài tập | HW03-AI |
| SUT | EShop |
| Màn hình | /profile - hồ sơ cá nhân FR-04 và lịch sử đơn hàng FR-11 |
| Flow usability | Đã đăng nhập → mở hồ sơ → cập nhật thông tin liên hệ/địa chỉ → lưu → mở lại để kiểm tra |

## 2. Task 1 - GUI checklist

### 2.1. Thiết kế và review

Checklist gồm 42 mục, đủ bốn khía cạnh giao diện. Kỳ vọng dựa trên SRS FR-04, FR-11, FR-21–24, SEC-04 và slide S13. Điện thoại áp dụng EP/BVA với độ dài 9/10/11/12; các trạng thái đăng nhập, lưu và tải đơn áp dụng kiểm tra chuyển trạng thái.

| IA | Khía cạnh | Số mục |
| --- | --- | ---: |
| IA-01 | Tiêu chuẩn giao diện chung | 11 |
| IA-02 | Form | 11 |
| IA-03 | Điều hướng | 9 |
| IA-04 | Phản hồi / trạng thái | 11 |
| Tổng | | 42 |

Các nội dung AI đề xuất đã được rà và điều chỉnh như sau:

| Nội dung rà soát | Điều chỉnh | Lý do |
| --- | --- | --- |
| Điện thoại hợp lệ và biên độ dài | Gộp thành một bộ 9/10/11/12 chữ số | Tránh lặp các trường hợp hợp lệ trong nhiều mục |
| Font phải khớp tuyệt đối | Giữ kiểm tra khả năng đọc và chữ không mất/cắt | SRS không quy định font-family/font-size phải giống tuyệt đối |
| Tiền thiếu, click nhãn phải focus, giữ nguyên xuống dòng | Bỏ các điều kiện này | Chưa có căn cứ kỳ vọng cụ thể trong SRS |
| Server không đổi khi mất mạng | Chỉ kiểm phản hồi lỗi hoặc chưa xác nhận kết quả | Mất mạng có thể xảy ra sau khi server đã xử lý |
| Chống submit lặp, nội dung dài/zoom, giữ input khi lỗi | Loại khỏi danh sách đã chọn | Theo quyết định thu hẹp của người dùng |

#### Mục người dùng bổ sung do AI bỏ sót

| Mục bổ sung | Nguồn đề xuất | Căn cứ | Lý do AI bỏ sót |
| --- | --- | --- | --- |
| GUI-042 - Hiển thị an toàn họ tên chứa HTML | Người dùng phát hiện và yêu cầu bổ sung; AI đối chiếu và biên tập thao tác/expected | FR-04 cho phép cập nhật họ tên; SEC-04 yêu cầu escape dữ liệu người dùng khi hiển thị, không đưa trực tiếp vào innerHTML | Bản nháp và checklist 41 mục chưa ánh xạ SEC-04 vào luồng nhập họ tên → hiển thị. Các mục về tên chỉ kiểm Unicode, giá trị cập nhật và persistence, chưa có lớp dữ liệu chứa HTML hoặc kiểm điểm hiển thị Header. Đây là thiếu sót coverage của AI. |

Đối chiếu xác nhận GUI-042 chưa có trong bản nháp 52 mục và checklist 41 mục trước bổ sung; không trùng GUI-016 hoặc GUI-034. `frontend-web/src/App.jsx:27` đang đưa `user.name` vào `dangerouslySetInnerHTML`, nên cần kiểm cả lời chào Header bên cạnh ô họ tên. GUI-042 hiện kiểm đường hiển thị từ tài khoản fixture HTML chuẩn bị sẵn sau reload, không kiểm nhập/lưu; actual và ảnh nằm tại mục 2.3.

### 2.2. Dữ liệu và quy ước kiểm tra

| Ký hiệu | Dữ liệu |
| --- | --- |
| A, B | Hai tài khoản thử có hồ sơ và đơn khác nhau; biết trước dữ liệu chuẩn |
| A0 | Tài khoản không có đơn |
| P | 091234567, 0912345678, 09123456789, 091234567890; chỉ 10–11 chữ số đầu 0 hợp lệ |
| V | Nguyễn Văn Mẫu; 0912345678; địa chỉ tiếng Việt có hai dòng và dấu phẩy |
| O | Đơn đủ pending/confirmed/shipping/delivered/canceled; tiền 0, 1234567, 123456789; ngày có phần ngày lớn hơn 12 |
| H1, H2 | Họ tên thử: `Nguyễn <b>Minh</b>` và `<em>An & Bình</em>`; tên chuẩn bị sẵn trong hai tài khoản fixture H1/H2; chỉ kiểm hiển thị sau reload, không nhập/lưu |
| Chậm/lỗi | Delay GET 3 giây, API 500 hoặc mất mạng trong môi trường thử |

- **B01:** Môi trường layout đề xuất: viewport CSS 390×844, 768×1024, 1366×768; zoom 100%. Cuộn bảng ngang hợp lệ nếu vẫn tiếp cận đủ nội dung. Đây là phạm vi kiểm thử, không phải số đo trong SRS.
- **B02:** Typography đề xuất: chữ và nhãn đọc được, không glyph thiếu/cắt; phân biệt tiêu đề và nội dung. Không yêu cầu font-family/font-size giống tuyệt đối hoặc tự đặt minimum 14/16 px.
- **B03:** Ghi locale và timezone cho mỗi run. Chấp nhận cách trình bày theo locale nếu giá trị ngày đúng và nhất quán; không tự bắt dd/MM/yyyy.
- **B04:** Focus/readability là review định tính theo slide: có dấu focus thấy được và thao tác tiếp được. Không dùng kết quả này chứng nhận accessibility hoặc tỷ lệ contrast.
- **B05:** Nhãn và accessible name phải diễn đạt đúng control; chấp nhận label/aria-label/aria-labelledby. Không yêu cầu click nhãn phải chuyển focus.
- **B06:** Quy ước thao tác GUI: link/nút đúng vai trò, giữ phiên trên điều hướng thường; giỏ 3 loại ×1 để không tranh luận badge đếm dòng hay số lượng. Không yêu cầu Enter trong mọi input submit.
- **B07:** Khôi phục phiên/loading phân biệt với logged-out/empty/error. Delay 3 giây chỉ để trạng thái đủ quan sát, không là yêu cầu tốc độ phản hồi.
- **B08:** Đề xuất phục hồi lỗi: message đúng loại lỗi, không báo thành công giả, thử lại được. Không bắt cụ thể HTTP error text hoặc nút Retry riêng.

### 2.3. Checklist chính thức

Bảng dưới ghi kết quả P1 Chrome; từng nền tảng ở GUI_Checklist.xlsx. Blocked nghĩa là chưa tới nhánh cần đánh giá; Chưa chạy dành cho lượt/nền tảng chưa thực hiện. GUI-016/019/020 là Failed vì không hoàn thành cập nhật với dữ liệu hợp lệ. Định nghĩa 42 mục không thay đổi.

| ID | IA | Thành phần / trạng thái | Thao tác và dữ liệu | Kết quả mong đợi | Căn cứ | Kết quả | Notes | Ảnh / Issue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| GUI-001 | IA-01 | Bố cục mặc định | Đăng nhập A, mở /profile tại 1366×768, zoom 100%; xem từ header đến footer. | Form và lịch sử tách thành hai vùng có tiêu đề; không chồng chữ/control; footer không che nội dung hay nút. | S13 tr.16; B01 | Passed | P1 Chrome: Hai vùng hồ sơ/lịch sử riêng; không chồng chữ, nút và footer tại 1366×768. |  |
| GUI-002 | IA-01 | Bố cục responsive | Mở cùng dữ liệu tại 390×844, 768×1024 và 1366×768; cuộn đến cuối form/bảng. | Mọi trường, nút và 4 cột dữ liệu đơn đều tiếp cận được; cho phép cuộn bảng ngang nhưng không có nội dung bị cắt không thể xem. | S13 tr.21–22; B01 | Passed | P1 Chrome: Đã xem 390×844, 768×1024, 1366×768. Bản 390 có cuộn ngang trang; các cột/nút vẫn tiếp cận được sau cuộn, không bị cắt vĩnh viễn. |  |
| GUI-003 | IA-01 | Chữ và khả năng đọc | Xem các nhãn form, input và hàng bảng ở zoom 100%, dùng dữ liệu có dấu. | Chữ và nhãn đọc được, không mất dấu/ký tự hoặc cắt nét chữ; phân biệt được tiêu đề với nội dung. | S13 tr.16; B02 | Passed | P1 Chrome: Chữ có dấu và glyph tiền đọc được; heading phân biệt với body ở zoom 100%. |  |
| GUI-004 | IA-01 | Ngôn ngữ | Đọc nhãn, tiêu đề, nút, message và trạng thái do SUT hiển thị trong các bước checklist. | Nội dung SUT dùng tiếng Việt có dấu nhất quán, trừ thuật ngữ kỹ thuật chuẩn và dữ liệu tài khoản do người dùng đặt; không chấm ngôn ngữ UI của browser. | SRS FR-21 | Failed | P1 Chrome: Trong đường đăng nhập dùng cho checklist, SUT hiển thị nút “Sign In” và nhãn “Username”, chưa nhất quán tiếng Việt. Profile dùng nhãn Việt. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-004-failed-1.png) |
| GUI-005 | IA-01 | Tiêu đề và hierarchy | Mở /profile; đối chiếu heading thấy trên trang với DOM chỉ đọc. | Có đúng 1 h1 mô tả trang; hai phần hồ sơ/lịch sử có heading phân biệt; không lấy tên tab browser thay cho h1. | SRS FR-21 | Failed | P1 Chrome: Profile có 0 h1; hai tiêu đề phần đều là h2. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-005-failed-1.png) |
| GUI-006 | IA-01 | Màu nút hành động | Xem Cập nhật và nút nguy hiểm nếu đang hiển thị, ở trạng thái idle. | Cập nhật có màu hành động xanh dương; nút nguy hiểm/hủy dùng đỏ; không bắt buộc mã hex cụ thể, không thực hiện hủy đơn. | SRS FR-21 | Passed | P1 Chrome: Cập nhật màu xanh dương; Thoát/Hủy đơn màu đỏ. Không kích hoạt Hủy đơn. |  |
| GUI-007 | IA-01 | Định dạng tổng tiền | Nạp fixture O; đối chiếu tiền từng đơn 0, 1234567, 123456789 với dữ liệu chuẩn. | Mỗi số tiền giữ đúng giá trị, có ký hiệu ₫ và phân cách nghìn. | SRS FR-11,FR-21 | Passed | P1 Chrome: 0 ₫, 1.234.567 ₫, 123.456.789 ₫ đúng các đơn fixture, có ký hiệu và phân cách nghìn. |  |
| GUI-008 | IA-01 | Ngày đặt | Nạp O với ngày 2026-03-14 12:00:00 và 2026-11-05 12:00:00; ghi locale/timezone của browser. | Ngày hiển thị đúng ngày/tháng/năm nguồn và theo cùng locale đã ghi; không hiển thị Invalid Date. SRS không bắt buộc dd/MM/yyyy. | SRS FR-11; S13 tr.12,16; B03 | Passed | P1 Chrome: Các ngày đúng 14/3/2026 và 5/11/2026, nhất quán vi-VN / Asia/Ho_Chi_Minh; không Invalid Date. |  |
| GUI-009 | IA-01 | Nhãn và màu trạng thái đơn | Nạp O đủ pending/confirmed/shipping/delivered/canceled; so sánh từng badge. | Có nhãn tiếng Việt đúng nghĩa cho cả 5 trạng thái và màu phân biệt; vẫn đọc được trạng thái bằng chữ; không bắt bảng màu code hiện tại làm chuẩn duy nhất. | SRS FR-11 | Passed | P1 Chrome: Đủ 5 nhãn Việt, 5 nền màu phân biệt; chữ trên badge đọc được. |  |
| GUI-010 | IA-01 | Focus nhìn thấy và khả năng đọc | Dùng Tab đến từng link/nút/input có thể tương tác; so sánh trước/sau focus ở zoom 100%. | Vị trí focus có thay đổi outline/border/background nhìn thấy được; chữ/nhãn vẫn đọc được trên nền thường và disabled. Đây là review định tính, chưa tuyên bố đạt tỷ lệ WCAG. | S13 tr.8,13,16; B04 | Passed | P1 Chrome: Đã xem focus cả 11 control tương tác: outline nhìn thấy; field email disabled vẫn đọc được. |  |
| GUI-011 | IA-01 | Cấu trúc bảng và đúng cột | Nạp O; đối chiếu mỗi hàng với cặp ID/ngày/tổng/status trong fixture. | Có header nhận diện Mã đơn, Ngày đặt, Tổng tiền, Trạng thái; giá trị thuộc đúng cột và đúng cùng một đơn; không lệch hàng. | SRS FR-11; S13 tr.12,16 | Passed | P1 Chrome: Đủ 4 cột dữ liệu yêu cầu, mapping ID/ngày/tiền/status đúng 5 đơn A; hàng/cột căn đúng. |  |
| GUI-012 | IA-02 | Giá trị ban đầu của form | Đăng nhập A có tên/phone/address đã biết; mở /profile mới. | Email, tên, điện thoại, địa chỉ đúng A và đúng trường; không lấy dữ liệu B hoặc placeholder làm giá trị thật. | SRS FR-04; S13 tr.11–12 | Passed | P1 Chrome: Email, tên, phone và địa chỉ prefill đúng A, không lấy B/placeholder. |  |
| GUI-013 | IA-02 | Email chỉ đọc và đúng loại field | Thử click/gõ/paste vào email; xem thuộc tính type qua DOM chỉ đọc. | Email vẫn đúng tài khoản và không đổi qua GUI; field email có type=email theo FR-22 dù đang disabled/readonly. Không thử validate email nhập mới. | SRS FR-04,FR-22 | Failed | P1 Chrome: Email disabled và không sửa được qua bàn phím, nhưng type thực tế là text, không phải email. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-013-failed-2.png) |
| GUI-014 | IA-02 | Nhãn và tên truy cập của control | Xem nhãn Tên/Điện thoại/Địa chỉ và accessible name của từng control. | Nhãn diễn đạt đúng trường; control có tên truy cập đúng vai trò qua label/aria-label/aria-labelledby; placeholder không thay nhãn. | S13 tr.16,18; B05 | Failed | P1 Chrome: Họ Tên, Số điện thoại và Địa chỉ có nhãn nhìn thấy nhưng không có accessible name qua label/aria; placeholder phone/address không thay nhãn. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-014-failed-1.png), [Ảnh 2](screenshots/chrome-windows/P1-GUI-014-failed-2.png), [Ảnh 3](screenshots/chrome-windows/P1-GUI-014-failed-3.png) |
| GUI-015 | IA-02 | Dấu trường bắt buộc | Ghi các trường đang được form khai báo required hoặc tài liệu đã chốt là bắt buộc; so sánh nhãn. | Mỗi trường được xác định bắt buộc đều có * cạnh nhãn. Mục này không tự kết luận phone/address bắt buộc hay tên toàn khoảng trắng hợp lệ. | SRS FR-22; S13 tr.11 | Failed | P1 Chrome: Field Họ Tên có required nhưng nhãn không có dấu *. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-015-failed-1.png) |
| GUI-016 | IA-02 | Cập nhật tên tiếng Việt | Giữ phone hợp lệ; đổi tên A thành Nguyễn Văn Mẫu, lưu và mở lại. | Tên được cập nhật đúng dấu/ký tự và đúng tài khoản; không thay email/role. Không suy ra giới hạn tên dài từ dữ liệu mẫu. | SRS FR-04 | Failed | P1 Chrome: Dữ liệu hợp lệ (tên Nguyễn Văn Mẫu, phone 0912345678) bị validation phone từ chối trước PUT, nên không hoàn thành cập nhật tên theo FR-04. Chưa đánh giá được các bước sau lưu. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-016-failed-validation.png) |
| GUI-017 | IA-02 | Biên độ dài điện thoại | Lần lượt gửi P: 091234567 (9), 0912345678 (10), 09123456789 (11), 091234567890 (12); trường khác hợp lệ. | 10/11 chữ số đầu 0 được chấp nhận và giữ số 0 đầu; 9/12 chữ số bị từ chối, không thay dữ liệu đã lưu bằng giá trị sai. Ghi actual từng biến thể. | SRS FR-04; S13 tr.19 EP/BVA | Failed | P1 Chrome: 9 số: từ chối, đúng; 10 số: từ chối, sai; 11 số: từ chối, sai; 12 số: từ chối, đúng. Hai số hợp lệ đầu 0 không được lưu. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-017-failed-2.png), [Ảnh 2](screenshots/chrome-windows/P1-GUI-017-failed-3.png) |
| GUI-018 | IA-02 | Phân lớp điện thoại sai | Gửi 1912345678, 09a2345678, 09123-5678, +84912345678; giữ trường khác hợp lệ. | Không lưu các chuỗi có đầu số khác 0 hoặc chứa ký tự không phải chữ số. Các quyết định trim khoảng trắng được tách khỏi mục này. | SRS FR-04; S13 tr.19 EP | Failed | P1 Chrome: 1912345678 được PUT và lưu, sai expected. 09a2345678, 09123-5678, +84912345678 bị từ chối và không lưu. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-018-failed-1.png) |
| GUI-019 | IA-02 | Nội dung địa chỉ | Giữ tên/phone hợp lệ; nhập địa chỉ V có tiếng Việt, 2 dòng và dấu phẩy; lưu rồi mở lại. | Địa chỉ mặc định sau tải lại còn đủ từ, chữ số và dấu; không bị chuyển sang trường khác. Không tự quy định maxLength. | SRS FR-04; S13 tr.12,20 | Failed | P1 Chrome: Địa chỉ thử hợp lệ cùng phone 0912345678 bị validation phone từ chối trước PUT, nên không hoàn thành cập nhật địa chỉ. Chưa đánh giá được nội dung địa chỉ sau lưu/mở lại. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-019-failed-validation.png) |
| GUI-020 | IA-02 | Gửi đúng thay đổi hồ sơ bằng chuột | Từ baseline A, đổi tên/phone/address hợp lệ; click Cập nhật một lần; đối chiếu bản lưu và request chỉ đọc. | Ba trường cập nhật đúng A; email/role không thay đổi và hồ sơ B giữ nguyên. Không gửi payload sửa role hoặc kiểm sâu API trong checklist GUI. | SRS FR-04 | Failed | P1 Chrome: Đã nhập ba trường hợp lệ và click Cập nhật; phone 09123456789 bị validation từ chối trước PUT, nên không hoàn thành cập nhật hồ sơ bằng chuột. Chưa đánh giá các kiểm tra sau lưu. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-020-failed-validation.png) |
| GUI-021 | IA-02 | Nội dung và vị trí lỗi nhập | Gửi 091234567 (9 số) rồi quan sát message và vùng trên Cập nhật. | Có lỗi nhận diện trường điện thoại và hướng dẫn quy tắc đầu 0, 10–11 số; lỗi hiển thị trong form phía trên submit theo FR-22; không chỉ kết luận từ alert ngoài form. | SRS FR-04,FR-22; S13 tr.16,18 | Failed | P1 Chrome: Chỉ hiện alert “Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số.”; không có lỗi inline phía trên submit và hướng dẫn sai quy tắc 0/10–11. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-021-failed-1.png) |
| GUI-022 | IA-03 | Tìm và mở Profile | Bắt đầu ở Home đã đăng nhập A; dùng link tài khoản trên navbar. | Mở được /profile và nhận diện được hai phần hồ sơ/lịch sử của A; không cần tự gõ URL để hoàn thành đường đi này. | SRS FR-04; S13 tr.17 | Passed | P1 Chrome: Từ Home mở Profile bằng link tài khoản, đúng /profile và hai phần của A. |  |
| GUI-023 | IA-03 | Navbar đang chọn | Từ Home vào /profile rồi trở lại Home; so sánh dấu chọn của link tài khoản. | Navbar có dấu highlight phân biệt trang hiện tại; không coi màu cố định giống nhau trên mọi route là bằng chứng active. | SRS FR-23 | Failed | P1 Chrome: Sau loại ảnh hưởng hover, link tài khoản có cùng class/màu/aria ở Home và Profile; không có dấu active theo route. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-023-failed-1.png) |
| GUI-024 | IA-03 | Logo về Home | Từ /profile đã login A, click EShop. | Đến đúng route /; phiên A vẫn còn, không tự đăng xuất hoặc sửa hồ sơ. | S13 tr.17–18; B06 | Passed | P1 Chrome: Logo về /, còn phiên A và hồ sơ baseline không đổi. |  |
| GUI-025 | IA-03 | Link và badge giỏ hàng chung | Chuẩn bị giỏ 0 rồi 3 sản phẩm khác nhau, mỗi loại số lượng 1; xem navbar tại Profile và mở Giỏ hàng. | Link đi đúng /cart; badge phản ánh 3 khi có 3 sản phẩm; với 0 cho phép ẩn hoặc hiển thị 0. Không đánh giá flow checkout. | SRS FR-23; B06 | Failed | P1 Chrome: Giỏ 0 đúng; thêm 3 sản phẩm khác nhau ×1 qua GUI, cart đúng 3 dòng ×1 nhưng navbar Profile không có badge 3. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-025-failed-2.png) |
| GUI-026 | IA-03 | Nhãn và đường thoát | Tại Profile đã login A, xem nhãn nút và kích hoạt đăng xuất. | Nút mang nhãn Đăng xuất; sau click navbar trở về các lựa chọn chưa login. Bảo vệ dữ liệu kiểm tiếp tại GUI-031. | SRS FR-23; S13 tr.17 | Failed | P1 Chrome: Nhãn thực tế “Thoát”, không phải “Đăng xuất”; sau click navbar về trạng thái chưa login. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-026-failed-1.png) |
| GUI-027 | IA-03 | URL trực tiếp và reload | Khi phiên A hợp lệ, mở /profile trực tiếp rồi reload. | Route tải được, cuối quá trình hiển thị form/lịch sử của A, không lỗi 404 hoặc trắng trang; không dùng việc này thay test persistence GUI-034. | SRS FR-04; S13 tr.17 | Passed | P1 Chrome: Direct /profile và reload đều khôi phục đúng A, hiện 5 đơn; không 404/trắng trang. |  |
| GUI-028 | IA-03 | Thứ tự Tab và Shift+Tab | Từ đầu trang nhấn Tab qua navbar, form và control đang hiển thị; đi ngược bằng Shift+Tab. | Focus theo thứ tự trên xuống dưới/trái sang phải, không vòng kẹt; đến mọi control tương tác; skip email khi thực sự disabled, readonly được phép focus. | SRS FR-21; S13 tr.18 | Passed | P1 Chrome: Tab tới đủ 11 control theo nhóm navbar → form → bảng; Shift+Tab đi ngược, không trap; email disabled được skip. |  |
| GUI-029 | IA-03 | Kích hoạt bằng bàn phím | Dùng Enter trên link; dùng Enter/Space trên nút Cập nhật và quan sát hành động được kích hoạt; nhấn Enter trong textarea. Có thể dùng phone sai để quan sát validation của nút, không kiểm lưu thành công. | Link/nút thực hiện đúng hành động khi kích hoạt bằng bàn phím; Enter trong textarea thêm dòng, không gửi nhầm form. Không yêu cầu lưu thành công và không bắt Enter trong mọi input phải submit. | S13 tr.18; B06 | Passed | P1 Chrome: Enter mở đúng Home/Profile; Space và Enter kích hoạt nút Cập nhật qua validation; Enter textarea tạo dòng mới, không submit. Không kiểm lưu thành công. |  |
| GUI-030 | IA-03 | Back và Forward | Lưu/không sửa form; điều hướng Profile → Home; Back rồi Forward. | Đến đúng các route trong lịch sử, phiên/tài khoản không đổi và dữ liệu đã lưu không bị thay bởi bản cũ. Không đánh giá bản nháp chưa lưu ở mục này. | S13 tr.17–18,20; B06 | Passed | P1 Chrome: Profile → Home → Back → Forward đúng route; giữ phiên A và baseline không đổi. |  |
| GUI-031 | IA-04 | Bảo vệ khi thiếu hoặc hết hiệu lực phiên | Lần lượt dùng phiên không token và token không hợp lệ; mở Profile, thử Back sau đăng xuất. | Không lộ hồ sơ/đơn riêng, không báo thao tác thành công như đang login; có thông báo/đường đăng nhập lại. Ghi riêng kết quả từng điều kiện. | SRS FR-04,FR-11; S13 tr.11; B07 | Passed | P1 Chrome: Không token/invalid token và Back sau logout không hiện form/đơn riêng; có đường login, đăng nhập lại phục hồi A. |  |
| GUI-032 | IA-04 | Đang khôi phục phiên | Reload khi token hợp lệ; làm chậm GET /users/me 3 giây trong môi trường thử. | Trong lúc chưa biết kết quả có dấu chờ trung tính, không khẳng định đã mất phiên; khi API thành công hiện đúng A. 3 giây là điều kiện gây chậm, không phải SLA. | S13 tr.13–14; B07 | Failed | P1 Chrome: Trong GET /users/me chậm 3 giây, trang khẳng định “Vui lòng đăng nhập”, không có trạng thái chờ trung tính; sau response thật trở về A. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-032-failed-1.png) |
| GUI-033 | IA-04 | Phản hồi lưu thành công | Gửi dữ liệu hợp lệ và chờ phản hồi API thành công. | Chỉ sau khi request thành công mới có thông báo xác nhận đã cập nhật; không báo lỗi cho lần lưu đó. Cơ chế alert/toast/inline đều được ở nhánh success. | SRS FR-04; S13 tr.16,20 | Blocked | P1 Chrome: Validation phone hợp lệ chặn trước PUT; chưa có response lưu thành công nên chưa tới nhánh kiểm feedback thành công và thứ tự response/thông báo. |  |
| GUI-034 | IA-04 | Đồng bộ và giữ dữ liệu sau lưu | Lưu tên/phone/address mới; xem form/navbar, rời Profile rồi mở lại và reload. | Tên trên navbar và dữ liệu form khớp bản đã lưu; các giá trị vẫn đúng sau mở lại/reload. Không dùng dữ liệu chỉ còn trong React state làm bằng chứng lưu. | SRS FR-04; S13 tr.12,14,20 | Blocked | P1 Chrome: Validation phone hợp lệ chặn trước PUT; chưa có lần lưu thành công nên chưa tới nhánh kiểm đồng bộ navbar/form và persistence sau lưu/mở lại/reload. |  |
| GUI-035 | IA-04 | Phản hồi lỗi lưu | Gây PUT trả 500 hoặc mất mạng trong môi trường thử, gửi dữ liệu hợp lệ. | Không có thông báo thành công; có lỗi cho biết chưa lưu hoặc chưa xác nhận được kết quả và hướng thử lại; có thể gửi lại sau phục hồi mạng. | S13 tr.11,16; B08 | Blocked | P1 Chrome: Đã cấu hình PUT 500 và network-abort nhưng validation phone chặn trước request; chưa kích hoạt nhánh lỗi lưu/mất mạng hoặc recovery. Không kết luận các nhánh này Failed. |  |
| GUI-036 | IA-04 | Focus sau đóng thông báo | Dùng keyboard gây validation, đóng thông báo nếu có, rồi tiếp tục Tab/nhập sửa phone. | Focus trở về trang, có thể tiếp cận trường lỗi và sửa/gửi lại bằng keyboard; không mắc kẹt trong dialog hoặc mất khả năng thao tác. | S13 tr.13,18; B04 | Passed | P1 Chrome: Đóng alert, Shift+Tab về phone, sửa và gửi lại bằng keyboard được; không trap. Lần gửi lại vẫn bị lỗi validation phone đã ghi riêng tại GUI-017. |  |
| GUI-037 | IA-04 | Đang tải danh sách đơn | Làm chậm GET my-orders 3 giây, mở Profile với tài khoản có đơn. | Trong lúc chờ có loading/dấu đang lấy dữ liệu; chưa hiển thị khẳng định không có đơn; sau thành công chuyển sang bảng dữ liệu. | S13 tr.13–14; B07 | Failed | P1 Chrome: Trong GET đơn chậm 3 giây đã hiện “Bạn chưa có đơn hàng nào.”, không loading; sau response thật hiện đủ 5 đơn. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-037-failed-1.png) |
| GUI-038 | IA-04 | Empty state thực sự | Dùng A0 không có đơn; chờ GET my-orders thành công trả []. | Có message thân thiện cho biết chưa có đơn và icon/hình minh họa; không hiển thị hàng đơn giả hoặc thông báo lỗi tải. | SRS FR-24; S13 tr.16 | Failed | P1 Chrome: A0 thực sự không có đơn, GET 200 và message empty đúng; thiếu icon/hình minh họa. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-038-failed-2.png) |
| GUI-039 | IA-04 | Lỗi tải lịch sử và phục hồi | Làm GET my-orders trả 500, rồi phục hồi API và reload/thử lại. | Khi lỗi có thông báo không tải được đơn, không đồng nhất với chưa có đơn; sau phục hồi có thể lấy và hiển thị dữ liệu thật. Không bắt buộc phải có nút Retry riêng. | S13 tr.11,16,20; B08 | Failed | P1 Chrome: GET đơn 500 có kiểm soát lại hiện message empty, không có lỗi tải riêng; gỡ fault/reload lấy lại đúng 5 đơn thật. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-039-failed-1.png) |
| GUI-040 | IA-04 | Chuyển tài khoản và cô lập dữ liệu | A và B có profile/đơn khác nhau; xem A, logout, login B, mở Profile rồi Back/Forward. | Chỉ profile và đơn của tài khoản hiện tại xuất hiện; không giữ flash/cache dữ liệu riêng A trong phiên B; mọi hàng khớp fixture theo chủ sở hữu. | SRS FR-04,FR-11; S13 tr.14 | Passed | P1 Chrome: Cùng context A logout → UI login B → Profile → Back/Forward: profile/2 đơn đúng B, không thấy A trong 17 frame đã thu. |  |
| GUI-041 | IA-04 | Trạng thái đơn thay đổi bên ngoài | Ghi baseline một đơn pending; đổi fixture riêng thành confirmed, không bấm Hủy đơn; mở lại/reload Profile. | Cùng mã đơn hiển thị nhãn/màu trạng thái confirmed mới; không làm thay đổi đơn khác. Không bắt buộc realtime/polling khi chưa reload. | SRS FR-11; S13 tr.12,14,20 | Passed | P1 Chrome: Đơn #960001 từ pending sang confirmed sau đổi dữ liệu ngoài trang và reload; nhãn/màu đổi, các đơn khác không đổi; cuối case reset baseline. |  |
| GUI-042 | IA-02 | Hiển thị an toàn họ tên chứa HTML | Dùng lần lượt tài khoản fixture H1/H2 có tên HTML chuẩn bị sẵn: Nguyễn <b>Minh</b> và <em>An & Bình</em>. Đăng nhập, mở Profile rồi reload; đối chiếu giá trị ô Họ tên, lời chào navbar và DOM. Chỉ kiểm hiển thị từ fixture, không nhập hoặc lưu tên. | Sau reload, ô Họ tên và lời chào navbar hiển thị nguyên văn tên fixture như văn bản, escape an toàn; không tạo phần tử HTML hoặc định dạng đậm/nghiêng từ tên. Không đánh giá bước nhập/lưu. | SRS SEC-04, FR-04 | Failed | P1 Chrome: Fixture H1/H2 có tên HTML chuẩn bị sẵn. Sau reload, form giữ nguyên chuỗi chứa thẻ; navbar tạo b cho H1 và em cho H2, hiện chữ đậm/nghiêng thay vì nguyên văn. Không có PUT nhập/lưu tên. | [Ảnh 1](screenshots/chrome-windows/P1-GUI-042-failed-2.png), [Ảnh 2](screenshots/chrome-windows/P1-GUI-042-failed-4.png) |

### 2.4. Kết quả thực thi

Ngày 09/11/2026 đã thử đủ 42 ca trên Chrome 156.0.8078.80, Windows build 10.0.26300; chốt kết quả Task 1 trên Chrome: **20 Passed, 19 Failed, 3 Blocked** (42 mục đã thử; 39 mục có kết luận Passed/Failed). GUI-016/019/020 Failed vì cập nhật với dữ liệu hợp lệ không hoàn thành do validation phone. GUI-033/034/035 Blocked vì chưa tới các nhánh cần kiểm sau request lưu. Phone hợp lệ đầu 0 bị validation từ chối trước PUT. GUI-017/018 đã ghi riêng actual từng biến thể; không đổi sang dữ liệu sai SRS để ép chạy các nhánh sau.

Công cụ thực thi: Playwright 1.62.1, Chrome thật ở chế độ có cửa sổ, SQLite fixture tổng hợp và đọc đối chiếu database. URL frontend `http://localhost:5176`, API `http://localhost:3000`; locale `vi-VN`, timezone `Asia/Ho_Chi_Minh`, zoom 100%, viewport theo B01. Login/API thật; delay GET 3 giây và GET 500 được chèn có kiểm soát cho các ca tương ứng. PUT 500/network-abort chưa được kích hoạt vì validation chặn trước request. Các tiêu chí thị giác được AI đối chiếu ảnh thật với DOM; chưa thay verdict audit của sinh viên.

Actual và công cụ test nằm ngoài hồ sơ nộp tại `../profile-tests/`; báo cáo giữ kết quả/Notes và ảnh Failed cần thiết. Ảnh hiện là ảnh nội dung trang thật, chưa có email sinh viên và khung URL/browser/OS theo Task 3; chưa hoàn thiện bằng chứng nộp đa nền tảng. GUI-029 chỉ kiểm kích hoạt bằng keyboard và Enter textarea. GUI-042 dùng tài khoản fixture H1/H2 có tên HTML chuẩn bị sẵn, chỉ kiểm form/navbar sau reload, không kiểm nhập/lưu; form hiển thị nguyên văn nhưng navbar diễn giải thẻ HTML nên Failed.

### 2.5. Bug report

Chưa có bug report chính thức hoặc GitHub Issue được ghi nhận.

## 3. Task 2 - Usability evaluation

### 3.1. Mục tiêu và scenario

Mục tiêu: đánh giá khả năng tìm hồ sơ, cập nhật thông tin, hiểu phản hồi và xác minh đã lưu.

Scenario: “Bạn vừa thay đổi thông tin liên hệ và chuyển nơi ở. Hãy cập nhật tài khoản bằng thông tin thử nghiệm được cung cấp để chuẩn bị cho lần mua hàng tiếp theo, sau đó kiểm tra thông tin đã được lưu đúng.”

### 3.2. Công cụ đánh giá

Dự kiến dùng SUS sau task và câu hỏi mở:

- Độ rõ ràng: Phần nào khiến bạn khó hiểu khi thực hiện nhiệm vụ?
- Phục hồi lỗi: Khi gặp lỗi, bạn hiểu cần làm gì tiếp theo?
- Tốc độ: Bước nào khiến bạn phải chờ hoặc mất nhiều công nhất?
- Độ tin cậy: Điều gì giúp bạn tin hoặc nghi ngờ thông tin đã được lưu?

### 3.3. Pilot và bảy phiên chính thức

Chưa thực hiện pilot. Chưa có danh sách participant, thông tin liên hệ xác minh, ghi chú quan sát, câu trả lời thang đo hoặc recording; số phiên chính thức là 0/7.

### 3.4. Phân tích và phát hiện

Chưa có dữ liệu để tính điểm SUS, tổng hợp pain point, xếp severity hoặc báo cáo bug từ usability.

## 4. Task 3 - Cross-browser / cross-platform

### 4.1. Kế hoạch chung

Dùng nguyên 42 ID/thao tác/expected ở mục 2.3 trên Chrome Windows, Firefox Windows và Chrome Android; không sao chép kết luận giữa các nền tảng. GUI-029 chỉ keyboard/textarea, GUI-042 chỉ hiển thị fixture H1/H2 sau reload. Cách phân loại giữ nguyên: GUI-016/019/020 Failed nếu cập nhật hợp lệ không hoàn thành; GUI-033/034/035 Blocked khi chưa tới nhánh cần kiểm.

| Bộ | Nền tảng | Dữ liệu / phương thức | Trạng thái |
| --- | --- | --- | --- |
| P1 | Chrome 156.0.8078.80 / Windows build 10.0.26300 | Fixture P1; actual tại mục 2.3, Excel Execution P1 | Giữ nguyên kết quả và 23 ảnh đã chốt |
| P2 | Firefox 153.0 / Windows build 10.0.26300 | Firefox do Playwright 1.62.1 quản lý, build 1538; fixture P2 riêng; cùng spec, headed, một worker | Đã thử đủ 42 mục, đối chiếu ảnh thật/DOM |
| P3 | Chrome 148.0.7778.180 / Android 11, Redmi Note 8 Pro thật | Fixture P3; Playwright qua ADB/CDP; ảnh PNG trực tiếp từ ADB | Đã thử 42 mục: 20 Passed, 19 Failed, 3 Blocked |

Điều kiện desktop: frontend `http://localhost:5176`, API `http://localhost:3000`; locale `vi-VN`, timezone `Asia/Ho_Chi_Minh`, zoom 100%, các viewport B01. Login và API thật; chỉ chèn delay GET 3 giây/GET 500 trong ca tương ứng. Không bypass validation bằng phone sai SRS hoặc mock success. Mỗi case reset riêng fixture của nền tảng, chạy nối tiếp; database được sao lưu trước startup vì backend tự DROP/seed, và khôi phục sau lượt chạy. Không sửa logic SUT.

Chrome Android: chuẩn bị thiết bị có Chrome và ADB đã xác thực hoặc phiên cloud có local tunnel. Với USB, reverse cả port 3000 và 5176 đến máy SUT rồi mở localhost trên chính Chrome của thiết bị; xác minh request tới API thật. Có thể dùng adapter Playwright Android experimental hoặc kiểm thủ công nếu thao tác không được hỗ trợ. Chuẩn bị keyboard Bluetooth/USB hoặc adapter gửi được Tab/Shift+Tab/Enter/Space tới Android thật cho các mục keyboard. Ghi viewport nào thực sự tái hiện được; không lấy mobile viewport trên Windows thay nền tảng Android. Thực hiện đủ 42 ID/biến thể, Failed có Notes/ảnh, điều kiện không thực hiện được ghi Blocked.

Nguồn cấu hình: [Playwright Browsers](https://playwright.dev/docs/browsers), [Android API](https://playwright.dev/docs/api/class-android); tiêu chí bằng chứng theo đề Task 3/§11.

### 4.2. Tổng hợp actual theo nền tảng

| Nền tảng | Mục cần kiểm | Đã thử | Passed | Failed | Blocked | Chưa chạy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Chrome / Windows | 42 | 42 | 20 | 19 | 3 | 0 |
| Firefox / Windows | 42 | 42 | 20 | 19 | 3 | 0 |
| Chrome / Android | 42 | 42 | 20 | 19 | 3 | 0 |
| Tổng lượt | 126 | 126 | 60 | 57 | 9 | 0 |

Firefox có actual độc lập, cùng phân loại với Chrome trong 42 mục của lượt này. GUI-010/028 được kiểm lại từ focus EShop xác định; không nhầm `activeElement` còn ở control cuối khi focus đã ra thanh công cụ trình duyệt là lỗi trap của SUT. Raw và ảnh hai lần được giữ ngoài work. Các tiêu chí thị giác được AI xem ảnh Firefox thật; chưa thay verdict audit của sinh viên.

Ảnh Firefox Failed nằm tại `screenshots/firefox-windows/`; 23 ảnh Chrome nằm tại `screenshots/chrome-windows/`, giữ nguyên nội dung. Ảnh Windows hiện là page screenshots cục bộ, chưa có đủ email sinh viên, tên/MSSV trong form và khung URL/browser/OS/device theo đề. Cần bổ sung bằng chứng cửa sổ/thiết bị thật hoặc phiên cloud với danh tính thật; chưa tuyên bố hoàn thành Task 3. Android đã có actual độc lập tại mục 4.4; không suy kết quả từ hai nền tảng Windows.

### 4.3. Actual Firefox Windows

| ID | Kết quả | Actual / Notes | Ảnh Failed |
| --- | --- | --- | --- |
| GUI-001 | Passed | 1366×768: hai vùng hồ sơ/lịch sử tách biệt; không chồng control, footer không che nút. |  |
| GUI-002 | Passed | Đã xem ba viewport 390×844, 768×1024, 1366×768. Bản 390 có nội dung bảng tràn ngang nhưng tiếp cận được sau cuộn; không bị cắt vĩnh viễn. |  |
| GUI-003 | Passed | Chữ Việt có dấu, nhãn và dữ liệu đọc được; heading phân biệt body; không áp điều kiện font giống Chrome tuyệt đối. |  |
| GUI-004 | Failed | Đường login trong checklist hiện Username/Sign In; Profile dùng nhãn Việt nhưng nội dung SUT chưa nhất quán tiếng Việt. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-004-failed-1.png) |
| GUI-005 | Failed | Profile có 0 h1; hai tiêu đề phần đều là h2. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-005-failed-1.png) |
| GUI-006 | Passed | Cập nhật xanh dương; Thoát/Hủy đơn đỏ, đọc được; không thực hiện Hủy đơn. |  |
| GUI-007 | Passed | Các tổng 0 / 1234567 / 123456789 giữ đúng giá trị, có ₫ và dấu nhóm nghìn. |  |
| GUI-008 | Passed | Ngày hiển thị 14/3/2026 và 5/11/2026 đúng nguồn, nhất quán vi-VN / Asia/Ho_Chi_Minh; không Invalid Date. |  |
| GUI-009 | Passed | Đủ 5 nhãn Việt, nền badge phân biệt; text trạng thái đọc được. |  |
| GUI-010 | Passed | Kiểm lại từ focus EShop: đủ 11 control khác nhau có focus nhìn thấy; email disabled vẫn đọc được. Màu/kiểu focus native Firefox khác Chrome, không chấm khớp tuyệt đối. |  |
| GUI-011 | Passed | Bốn header yêu cầu đúng thứ tự; ID/ngày/tiền/status khớp cùng đơn P2; hàng/cột căn đúng. |  |
| GUI-012 | Passed | Email/tên/phone/địa chỉ prefill đúng A của P2, không lấy B hoặc placeholder. |  |
| GUI-013 | Failed | Email disabled, không đổi qua GUI; type thực tế text, không đạt yêu cầu type=email. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-013-failed-2.png) |
| GUI-014 | Failed | Ba field tên/phone/địa chỉ thiếu accessible name liên kết label/aria; có nhãn nhìn thấy và placeholder nhưng không thay accessible name. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-014-failed-1.png), [Ảnh 2](screenshots/firefox-windows/P2-GUI-014-failed-2.png), [Ảnh 3](screenshots/firefox-windows/P2-GUI-014-failed-3.png) |
| GUI-015 | Failed | Họ Tên khai báo required nhưng nhãn thiếu dấu *. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-015-failed-1.png) |
| GUI-016 | Failed | Nhập dữ liệu hợp lệ gồm Nguyễn Văn Mẫu và phone 0912345678; validation phone từ chối trước PUT, không hoàn thành cập nhật tên. Chưa kiểm các bước sau lưu. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-016-failed-1.png) |
| GUI-017 | Failed | Phone 9/12 số đầu 0 bị từ chối đúng; 10/11 số hợp lệ đầu 0 cũng bị từ chối, sai expected; không PUT ở các biến thể này. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-017-failed-2.png), [Ảnh 2](screenshots/firefox-windows/P2-GUI-017-failed-3.png) |
| GUI-018 | Failed | 1912345678 được PUT và lưu, sai expected; 09a2345678, 09123-5678, +84912345678 bị từ chối, không lưu. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-018-failed-1.png) |
| GUI-019 | Failed | Địa chỉ tiếng Việt hai dòng cùng phone 0912345678 hợp lệ bị validation phone chặn trước PUT; không hoàn thành cập nhật địa chỉ. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-019-failed-1.png) |
| GUI-020 | Failed | Click Cập nhật với ba trường hợp lệ, phone 09123456789 bị validation từ chối trước PUT; không hoàn thành cập nhật hồ sơ bằng chuột. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-020-failed-1.png) |
| GUI-021 | Failed | Chỉ có alert yêu cầu 9–10 số; không có lỗi inline phía trên submit, không hướng dẫn đúng quy tắc đầu 0 và 10–11 số. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-021-failed-1.png) |
| GUI-022 | Passed | Từ Home, link tài khoản mở đúng /profile với form và lịch sử A/P2. |  |
| GUI-023 | Failed | Loại ảnh hưởng hover: class/màu/aria của link tài khoản không đổi giữa Home/Profile/Home; thiếu active theo route. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-023-failed-1.png) |
| GUI-024 | Passed | Logo về Home, giữ phiên A/P2 và hồ sơ baseline. |  |
| GUI-025 | Failed | Giỏ ban đầu trống; thêm ba sản phẩm ×1 qua GUI thì cart có đúng ba dòng ×1, nhưng navbar Profile thiếu badge 3. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-025-failed-2.png) |
| GUI-026 | Failed | Nhãn nút là Thoát, không phải Đăng xuất; click vẫn đưa navbar về trạng thái chưa login. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-026-failed-1.png) |
| GUI-027 | Passed | Direct /profile và reload khôi phục đúng A/P2 và năm đơn; không 404/trắng trang. |  |
| GUI-028 | Passed | Kiểm lại từ EShop: Tab tới đủ 11 control theo navbar → form → bảng; Shift+Tab đi ngược chính xác; không trap trong trang, email disabled được skip. |  |
| GUI-029 | Passed | Enter mở đúng Home/Profile; Enter/Space kích hoạt Cập nhật qua validation; Enter textarea xuống dòng và không submit. Không kiểm lưu thành công. |  |
| GUI-030 | Passed | Back/Forward đến đúng Profile/Home, giữ phiên A/P2 và baseline không đổi. |  |
| GUI-031 | Passed | Không token/invalid token và Back sau logout không lộ form/đơn riêng; đường login và login recovery hoạt động. |  |
| GUI-032 | Failed | Trong GET /users/me chậm 3 giây hiện Vui lòng đăng nhập, không chờ trung tính; sau response thật hiển thị A/P2. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-032-failed-1.png) |
| GUI-033 | Blocked | Validation phone hợp lệ chặn trước PUT; chưa có response lưu thành công nên chưa tới nhánh feedback/thứ tự response và thông báo. |  |
| GUI-034 | Blocked | Validation phone hợp lệ chặn trước PUT; chưa có lần lưu thành công để kiểm đồng bộ navbar/form và persistence sau lưu. |  |
| GUI-035 | Blocked | Cấu hình PUT 500 và network-abort nhưng không có PUT vì validation phone chặn; chưa tới nhánh lỗi lưu hoặc recovery, giữ Blocked. |  |
| GUI-036 | Passed | Sau đóng alert có thể Shift+Tab về phone, sửa và gửi lại bằng keyboard; không trap. Việc phone hợp lệ bị từ chối ghi ở GUI-017. |  |
| GUI-037 | Failed | GET đơn đang chờ 3 giây đã hiện Bạn chưa có đơn hàng nào, thiếu loading; sau response thật chuyển sang năm đơn A/P2. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-037-failed-1.png) |
| GUI-038 | Failed | A0/P2 có GET 200 và [] thật, message empty đúng nhưng không có icon/hình minh họa. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-038-failed-2.png) |
| GUI-039 | Failed | GET đơn 500 có kiểm soát lại hiển thị empty, thiếu thông báo lỗi tải riêng; gỡ fault/reload lấy lại năm đơn thật. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-039-failed-1.png) |
| GUI-040 | Passed | Cùng context, A logout → login B/P2 → Profile → Back/Forward: đúng profile và hai đơn B, không thấy dữ liệu A trong các frame đã thu. Số frame quan sát: 30. |  |
| GUI-041 | Passed | Đơn P2 #960101 từ pending sang confirmed sau đổi fixture bên ngoài/reload; nhãn/màu mới đúng, các đơn khác không đổi; cuối case reset. |  |
| GUI-042 | Failed | Fixture H1/H2 của P2: sau reload form giữ nguyên chuỗi chứa thẻ, nhưng navbar tạo b/em và hiện đậm/nghiêng; không có PUT nhập/lưu tên. | [Ảnh 1](screenshots/firefox-windows/P2-GUI-042-failed-2.png), [Ảnh 2](screenshots/firefox-windows/P2-GUI-042-failed-4.png) |

### 4.4. Actual Chrome Android trên điện thoại thật

Thiết bị Redmi Note 8 Pro, Android 11, Chrome 148.0.7778.180; màn hình 1080×2340, density hiện có 401 (physical 440), native CSS viewport 431×847, DPR≈2.506, locale vi-VN, timezone Asia/Saigon (UTC+07). OS được xác minh từ thiết bị và trang phiên bản Chrome; UA rút gọn ghi Android 10 nên không dùng UA để kết luận phiên bản OS.

Đã xác minh Chrome điện thoại mở được `http://localhost:5176` và gọi API thật ở `http://localhost:3000` qua ADB reverse. Playwright `_android.devices()` nhận thiết bị; kết nối Chrome đang mở bằng ADB forward/CDP. Android Chrome không tạo được browser context tách biệt, nên dùng tab thử riêng trong context hiện có, chỉ xử lý token của localhost và không can thiệp các tab cá nhân. Đã đóng tab thử, trả về tab localhost, dừng server của lượt thử và khôi phục DB gốc/kiểm hash sau khi thu bằng chứng.

Đã chạy lại đủ 42 mục trên cùng thiết bị/fixture P3; ảnh Failed/xác minh Android được lấy trực tiếp bằng `adb exec-out screencap -p`, PNG nguyên trạng 1080×2340. Không dùng Playwright page screenshot hoặc ảnh chụp cửa sổ scrcpy trong bộ ảnh hiện tại. Native alert được chụp trước khi đóng. Với GET chậm, giữ pending tối thiểu 3 giây và tới lúc chụp xong; đây không phải kiểm SLA. Thông báo flag/debug của Chrome có thể xuất hiện trong ảnh, không tính là message hay lỗi SUT. Kết quả P3 sau kiểm lại GUI-001/002: 20 Passed, 19 Failed, 3 Blocked.

GUI-001/002 được kiểm lại bằng viewport nội dung native trên Chrome Android thật: tạm đặt density 160 và kích thước hiển thị để đo đúng visualViewport 1366×768, 390×844, 768×1024, scale=1. Không dùng override viewport CDP trong lượt chốt này; density gốc 401 và kích thước physical 1080×2340 đã khôi phục. Tại 390, innerWidth/scrollWidth=443 do tràn ngang; phép kiểm đối chiếu vùng nhìn thực và cuộn tới từng trường/nút/ô dữ liệu, không yêu cầu innerWidth bằng chiều rộng vùng nhìn. Đã xem ảnh ADB và đối chiếu DOM từ đầu trang đến footer; ảnh review/actual kỹ thuật giữ ngoài work.

Xác minh thiết bị: [SUT qua localhost](screenshots/chrome-android/P3-localhost-adb.png), [Chrome version / Android / model](screenshots/chrome-android/P3-chrome-version-adb.png).

| ID | Kết quả | Actual / Notes | Ảnh Failed |
| --- | --- | --- | --- |
| GUI-001 | Passed | Passed sau kiểm lại trên Chrome Android thật: viewport nội dung thực 1366×768, visualViewport.scale=1. Hai vùng hồ sơ/lịch sử có heading riêng, không chồng chữ/control; cuộn tới footer static, không che nội dung hoặc nút. Đã xem ảnh ADB đầu/cuối trang và đối chiếu DOM. |  |
| GUI-002 | Passed | Passed sau kiểm lại: visualViewport thực 390×844, 768×1024, 1366×768, scale=1. Mọi trường/nút và các ô dữ liệu của 5 đơn tiếp cận được sau cuộn. Tại 390 có tràn ngang (innerWidth/scrollWidth=443), nhưng cuộn tới được đầy đủ cột/nút, không bị cắt vĩnh viễn. |  |
| GUI-003 | Passed | Tại viewport native 431×847, chữ Việt/nhãn đọc được và heading khác body; không áp font phải khớp Windows. Ảnh lấy nguyên trạng màn hình vật lý 1080×2340 bằng ADB. |  |
| GUI-004 | Failed | Đường login trong checklist hiện Username/Sign In; Profile dùng nhãn Việt nhưng nội dung SUT chưa nhất quán tiếng Việt. | [Ảnh 1](screenshots/chrome-android/P3-GUI-004-001-failed-1.png) |
| GUI-005 | Failed | Profile có 0 h1; hai tiêu đề phần đều là h2. | [Ảnh 1](screenshots/chrome-android/P3-GUI-005-001-failed-1.png) |
| GUI-006 | Passed | Cập nhật xanh dương; Thoát/Hủy đơn đỏ, đọc được; không thực hiện Hủy đơn. |  |
| GUI-007 | Passed | Các tổng 0 / 1234567 / 123456789 giữ đúng giá trị, có ₫ và dấu nhóm nghìn. |  |
| GUI-008 | Passed | Ngày hiển thị 14/3/2026 và 5/11/2026 đúng nguồn, nhất quán vi-VN / Asia/Ho_Chi_Minh; không Invalid Date. |  |
| GUI-009 | Passed | Đủ 5 nhãn Việt, nền badge phân biệt; text trạng thái đọc được. |  |
| GUI-010 | Passed | CDP gửi Tab trên Chrome điện thoại thật: đủ 11 control khác nhau, có dấu focus thấy được ở navbar/form/bảng; field email disabled vẫn đọc được. Đây là kiểm tự động, không phải phiên thao tác bằng bàn phím Bluetooth/USB. |  |
| GUI-011 | Passed | Đã chờ GET đơn hoàn tất: đủ bốn header theo thứ tự; năm hàng đúng cặp ID/ngày/tiền/status P3, căn cột đúng. Lỗi header rỗng của lượt đầu là kiểm quá sớm và đã kiểm lại, không tính lỗi SUT. |  |
| GUI-012 | Passed | Email/tên/phone/địa chỉ prefill đúng A của P3, không lấy B hoặc placeholder. |  |
| GUI-013 | Failed | Email disabled, không đổi qua GUI; type thực tế text, không đạt yêu cầu type=email. | [Ảnh 1](screenshots/chrome-android/P3-GUI-013-001-failed-2.png) |
| GUI-014 | Failed | Ba field tên/phone/địa chỉ thiếu accessible name liên kết label/aria; có nhãn nhìn thấy và placeholder nhưng không thay accessible name. | [Ảnh 1](screenshots/chrome-android/P3-GUI-014-001-failed-1.png) |
| GUI-015 | Failed | Field Họ Tên có required nhưng nhãn thiếu *. Ảnh ADB ghi trạng thái thực của lượt chạy lại. | [Ảnh 1](screenshots/chrome-android/P3-GUI-015-001-failed-1.png) |
| GUI-016 | Failed | Nhập dữ liệu hợp lệ gồm Nguyễn Văn Mẫu và phone 0912345678; validation phone từ chối trước PUT, không hoàn thành cập nhật tên. Chưa kiểm các bước sau lưu. | [Ảnh 1](screenshots/chrome-android/P3-GUI-016-001-dialog-1.png), [Ảnh 2](screenshots/chrome-android/P3-GUI-016-002-failed-1.png) |
| GUI-017 | Failed | Phone 9/12 số đầu 0 bị từ chối đúng; 10/11 số hợp lệ đầu 0 cũng bị từ chối, sai expected; không PUT ở các biến thể này. | [Ảnh 1](screenshots/chrome-android/P3-GUI-017-002-dialog-2.png), [Ảnh 2](screenshots/chrome-android/P3-GUI-017-003-failed-2.png), [Ảnh 3](screenshots/chrome-android/P3-GUI-017-004-dialog-3.png), [Ảnh 4](screenshots/chrome-android/P3-GUI-017-005-failed-3.png) |
| GUI-018 | Failed | 1912345678 được PUT và lưu, sai expected; 09a2345678, 09123-5678, +84912345678 bị từ chối, không lưu. | [Ảnh 1](screenshots/chrome-android/P3-GUI-018-001-dialog-1.png), [Ảnh 2](screenshots/chrome-android/P3-GUI-018-002-failed-1.png) |
| GUI-019 | Failed | Địa chỉ tiếng Việt hai dòng cùng phone 0912345678 hợp lệ bị validation phone chặn trước PUT; không hoàn thành cập nhật địa chỉ. | [Ảnh 1](screenshots/chrome-android/P3-GUI-019-001-dialog-1.png), [Ảnh 2](screenshots/chrome-android/P3-GUI-019-002-failed-1.png) |
| GUI-020 | Failed | Click Cập nhật với ba trường hợp lệ, phone 09123456789 bị validation từ chối trước PUT; không hoàn thành cập nhật hồ sơ bằng chuột. | [Ảnh 1](screenshots/chrome-android/P3-GUI-020-001-dialog-1.png), [Ảnh 2](screenshots/chrome-android/P3-GUI-020-002-failed-1.png) |
| GUI-021 | Failed | Chỉ có alert yêu cầu 9–10 số; không có lỗi inline phía trên submit, không hướng dẫn đúng quy tắc đầu 0 và 10–11 số. | [Ảnh 1](screenshots/chrome-android/P3-GUI-021-001-dialog-1.png), [Ảnh 2](screenshots/chrome-android/P3-GUI-021-002-failed-1.png) |
| GUI-022 | Passed | Từ Home, link tài khoản mở đúng /profile với form và lịch sử A/P3. |  |
| GUI-023 | Failed | Loại ảnh hưởng hover: class/màu/aria của link tài khoản không đổi giữa Home/Profile/Home; thiếu active theo route. | [Ảnh 1](screenshots/chrome-android/P3-GUI-023-001-failed-1.png) |
| GUI-024 | Passed | Logo về Home, giữ phiên A/P3 và hồ sơ baseline. |  |
| GUI-025 | Failed | Giỏ ban đầu trống; thêm ba sản phẩm ×1 qua GUI thì cart có đúng ba dòng ×1, nhưng navbar Profile thiếu badge 3. | [Ảnh 1](screenshots/chrome-android/P3-GUI-025-001-failed-2.png) |
| GUI-026 | Failed | Nhãn nút là Thoát, không phải Đăng xuất; click vẫn đưa navbar về trạng thái chưa login. | [Ảnh 1](screenshots/chrome-android/P3-GUI-026-001-failed-1.png) |
| GUI-027 | Passed | Direct /profile và reload khôi phục đúng A/P3 và năm đơn; không 404/trắng trang. |  |
| GUI-028 | Passed | CDP Tab/Shift+Tab trên Chrome Android: tới đủ 11 control từ EShop theo navbar → form → bảng và đi ngược chính xác; không trap trong trang. Không dùng kết quả Windows để thay. |  |
| GUI-029 | Passed | Enter mở đúng Home/Profile; Enter/Space kích hoạt Cập nhật qua validation; Enter textarea xuống dòng và không submit. Không kiểm lưu thành công. |  |
| GUI-030 | Passed | Back/Forward đến đúng Profile/Home, giữ phiên A/P3 và baseline không đổi. |  |
| GUI-031 | Passed | Không token/invalid token và Back sau logout không lộ form/đơn riêng; đường login và login recovery hoạt động. |  |
| GUI-032 | Failed | Trong GET /users/me chậm 3 giây hiện Vui lòng đăng nhập, không chờ trung tính; sau response thật hiển thị A/P3. | [Ảnh 1](screenshots/chrome-android/P3-GUI-032-001-failed-1.png) |
| GUI-033 | Blocked | Validation phone hợp lệ chặn trước PUT; chưa có response lưu thành công nên chưa tới nhánh feedback/thứ tự response và thông báo. |  |
| GUI-034 | Blocked | Validation phone hợp lệ chặn trước PUT; chưa có lần lưu thành công để kiểm đồng bộ navbar/form và persistence sau lưu. |  |
| GUI-035 | Blocked | Cấu hình PUT 500 và network-abort nhưng không có PUT vì validation phone chặn; chưa tới nhánh lỗi lưu hoặc recovery, giữ Blocked. |  |
| GUI-036 | Passed | Sau đóng alert có thể Shift+Tab về phone, sửa và gửi lại bằng keyboard; không trap. Việc phone hợp lệ bị từ chối ghi ở GUI-017. |  |
| GUI-037 | Failed | GET đơn đang chờ 3 giây đã hiện Bạn chưa có đơn hàng nào, thiếu loading; sau response thật chuyển sang năm đơn A/P3. | [Ảnh 1](screenshots/chrome-android/P3-GUI-037-001-failed-1.png) |
| GUI-038 | Failed | A0/P3 có GET 200 và [] thật, message empty đúng nhưng không có icon/hình minh họa. | [Ảnh 1](screenshots/chrome-android/P3-GUI-038-001-failed-2.png) |
| GUI-039 | Failed | GET đơn 500 có kiểm soát lại hiển thị empty, thiếu thông báo lỗi tải riêng; gỡ fault/reload lấy lại năm đơn thật. | [Ảnh 1](screenshots/chrome-android/P3-GUI-039-001-failed-1.png) |
| GUI-040 | Passed | A logout → UI login B/P3 trong cùng context/tab, rồi Profile/Back/Forward: đúng profile và hai đơn B; không quan sát thấy dữ liệu A trong frame đã thu. Số frame: 24. |  |
| GUI-041 | Passed | Đơn fixture P3 #960201 từ pending sang confirmed sau đổi dữ liệu ngoài trang/reload; nhãn/màu mới đúng và các đơn khác không đổi; cuối ca reset. |  |
| GUI-042 | Failed | Tài khoản fixture H1/H2 dựng sẵn của P3: sau reload form hiển thị nguyên chuỗi có thẻ, navbar tạo b/em và hiện đậm/nghiêng. Không nhập/lưu tên; không có PUT. | [Ảnh 1](screenshots/chrome-android/P3-GUI-042-001-failed-2.png), [Ảnh 2](screenshots/chrome-android/P3-GUI-042-002-failed-4.png) |

### 4.5. Phần còn thiếu của Task 3

- GUI-033/034/035 trên cả ba nền tảng: 9 lượt Blocked vì validation phone hợp lệ chặn trước PUT, chưa kiểm được phản hồi lưu thành công, đồng bộ/persistence hoặc lỗi lưu/recovery. Không sửa SUT để ép chạy các nhánh này.
- Chưa có họ tên, MSSV và email sinh viên để hoàn thiện bằng chứng danh tính. Ảnh Android ADB đã có màn hình thiết bị và URL localhost; ảnh phiên bản xác minh riêng Chrome/OS. Ảnh Windows vẫn thiếu khung URL/browser/OS theo yêu cầu; cần hoàn thiện metadata/danh tính cho bộ ảnh nộp, không bịa hoặc vẽ UI trình duyệt giả. Vì còn 9 Blocked và bằng chứng chưa đủ, chưa tuyên bố hoàn thành Task 3.

## 5. Agent Skills và demo

Chưa thực hiện; chưa có link demo.

## 6. AI Critique

Chưa hoàn thiện đoạn critique 200–300 words.

## 7. Khai báo sử dụng AI

I use AI tools for the following tasks,

- Đọc yêu cầu, SRS và slide; khảo sát thành phần/trạng thái của trang Profile.
- Tạo nháp, rà trùng và biên tập checklist theo góp ý người dùng.
- Tạo tài liệu và ghi nhật ký prompt/output.
- Chuẩn bị fixture tổng hợp, viết/chạy Playwright trên Chrome/Firefox Windows và Chrome Android thật; thu actual/Notes, chụp màn hình thiết bị Android bằng ADB và đối chiếu ảnh giao diện. Công cụ và dữ liệu test đặt ngoài thư mục nộp.

Công cụ: OpenAI Codex. Prompt/output nguyên văn, tên công cụ và thời gian từng tương tác nằm trong prompt_log.md. Người dùng quyết định các mục cần sửa/bỏ và bổ sung ý tưởng GUI-042 về họ tên chứa HTML; AI đối chiếu SRS/code và biên tập mục kiểm tra. Chưa có verdict audit đầy đủ.

## Phụ lục A - AI Audit Report

| Prompt / công cụ / thời gian | Output AI | Verdict | Lý do / căn cứ review | Chỉnh sửa thực tế |
| --- | --- | --- | --- | --- |
| Đọc bài và thiết lập log; Codex; timestamp tại prompt_log.md | Tổng hợp yêu cầu và log | Chưa điền | HW03 §9 và AI Templates | Người dùng yêu cầu log đơn giản và chỉ xuất Git log cuối bài |
| Khảo sát FR-04/FR-11; Codex; timestamp tại prompt_log.md | Bản nháp 52 mục | Chưa điền | SRS FR-04/11/21–24, S13 | AI rà trùng và căn cứ; người dùng tiếp tục góp ý |
| Gộp checklist và thêm ID; Codex; timestamp tại prompt_log.md | Checklist hợp nhất | Chưa điền | Đối chiếu kỳ vọng, loại phần trùng và không có căn cứ | Gộp phone hợp lệ/biên; bỏ các điều kiện font, tiền thiếu, label-focus, newline và server không đổi khi mất mạng |
| Chốt 41 mục, đổi ID và dọn tài liệu; Codex; timestamp tại prompt_log.md | GUI-001–GUI-041 và workbook | Chưa điền | Phạm vi đã chọn; bốn IA 11/10/9/11 | Loại các mục người dùng chỉ định, đánh ID liên tục; giữ 41 mục hiện tại |
| `thêm vào report phần checklist ai bỏ sót kiểm tra hiển thị an toàn họ tên chứa html dựa sec-04 và fr-04, check xem cái tôi yêu cầu là đúng là thứ bạn bỏ sót không, nếu có thì thêm vào báo cáo đầy đủ theo đúng yêu cầu đề bào`; OpenAI Codex; 08/11/2026 23:55:05 (UTC+07:00) | GUI-042, dữ liệu H1/H2 và phần giải thích AI bỏ sót tại mục 2.1/2.3 | Chưa điền | FR-04, SEC-04; bản nháp cũ thiếu kiểm HTML; App.jsx:27 dùng dangerouslySetInnerHTML với user.name | Người dùng phát hiện mục thiếu; AI xác minh và bổ sung. GUI-042 Chưa chạy |
| `đọc checklist mới nhất, chuẩn bị dữ liệu thử , không sửa logic sut hay checklist đã chốt, đưa ra kế hoặc viết test bằng playwright để test hết các checklist<br>`; OpenAI Codex; 2026-11-09T00:19:49.658000+07:00 | Dữ liệu tổng hợp và kế hoạch Playwright cho 42 mục | Chưa điền | Checklist chốt và code SUT; chưa coi chuẩn bị dữ liệu là thực thi | Chuẩn bị SQLite riêng, xác định blocker phone và phần cần review giao diện. |
| `để các file vừa tạo ở ngoài thư mục work, có thể bỏ vào một folder ở ngoài phục vụ việc test, cái này không yêu cầu nộp, khi báo cáo sẽ nêu rõ mình sử dụng gì, chỉ những yêu cầu nộp mới để vào work, viết và chạy playwright trên chrome đầy đủ, lưu actual và ảnh failed, ko commit<br>`; OpenAI Codex; 2026-11-09T00:43:27.010000+07:00 | 42 ca Chrome đã thử; 19 Passed, 15 Failed, 8 bị chặn; 18 ảnh Failed | Chưa điền | Actual GUI/API/SQLite và ảnh thật; không sửa SUT hoặc định nghĩa checklist | Chuyển công cụ/dữ liệu ra ngoài work; sửa test phân biệt hover với active navbar và kiểm thêm focus thứ 11; giữ actual hai lần, khôi phục database gốc. |
| Sửa GUI-029/042 theo phạm vi keyboard và hiển thị fixture; Codex + Playwright; timestamp tại prompt_log.md | Test sửa và chạy lại Chrome: GUI-029 Passed, GUI-042 Failed với H1/H2; 2 ảnh lỗi mới | Chưa điền | Checklist mới của người dùng, actual keyboard/DOM và ảnh sau reload; không PUT tên | Bỏ điều kiện lưu thành công ở GUI-029; GUI-042 chỉ dùng tài khoản fixture dựng sẵn để kiểm form/navbar sau reload. |
| Chốt Task 1 theo bằng chứng thực tế; Codex; timestamp tại prompt_log.md | 20 Passed, 19 Failed, 3 Blocked trên Chrome | Chưa điền | Actual GUI/API và ảnh đã thu; không chạy lại hoặc sửa SUT | Người dùng chốt GUI-016/019/020 Failed; giữ GUI-033/034/035 Blocked; giữ kết quả chạy lại GUI-029/042. |
| Lập kế hoạch Task 3 và chạy Firefox cùng checklist, giữ Chrome; Codex + Playwright; timestamp tại prompt_log.md | Firefox: 20 Passed, 19 Failed, 3 Blocked; 23 ảnh Failed, Notes đủ 19 mục; kế hoạch Chrome Windows/Firefox Windows/Chrome Android | Chưa điền | Actual Firefox độc lập; đối chiếu 42 ID và ảnh/DOM; hash/P1 Execution bảo toàn | Tách fixture P2 và cấu hình browser; kiểm lại GUI-010/028 từ focus xác định; không thay kết quả Chrome, không giả Android đã chạy. |
| Chạy checklist trên điện thoại Android qua ADB/Playwright, chụp scrcpy bằng Computer Use; Codex; timestamp tại prompt_log.md | P3: 18 Passed, 19 Failed, 5 Blocked; 42 actual, Notes và ảnh scrcpy; giữ P1/P2 | Chưa điền | Thiết bị/Chrome thật, API localhost và DOM/ảnh đo được; không giả lập Android trên Windows | Loại ảnh đen, kiểm lại header bảng/required; giữ Blocked cho viewport chưa đủ điều kiện và nhánh lưu chưa tới; khôi phục database gốc. |
| Chạy chụp lại toàn bộ ảnh Android bằng ADB theo yêu cầu; Codex + Playwright; timestamp tại prompt_log.md | 42 mục chạy lại, ảnh PNG ADB thay toàn bộ ảnh Android cũ; 18 Passed, 19 Failed, 5 Blocked | Chưa điền | Actual lượt chạy lại và byte PNG trực tiếp từ thiết bị; không đổi P1/P2 | Đồng bộ liên kết ảnh và nguồn ảnh; giữ Notes cho Failed/Blocked; không sửa SUT hoặc commit. |
| Kiểm lại GUI-001/002 Android bằng viewport native và ảnh ADB; Codex + Playwright; timestamp tại prompt_log.md | Hai mục Passed; P3 20 Passed, 19 Failed, 3 Blocked | Chưa điền | Đo đủ ba visualViewport scale=1, kiểm mọi control/cell sau cuộn và footer static; đối chiếu ảnh ADB/DOM | Đổi tạm display/density rồi khôi phục; không sửa SUT/checklist hoặc actual 40 ID khác/P1/P2. |

Chưa có verdict để tổng hợp tỷ lệ VALID/INVALID/INCOMPLETE. Kết luận audit 80–150 chữ và khai báo/chữ ký theo biểu mẫu chưa hoàn thiện.

## Tài liệu tham chiếu

- Đề HW03 - GUI & Usability, §5–6, §9–12, §14–15.
- SRS EShop: FR-04, FR-11, FR-21–24, SEC-04.
- Slide S13 GUI Testing & Usability Testing: trang 8, 11–22.
- AI Templates: AI-01, AI-02, AI-03 và AI-05.
