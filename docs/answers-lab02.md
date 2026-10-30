# Thảo luận Lab 02

## Vì sao cần đồng bộ master trước khi tạo PR?

Đồng bộ giúp phát hiện xung đột sớm và kiểm tra tính năng
trên trạng thái mới nhất của dự án trước khi tích hợp.

## Khi nào không được rebase?

Không rebase các commit đã được chia sẻ và đang được người
khác sử dụng, vì rebase tạo SHA mới và viết lại lịch sử.

## Feature khác topic như thế nào?

feature dùng cho chức năng của sản phẩm. topic dùng cho một
công việc hỗ trợ như tài liệu, cấu hình hoặc PR template.

## So sánh ba kiểu merge

Merge commit giữ nguyên các commit và cấu trúc nhánh.
Squash gộp toàn bộ PR thành một commit mới.
Rebase giữ nội dung từng commit nhưng xếp chúng thành lịch sử
tuyến tính và tạo SHA mới.