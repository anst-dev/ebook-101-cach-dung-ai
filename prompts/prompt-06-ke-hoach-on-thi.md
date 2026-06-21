# Prompt 06 — Tạo Kế Hoạch Ôn Thi Thông Minh (Spaced Repetition + AI)

## Feed vào NotebookLM

```
Bạn là chuyên gia học tập và quản lý thời gian. Dựa trên nguồn tài liệu, viết bài chuyên sâu (800-1200 từ) TIẾNG VIỆT:

"Kế Hoạch Ôn Thi Thông Minh — Phối Hợp ChatGPT, Notion và Google Calendar Để Không Bao Giờ Nhồi Nhét"

YÊU CẦU:

1. HOOK: "Cramming đêm trước kỳ thi = học được 30% sau 1 tuần. Spaced repetition = nhớ 90% mãi mãi. AI giúp bạn lên kế hoạch tự động."

2. NỖI ĐAU:
- Không biết bắt đầu ôn từ đâu
- Học theo cảm hứng, không theo kế hoạch
- Trích dẫn về spacing effect / Ebbinghaus [nguồn]

3. GIẢI PHÁP PHỐI HỢP 3 AI:
- ChatGPT: Phân tích syllabus → tạo kế hoạch spaced repetition
- Notion AI: Quản lý task ôn tập + tự động nhắc
- Google Calendar: Block thời gian cố định
Vì sao kết hợp: ChatGPT thiết kế, Notion theo dõi, Calendar nhắc

4. HƯỚNG DẪN 7 BƯỚC:
Bước 1: Liệt kê môn thi + ngày + trọng số mỗi chương
Bước 2: Prompt ChatGPT: "Tôi thi [5 môn, ngày X]. Trọng số: [chi tiết]. Dựa spaced repetition (xem lại sau 1-3-7-14 ngày), tạo lịch ôn từng ngày."
Bước 3: ChatGPT output bảng: Ngày | Môn | Chương | Hoạt động | Thời gian
Bước 4: Tạo Notion database: columns = Ngày, Môn, Trạng thái, Ghi chú
Bước 5: Import kế hoạch vào Notion (copy paste)
Bước 6: Sync deadline vào Google Calendar
Bước 7: Mỗi ngày check Notion → làm task → tick hoàn thành
Mỗi bước có prompt mẫu cụ thể.

5. VÍ DỤ THỰC TẾ:
- Scenario: 5 môn thi cuối kỳ, 3 tuần chuẩn bị
- ChatGPT chia: Tuần 1 học mới, Tuần 2 ôn + học mới, Tuần 3 chỉ ôn
- Mỗi môn weight khác nhau (Toán 30%, Lý 25%, Hóa 20%...)
- Notion theo dõi progress bar từng môn
- Kết quả: Không thức đêm, đi thi tự tin

6. PRO TIPS (3):
- Prompt ChatGPT: "Dành nhiều thời gian hơn cho môn tôi yếu [tên môn]"
- Notion template: có progress bar + countdown đến ngày thi
- Dùng Pomodoro (25 phút học + 5 phút nghỉ) trong mỗi session

7. PITFALLS:
- Kế hoạch quá dày →现实的, ChatGPT thường optimist
- Quên ôn lại → spaced repetition cần kỷ luật, đặt reminder

VĂN PHONG: Động viên + thực tế.
TRÍCH DẪN nguồn.
```

## Sau khi ask: `notebooklm generate report`
