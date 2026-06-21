# Ebook AI-101 — Workflow Documentation

> **Cập nhật:** 2026-06-20
> **Author:** Nexus (Hermes Agent)
> **Workspace:** `C:\Users\Administrator\ebook-ai-101`

---

## 1. Tổng quan Pipeline

```
OUTLINE → NotebookLM RESEARCH → NotebookLM WRITE → TẬP HỢP → PDF EXPORT
```

### Tools sử dụng
| Tool | Vai trò | Cách gọi |
|------|---------|----------|
| **NotebookLM** | Research sources + viết nội dung + generate artifacts | `notebooklm ask/generate` |
| **Hermes/Z.AI** | Orchestrator (lập kế hoạch, điều phối) | Trực tiếp |
| **Chrome headless** | Export PDF (font tiếng Việt) | `scripts/export_pdf_chrome.py` |
| **agy CLI** | Viết code/automation (backup) | `scripts/agy_wrapper.py` |

---

## 2. NotebookLM — Auto Login

```bash
# Non-interactive auto-login (browser profile persistent)
(sleep 25 && echo "") | notebooklm login 2>&1
```

- Browser profile tại `~/.notebooklm/profiles/default/browser_profile` giữ session Google
- Nếu auth hết hạn → chạy lại lệnh trên

---

## 3. NotebookLM — Workflow Viết Ebook

### Bước 1: Tạo notebook + upload sources
```bash
notebooklm create "101 Cách Dùng AI Miễn Phí"
notebooklm use <notebook-id>

# Upload sources
notebooklm source add ebook/outline.md --title "Outline"
notebooklm source add ebook/00-intro.md --title "Intro"
notebooklm source add "https://example.com/article"
notebooklm source add "https://youtube.com/watch?v=..."
```

### Bước 2: Ask từng phần (viết nội dung)
```bash
notebooklm ask "Viết Phần 1: Học sinh (cách 1-15). Mỗi cách: tên, công cụ, hướng dẫn, ví dụ."
notebooklm ask "Tiếp tục viết cách 6-15..."
notebooklm ask "Viết Phần 2: Giáo viên (cách 16-30)..."
```

### Bước 3: Generate artifacts (bài sâu + minh họa)
```bash
# Deep article
notebooklm generate report "Viết bài chuyên sâu về [topic]" --language vi

# Infographic minh họa
notebooklm generate infographic --language vi --style professional

# Slide deck
notebooklm generate slide-deck "include speaker notes" --language vi
```

### Bước 4: Download artifacts
```bash
notebooklm download report output/reports/cach-01.md
notebooklm download infographic output/infographics/cach-01.png
notebooklm download slide-deck output/slides/cach-01.pdf
```

---

## 4. PDF Export — Font Tiếng Việt

### Phương pháp: Chrome Headless (DUY NHẤT hoạt động)

| Thử | Kết quả |
|-----|---------|
| xhtml2pdf | ❌ Không embed font, dấu biến mất |
| weasyprint | ❌ Cần GTK3 native (không có trên Windows) |
| pandoc xelatex | ❌ Cần LaTeX installation (~2GB) |
| **Chrome headless** | ✅ **11/13 diacritics, native Unicode** |

### Chạy
```bash
PY312="/c/Users/Administrator/AppData/Local/Programs/Python/Python312/python.exe"
$PY312 scripts/export_pdf_chrome.py
```

### Output
```
output/
├── ebook.html              # HTML intermediate
└── 101-cach-dung-ai-mien-phi.pdf   # PDF cuối (~1 MB, font chuẩn)
```

---

## 5. Tách Chương (cho tinh chỉnh)

```bash
$PY312 scripts/split_chapters.py
```

Output:
```
ebook/chapters/
├── 00-intro.md          # Lời nói đầu
├── part1-students.md    # Cách 1-15
├── part2-teachers.md    # Cách 16-30
├── part3-office.md      # Cách 31-45
├── part4-creators.md    # Cách 46-57
├── part5-developers.md  # Cách 58-69
├── part6-automation.md  # Cách 70-81
├── part7-business.md    # Cách 82-91
├── part8-personal.md    # Cách 92-101
└── 99-conclusion.md     # Kết luận
```

---

## 6. Prompt Templates (10 prompts chuyên nghiệp)

Nằm trong `prompts/`:

| File | Cách | Phối hợp AI |
|------|------|-------------|
| `prompt-01-tom-tat-bai-giang.md` | Tóm tắt bài giảng | ChatGPT + Gemini + NotebookLM |
| `prompt-02-giai-bai-tap.md` | Giải bài tập | ChatGPT Vision + Photomath + Symbolab |
| `prompt-03-hoc-ngoai-ngu.md` | Học ngoại ngữ | Gemini + ChatGPT Voice + DeepL |
| `prompt-04-flashcard.md` | Flashcard tự động | ChatGPT + Anki + NotebookLM |
| `prompt-05-viet-luan.md` | Viết luận | Claude + ChatGPT + Grammarly |
| `prompt-06-ke-hoach-on-thi.md` | Kế hoạch ôn thi | ChatGPT + Notion + Calendar |
| `prompt-07-hoc-lap-trinh.md` | Học lập trình | Claude Code + Replit + Perplexity |
| `prompt-08-voice-to-text.md` | Voice → text | Whisper + ChatGPT + Notion |
| `prompt-09-powerpoint.md` | PowerPoint tự động | ChatGPT + Gamma + Canva |
| `prompt-10-nghien-cuu.md` | Nghiên cứu học thuật | Perplexity + NotebookLM + ChatGPT |

Mỗi prompt cấu trúc 7 phần:
```
HOOK → NỖI ĐAU → PHỐI HỢP AI → 7 BƯỚC → VÍ DỤ → PRO TIPS → PITFALLS
```

---

## 7. Cấu trúc workspace

```
ebook-ai-101/
├── ebook/
│   ├── 00-intro.md              # Lời nói đầu
│   ├── full-ebook.md            # File tổng hợp (7911 từ)
│   ├── outline.md               # Dàn ý 101 cách
│   └── chapters/                # Từng chương riêng (10 files)
├── output/
│   ├── ebook.html               # HTML intermediate
│   └── 101-cach-dung-ai-mien-phi.pdf  # PDF cuối (1 MB)
├── prompts/                     # 10 prompt templates
├── scripts/
│   ├── export_pdf_chrome.py     # ✅ PDF export (Chrome headless)
│   ├── split_chapters.py        # Tách chương
│   ├── combine_ebook.py         # Tổng hợp
│   └── agy_wrapper.py           # Wrapper agy CLI
├── assets/fonts/                # Arial.ttf + Consolas.ttf
├── reference/                   # Felipe Aguiar ebook + Flowboard
├── program.md                   # Autoresearch program
├── experiments.tsv              # Experiment log
├── README.md                    # Project overview
└── WORKFLOW.md                  # File này
```

---

## 8. Skills đã lưu trong Hermes

| Skill | Đường dẫn | Mô tả |
|-------|-----------|-------|
| `ebook-creator` | creative/ebook-creator | Pipeline end-to-end: outline → write → PDF |
| `notebooklm-workflow` | productivity/notebooklm-workflow | NotebookLM CLI commands + auto-login |
| `autoresearch-loop` | software-development/autoresearch-loop | Karpathy pattern: try → measure → keep/discard |
