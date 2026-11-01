# Thảo luận Lab 04

## Vì sao release/* không merge ngược vào master?

Nhánh release được tạo từ master để lưu một dòng baseline
phát hành. Master tiếp tục nhận tính năng mới. Nếu có lỗi trên
bản đã phát hành, chỉ bản sửa lỗi cần được lan truyền có kiểm
soát; không merge toàn bộ release về master vì có thể đưa
thông tin phiên bản cũ và thay đổi riêng của dòng bảo trì vào
dòng phát triển mới.

## So sánh Release Flow của bài với GitFlow

Release Flow của bài dùng master làm dòng phát triển chính,
release/* làm dòng bảo trì và các nhánh feature ngắn hạn.
Release không merge ngược toàn bộ vào master.

GitFlow thường có cả main và develop. Feature merge vào
develop; release và hotfix được phối hợp giữa nhiều nhánh.
GitFlow nhiều nhánh dài hạn và phức tạp hơn.

## Vì sao chọn phiên bản 1.0.0 thay vì 0.4.0?

Các phiên bản 0.y.z thể hiện giai đoạn chưa ổn định. Lab 04
xác lập baseline ổn định đầu tiên có CHANGELOG, tag và GitHub
Release, nên được đánh dấu 1.0.0 theo Semantic Versioning.

## Tag và nhánh release khác nhau thế nào?

Tag là mốc bất biến trỏ đến chính xác một phiên bản. Nhánh
release có thể tiến thêm commit khi cần bảo trì hoặc hotfix.
Vì vậy tag định danh một bản phát hành, còn nhánh release
đại diện cho dòng bảo trì của bản đó.