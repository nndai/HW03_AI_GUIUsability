"""One content source for the reviewed checklist, review trail, Excel and PDF."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'outputs' / 'HW03-01a1ba88'
OUT.mkdir(parents=True, exist_ok=True)

# old reference, IA, component, reproducible action/data, observable expected result, basis
ROWS = [
('1.01','01','Bố cục mặc định','Đăng nhập A, mở /profile tại 1366×768, zoom 100%; xem từ header đến footer.','Form và lịch sử tách thành hai vùng có tiêu đề; không chồng chữ/control; footer không che nội dung hay nút.','S13 tr.16; B01'),
('1.02','01','Bố cục responsive','Mở cùng dữ liệu tại 390×844, 768×1024 và 1366×768; cuộn đến cuối form/bảng.','Mọi trường, nút và 4 cột dữ liệu đơn đều tiếp cận được; cho phép cuộn bảng ngang nhưng không có nội dung bị cắt không thể xem.','S13 tr.21–22; B01'),
('1.03','01','Chữ và tính nhất quán','So sánh các nhãn form, input và hàng bảng ở zoom 100%, dùng dữ liệu có dấu.','Không mất dấu/ký tự hoặc cắt nét chữ; các nhãn form cùng vai trò có cùng font-family và font-size; heading khác vai trò được phép khác kiểu.','S13 tr.16; B02'),
('1.04','01','Nội dung dài và zoom','Nạp fixture L; xem tại 1366×768 với zoom 100% rồi 200%; cuộn/đặt caret xem nội dung.','Đọc được toàn bộ tên/email/địa chỉ bằng vùng nhập hoặc cuộn; không che Cập nhật, navbar hay các cột đơn; không mất control khi zoom.','S13 tr.16,22; B01,B03'),
('1.05','01','Ngôn ngữ','Đọc nhãn, tiêu đề, nút, message và trạng thái do SUT hiển thị trong các bước checklist.','Nội dung SUT dùng tiếng Việt có dấu nhất quán, trừ thuật ngữ kỹ thuật chuẩn và dữ liệu tài khoản do người dùng đặt; không chấm ngôn ngữ UI của browser.','SRS FR-21'),
('1.06','01','Tiêu đề và hierarchy','Mở /profile; đối chiếu heading thấy trên trang với DOM chỉ đọc.','Có đúng 1 h1 mô tả trang; hai phần hồ sơ/lịch sử có heading phân biệt; không lấy tên tab browser thay cho h1.','SRS FR-21'),
('1.07','01','Màu nút hành động','Xem Cập nhật và nút nguy hiểm nếu đang hiển thị, ở trạng thái idle.','Cập nhật có màu hành động xanh dương; nút nguy hiểm/hủy dùng đỏ; không bắt buộc mã hex cụ thể, không thực hiện hủy đơn.','SRS FR-21'),
('1.08','01','Định dạng tổng tiền','Nạp fixture O; đối chiếu tiền từng đơn 0, 1234567, 123456789 với dữ liệu chuẩn.','Mỗi số tiền giữ đúng giá trị, có ký hiệu ₫ và phân cách nghìn; không dùng giá trị mặc định 0 thay cho dữ liệu thiếu.','SRS FR-11,FR-21'),
('1.09','01','Ngày đặt','Nạp O với ngày 2026-03-14 12:00:00 và 2026-11-05 12:00:00; ghi locale/timezone của browser.','Ngày hiển thị đúng ngày/tháng/năm nguồn và theo cùng locale đã ghi; không hiển thị Invalid Date. SRS không bắt buộc dd/MM/yyyy.','SRS FR-11; S13 tr.12,16; B04'),
('1.10','01','Nhãn và màu trạng thái đơn','Nạp O đủ pending/confirmed/shipping/delivered/canceled; so sánh từng badge.','Có nhãn tiếng Việt đúng nghĩa cho cả 5 trạng thái và màu phân biệt; vẫn đọc được trạng thái bằng chữ; không bắt bảng màu code hiện tại làm chuẩn duy nhất.','SRS FR-11'),
('1.11','01','Focus nhìn thấy và khả năng đọc','Dùng Tab đến từng link/nút/input có thể tương tác; so sánh trước/sau focus ở zoom 100%.','Vị trí focus có thay đổi outline/border/background nhìn thấy được; chữ/nhãn vẫn đọc được trên nền thường và disabled. Đây là review định tính, chưa tuyên bố đạt tỷ lệ WCAG.','S13 tr.8,13,16; B05'),
('1.12','01','Cấu trúc bảng và đúng cột','Nạp O; đối chiếu mỗi hàng với cặp ID/ngày/tổng/status trong fixture.','Có header nhận diện Mã đơn, Ngày đặt, Tổng tiền, Trạng thái; giá trị thuộc đúng cột và đúng cùng một đơn; không lệch hàng.','SRS FR-11; S13 tr.12,16'),
('2.01','02','Giá trị ban đầu của form','Đăng nhập A có tên/phone/address đã biết; mở /profile mới.','Email, tên, điện thoại, địa chỉ đúng A và đúng trường; không lấy dữ liệu B hoặc placeholder làm giá trị thật.','SRS FR-04; S13 tr.11–12'),
('2.02,2.03','02','Email chỉ đọc và đúng loại field','Thử click/gõ/paste vào email; xem thuộc tính type qua DOM chỉ đọc.','Email vẫn đúng tài khoản và không đổi qua GUI; field email có type=email theo FR-22 dù đang disabled/readonly. Không thử validate email nhập mới.','SRS FR-04,FR-22'),
('2.04','02','Nhãn gắn đúng control','Click nhãn Tên/Điện thoại/Địa chỉ; xem accessible name của từng control.','Nhãn đưa focus đúng ô tương ứng; control có tên truy cập diễn đạt đúng vai trò qua label/aria-label/aria-labelledby; placeholder không thay nhãn.','S13 tr.16,18; B06'),
('2.05','02','Dấu trường bắt buộc','Ghi các trường đang được form khai báo required hoặc tài liệu đã chốt là bắt buộc; so sánh nhãn.','Mỗi trường được xác định bắt buộc đều có * cạnh nhãn. Mục này không tự kết luận phone/address bắt buộc hay tên toàn khoảng trắng hợp lệ.','SRS FR-22; S13 tr.11'),
('2.07','02','Cập nhật tên tiếng Việt','Giữ phone hợp lệ; đổi tên A thành Nguyễn Văn Mẫu, lưu và mở lại.','Tên được cập nhật đúng dấu/ký tự và đúng tài khoản; không thay email/role. Không suy ra giới hạn tên dài từ dữ liệu mẫu.','SRS FR-04'),
('2.08,2.09','02','Biên độ dài điện thoại','Lần lượt gửi P: 091234567 (9), 0912345678 (10), 09123456789 (11), 091234567890 (12); trường khác hợp lệ.','10/11 chữ số đầu 0 được chấp nhận và giữ số 0 đầu; 9/12 chữ số bị từ chối, không thay dữ liệu đã lưu bằng giá trị sai. Ghi actual từng biến thể.','SRS FR-04; S13 tr.19 EP/BVA'),
('2.10','02','Phân lớp điện thoại sai','Gửi 1912345678, 09a2345678, 09123-5678, +84912345678; giữ trường khác hợp lệ.','Không lưu các chuỗi có đầu số khác 0 hoặc chứa ký tự không phải chữ số. Các quyết định trim khoảng trắng được tách khỏi mục này.','SRS FR-04; S13 tr.19 EP'),
('2.12','02','Địa chỉ nhiều dòng','Giữ tên/phone hợp lệ; nhập địa chỉ V có tiếng Việt, 2 dòng và dấu phẩy; lưu rồi mở lại.','Địa chỉ mặc định sau tải lại còn đủ nội dung, thứ tự dòng và dấu; không bị chuyển sang trường khác. Không tự quy định maxLength.','SRS FR-04; S13 tr.12,20'),
('2.13','02','Gửi đúng thay đổi hồ sơ bằng chuột','Từ baseline A, đổi tên/phone/address hợp lệ; click Cập nhật một lần; đối chiếu bản lưu và request chỉ đọc.','Ba trường cập nhật đúng A; email/role không thay đổi và hồ sơ B giữ nguyên. Không gửi payload sửa role hoặc kiểm sâu API trong checklist GUI.','SRS FR-04'),
('2.14','02','Nội dung và vị trí lỗi nhập','Gửi 091234567 (9 số) rồi quan sát message và vùng trên Cập nhật.','Có lỗi nhận diện trường điện thoại và hướng dẫn quy tắc đầu 0, 10–11 số; lỗi hiển thị trong form phía trên submit theo FR-22; không chỉ kết luận từ alert ngoài form.','SRS FR-04,FR-22; S13 tr.16,18'),
('3.01','03','Tìm và mở Profile','Bắt đầu ở Home đã đăng nhập A; dùng link tài khoản trên navbar.','Mở được /profile và nhận diện được hai phần hồ sơ/lịch sử của A; không cần tự gõ URL để hoàn thành đường đi này.','SRS FR-04; S13 tr.17'),
('3.02','03','Navbar đang chọn','Từ Home vào /profile rồi trở lại Home; so sánh dấu chọn của link tài khoản.','Navbar có dấu highlight phân biệt trang hiện tại; không coi màu cố định giống nhau trên mọi route là bằng chứng active.','SRS FR-23'),
('3.03','03','Logo về Home','Từ /profile đã login A, click EShop.','Đến đúng route /; phiên A vẫn còn, không tự đăng xuất hoặc sửa hồ sơ.','S13 tr.17–18; B07'),
('3.04','03','Link và badge giỏ hàng chung','Chuẩn bị giỏ 0 rồi 3 sản phẩm khác nhau, mỗi loại số lượng 1; xem navbar tại Profile và mở Giỏ hàng.','Link đi đúng /cart; badge phản ánh 3 khi có 3 sản phẩm; với 0 cho phép ẩn hoặc hiển thị 0. Không đánh giá flow checkout.','SRS FR-23; B07'),
('3.05','03','Nhãn và đường thoát','Tại Profile đã login A, xem nhãn nút và kích hoạt đăng xuất.','Nút mang nhãn Đăng xuất; sau click navbar trở về các lựa chọn chưa login. Bảo vệ dữ liệu kiểm tiếp tại GUI-032.','SRS FR-23; S13 tr.17'),
('3.06','03','URL trực tiếp và reload','Khi phiên A hợp lệ, mở /profile trực tiếp rồi reload.','Route tải được, cuối quá trình hiển thị form/lịch sử của A, không lỗi 404 hoặc trắng trang; không dùng việc này thay test persistence GUI-036.','SRS FR-04; S13 tr.17'),
('3.07','03','Thứ tự Tab và Shift+Tab','Từ đầu trang nhấn Tab qua navbar, form và control đang hiển thị; đi ngược bằng Shift+Tab.','Focus theo thứ tự trên xuống dưới/trái sang phải, không vòng kẹt; đến mọi control tương tác; skip email khi thực sự disabled, readonly được phép focus.','SRS FR-21; S13 tr.18'),
('3.08','03','Kích hoạt bằng bàn phím','Dùng Enter trên link; Enter/Space trên nút; Enter trong textarea; gửi dữ liệu hợp lệ từ nút Cập nhật.','Link/nút thực hiện đúng hành động; Enter trong textarea thêm dòng, không gửi nhầm; có thể cập nhật qua keyboard. Không bắt Enter trong mọi input phải submit.','S13 tr.18; B07'),
('3.09','03','Back và Forward','Lưu/không sửa form; điều hướng Profile → Home; Back rồi Forward.','Đến đúng các route trong lịch sử, phiên/tài khoản không đổi và dữ liệu đã lưu không bị thay bởi bản cũ. Không đánh giá bản nháp chưa lưu ở mục này.','S13 tr.17–18,20; B07'),
('4.01,4.03','04','Bảo vệ khi thiếu hoặc hết hiệu lực phiên','Lần lượt dùng phiên không token và token không hợp lệ; mở Profile, thử Back sau đăng xuất.','Không lộ hồ sơ/đơn riêng, không báo thao tác thành công như đang login; có thông báo/đường đăng nhập lại. Ghi riêng kết quả từng điều kiện.','SRS FR-04,FR-11; S13 tr.11; B08'),
('4.02','04','Đang khôi phục phiên','Reload khi token hợp lệ; làm chậm GET /users/me 3 giây trong môi trường thử.','Trong lúc chưa biết kết quả có dấu chờ trung tính, không khẳng định đã mất phiên; khi API thành công hiện đúng A. 3 giây là điều kiện gây chậm, không phải SLA.','S13 tr.13–14; B08'),
('4.04,4.05','04','Đang lưu và click lặp','Làm chậm PUT hồ sơ 3 giây; gửi dữ liệu hợp lệ rồi click nhanh 3 lần khi còn pending.','Có dấu đang xử lý; nút bị khóa hoặc cơ chế tương đương ngăn request trùng khi request đầu chưa xong; kết thúc không có thông báo thành công chồng nhau.','S13 tr.13–14; B09'),
('4.06','04','Phản hồi lưu thành công','Gửi dữ liệu hợp lệ và chờ phản hồi API thành công.','Chỉ sau khi request thành công mới có thông báo xác nhận đã cập nhật; không báo lỗi cho lần lưu đó. Cơ chế alert/toast/inline đều được ở nhánh success.','SRS FR-04; S13 tr.16,20'),
('4.07','04','Đồng bộ và giữ dữ liệu sau lưu','Lưu tên/phone/address mới; xem form/navbar, rời Profile rồi mở lại và reload.','Tên trên navbar và dữ liệu form khớp bản đã lưu; các giá trị vẫn đúng sau mở lại/reload. Không dùng dữ liệu chỉ còn trong React state làm bằng chứng lưu.','SRS FR-04; S13 tr.12,14,20'),
('4.08','04','Phản hồi lỗi lưu','Gây PUT trả 500 hoặc mất mạng trong môi trường thử, gửi dữ liệu hợp lệ.','Không có thông báo thành công; có lỗi cho biết chưa lưu và hướng thử lại; baseline server không thay đổi; có thể gửi lại sau phục hồi mạng.','S13 tr.11,16; B10'),
('4.09','04','Giữ nội dung khi lỗi','Nhập tên/địa chỉ V mới, gửi với phone sai; lặp lại trong điều kiện lỗi PUT, ghi riêng hai nhánh.','Sau lỗi, các giá trị vừa nhập vẫn còn để sửa/thử lại, không tự reset về baseline; không mất phần nội dung không gây lỗi.','S13 tr.11,14; B10'),
('4.10','04','Focus sau đóng thông báo','Dùng keyboard gây validation, đóng thông báo nếu có, rồi tiếp tục Tab/nhập sửa phone.','Focus trở về trang, có thể tiếp cận trường lỗi và sửa/gửi lại bằng keyboard; không mắc kẹt trong dialog hoặc mất khả năng thao tác.','S13 tr.13,18; B05'),
('4.11','04','Đang tải danh sách đơn','Làm chậm GET my-orders 3 giây, mở Profile với tài khoản có đơn.','Trong lúc chờ có loading/dấu đang lấy dữ liệu; chưa hiển thị khẳng định không có đơn; sau thành công chuyển sang bảng dữ liệu.','S13 tr.13–14; B08'),
('4.12','04','Empty state thực sự','Dùng A0 không có đơn; chờ GET my-orders thành công trả [].','Có message thân thiện cho biết chưa có đơn và icon/hình minh họa; không hiển thị hàng đơn giả hoặc thông báo lỗi tải.','SRS FR-24; S13 tr.16'),
('4.13','04','Lỗi tải lịch sử và phục hồi','Làm GET my-orders trả 500, rồi phục hồi API và reload/thử lại.','Khi lỗi có thông báo không tải được đơn, không đồng nhất với chưa có đơn; sau phục hồi có thể lấy và hiển thị dữ liệu thật. Không bắt buộc phải có nút Retry riêng.','S13 tr.11,16,20; B10'),
('4.14','04','Chuyển tài khoản và cô lập dữ liệu','A và B có profile/đơn khác nhau; xem A, logout, login B, mở Profile rồi Back/Forward.','Chỉ profile và đơn của tài khoản hiện tại xuất hiện; không giữ flash/cache dữ liệu riêng A trong phiên B; mọi hàng khớp fixture theo chủ sở hữu.','SRS FR-04,FR-11; S13 tr.14'),
('4.15','04','Trạng thái đơn thay đổi bên ngoài','Ghi baseline một đơn pending; đổi fixture riêng thành confirmed, không bấm Hủy đơn; mở lại/reload Profile.','Cùng mã đơn hiển thị nhãn/màu trạng thái confirmed mới; không làm thay đổi đơn khác. Không bắt buộc realtime/polling khi chưa reload.','SRS FR-11; S13 tr.12,14,20'),
]

CRITERIA = {
'B01':'Môi trường layout đề xuất: viewport CSS 390×844, 768×1024, 1366×768; zoom 100% và 200%. Cuộn bảng ngang hợp lệ nếu vẫn tiếp cận đủ nội dung. Đây là phạm vi kiểm thử, không phải số đo trong SRS.',
'B02':'Typography đề xuất: nhãn cùng vai trò thống nhất font-family/font-size; không glyph thiếu/cắt. Không tự đặt minimum 14/16 px hoặc tuyên bố đạt WCAG khi chưa có chuẩn đó.',
'B03':'Fixture L để kiểm trình bày: tên 80 ký tự Unicode, email dài 100 ký tự hợp lệ, địa chỉ 300 ký tự. Nạp qua fixture riêng, không coi đây là maxLength hoặc bắt form chấp nhận độ dài chưa được đặc tả.',
'B04':'Ghi locale và timezone cho mỗi run. Chấp nhận cách trình bày theo locale nếu giá trị ngày đúng và nhất quán; không tự bắt dd/MM/yyyy.',
'B05':'Focus/readability là review định tính theo slide: có dấu focus thấy được và thao tác tiếp được. Không dùng kết quả này chứng nhận accessibility hoặc tỷ lệ contrast.',
'B06':'Liên kết nhãn-control xét theo hành vi focus và accessible name; không bắt duy nhất một cách viết HTML nếu cách khác cho cùng kết quả truy cập.',
'B07':'Quy ước thao tác GUI: link/nút đúng vai trò, giữ phiên trên điều hướng thường; giỏ 3 loại ×1 để không tranh luận badge đếm dòng hay số lượng. Không yêu cầu Enter trong mọi input submit.',
'B08':'Khôi phục phiên/loading phân biệt với logged-out/empty/error. Delay 3 giây chỉ để trạng thái đủ quan sát, không là yêu cầu tốc độ phản hồi.',
'B09':'Đề xuất chống submit lặp: trong lúc request đầu pending có dấu xử lý và không tạo request trùng do 3 click nhanh. Chấp nhận disable/debounce/cơ chế tương đương; không quy định implementation.',
'B10':'Đề xuất phục hồi lỗi: message đúng loại lỗi, không báo thành công giả, giữ input và thử lại được. Không bắt cụ thể HTTP error text hoặc nút Retry riêng.',
}

DEFERRED = [
('2.06','Họ tên rỗng/toàn khoảng trắng','SRS FR-04 chưa chốt họ tên có bắt buộc hoặc trim không. required trong code chỉ là hiện trạng.','Giữ kiểm dấu * tại GUI-016. Xin quy tắc tên trước khi tạo test chấp nhận/từ chối tên rỗng; không tự ghi Failed chỉ vì thiếu quy tắc.'),
('2.11','Phone/address trống','SRS chưa nói optional/required, cũng chưa phân biệt chưa khai báo và xóa giá trị đã có.','Tách khảo sát hành vi để hỏi TA/đặc tả; chưa tính là checklist có oracle đủ rõ.'),
('3.10','Rời trang khi chưa lưu','Slide nêu đồng bộ/trạng thái nhưng SRS không bắt autosave, giữ draft hoặc dialog xác nhận.','Đưa vào probe usability; không bắt có dialog/giữ draft trong checklist chuẩn.'),
('4.16','Payload thiếu/sai kiểu và response bất thường','Bản nháp gộp ngày/status/tổng lỗi với API chậm; thiếu hợp đồng schema và fallback.','Loading/error đã có GUI-040/042. Payload malformed giữ ở robustness bổ trợ sau khi chốt schema; không tạo hàng loạt Failed không có oracle.'),
]

def old_id(value):
    group, number = value.split('.')
    return f'INV-IA0{group}-{int(number):02d}'

items=[]
mapping={}
for n,(old,ia,component,steps,expected,basis) in enumerate(ROWS,1):
    item={'id':f'GUI-{n:03d}','ia':f'IA-{ia}','component':component,'steps':steps,'expected':expected,'basis':basis,
          'origin':[old_id(v) for v in old.split(',')], 'status':'Chưa chạy','notes':'','evidence':''}
    items.append(item)
    for source in item['origin']:
        mapping[source]=item['id']
for old,*_ in DEFERRED:
    mapping[old_id(old)]='Tách chờ làm rõ'
assert len(items)==44 and len(mapping)==52
assert Counter(i['ia'] for i in items)=={'IA-01':12,'IA-02':10,'IA-03':9,'IA-04':13}

meta={
'title':'HW03 - GUI Checklist FR-04 và FR-11', 'version':'1.0', 'date':'08/11/2026',
'state':'Bản thiết kế chuẩn đề xuất sau AI review; chưa có xác nhận review của sinh viên, chưa thực thi.',
'platforms':['P1 Chrome/Windows','P2 Firefox/Windows','P3 Safari/macOS hoặc Android Chrome'],
'scope':'Một trang /profile: hồ sơ FR-04 và lịch sử đơn FR-11; navbar chung có liên quan. Không mở rộng sang hủy đơn FR-10/checkout.',
}
payload={'meta':meta,'items':items,'criteria':CRITERIA,'deferred':DEFERRED,'mapping':mapping}
(ROOT/'scripts/checklist_data.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8')

intro=f'''# {meta['title']}

Phiên bản {meta['version']} - {meta['date']}. {meta['state']}

## Phạm vi và cách dùng

{meta['scope']}

- 44 mục có ID ổn định GUI-001 đến GUI-044; IA-01: 12, IA-02: 10, IA-03: 9, IA-04: 13. ID INV trong hồ sơ review chỉ nguồn từ 52 mục nháp, không phải mục cộng thêm.
- Cột căn cứ phân biệt SRS với slide S13 và tiêu chí bổ sung B01–B10. B là tiêu chí thiết kế **AI đề xuất**, cần sinh viên review trước execution; không trích như điều khoản SRS hoặc chuẩn WCAG.
- Chưa chạy thì để Chưa chạy. Khi thực thi, ghi Passed/Failed theo expected và actual của từng biến thể. Một mục chỉ Passed khi mọi biến thể bắt buộc của nó đã chạy và đạt; có biến thể thất bại thì Failed và nêu rõ biến thể. Nếu không đến được bước do lỗi trước đó, để Chưa chạy và ghi blocker, không suy ra Failed hoặc Passed cho bước chưa chạy.
- Mỗi Failed phải có Notes giải thích actual/expected và ảnh thật. Evidence ghi đường dẫn trong gói nộp; bug do sinh viên tự viết, có thể thêm ID/link GitHub Issue. Không đòi ảnh cho Passed.
- Thực thi cùng 44 mục trên ít nhất 3 nền tảng theo đề. Workbook có 132 dòng ở Execution (44 × 3) để không trộn kết quả môi trường; đây vẫn là 44 mục thiết kế, không phải 132 mục khác nhau. Chốt phương án P3 trước khi chạy.
- Bảng Markdown dưới là bản mẫu một run. Kết quả gốc theo môi trường nhập ở workbook Execution; sau execution phải cập nhật bảng/report/PDF từ số liệu thực, không nộp bản trống như báo cáo đã hoàn tất.

## Thông tin lần chạy

| Trường | Giá trị |
| --- | --- |
| Sinh viên / MSSV / email | Chưa cung cấp |
| Người thực thi / thời gian | Chưa thực hiện |
| Nền tảng / browser version / OS / device | Chưa điền |
| URL frontend / backend | Ghi môi trường thực tế; khảo sát trước dùng localhost:5175 / localhost:13000 |
| SUT commit / thay đổi môi trường | 85af3ba875c88283615e22cb108f13e2fccaf0e9; ghi thêm thay đổi cục bộ và port trước run |
| Viewport / zoom / locale / timezone | Chưa điền |
| Baseline / fixture / tài khoản thử | Chưa chuẩn bị cho run chính thức |

## Dữ liệu chuẩn cần chuẩn bị

| Fixture | Nội dung và nguyên tắc |
| --- | --- |
| A, B | Hai tài khoản thử khác nhau; biết trước id, email, role, name, phone, address và đơn thuộc từng người; dùng thông tin giả |
| A0 | Tài khoản thử không có đơn; GET danh sách thành công trả [] |
| P | 091234567 / 0912345678 / 09123456789 / 091234567890; chỉ 10–11 chữ số đầu 0 hợp lệ |
| V | Tên Nguyễn Văn Mẫu; phone 0912345678; địa chỉ hai dòng: 123 Đường Thử Nghiệm, Phường Mẫu / Thành phố Thử Nghiệm |
| O | Các đơn đủ 5 status; tiền 0, 1234567, 123456789; ngày có ngày >12 để phân biệt tháng/ngày; ít nhất một đơn của B không được thấy khi A login |
| L | Fixture dài theo B03, nạp riêng để kiểm layout; không dùng làm yêu cầu maxLength |
| Lỗi/chậm | Trên môi trường thử riêng: delay 3 giây, 500 hoặc network offline; ghi rõ cách tạo và khôi phục; không thay expected theo code đang lỗi |

## Checklist hợp nhất

| ID | IA | Thành phần / trạng thái | Thao tác và dữ liệu | Kết quả mong đợi | Căn cứ | Kết quả | Notes | Ảnh / Issue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
'''
md=intro
for i in items:
    md+='| '+' | '.join(i[k].replace('|','\\|').replace('\n','<br>') for k in ['id','ia','component','steps','expected','basis','status','notes','evidence'])+' |\n'
md+='\n## Tiêu chí bổ sung đề xuất\n\n'
for key,value in CRITERIA.items():
    md+=f'- **{key}:** {value}\n'
md+='''
## Nguồn và nguyên tắc đối chiếu

- SRS EShop: README.md của SUT, FR-04 (dòng 62–68), FR-11 (164–168), FR-21 (242–248), FR-22 (250–256), FR-23 (258–263), FR-24 (265–270), bản đọc ngày 08/11/2026. Code dùng để nhận diện control/trạng thái; không dùng làm oracle thay SRS.
- Slide S13 GUI Testing & Usability Testing: trang 8 (accessibility), 11–14 (validation/default/failure/synchronization/control state), 16 (GUI checklist), 17–18 (navigation), 19 (EP/BVA/state transition), 20–22 (integration/compatibility/platform). Số trang theo bản PDF, không theo số dòng Markdown.
- HW03 §6 Task 1/3: >40 mục, đủ bốn IA; execute Passed/Failed, Notes và ảnh Failed; thực thi trên ≥3 nền tảng. HW03 §14 yêu cầu Excel checklist, test summary, Markdown/PDF. Thông tin sinh viên và ảnh môi trường sẽ điền bằng dữ liệu thật.
- Không gán Failed vì thiếu breadcrumb tại Profile, dark mode, RTL, pagination hoặc step indicator một bước: chưa có yêu cầu áp dụng. Các điểm cần làm rõ và toàn bộ mapping từ bản nháp nằm trong docs/checklist_review.md.

## Test summary hiện tại

| IA | Đã thiết kế | Lượt dự kiến trên 3 nền tảng | Đã chạy | Passed | Failed |
| --- | ---: | ---: | ---: | ---: | ---: |
| IA-01 | 12 | 36 | 0 | 0 | 0 |
| IA-02 | 10 | 30 | 0 | 0 | 0 |
| IA-03 | 9 | 27 | 0 | 0 | 0 |
| IA-04 | 13 | 39 | 0 | 0 | 0 |
| Tổng | 44 | 132 | 0 | 0 | 0 |

## Khai báo AI và review

Phiên bản nháp và bản chỉnh kỹ thuật này do OpenAI Codex tạo. Người dùng đã yêu cầu gộp, thêm ID và rà trùng/căn cứ/kỳ vọng; đây chưa phải bằng chứng sinh viên đã review hoặc bổ sung thủ công. Chưa có phần “SV bổ sung” được xác nhận. Sinh viên cần đối chiếu, ghi quyết định và bổ sung mục còn thiếu cùng lý do trước khi hoàn thiện yêu cầu human review của đề. Prompt/output nguyên văn được giữ trong prompt_log.md; AI Audit trong ai_audit.md.
'''
(OUT/'GUI_Checklist.md').write_text(md,encoding='utf-8')

review='''# Review bản nháp và truy vết checklist chuẩn

Ngày 08/11/2026. Người thực hiện review kỹ thuật: OpenAI Codex, theo yêu cầu của người dùng. Đây không phải chữ ký/verdict review của sinh viên. Giữ nguyên docs/profile_inventory.md làm bản AI nháp để so sánh.

## Kết quả hợp nhất

52 mục nháp → gộp 4 cặp (giảm 4) → tách 4 mục chưa đủ oracle → **44 mục**. Phân bổ mới: IA-01 12, IA-02 10, IA-03 9, IA-04 13. Không thêm mục nhân tạo để bù số lượng. Các phần bàn phím/trình bày/persistence được chuyển đúng mục, tránh tính lại cùng assertion. Nội dung inventory được giữ nguyên; chỉ thêm ID nguồn để truy vết. Git giữ phiên bản trước khi thêm ID.

ID nguồn INV-IA01-01 nghĩa là mục 01 của IA-01 trong inventory, tương tự cho bốn nhóm; GUI-xxx là ID dùng thực thi. File chuẩn: outputs/HW03-01a1ba88/GUI_Checklist.md và workbook cùng tên; PDF ở output/pdf/GUI_Checklist.pdf.

## Các quyết định và lý do sửa

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

## Mục tách chờ làm rõ, không tính vào 44

| ID nguồn | Nội dung | Thiếu căn cứ/kỳ vọng | Đề xuất xử lý |
| --- | --- | --- | --- |
'''
for old,title,reason,action in DEFERRED:
    review+=f'| {old_id(old)} | {title} | {reason} | {action} |\n'
review+='''
Các câu hỏi bổ sung: trim phone trước validation hay từ chối khoảng trắng; giới hạn tên/địa chỉ; bắt buộc breadcrumb tại Profile hay không. Chưa có câu trả lời thì không tạo expected bắt buộc. Dark mode/RTL chỉ là ý tưởng mở rộng, không thêm hàng Failed mặc định.

## Mapping toàn bộ 52 mục nháp

| ID nguồn | Đích / quyết định |
| --- | --- |
'''
for key,value in sorted(mapping.items()):
    review+=f'| {key} | {value} |\n'
review+='''
## Phần sinh viên cần thực hiện

- [ ] Rà 44 mục, các quy ước B01–B10 và quyết định sửa; ghi ngày/người review thật.
- [ ] Chấp nhận/sửa/bỏ các tiêu chí bổ sung; cập nhật ID ổn định và số lượng thực nếu có thay đổi.
- [ ] Bổ sung mục AI bỏ sót dựa trên quan sát của chính sinh viên, giải thích vì sao AI bỏ sót. Các sửa do AI ở trên không được ghi là “SV tự bổ sung”.
- [ ] Điền verdict VALID/INVALID/INCOMPLETE, căn cứ và bản SV sửa trong AI Audit; chưa tự điền thay.
- [ ] Chốt 3 nền tảng, baseline và oracle còn phụ thuộc trước execution; không sửa SUT để ép Passed.
- [ ] Sau execution: cập nhật actual/Passed/Failed/Notes/ảnh thật, report và PDF; phần bị blocker phải được nêu, không báo hoàn tất giả.

Không có bước thực thi hoặc bug report mới trong lượt review này. Git commit log sẽ xuất ở cuối bài theo yêu cầu người dùng.
'''
(ROOT/'docs/checklist_review.md').write_text(review,encoding='utf-8')

# Add traceable IDs to the draft without changing the proposed checks.
inventory_path=ROOT/'docs/profile_inventory.md'
inventory=inventory_path.read_text(encoding='utf-8')
import re
active_group=None
annotated=[]
for line in inventory.splitlines():
    match=re.match(r'### IA-(0[1-4]) — ',line)
    if match:
        active_group=match.group(1)
    elif line.startswith('## 5.'):
        active_group=None
    if active_group:
        if line.startswith('| STT |'):
            line=line.replace('| STT |','| ID nguồn |',1)
        elif re.match(r'^\| \d{2} \|',line):
            line=re.sub(r'^\| (\d{2}) \|',lambda m:f'| INV-IA{active_group}-{m.group(1)} |',line,count=1)
    annotated.append(line)
inventory_path.write_text('\n'.join(annotated)+'\n',encoding='utf-8')
print('Prepared 44-item checklist and review mapping for all 52 draft entries.')
