## PHẦN 5: LẬP TRÌNH VIÊN & TECH (Cách 58–69)

*Trợ lý đắc lực cho dân IT.*

### Cách 58: Code review tự động
**Công cụ:** Claude Code hoặc Codex CLI | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Copy đoạn code vừa viết.
2. Dán vào AI: *"Review code này, chỉ ra rủi ro bảo mật, gợi ý tối ưu."*
3. Chỉnh sửa theo nhận xét.

**Ví dụ:** Trước khi push code → AI phát hiện leak biến môi trường hoặc hàm tốn quá nhiều bộ nhớ.

### Cách 59: Debug code với AI assistant
**Công cụ:** ChatGPT hoặc Claude | **Mức độ:** Dễ

**Hướng dẫn:**
1. Copy toàn bộ error log.
2. Dán vào ChatGPT cùng code lỗi: *"Tại sao lỗi này và cách sửa?"*
3. Áp dụng code đã sửa.

**Ví dụ:** "Null pointer exception" 2 tiếng không ra → AI chỉ đích danh dòng 45 chưa khởi tạo biến.

### Cách 60: Tạo boilerplate code
**Công cụ:** Cursor hoặc Copilot | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cài Cursor IDE.
2. Mở file mới, gọi AI: *"Tạo khung server Express.js có kết nối MongoDB."*
3. Code tự sinh ra trong IDE.

**Ví dụ:** Dự án mới không cần gõ lại cấu hình server, router, middleware → AI tạo khung sườn 5 giây.

### Cách 61: Viết unit test tự động
**Công cụ:** Codex CLI hoặc Claude | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Cung cấp hàm cần test.
2. Lệnh: *"Viết Unit Test bằng Jest. Bao phủ trường hợp thường và edge cases."*
3. Chạy test trong terminal.

**Ví dụ:** Claude tự đẻ ra 10 file test cho component React chỉ bằng một cú nhấp.

### Cách 62: Chuyển đổi code giữa ngôn ngữ
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Dán code cũ (VD: Python).
2. Lệnh: *"Dịch sang Go (Golang), giữ nguyên logic."*
3. Tích hợp code mới.

**Ví dụ:** Port thuật toán Java sang JavaScript mà không cần nắm vững cú pháp Java.

### Cách 63: Tạo API documentation
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Dán file chứa API endpoints.
2. Lệnh: *"Tạo tài liệu API chuẩn Swagger/OpenAPI, giải thích request body và response."*
3. Xuất ra YAML/Markdown.

**Ví dụ:** Làm xong tính năng, ngại viết tài liệu → AI mô tả chi tiết từng param siêu chuyên nghiệp.

### Cách 64: Refactor code
**Công cụ:** Claude Code | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Dán đoạn code dài, if-else phức tạp.
2. Lệnh: *"Refactor cho Clean Code, áp dụng Design Pattern phù hợp."*
3. Đọc kỹ logic mới.

**Ví dụ:** Code "Spaghetti" của thực tập sinh → cấu trúc Module gọn gàng, chuẩn Senior.

### Cách 65: Học framework mới
**Công cụ:** ChatGPT + Perplexity | **Mức độ:** Dễ

**Hướng dẫn:**
1. Perplexity: *"Cập nhật tính năng mới nhất Next.js 14."*
2. ChatGPT: *"App Router khác gì Pages Router? Cho ví dụ."*

**Ví dụ:** AI tóm tắt tinh hoa trang Document dài dằng dặc, học nhanh framework mới.

### Cách 66: Tạo regex bằng ngôn ngữ tự nhiên
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nêu định dạng muốn trích xuất.
2. Lệnh: *"Viết Regex JavaScript bắt số điện thoại VN (10 số, bắt đầu 0)."*
3. Dán vào source code.

**Ví dụ:** Không cần nhớ `\d`, `^`, `$` → miêu tả bằng lời, AI trả Regex chính xác 100%.

### Cách 67: Tối ưu database queries
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Dán SQL chậm + cấu trúc bảng (Schema).
2. Lệnh: *"Query này chậm. Tối ưu hóa? Đánh Index ở cột nào?"*
3. Chạy lại query đo lường.

**Ví dụ:** Query bảng triệu dòng → AI gợi ý JOIN đúng + Index, tăng tốc từ 5s xuống 0.1s.

### Cách 68: Viết commit messages chuyên nghiệp
**Công cụ:** Claude Code | **Mức độ:** Dễ

**Hướng dẫn:**
1. Copy `git diff`.
2. Lệnh: *"Viết commit message chuẩn Conventional Commits."*
3. Dán vào Git.

**Ví dụ:** Thay vì "Fix bug" → AI viết: `fix(auth): resolve token expiration issue`.

### Cách 69: Tạo CI/CD pipeline templates
**Công cụ:** ChatGPT hoặc Claude | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Cung cấp thông tin dự án (VD: React, deploy AWS).
2. Lệnh: *"Tạo file GitHub Actions YAML tự động build+deploy khi push main."*
3. Copy `.yml` vào dự án.

**Ví dụ:** Tự động hóa triển khai không cần rành DevOps → AI tạo file cấu hình chuẩn bảo mật.

---