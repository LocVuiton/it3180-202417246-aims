# Thảo luận Lab 03

## Merge base là gì?

Merge base là commit tổ tiên chung gần nhất của hai nhánh.
Git dùng mốc này để xác định thay đổi thuộc từng nhánh khi
merge và phát hiện xung đột.

## Vì sao master và release/* phải dùng revert?

Các nhánh này chứa lịch sử đã chia sẻ. Revert tạo một commit
mới đảo ngược thay đổi nên không viết lại lịch sử và vẫn giữ
được khả năng truy vết.

## Reset và revert khác nhau thế nào?

Reset di chuyển con trỏ nhánh và có thể viết lại lịch sử,
phù hợp với commit local chưa chia sẻ. Revert tạo commit mới
đảo ngược thay đổi, phù hợp với lịch sử đã push.

## Reset soft, mixed và hard khác nhau thế nào?

- soft: bỏ commit nhưng giữ thay đổi trong staging.
- mixed: bỏ commit và đưa thay đổi về working directory.
- hard: bỏ cả commit lẫn thay đổi trong working directory.