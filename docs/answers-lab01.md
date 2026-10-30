# Thảo luận Lab 01

## 1. Cấu hình --global được lưu ở đâu? Khác --local?
--global thường được lưu trong ~/.gitconfig, áp dụng cho
các repository của người dùng hiện tại.
--local lưu trong .git/config, chỉ áp dụng cho repository
hiện tại và được ưu tiên hơn global.

## 2. Vì sao dùng git mv?
git mv thực hiện di chuyển file và cập nhật staging.
Git có thể nhận diện việc đổi tên dựa trên nội dung;
dùng git mv giúp thao tác thuận tiện, tránh quên add/xóa file.

## 3. release/lab01 có phải baseline không?
Có. Trong quy trình bài thực hành, đây là mốc bài nộp
đã được kiểm tra. Các sửa đổi sau đó phải được kiểm soát
qua quy trình PR/hotfix.

## 4. Vì sao làm một mình vẫn không commit thẳng master?
PR giúp tự kiểm tra thay đổi, ghi mục đích và kết quả
kiểm thử, đồng thời lưu dấu vết tích hợp vào master.