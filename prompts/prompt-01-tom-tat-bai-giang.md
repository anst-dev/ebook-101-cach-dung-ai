# Prompt 01 — Tóm Tắt Bài Giảng Dài Thành Ghi Chú Xuyên Sâu

## Feed vào NotebookLM (ask trước, rồi generate report)

```
Bạn là chuyên gia giáo dục và productivity. Dựa trên tất cả nguồn tài liệu trong notebook này, hãy viết một bài viết dài và chuyên sâu (800-1200 từ) bằng TIẾNG VIỆT với chủ đề:

"Tóm Tắt Bài Giảng Dài Thành Ghi Chú Xuyên Sáu — Phối Hợp ChatGPT, Gemini và NotebookLM"

YÊU CẦU NỘI DUNG:

1. HOOK (Mở đầu hấp dẫn):
- Bắt đầu bằng 1 câu hỏi gây tò mò hoặc thống kê giật gân
- Ví dụ: "Bạn có biết sinh viên trung bình mất 6 giờ/tuần chỉ để đọc lại ghi chú bài giảng?"

2. NỖI ĐAU (Vấn đề cụ thể):
- Mô tả tình cảnh: bài giảng 45 phút, tài liệu 50 trang, deadline thi gần
- Vì sao cách truyền thống (gạch chân, copy) không hiệu quả
- Trích dẫn nguồn về quỹ thời gian học tập [trích nguồn từ notebook]

3. GIẢI PHÁP — PHỐI HỢP 3 AI:
Trình bày workflow kết hợp:
- Bước A: ChatGPT/Gemini tóm tắt ý chính → tạo skeleton notes
- Bước B: NotebookLM upload tài liệu gốc → hỏi sâu từng phần
- Bước C: ChatGPT tạo flashcard từ tóm tắt + so sánh chéo với NotebookLM
Giải thích VÌ SAO phối hợp 3 tools tốt hơn dùng 1 (mỗi tool mạnh gì)

4. HƯỚNG DẪN TỪNG BƯỚC (5-7 bước):
Mỗi bước có:
- Tên bước rõ ràng
- Prompt mẫu cụ thể (copy-paste được) bằng tiếng Việt
- Tool sử dụng
- Kết quả mong đợi

5. VÍ DỤ THỰC TẾ (Scenario chi tiết):
- Monnen cụ thể (VD: Sinh học đại cương chương 3)
- Input thực → Output thực
- Time before vs after (VD: 3 giờ → 20 phút)

6. PRO TIPS (3 mẹo):
- Tip 1: Cách prompt tốt hơn (role-playing, few-shot)
- Tip 2: Tổ chức ghi chú (Cornell method + AI)
- Tip 3: Phối hợp với Notion/Obsidian

7. PITFALLS (2-3 cạm bẫy):
- Sai lầm 1: Tin AI 100% không kiểm tra
- Sai lầm 2: Prompt quá chung chung

VĂN PHONG: Năng động, trực tiếp, như một người bạn giỏi chia sẻ bí kíp. Dùng "bạn" thay "người đọc". Có emoji vừa đủ. Có in đậm từ khóa.

TRÍCH DẪN: Trích dẫn nguồn [1] [2] [3] từ notebook để chứng minh thông tin cập nhật 2025-2026.
```

## Sau khi ask xong, chạy:
```bash
notebooklm generate report
```
