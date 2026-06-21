# Prompt 08 — Chuyển Voice Memo Thành Ghi Chú Text + Học Liền

## Feed vào NotebookLM

```
Bạn là chuyên gia productivity và note-taking. Dựa trên nguồn tài liệu, viết bài chuyên sâu (800-1200 từ) TIẾNG VIỆT:

"Từ Giọng Nói Đến Ghi Chú Hoàn Hảo — Phối Hợp Whisper, ChatGPT và Notion"

YÊU CẦU:

1. HOOK: "Bạn ghi âm bài giảng 45 phút. Nghe lại 3 lần = 2 giờ 15. Whisper transcript = 5 phút. ChatGPT tóm tắt = thêm 2 phút. Tổng: 7 phút thay vì 2+ giờ."

2. NỖI ĐAU:
- Ghi âm xong không bao giờ nghe lại
- Chép tay theo băng ghi quá chậm
- Tiếng Việt nhận diện giọng nói còn yếu
- Trích dẫn về note-taking effectiveness [nguồn]

3. GIẢI PHÁP PHỐI HỢP 3 AI:
- Whisper (OpenAI, free): Transcript chính xác tiếng Việt
- ChatGPT: Làm sạch text + tóm tắt + tạo ghi chú Cornell
- Notion: Lưu trữ + search + liên kết với tài liệu khác
Workflow: Ghi âm → Whisper transcript → ChatGPT format → Notion lưu

4. HƯỚNG DẪN 7 BƯỚC:
Bước 1: Ghi âm bài giảng (xin phép thầy cô trước)
Bước 2: Tải file audio (.mp3/.m4a)
Bước 3: Upload lên whisper AI (whisper.alibaba.com hoặc Hugging Face free)
Bước 4: Copy transcript thô (sẽ có lỗi nhỏ)
Bước 5: Prompt ChatGPT: "Đây là transcript bài giảng. Hãy: (1) sửa lỗi chính tả, (2) chia thành ghi chú Cornell (Cột trái: từ khóa, Cột phải: nội dung, Dưới: tóm tắt), (3) highlight 5 điểm quan trọng nhất"
Bước 6: Copy vào Notion → tag môn học + ngày
Bước 7: Trước khi thi, search Notion → ôn lại nhanh
Mỗi bước có tool link + prompt mẫu.

5. VÍ DỤ THỰC TẾ:
- Môn: Luật Kinh tế, bài giảng về Hợp đồng thương mại
- Ghi âm: 52 phút
- Whisper transcript: 12 trang text (3 phút xử lý)
- ChatGPT Cornell notes: 3 trang có cấu trúc
- Notion: tag "Luật Kinh tế" + "Hợp đồng"
- Kết quả: Ôn thi = search "hợp đồng" → 5 giây ra ghi chú

6. PRO TIPS (3):
- Whisper chính xác hơn nếu ngồi gần loa/thầy cô
- Prompt ChatGPT: "Giữ nguyên thuật ngữ pháp lý, không dịch sang thông thường"
- Notion AI: "Tạo tóm tắt 1 câu cho mỗi buổi học" → overview nhanh

7. PITFALLS:
- File audio quá lớn → chia nhỏ 15 phút/file
- Whisper nhầm tên riêng → review + sửa thủ công

VĂN PHONG: Thực tế, có con số thời gian cụ thể.
TRÍCH DẪN nguồn.
```

## Sau khi ask: `notebooklm generate report`
