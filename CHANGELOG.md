# Changelog

Các thay đổi đáng chú ý của AIMS-mini được ghi lại trong file này.

## [Unreleased]
### Added

- Sắp xếp giỏ hàng theo tiêu đề DVD.
- Sắp xếp giỏ hàng theo giá DVD.

## [1.0.0] - 2026-11-02

### Added

- Tổ chức mã nguồn thành package `aims`.
- Hiển thị chi tiết các DVD trong giỏ hàng.
- Xử lý trường hợp in giỏ hàng trống.
- Tìm DVD theo tiêu đề.
- Tính tổng tiền sau giảm giá.
- Kiểm thử giới hạn giỏ hàng và tính toán giảm giá.
- Tài liệu use case và câu trả lời cho các lab.

### Fixed

- Không cho phép thêm DVD thứ 21 khi giới hạn là 20.
- Sửa công thức tính tổng tiền sau giảm giá.
- Kiểm tra phần trăm giảm giá phải nằm trong khoảng 0 đến 100.

### Changed

- Chuẩn hóa quy trình làm việc bằng branch và Pull Request.
- Hiển thị thông báo thêm DVD bằng tiếng Việt.