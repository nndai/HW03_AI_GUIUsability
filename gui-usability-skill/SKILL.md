---
name: hw3-gui-usability-skill
description: Thiết kế, review và thực thi GUI checklist, chuẩn bị và phân tích usability cho một màn hình hoặc flow, theo yêu cầu HW03 và bằng chứng thực tế.
---

# GUI checklist và usability

## Mục tiêu và đầu vào

Thực hiện trọn phần việc người dùng giao, từ đọc yêu cầu đến kết quả có thể review. Skill này tự chứa hướng dẫn, không cần tải tài liệu phụ hoặc truy cập website ngoài.

Nhận các đầu vào: màn hình/flow, SRS hoặc yêu cầu sản phẩm, source SUT nếu có, địa chỉ ứng dụng, nền tảng kiểm thử, thư mục output và phạm vi quyền thao tác. Khi phân tích usability, cần dữ liệu khảo sát thật. Tìm thông tin trong tài liệu người dùng cung cấp trước khi hỏi; chỉ hỏi phần thiếu ảnh hưởng đến kết quả. Đề hoặc quy định mới do người dùng cung cấp được ưu tiên hơn bản tóm tắt HW03 trong skill.

Chỉ ghi vào nơi được phép. Nếu chỉ review thì không tạo file, log hoặc commit. Không tự sửa logic SUT, reset dữ liệu, tạo Issue, upload video hoặc commit ngoài quyền đã được giao.

## Cách sử dụng bộ skill

Đây là bộ hướng dẫn độc lập: mọi chỉ dẫn cần thiết nằm trong thư mục này. SRS, source và ứng dụng là đối tượng đầu vào do người dùng cung cấp, không phải tài liệu phụ thuộc cố định trên một máy. Không cần cài thêm skill khác để hiểu quy trình; chọn công cụ có sẵn phù hợp với quyền thao tác.

Các phần dưới đây bao gồm thiết kế checklist, thực thi, usability và bàn giao. Đọc phần tương ứng với công việc được giao.

Nếu yêu cầu làm từ đầu đến cuối, thực hiện lần lượt thiết kế, review, chạy, tổng hợp và kiểm tra đầu ra. Nếu chỉ được giao một phần, đọc phần tương ứng và không tự sửa những phần đã chốt. Thiếu người thật hoặc thiết bị thì hoàn thành phần độc lập trước, ghi rõ phần chưa thể thực hiện thay vì tự điền bằng suy đoán.

Prompt ví dụ: dùng skill này cho trang hồ sơ gồm form thông tin và lịch sử đơn, đọc SRS và source tôi cung cấp, tạo rồi review checklist, chạy trên môi trường được phép, xuất vào thư mục demo riêng, không sửa SUT và không commit.

## 1. Chốt phạm vi và căn cứ

- Chọn ít nhất một màn hình GUI và một flow usability; tránh trùng màn hình chính/flow với thành viên nhóm theo thông tin người dùng cung cấp.
- Một trang có thể gồm nhiều khu vực, ví dụ form hồ sơ và bảng lịch sử đơn; có thể xử lý trong một lần gọi skill.
- Đọc yêu cầu và code liên quan, lập inventory control, trạng thái, dữ liệu và FR. Code mô tả triển khai, không thay thế yêu cầu kỳ vọng.
- Phân biệt yêu cầu minh thị, tiêu chí GUI chung và khuyến nghị thiết kế. Không tự đặt giới hạn ký tự, định dạng, dark mode hoặc RTL nếu không có căn cứ.
- Có thể dùng nguyên tắc accessibility như nhãn rõ, thao tác bàn phím, focus nhìn thấy, lỗi dễ hiểu; ghi đúng nguồn áp dụng, không tự tuyên bố chứng nhận WCAG.

## 2. Thiết kế và review checklist

Với HW03, cần hơn 40 mục có ý nghĩa, bao phủ đủ bốn nhóm:

| Nhóm | Phạm vi |
| --- | --- |
| IA-01 | Bố cục, nội dung, tính nhất quán, định dạng và khả năng đọc |
| IA-02 | Nhãn/control, nhập liệu, readonly, validation và tương tác form |
| IA-03 | Đường vào màn hình, liên kết, điều hướng và bàn phím |
| IA-04 | Loading, empty, error, success và trạng thái dữ liệu |

Dùng các cột: ID, khu vực, IA, mục kiểm tra, tiền điều kiện/dữ liệu, thao tác, kỳ vọng, căn cứ, nền tảng, kết quả, Notes, bằng chứng.

Mỗi mục kiểm một mục tiêu, có kỳ vọng quan sát được. Các trường hợp lệ khác có thể là tiền điều kiện, không cần tạo assertion cho tất cả. Không tách các biến thể tương đương để tăng số lượng; không gộp nhiều mục tiêu độc lập vào một dòng.

Trước khi chốt, loại mục trùng, ngoài phạm vi, thiếu căn cứ hoặc không thể xác định kết quả. Nếu còn dưới 41, tìm coverage thật hoặc đề xuất mở rộng phạm vi, không bịa yêu cầu. Không bắt mỗi nhóm IA có số mục bằng nhau.

Giữ đúng lịch sử AI draft và review của sinh viên. Mục do sinh viên bổ sung cần giải thích AI đã bỏ sót gì và vì sao; không gán gợi ý của AI thành phát hiện độc lập của sinh viên.


## Quy trình thiết kế chi tiết

Bắt đầu bằng bảng inventory ngắn: khu vực, control, trạng thái, dữ liệu cần có và yêu cầu liên quan. Đọc cả handler và component con để không bỏ trạng thái lỗi hoặc điều hướng. Nếu source không có, khảo sát UI và ghi rõ giới hạn; không khẳng định đã đối chiếu triển khai.

Đánh dấu mỗi kỳ vọng là yêu cầu SRS, tiêu chí GUI từ môn học, hoặc khuyến nghị bổ sung. Nếu chưa rõ, đưa vào danh sách cần làm rõ và không dùng để kết luận lỗi. Ví dụ trường địa chỉ có dấu phẩy không tự mang nghĩa bắt buộc hệ thống chuẩn hóa địa chỉ; multiline chỉ cần kiểm nếu phù hợp mục tiêu và control.

Dùng một bảng truy vết vừa đủ: ID, yêu cầu, control và trạng thái. Một yêu cầu có thể cần nhiều mục nếu chúng kiểm những hành vi khác nhau; nhiều dữ liệu tương đương không tự tạo thêm coverage. Một mục có nhiều biến thể phải ghi rõ biến thể nào đã chạy, không đánh Passed tổng thể khi vẫn chưa kiểm biến thể quan trọng.

Ví dụ cấu trúc hợp lệ: mục kiểm “email chỉ đọc”, tiền điều kiện “đăng nhập tài khoản thử”, thao tác “thử sửa bằng tương tác UI”, kỳ vọng “không sửa được email qua UI”. Không suy ra rằng API cũng chặn thay email nếu chưa kiểm API, vì đó là kết luận khác phạm vi.

## 3. Thực thi và bằng chứng

Kiểm tra SUT đang chạy trước khi khởi động. Đọc cơ chế seed/reset DB; bảo toàn dữ liệu và dùng fixture thử nghiệm được phép. Không restart nếu có nguy cơ mất dữ liệu chưa xử lý.

Có thể kiểm tay hoặc dùng Playwright. Automation phù hợp với giá trị, thuộc tính, điều hướng và request; quan sát thủ công phù hợp với hình ảnh hoặc thiết bị khó tự động hóa. Dùng selector theo role/label, chờ trạng thái thực và assertion đúng mục tiêu. Không dùng click thay kiểm bàn phím, mock success thay lưu thật, hoặc sửa sản phẩm để test xanh.

| Kết quả | Điều kiện |
| --- | --- |
| Passed | Đã thực thi đúng tiền điều kiện và quan sát được kỳ vọng đạt |
| Failed | Đã kiểm mục tiêu và có bằng chứng kỳ vọng bị vi phạm |
| Blocked | Chưa tới được mục tiêu vì lỗi tiền điều kiện hoặc công cụ |

Timeout/script lỗi không tự đồng nghĩa sản phẩm Failed. Đọc code chỉ là bằng chứng tĩnh, không được khai đã chạy. Ví dụ lưu dữ liệu hợp lệ bị chặn là Failed của mục lưu; nhánh thông báo sau lưu thành công chưa quan sát được là Blocked.

Đề HW03 yêu cầu Passed/Failed: nếu còn Blocked thì khai rõ execution chưa hoàn tất; thử phương án hợp lệ như kiểm tay, không đổi nhãn để đủ bảng. Workaround phải ghi điều kiện thay đổi và không được dùng để chứng minh ca chuẩn.

Mỗi Failed có Notes nêu thực tế so với kỳ vọng và ảnh phù hợp. Giữ ID ổn định, dẫn ảnh tương đối. Một bug gốc có thể liên quan nhiều mục, không nhân bản bug theo số dòng Failed. Theo policy môn học, bug report phải do sinh viên viết; AI không nháp mô tả, chỉ review bản sinh viên cung cấp. Bug thật cần báo cáo Markdown và GitHub Issue có ảnh; chỉ tạo Issue khi được giao.

## 4. Kiểm thử ba nền tảng

Task 3 dùng cùng checklist trên ít nhất ba nền tảng: Chrome, Firefox và Safari hoặc Android Chrome; Expo Go trên điện thoại thật có thể thay một nền tảng. BrowserStack/LambdaTest trial được ưu tiên; đề cho phương án thay thế khi trial hết hạn, cần ghi đúng điều kiện sử dụng.

Ghi browser/version, OS, thiết bị, viewport và điều kiện chạy thực tế. Không gọi giả lập mobile trên Windows là Android thật hoặc WebKit trên Windows là Safari. Không sao chép kết quả giữa nền tảng.

Ảnh cần thể hiện browser/OS/device, localhost, student email overlay; ID/họ tên theo đề hoặc ngoại lệ giảng viên đã xác nhận. Không thêm nhãn để giả môi trường, che lỗi hoặc sửa nội dung kết quả.

Tách số mục độc lập khỏi số lượt theo nền tảng. Tính Passed/Failed/Blocked từ dữ liệu thật, không ép các nền tảng có kết quả giống nhau.


## Chuẩn bị từng ca và xử lý trở ngại

Trước mỗi ca, xác nhận tài khoản, dữ liệu ban đầu và nền tảng khớp mục kiểm tra. Chỉ dùng fixture có quyền thay đổi. Nếu cần backup, kiểm đường dẫn, tính nhất quán và cách khôi phục; sao chép file DB khi đang ghi không mặc nhiên là bản sao an toàn. Không reset toàn bộ hệ thống chỉ để sửa một fixture.

Khi test đỏ, phân loại nguyên nhân trước khi chạy lại: sản phẩm vi phạm kỳ vọng, setup sai, selector hỏng, dữ liệu không đúng, hoặc công cụ không hỗ trợ. Chỉ retry khi có giả thuyết kiểm chứng được. Sau vài lần cùng trở ngại, chuyển sang phương pháp hợp lệ khác hoặc ghi blocker; không lặp vô hạn.

Kiểm persistence cần quan sát vượt khỏi form hiện tại: thao tác lưu, kết quả xử lý và dữ liệu khi quay lại. Nếu request không được gửi vì validation, không thể kết luận nhánh server error đã được kiểm. Nếu dùng delay hoặc lỗi giả để kiểm trạng thái, ghi đây là điều kiện điều khiển có chủ đích, không báo thành bug tự nhiên.

Khi chạy trên điện thoại thật, xác nhận ứng dụng gọi được backend và không chỉ tải trang tĩnh. Nếu thay mật độ hiển thị hoặc kích thước màn hình để kiểm điều kiện đặc biệt, công bố cấu hình, không gọi đó là mặc định thiết bị. Khôi phục thay đổi thử nghiệm khi nằm trong quyền đã được giao.

## 5. Usability với người thật

Chuẩn bị một nhiệm vụ theo mục tiêu, không chỉ từng nút. Xác định trạng thái bắt đầu, dữ liệu thử và tiêu chí thành công. Nếu bắt đầu từ Home đã đăng nhập, có thể đăng nhập sẵn trên máy người tổ chức; người tham gia phải tự thao tác.

HW03 cần bảy người thật ngoài lớp, phù hợp đối tượng; ưu tiên không IT/testing. Bảng nộp có tên và liên hệ xác minh được, che bốn số giữa của số điện thoại theo đề. Không dùng placeholder “đã che” thay giá trị thật. Không công khai liên hệ đầy đủ.

Chạy pilot với một người trước các phiên chính thức: ghi thời điểm, vấn đề phát hiện và điều chỉnh hoặc lý do không đổi. Kiểm tra khởi động/ghi hình không thay pilot. Nếu làm sau khảo sát, ghi là lượt thử bổ sung, không sửa thứ tự quá khứ.

Xin consent phù hợp cho tham gia, ghi màn hình/âm thanh và công bố. Giới thiệu đang kiểm sản phẩm, khuyến khích think aloud, quan sát trung lập và chỉ hỗ trợ khi thực sự mắc kẹt. Ghi trợ giúp nếu có. Thu thang đo sau nhiệm vụ, rồi hỏi về rõ ràng, phục hồi lỗi, tốc độ và tin cậy.

AI không được tạo participant, đáp án, lời nói, consent hoặc video diễn lại rồi khai là khảo sát thật. Khi đổi người/quay phiên mới, dữ liệu phải thuộc đúng phiên mới. Bản quay minh họa hoặc lượt lặp cần được ghi đúng tính chất.

Dùng SUS, UEQ-S hoặc thang tự thiết kế có giải thích. Với SUS, giữ nội dung 10 câu thực dùng, đáp án 1–5, điểm từng người và trung bình. Câu lẻ: đáp án trừ 1; câu chẵn: 5 trừ đáp án; tổng nhân 2,5. Điểm SUS 0–100 không phải phần trăm hoàn thành. Thiếu đáp án thì báo thiếu, không tự điền.

Giữ kết quả nhiệm vụ thật kể cả 0/7 hoàn tất. Thời gian không là cột bắt buộc riêng; nếu đo, nêu cách đo và không gọi thời gian dừng do thất bại là hoàn thành thành công.

Nhóm finding theo bằng chứng, số người gặp, tác động, mức độ và đề xuất. Phân biệt bug vi phạm yêu cầu với vấn đề thiết kế và giả thuyết chưa kiểm chứng. Không suy nhánh success bị lỗi nếu chưa tới nhánh đó; không suy rộng bảy người thành toàn bộ người dùng.


## Biểu mẫu tối thiểu và cách tổng hợp

Một phiếu phiên có thể gồm: mã người, thời điểm, phiên bản task card, xác nhận consent, kết quả nhiệm vụ, hành vi đáng chú ý, trợ giúp đã cung cấp, đáp án thang đo, bốn phản hồi mở và bằng chứng. Chỉ thu thông tin cần thiết, không ép thêm tuổi hoặc nghề khi chúng không phục vụ đối tượng nghiên cứu.

Bảng pilot cần ghi thực tế người thử đã làm gì và quy trình thay đổi ra sao. Không bắt pilot phải phát hiện lỗi mới; kết luận task card đủ rõ và không cần sửa là hợp lệ nếu quan sát thật hỗ trợ. Khi phát hiện blocker đã biết, vẫn có thể kiểm tính rõ ràng của nhiệm vụ và cách ghi nhận.

Phân biệt tỷ lệ thực hiện đủ phiên với tỷ lệ hoàn thành nhiệm vụ. Bảy người đều tham gia đến cuối nhưng không ai lưu được là bảy phiên thực hiện và không có nhiệm vụ thành công. Không viết “hoàn tất nhanh” chỉ vì họ dừng sớm do lỗi. Nếu thiếu recording hoặc không được phép ghi âm, khai rõ bằng chứng đang có và hạn chế, không tự viết đã được miễn.

Chấm SUS từ đáp án thật và kiểm từng giá trị thuộc thang 1–5. Ví dụ một người chọn tất cả câu lẻ là 4, câu chẵn là 2 thì có tổng đóng góp 30 và SUS 75. Đây chỉ là ví dụ tính toán, không được đưa vào bảng participant thật. Nếu dùng bản dịch, giữ nội dung đã hỏi để người review hiểu Q1 tới Q10.

Với findings, dẫn đúng người thực sự gặp vấn đề. Một người muốn focus rõ hơn không tự được tính là khó tìm trang tài khoản. Đếm tần suất trên người duy nhất, không đếm số lần thử lưu thành số người. Severity nói mức ảnh hưởng; priority còn phụ thuộc tần suất, phạm vi và khả năng khắc phục.

## 6. Báo cáo và bàn giao

Giữ báo cáo gọn: phạm vi/môi trường; Task 1 checklist và kết quả; Task 2 nhiệm vụ, người, pilot/protocol, quan sát, SUS và findings; Task 3 matrix/bằng chứng. Tránh lặp baseline, log API, timeline từng giây, codec video và thống kê không phục vụ kết luận.

Hồ sơ HW03 gồm báo cáo chính MD/PDF, bug report và Issue có ảnh, Excel checklist và summary, bằng chứng usability/bảng bảy người, ảnh nền tảng, AI critique/audit MD/PDF, git log text và README. Critique dài 200–300 từ; audit ghi công cụ, thời điểm, prompt và output thực. Các tài liệu khai báo/quyền riêng tư theo quy định được cung cấp. Không tạo lịch sử, chữ ký hoặc commit quá khứ giả.

README có số màn hình/flow, checklist thiết kế/thực thi/Passed/Failed, bug, participant, video và tự đánh giá 30/40/20/10. Tên ZIP: StudentID_HW03_AI_GUIUsability_000-100.zip, phần điểm dùng ba chữ số. Không chỉ nộp liên kết thay tệp bắt buộc.

Phần Agent Skills nộp chính thư mục skill này và YouTube demo sử dụng thật từ đầu đến cuối trên một màn hình/flow hoàn chỉnh. Cho thấy prompt, đầu vào, quá trình, đầu ra và review; không chỉ đọc nội dung skill. Skill được kiểm cấu trúc chưa đồng nghĩa đã demo thành công.

Trước bàn giao, đối chiếu report/README/Excel, số liệu và bằng chứng; kiểm file/link, dữ liệu participant, nguồn kết quả và phần còn thiếu. Nếu có PDF, kiểm đọc được bảng và tiếng Việt. Trả lời ngắn: file đã tạo, việc đã kiểm chứng, giới hạn và phần người dùng cần bổ sung. Không hứa tối đa điểm khi còn yêu cầu chưa đáp ứng.

## Kiểm tra cuối và minh chứng tái sử dụng

Đối chiếu ít nhất bốn nguồn: bảng checklist, dữ liệu thực thi, báo cáo và README. Số bug không bắt buộc bằng số Failed vì nhiều mục có thể chung nguyên nhân. Số người không tính pilot. Không để báo cáo chính còn ghi chưa khảo sát trong khi file riêng đã có kết quả đầy đủ.

Kiểm các liên kết tương đối trong bản đóng gói, các tệp bắt buộc và khả năng mở bằng chứng. Với liên kết video, không kết luận đã xem nội dung chỉ vì URL tồn tại. Tôn trọng quyền công bố: đồng ý tham gia không tự đồng nghĩa đồng ý xuất hiện trong video công khai.

Để demo, dùng thư mục output riêng, cho thấy prompt thật, skill xử lý đầu vào, checklist tạo ra và kết quả review. Nếu được giao chạy, trình diễn thực thi thật rồi cho thấy tổng hợp phù hợp. Không dựng một lỗi giả chỉ để video có tình tiết. Một trang gồm hai khu vực có thể nằm trong cùng video.
