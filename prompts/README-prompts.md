# PROMPT TEMPLATE — Cách tạo 1 bài viết sâu cho mỗi "cách dùng AI"

## Cấu trúc bài viết (~800-1200 từ/cách)

```
HOOK (Tiêu đề giật + dẫn nhập 2-3 câu)
├── VẤN ĐỀ (Nỗi đau người dùng — 1 đoạn)
├── GIẢI PHÁP AI (Tổng quan tool + lý do chọn — 1 đoạn)
├── PHỐI HỢP AI (Cách kết hợp 2-3 tools tạo workflow mạnh — 1-2 đoạn)
├── HƯỚNG DẪN STEP-BY-STEP (5-7 bước chi tiết, có prompt mẫu)
├── VÍ DỤ THỰC TẾ (Scenario cụ thể, có kết quả thật)
├── PRO TIPS (3 mẹo nâng cao)
└── PITFALLS (2-3 cạm bẫy tránh)
```

## Cách dùng prompt

```bash
# Mỗi prompt feed vào NotebookLM:
notebooklm ask "<prompt content>"

# Hoặc tạo report:
notebooklm generate report
# (trước đó ask để set context, rồi generate)
```

## Danh sách 10 prompt

| File | Cách | Chủ đề |
|------|------|--------|
| `prompt-01-tom-tat-bai-giang.md` | Cách 1 | Tóm tắt bài giảng |
| `prompt-02-giai-bai-tap.md` | Cách 2 | Giải bài tập |
| `prompt-03-hoc-ngoai-ngu.md` | Cách 3 | Học ngoại ngữ |
| `prompt-04-flashcard.md` | Cách 4 | Flashcard tự động |
| `prompt-05-viet-luan.md` | Cách 5 | Viết luận |
| `prompt-06-ke-hoach-on-thi.md` | Cách 6 | Kế hoạch ôn thi |
| `prompt-07-hoc-lap-trinh.md` | Cách 7 | Học lập trình |
| `prompt-08-voice-to-text.md` | Cách 8 | Voice → text |
| `prompt-09-powerpoint.md` | Cách 9 | PowerPoint tự động |
| `prompt-10-nghien-cuu.md` | Cách 10 | Nghiên cứu AI search |
