#!/usr/bin/env python3
"""export_pdf_chrome.py — Markdown → HTML (pandoc) → PDF (Chrome headless).
Chrome renders Vietnamese Unicode perfectly with system fonts."""
import subprocess
from pathlib import Path
import markdown
import pypandoc

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "ebook" / "full-ebook.md"
HTML_OUT = BASE / "output" / "ebook.html"
PDF_OUT = BASE / "output" / "101-cach-dung-ai-mien-phi.pdf"
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

CSS = """
body { font-family: Arial, 'Segoe UI', sans-serif; font-size: 12pt; line-height: 1.6; color: #2c3e50; max-width: 800px; margin: 0 auto; padding: 40px; text-align: justify; }
h1 { color: #1f3a93; font-size: 28pt; text-align: center; margin-top: 100px; page-break-after: always; }
h2 { color: #1f3a93; font-size: 20pt; border-bottom: 2px solid #d5dbdb; padding-bottom: 5px; page-break-before: always; }
h3 { color: #2980b9; font-size: 14pt; border-left: 4px solid #2980b9; padding-left: 10px; margin-top: 25px; }
h4 { color: #34495e; font-size: 12pt; }
p { margin: 10px 0; }
strong { color: #1a2a40; }
em { color: #34495e; }
ul, ol { margin: 10px 0; padding-left: 25px; }
li { margin: 5px 0; }
hr { border: none; border-top: 1px solid #d5dbdb; margin: 25px 0; }
blockquote { background: #eaf2fb; border-left: 4px solid #1f3a93; padding: 10px 20px; margin: 20px 0; font-style: italic; color: #1f3a93; }
code { font-family: Consolas, monospace; background: #f4f6f7; padding: 2px 6px; border-radius: 3px; font-size: 10pt; color: #c0392b; }
table { border-collapse: collapse; width: 100%; margin: 20px 0; }
th { background: #1f3a93; color: white; padding: 8px; border: 1px solid #bdc3c7; }
td { padding: 8px; border: 1px solid #bdc3c7; }
@page { margin: 2.5cm; }
"""

def convert():
    # 1. Markdown → HTML
    print("📄 Converting Markdown → HTML...")
    text = SRC.read_text(encoding='utf-8')
    md = markdown.Markdown(extensions=['extra', 'sane_lists', 'toc'])
    body_html = md.convert(text)
    
    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>{body_html}</body>
</html>"""
    
    HTML_OUT.parent.mkdir(parents=True, exist_ok=True)
    HTML_OUT.write_text(html, encoding='utf-8')
    print(f"   ✅ HTML: {HTML_OUT} ({len(html):,} chars)")
    
    # 2. HTML → PDF via Chrome headless
    print("🖨️  Converting HTML → PDF via Chrome headless...")
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        "--print-to-pdf=" + str(PDF_OUT),
        str(HTML_OUT),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    
    if PDF_OUT.exists():
        size = PDF_OUT.stat().st_size
        print(f"✅ PDF created: {PDF_OUT}")
        print(f"📊 Size: {size:,} bytes ({size/1024:.1f} KB)")
        
        # Verify Vietnamese
        import pypdf
        reader = pypdf.PdfReader(str(PDF_OUT))
        total_text = ""
        for page in reader.pages[:3]:
            total_text += page.extract_text() or ""
        
        vn_chars = ['ế', 'ư', 'ơ', 'ạ', 'ự', 'ụ', 'ố', 'ờ', 'ậ', 'ẫ', 'ặ', 'ắ', 'ằ']
        found = [c for c in vn_chars if c.lower() in total_text.lower()]
        print(f"🔍 Vietnamese diacritics: {len(found)}/{len(vn_chars)}")
        if found:
            print(f"   Found: {' '.join(found)}")
        if len(found) >= 8:
            print("✅ Vietnamese font PERFECT!")
        elif len(found) >= 4:
            print("✅ Vietnamese font working well!")
        elif found:
            print("⚠️  Partial Vietnamese support")
        else:
            print("❌ Vietnamese still missing")
        
        return 0
    else:
        print(f"❌ PDF not created. stderr: {result.stderr[:500]}")
        return 1

if __name__ == '__main__':
    raise SystemExit(convert())
