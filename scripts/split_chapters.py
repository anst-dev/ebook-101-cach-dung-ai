#!/usr/bin/env python3
"""split_chapters.py — Split full-ebook.md into individual chapter files."""
import re
from pathlib import Path

EBOOK_DIR = Path(r"C:\Users\Administrator\ebook-ai-101\ebook")
SRC = EBOOK_DIR / "full-ebook.md"

text = SRC.read_text(encoding='utf-8')

# Split by ## PHẦN headers
parts = re.split(r'(?=^## PHẦN)', text, flags=re.M)

# First chunk = intro/title
intro = parts[0].strip()
(EBOOK_DIR / "chapters" / "00-intro.md").parent.mkdir(parents=True, exist_ok=True)
(EBOOK_DIR / "chapters" / "00-intro.md").write_text(intro, encoding='utf-8')

chapter_map = {
    "HỌC SINH": "part1-students",
    "GIÁO VIÊN": "part2-teachers", 
    "NGƯỜI ĐI LÀM": "part3-office",
    "NHÀ SÁNG TẠO": "part4-creators",
    "LẬP TRÌNH VIÊN": "part5-developers",
    "TỰ ĐỘNG HÓA": "part6-automation",
    "KINH DOANH": "part7-business",
    "ĐỜI SỐNG": "part8-personal",
}

files_created = ["00-intro.md"]

for part in parts[1:]:
    # Extract part title
    title_match = re.match(r'^## (PHẦN \d+:.+?)(?:\n|$)', part)
    if not title_match:
        continue
    title = title_match.group(1)
    
    # Match to filename
    filename = None
    for key, val in chapter_map.items():
        if key in title:
            filename = f"{val}.md"
            break
    
    if not filename:
        # Extract part number
        num_match = re.search(r'PHẦN (\d+)', title)
        if num_match:
            filename = f"part{num_match.group(1)}.md"
        else:
            filename = "part-unknown.md"
    
    filepath = EBOOK_DIR / "chapters" / filename
    filepath.write_text(part.strip(), encoding='utf-8')
    files_created.append(filename)
    print(f"  ✅ {filename}: {title}")

# Also extract conclusion if present
conclusion_match = re.search(r'(## KẾT LUẬN.*)', text, re.S)
if conclusion_match:
    (EBOOK_DIR / "chapters" / "99-conclusion.md").write_text(conclusion_match.group(1).strip(), encoding='utf-8')
    files_created.append("99-conclusion.md")

print(f"\n📊 Total files: {len(files_created)}")
for f in files_created:
    p = EBOOK_DIR / "chapters" / f
    wc = len(p.read_text(encoding='utf-8').split())
    print(f"  {f}: {wc} words")
