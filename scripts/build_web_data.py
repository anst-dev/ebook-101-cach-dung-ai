#!/usr/bin/env python3
import re
import json
from pathlib import Path

# Paths
ROOT_DIR = Path(r"C:\Users\Administrator\ebook-ai-101")
SRC_FILE = ROOT_DIR / "ebook" / "full-ebook.md"
OUT_DIR = ROOT_DIR / "web-reader"
OUT_FILE = OUT_DIR / "ebook-data.js"

OUT_DIR.mkdir(parents=True, exist_ok=True)

def parse_ebook():
    if not SRC_FILE.exists():
        print(f"Error: {SRC_FILE} does not exist.")
        return None
        
    text = SRC_FILE.read_text(encoding="utf-8")
    
    # Split text into chapters using regex
    # We split by '## PHẦN' or '## KẾT LUẬN'
    pattern = r'(?=^## PHẦN|^## KẾT LUẬN)'
    parts = re.split(pattern, text, flags=re.M)
    
    chapters = []
    
    # Part 0 is intro
    intro_content = parts[0].strip()
    # Strip leading '# 101 Cách Dùng AI Miễn Phí' title if it exists to avoid redundancy
    book_title = "101 Cách Dùng AI Miễn Phí"
    book_subtitle = "Cẩm nang thực hành cho mọi người"
    
    # Clean intro a bit
    intro_lines = intro_content.split('\n')
    clean_intro_lines = []
    for line in intro_lines:
        if line.startswith('# '):
            book_title = line.replace('# ', '').strip()
            continue
        if line.strip() == '---' and len(clean_intro_lines) == 0:
            continue
        if line.startswith('*') and line.endswith('*') and len(clean_intro_lines) < 3:
            book_subtitle = line.replace('*', '').strip()
            continue
        clean_intro_lines.append(line)
        
    intro_clean_content = '\n'.join(clean_intro_lines).strip()
    
    # Add Intro chapter
    chapters.append({
        "id": "intro",
        "title": "Lời nói đầu",
        "content": intro_clean_content
    })
    
    # Add rest of the chapters
    for part in parts[1:]:
        part = part.strip()
        if not part:
            continue
            
        # Extract title from the first line
        lines = part.split('\n')
        first_line = lines[0].strip()
        
        # Determine ID and Title
        if first_line.startswith("## PHẦN"):
            # Extract number
            match = re.search(r'## PHẦN (\d+): (.+)', first_line)
            if match:
                part_num = match.group(1)
                part_name = match.group(2)
                ch_id = f"part{part_num}"
                ch_title = f"Phần {part_num}: {part_name}"
            else:
                ch_id = "part_unknown"
                ch_title = first_line.replace("## ", "")
        elif first_line.startswith("## KẾT LUẬN"):
            ch_id = "conclusion"
            ch_title = "Kết luận"
        else:
            ch_id = "section"
            ch_title = first_line.replace("## ", "")
            
        chapters.append({
            "id": ch_id,
            "title": ch_title,
            "content": part # Keep the full content including the header H2 for rendering
        })
        
    ebook_data = {
        "title": book_title,
        "subtitle": book_subtitle,
        "author": "Hermes Agent + NotebookLM + Antigravity CLI",
        "chapters": chapters
    }
    
    return ebook_data

def main():
    data = parse_ebook()
    if data:
        # Write to js file as a global constant EBOOK_DATA
        js_content = f"// Tự động tạo bởi build_web_data.py\nconst EBOOK_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
        OUT_FILE.write_text(js_content, encoding="utf-8")
        print(f"Success! Output written to {OUT_FILE}")
        print(f"Total chapters: {len(data['chapters'])}")

if __name__ == "__main__":
    main()
