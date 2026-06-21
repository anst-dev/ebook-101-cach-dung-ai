# Prompt 05 — Luyện Viết Luận Và Nhận Phản Hồi Sâu Với AI

## Feed vào NotebookLM

```
Bạn là chuyên gia học thuật và viết sáng tạo. Dựa trên nguồn tài liệu, viết bài chuyên sâu (800-1200 từ) TIẾNG VIỆT:

"Viết Luận Điểm Cao Nhờ AI Chấm Bài — Phối Hợp Claude, ChatGPT và Grammarly"

YÊU CẦU:

1. HOOK: "Giáo viên chấm 40 bài trong 1 đêm → nhận xét chung chung. Claude chấm 1 bài trong 1 phút → từng câu, từng lỗi."

2. NỖI ĐAU:
- Học sinh viết luận không ai phản hồi chi tiết
- Giáo viên quá tải, chỉ ghi "cần cải thiện" → không biết cải thiện gì
- Trích dẫn về importance of feedback in writing [nguồn]

3. GIẢI PHÁP PHỐI HỢP 3 AI:
- Claude: Chấm luận tiếng Anh/Tiếng Việt → nhận xét logic + lập luận (best cho writing)
- ChatGPT: Viết lại đoạn yếu → gợi ý 3 phiên bản tốt hơn
- Grammarly (free): Bắt lỗi ngữ pháp + từ vựng cuối cùng
Bảng so sánh: Tool | Tốt cho gì | Yếu điểm

4. HƯỚNG DẪN 7 BƯỚC:
Bước 1: Viết bản nháp luận (không cần hoàn hảo)
Bước 2: Prompt Claude: "Đóng vai IELTS examiner band 7+. Chấm bài này theo 4 tiêu chí: Task Response, Coherence, Lexical, Grammar. Đưa ra điểm + 5 lỗi cụ thể + cách sửa"
Bước 3: Đọc nhận xét, sửa lỗi logic trước
Bước 4: ChatGPT: "Viết lại đoạn [X] sao cho học thuật hơn, 3 phiên bản"
Bước 5: Chọn phiên bản tốt, paste vào
Bước 6: Grammarly quét lần cuối (lỗi chính tả, dấu câu)
Bước 7: So sánh bản nháp vs bản cuối → học từ khác biệt
Mỗi bước có prompt mẫu.

5. VÍ DỤ THỰC TẾ:
- Bài: IELTS Task 2 "Some people think technology makes us less social"
- Claude chấm: Band 6.0 → chỉ ra: thesis mờ, ví dụ không cụ thể
- ChatGPT viết lại mở bài → band 7.0
- Grammarly: sửa 3 lỗi article (a/an/the)
- Kết quả: 6.0 → 7.5 trong 30 phút

6. PRO TIPS (3):
- Prompt Claude: "Đừng sửa cho tôi, chỉ GỢI Ý để tôi tự sửa"
- Upload rubric của giáo viên vào Claude để chấm đúng tiêu chí
- Dùng Claude (free) thay vì ChatGPT vì Claude viết tự nhiên hơn

7. PITFALLS:
- Copy paste nguyên văn AI → đạo văn → dùng AI để HỌC, không để LƯỢN
- Chỉ sửa ngữ pháp, bỏ qua logic → Claude mạnh về logic

VĂN PHONG: Học thuật nhưng dễ hiểu.
TRÍCH DẪN nguồn.
```

## Sau khi ask: `notebooklm generate report`
