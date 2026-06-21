# Prompt 02 — Giải Bài Tập Toán/Lý/Hóa Từng Bước Với AI

## Feed vào NotebookLM

```
Bạn là gia sư AI chuyên nghiệp. Dựa trên nguồn tài liệu trong notebook, hãy viết bài chuyên sâu (800-1200 từ) bằng TIẾNG VIỆT:

"Giải Bài Tập Toán Lý Hóa Như Một Gia Sư 1-Kèm-1 — Phối Hợp ChatGPT Vision, Photomath và Symbolab"

YÊU CẦU:

1. HOOK: Mở bằng scenario quen thuộc — "2 giờ sáng, cày đề Toán, gặp bài tích phân không biết giải..."

2. NỖI ĐAU:
- Học sinh bí bài → không ai hỏi → nản → bỏ cuộc
- Photomath chỉ ra đáp án không giải thích → không học được
- Trích dẫn về tỷ lệ học sinh sợ Toán [trích nguồn]

3. GIẢI PHÁP PHỐI HỢP 3 AI:
- Photomath: Chụp ảnh → quét đề → ra đáp án nhanh
- ChatGPT Vision: Chụp ảnh → AI giải TỪNG BƯỚC + giải thích "tại sao"
- Symbolab / Wolfram Alpha: Kiểm tra chéo đáp án + vẽ đồ thị
Vì sao dùng 3: Photomath nhanh, ChatGPT sâu, Symbolab chính xác

4. HƯỚNG DẪN 7 BƯỚC:
Bước 1: Chụp ảnh rõ nét đề bài
Bước 2: Upload lên ChatGPT với prompt: "Giải bài này từng bước, giải thích tại sao áp dụng công thức đó"
Bước 3: Nếu ChatGPT nhầm → Photomath kiểm tra
Bước 4: Symbolab vẽ đồ thị hàm số (nếu cần)
Bước 5: Hỏi ChatGPT "Cho bài tương tự để luyện"
Bước 6: NotebookLM upload đề + lời giải → tạo flashcard công thức
Bước 7: Lưu vào Obsidian/Notion
Mỗi bước có prompt mẫu cụ thể.

5. VÍ DỤ THỰC TẾ:
- Bài cụ thể: Tính tích phân ∫(x²+2x)dx từ 0 đến 2
- Input: ảnh bài toán
- Output: ChatGPT giải từng bước + giải thích quy tắc lũy thừa
- Symbolab kiểm tra: kết quả = 8/3 ✓
- Time: 30 phút tự mò → 5 phút với AI

6. PRO TIPS (3):
- Prompt "giải thích như tôi học sinh lớp 10"
- Dùng "cho 3 bài tương tự khó hơn" để luyện
- Chụp ảnh thẳng, đủ sáng, không cong giấy

7. PITFALLS:
- ChatGPT có thể nhầm tính toán → luôn kiểm tra Symbolab
- Không copy-paste đáp án mà phải hiểu bước giải

VĂN PHONG: Gần gũi, như anh chị dạy kèm. Emoji vừa đủ.
TRÍCH DẪN nguồn notebook.
```

## Sau khi ask: `notebooklm generate report`
