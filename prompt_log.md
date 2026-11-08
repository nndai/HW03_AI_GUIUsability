# Prompt log

## 1

Tool: OpenAI Codex

Thời gian: 08/11/2026 16:43:35 (UTC+07:00)

### Prompt

```text
bạn hãy đọc folder bài tập, hiểu nó bài tập, tạo git cho thư mục work, và log lại tất cả nội dung prompt trong chat ra file theo đúng yêu cầu

```

### Output

```text
Mình sẽ đọc đề và các yêu cầu trong thư mục, xác định thư mục `work`, rồi khởi tạo Git và ghi lại prompt trong chat theo định dạng đề yêu cầu.


Đề yêu cầu lưu cả prompt nguyên văn, đầu ra AI, tên công cụ và thời gian; mẫu audit còn có phần sinh viên đánh giá và sửa đầu ra. Thư mục `work` hiện trống và chưa có Git. Hướng dẫn sẵn có chọn phạm vi Hồ sơ cá nhân và Lịch sử đơn hàng, nên mình sẽ ghi nhận phạm vi này và thiết lập log để tiếp tục dùng trong các bước sau.


Mình đã tạo bản tóm tắt yêu cầu, khung audit chờ bạn review và công cụ lưu nguyên văn hội thoại từ bản ghi của chat này, với giờ Việt Nam. Mình đang kiểm tra log và tạo các commit khởi tạo. Log sẽ tiếp tục ghi cả câu trả lời cuối; các chat cũ chưa có dữ liệu gốc sẽ được ghi rõ là chưa nhập.


Đã hoàn tất:

- Đọc đề, quy định và hướng dẫn; ghi nhận phạm vi **FR-04 + FR-11 tại `/profile`**.
- Khởi tạo Git trong thư mục `work`, nhánh `main`, có **2 commit** và file lịch sử.
- Lưu [prompt và phản hồi AI nguyên văn](C:/Users/daila/Desktop/HW3/2026.HW03.GUI_Usability_work/ai/prompt_log.md), kèm công cụ và giờ Việt Nam; đã kiểm tra khớp bản ghi gốc.
- Tạo [khung AI Audit](C:/Users/daila/Desktop/HW3/2026.HW03.GUI_Usability_work/ai/ai_audit.md) chờ bạn review.

Đã bật ghi tiếp chat tự động, tự dừng sau 30 phút không có tin nhắn. Git hiện ở máy, chưa nối GitHub vì chưa có địa chỉ repo.
```

## 2

Tool: OpenAI Codex

Thời gian: 08/11/2026 16:57:54 (UTC+07:00)

### Prompt

```text
log prompt chỉ cần đánh số, tool, thời gian lúc prompt, prompt nguyên văn, và output nguyên văn, format đơn giản, ko cần id, session, md có style đơn giản

```

### Output

```text
Mình sẽ đổi log sang Markdown đơn giản, mỗi lượt chỉ có số thứ tự, tool, thời gian gửi prompt, prompt nguyên văn và output nguyên văn; đồng thời sửa bộ ghi tự động để giữ đúng định dạng này.

```

## 3

Tool: OpenAI Codex

Thời gian: 08/11/2026 16:59:10 (UTC+07:00)

### Prompt

```text
bỏ thử mục ai, .local luôn

```

### Output

```text
Mình sẽ bỏ hai thư mục `ai` và `.local`, đưa `prompt_log.md` và `ai_audit.md` ra ngay thư mục `work`, rồi cập nhật bộ ghi tự động theo vị trí mới.

```

## 4

Tool: OpenAI Codex

Thời gian: 08/11/2026 17:00:09 (UTC+07:00)

### Prompt

```text
git commit log để cuối xuất sau

```

### Output

```text
Mình sẽ để cuối bài mới xuất `git_commit_log.txt`, bỏ bản log tạm hiện tại và vẫn commit từng bước như yêu cầu của đề.


Đã chỉnh xong:

- Log chỉ có số thứ tự, tool, thời gian prompt, prompt và output nguyên văn.
- Bỏ thư mục `ai`, `.local`; đưa [prompt_log.md](C:/Users/daila/Desktop/HW3/2026.HW03.GUI_Usability_work/prompt_log.md) ra thư mục `work`.
- Vẫn commit từng bước, **cuối bài mới xuất Git commit log**.
```

## 5

Tool: OpenAI Codex

Thời gian: 08/11/2026 17:05:19 (UTC+07:00)

### Prompt

```text
ok, xem trang hồ sơ và lịch sử đơn hàng trên web, fr-04 và fr-11, đọc code, srs liên quan, liệt kê các thành phần và trạng thái cần kiểm tra, bạn có thể chạy sut, dùng computer use để check giao điện chuẩn hơn, đối chiếu srs và slide, chia các nội dung cần kiểm tra vào ia-01 đến ia-04


```

### Output

```text
Mình sẽ đọc SRS và code của FR-04, FR-11, mở trang web để đối chiếu giao diện thực tế, rồi lập danh sách thành phần và trạng thái cần kiểm tra theo IA-01 đến IA-04, bám theo slide.


SRS xác định ba trường được sửa là họ tên, số điện thoại và địa chỉ; email chỉ đọc. Lịch sử đơn phải hiển thị đúng đơn của tài khoản, với mã, ngày, tổng tiền và trạng thái tiếng Việt có màu phân biệt. Mình đã chạy SUT với database thử riêng và thấy trang yêu cầu đăng nhập; tiếp theo sẽ xem form và bảng đơn để phân biệt phần đã có trên giao diện với trạng thái còn cần chuẩn bị dữ liệu để kiểm tra.


Cổng API mặc định `3000` đang bị Windows từ chối, nên mình sẽ chuyển bản chạy khảo sát sang cổng khác và đổi địa chỉ kết nối trong bản sao chạy thử, giữ nguyên logic SUT. Danh sách sẽ ghi rõ căn cứ từ SRS hay slide; những mục như breadcrumb, dark mode hoặc RTL sẽ không được coi là yêu cầu bắt buộc nếu chưa có căn cứ áp dụng.


Mình đã xem được form hồ sơ, lịch sử trống và bảng có đủ năm trạng thái đơn bằng dữ liệu thử. Danh sách kiểm tra sẽ bao gồm email chỉ đọc, ba trường được sửa, nút cập nhật, các cột đơn hàng, nhãn/màu trạng thái, cùng các trạng thái chờ xử lý, thành công và lỗi. Mình cũng sẽ tách yêu cầu SRS khỏi các tiêu chí bổ sung từ slide như focus, phục hồi sau lỗi, đồng bộ sau tải lại và bố cục màn hình hẹp.


Bản phân tích đã có **52 nội dung**: IA-01 gồm 12, IA-02 gồm 14, IA-03 gồm 10 và IA-04 gồm 16. Mỗi mục có căn cứ và trạng thái cần tạo để kiểm tra. Mình cũng đã lưu hai ảnh khảo sát thật: lịch sử trống và bảng đủ năm trạng thái. Phần chụp thông báo validation bị công cụ trình duyệt timeout, nên mình ghi rõ giới hạn này trong tài liệu.

```
