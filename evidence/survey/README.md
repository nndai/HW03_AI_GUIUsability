# Ảnh khảo sát Profile

Ngày 08/11/2026. Ảnh chụp thật từ trình duyệt tích hợp, trang `http://localhost:5175/profile`, API bản chạy riêng tại cổng 13000.

| File | Điều kiện |
| --- | --- |
| profile-empty.jpg | Test User mới login, chưa có phone/address, chưa có đơn |
| profile-orders.jpg | Sau setup dữ liệu giả bằng scripts/seed_survey_data.py và reload; 5 đơn đủ pending/confirmed/shipping/delivered/canceled |

Không có ảnh validation: native alert khiến công cụ chụp timeout. Không tạo ảnh thay thế hoặc sửa ảnh để giả bằng chứng.

Ảnh này phục vụ nhận diện thành phần/trạng thái. Chưa có overlay danh tính và chưa đủ metadata môi trường theo đề để tính vào Task 3; không thể dùng ảnh này làm bằng chứng mọi checklist item đã chạy. Xem `docs/profile_inventory.md` để biết phạm vi đã/chưa khảo sát.
