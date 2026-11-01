# Thảo luận Lab 05

## Upstream first và release first khác nhau thế nào?

Upstream first sửa lỗi trên nhánh phát triển chính trước, sau đó chọn các
commit cần thiết để đưa về các dòng release. Cách này giúp bản sửa được tích
hợp sớm với mã mới nhưng có thể khó áp dụng nguyên vẹn cho phiên bản cũ.

Release first sửa lỗi trên đúng phiên bản đang được người dùng sử dụng, phát
hành bản vá rồi lan truyền bản sửa về master và các release còn bị ảnh hưởng.
Cách này ưu tiên khôi phục bản đã phát hành, nhưng phải kiểm toán kỹ để tránh
bỏ sót một dòng phiên bản.

## Vì sao chỉ cherry-pick commit sửa lỗi?

Commit nâng phiên bản 1.0.1 chỉ thuộc dòng release 1.0.x. Nếu đưa cả commit đó
về master hoặc release/lab05, phiên bản 1.1.0 sẽ bị đổi sai. Vì vậy mã sửa lỗi
và thay đổi phiên bản được tách thành hai commit, rồi chỉ commit sửa lỗi được
lan truyền.

## Tùy chọn cherry-pick -x có tác dụng gì?

Tùy chọn `-x` thêm SHA của commit nguồn vào thông điệp commit mới. Dấu vết này
cho phép kiểm toán bản sửa đã xuất phát từ đâu và đã được đưa đến những dòng
phiên bản nào.

## Làm sao phát hiện quên đưa bản sửa vào release/lab05?

Có thể dùng `git cherry -v` để so sánh các thay đổi tương đương giữa hai nhánh,
kiểm tra lịch sử có dòng `cherry picked from commit`, và chạy regression test
trên `v1.0.1`, `v1.1.0` cùng `master`. Nếu một dòng vẫn không tìm được từ khóa
`lion`, bản sửa chưa được lan truyền đầy đủ.
