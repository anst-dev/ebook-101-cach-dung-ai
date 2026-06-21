# Prompt 04 — Tạo Flashcard Tự Động Từ Sách Giáo Khoa

## Feed vào NotebookLM

```
Bạn là chuyên gia học tập và spaced repetition. Dựa trên nguồn tài liệu, viết bài chuyên sâu (800-1200 từ) TIẾNG VIỆT:

"Flashcard Tự Động Từ Sách Giáo Khoa — Phối Hợp ChatGPT, Anki và NotebookLM Để Nhớ Lâu Mãi Mãi"

YÊU CẦU:

1. HOOK: "Quy tắc 80/20 của quên: 80% kiến thức biến mất sau 1 tuần nếu không ôn. Trừ khi bạn có flashcard."

2. NỖI ĐAU:
- Tạo flashcard thủ công tốn quá nhiều thời gian (1 chương = 2 giờ)
- Quizlet free có giới hạn, Anki khó dùng cho người mới
- Trích dẫn về quên lãng / Ebbinghaus curve [nguồn]

3. GIẢI PHÁP PHỐI HỢP 3 AI:
- ChatGPT: Đọc chương sách → sinh 20-30 cặp Q&A chất lượng
- NotebookLM: Upload cả sách → hỏi "5 câu hỏi quan trọng nhất chương 3"
- Anki (free desktop): Import Q&A → spaced repetition algorithm
So sánh Anki vs Quizlet: vì sao Anki miễn phí và mạnh hơn

4. HƯỚNG DẪN 7 BƯỚC:
Bước 1: Copy text 1 chương sách giáo khoa
Bước 2: Prompt ChatGPT: "Tạo 25 flashcard dạng Q&A ngắn gọn từ đoạn văn. Format: mặt trước|sau. Chủ đề: [tên chương]"
Bước 3: Copy output dạng text phân tách bằng |
Bước 4: Mở Anki → Create Deck → Import → paste
Bước 5: NotebookLM upload sách → hỏi "Những khái niệm nào dễ nhầm nhất?"
Bước 6: Thêm các flashcard về khái niệm dễ nhầm
Bước 7: Ôn 15 phút/ngày bằng Anki app điện thoại
Mỗi bước có prompt + screenshot mô tả.

5. VÍ DỤ THỰC TẾ:
- Môn: Hóa học hữu cơ chương Andehit-Xeton
- Input: 5 trang SGK
- ChatGPT sinh: 30 flashcard (công thức, phản ứng, điều kiện)
- NotebookLM bổ sung: 5 câu về điểm dễ nhầm (Andehit vs Xeton)
- Kết quả: Điểm kiểm tra 15 phút từ 6 → 9

6. PRO TIPS (3):
- Prompt ChatGPT dùng Bloom's taxonomy: "Tạo câu hỏi ở mức Hiểu + Vận dụng, không chỉ Nhớ"
- Anki settings: show 20 card mới/ngày, algorithm mặc định
- Phối hợp Anki với mindmap (Cách 12)

7. PITFALLS:
- Quá nhiều flashcard → nản → giới hạn 30/chương
- Flashcard quá dài → AI sinh ngắn gọn 1 câu

VĂN PHONG: Thực tế, có data cụ thể.
TRÍCH DẪN nguồn.
```

## Sau khi ask: `notebooklm generate report`
