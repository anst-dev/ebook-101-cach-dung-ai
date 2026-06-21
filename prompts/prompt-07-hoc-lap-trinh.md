# Prompt 07 — Học Lập Trình Miễn Phí Với AI Tutor

## Feed vào NotebookLM

```
Bạn là senior developer và mentor. Dựa trên nguồn tài liệu, viết bài chuyên sâu (800-1200 từ) TIẾNG VIỆT:

"Tự Học Lập Trình Từ Zero Đến Có Việc — Phối Hợp Claude Code, Replit và Perplexity"

YÊU CẦU:

1. HOOK: "Bootcamp lập trình: 30 triệu, 6 tháng. AI tutor miễn phí: 0 đồng, học theo tốc độ bạn. Kết quả tạo ra giống nhau."

2. NỖI ĐAU:
- Tutorial YouTube xem xong quên, không thực hành
- Lỗi code không ai giúp fix → nản
- Trích dẫn về tỷ lệ bỏ cuộc học code [nguồn]

3. GIẢI PHÁP PHỐI HỢP 3 AI:
- Claude Code: Gia sư 1-kèm-1, giải thích + sửa code + review
- Replit: IDE online miễn phí, chạy code ngay không cần cài
- Perplexity: Tra docs mới nhất (framework update liên tục)
Workflow: Học lý thuyết (Claude) → Code (Replit) → Lỗi (Claude fix) → Docs (Perplexity)

4. HƯỚNG DẪN 7 BƯỚC:
Bước 1: Chọn ngôn ngữ (VD: Python cho người mới)
Bước 2: Prompt Claude: "Tôi chưa từng code. Dạy tôi Python bài 1: variables. Giải thích + cho 3 bài tập nhỏ."
Bước 3: Mở Replit.com → tạo Repl Python
Bước 4: Code theo hướng dẫn, bấm Run
Bước 5: Nếu lỗi → copy error paste Claude: "Code báo lỗi [X], sửa giúp + giải thích vì sao"
Bước 6: Perplexity tra: "Python best practices 2025" (tránh info cũ)
Bước 7: Lưu code vào GitHub (free) → build portfolio
Mỗi bước có prompt + code mẫu.

5. VÍ DỤ THỰC TẾ:
- Project: Tạo chatbot đơn giản bằng Python
- Buổi 1-3: Học variables, loops, functions với Claude
- Buổi 4-7: Build chatbot trên Replit
- Lỗi: "NameError: name 'response' is not defined" → Claude chỉ ra thiếu `global`
- Buổi 8: Perplexity tra "how to deploy Python app free"
- Kết quả: Deploy lên Render miễn phí, có portfolio

6. PRO TIPS (3):
- Prompt: "Đừng cho code sẵn, gợi ý để tôi tự viết"
- Dùng Claude Code CLI (terminal) thay vì web → tích hợp git
- Perplexity Pro free cho sinh viên → tra docs nhanh

7. PITFALLS:
- Copy code AI mà không hiểu → prompt "giải thích từng dòng"
- Học quá nhiều ngôn ngữ cùng lúc → chọn 1 (Python/JS)

VĂN PHONG: Kỹ thuật nhưng dễ hiểu cho người mới.
TRÍCH DẪN nguồn.
```

## Sau khi ask: `notebooklm generate report`
