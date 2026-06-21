#!/usr/bin/env python3
"""
combine_ebook.py — Tổng hợp toàn bộ nội dung ebook từ NotebookLM output
thành file Markdown hoàn chỉnh, sẵn sàng export PDF.
"""
import os
from pathlib import Path

EBOOK_DIR = Path(r"C:\Users\Administrator\ebook-ai-101\ebook")

# Read intro
intro = (EBOOK_DIR / "00-intro.md").read_text(encoding='utf-8')

# Full ebook content - all 101 ways from NotebookLM
content = f"""# 101 Cách Dùng AI Miễn Phí

*Cẩm nang thực hành cho mọi người*

---

{intro}

---

## PHẦN 1: HỌC SINH & SINH VIÊN (Cách 1–15)

*15 cách dùng AI để học nhanh, nhớ lâu, và giảm tải áp lực học tập.*

### Cách 1: Tóm tắt bài giảng dài thành ghi chú ngắn
**Công cụ:** ChatGPT hoặc Google Gemini | **Mức độ:** Dễ

**Hướng dẫn:**
1. Copy nội dung văn bản bài giảng hoặc transcript video.
2. Mở ChatGPT/Gemini, nhập: *"Hãy tóm tắt bài giảng này thành các ý chính ngắn gọn dạng gạch đầu dòng."*
3. Lưu bản tóm tắt vào sổ tay.

**Ví dụ:** Tài liệu Lịch sử 10 trang → ChatGPT tóm tắt thành 1 trang các mốc thời gian, nhân vật, sự kiện cốt lõi trong 5 giây.

### Cách 2: Giải bài tập Toán/Lý/Hóa từng bước
**Công cụ:** Photomath + ChatGPT Vision | **Mức độ:** Dễ

**Hướng dẫn:**
1. Chụp ảnh đề bài bằng điện thoại.
2. Tải ảnh lên ChatGPT hoặc mở Photomath.
3. Nhập: *"Giải bài toán này và giải thích chi tiết từng bước."*

**Ví dụ:** Phương trình Đại số phức tạp → AI phân tích đặt ẩn phụ, biến đổi từng dòng, ra kết quả như gia sư trực tiếp.

### Cách 3: Dịch và học ngoại ngữ thông minh
**Công cụ:** Google Gemini | **Mức độ:** Dễ

**Hướng dẫn:**
1. Dán đoạn văn bản tiếng nước ngoài vào Gemini.
2. Nhập: *"Dịch sang tiếng Việt. Trích xuất 5 từ vựng khó và giải thích cấu trúc ngữ pháp."*
3. Ghi chép từ vựng mới.

**Ví dụ:** Đọc báo tiếng Anh → Gemini dịch theo ngữ cảnh + dạy từ lóng, thành ngữ có trong bài.

### Cách 4: Tạo flashcard tự động từ sách giáo khoa
**Công cụ:** Quizlet AI + ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Copy đoạn thông tin trong sách giáo khoa.
2. Dán vào ChatGPT: *"Tạo 10 cặp câu hỏi-đáp ngắn gọn để làm flashcard."*
3. Copy danh sách, mở Quizlet tạo Set mới, dán vào.

**Ví dụ:** Chương "Chuỗi thức ăn" Sinh học → 20 câu hỏi trắc nghiệm ngắn → lướt thẻ Quizlet trên xe buýt.

### Cách 5: Luyện viết luận và nhận phản hồi
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Viết bản nháp bài luận.
2. Dán vào Claude: *"Đóng vai giáo viên chấm thi khắt khe. Nhận xét ưu/khuyết điểm, gợi ý sửa lỗi ngữ pháp và cải thiện lập luận."*
3. Sửa lại theo góp ý.

**Ví dụ:** Luận tranh biện tiếng Anh → Claude phát hiện lặp từ, sai ngữ pháp, gợi ý cấu trúc câu nâng cao.

### Cách 6: Tạo kế hoạch ôn thi thông minh
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Liệt kê môn thi, ngày thi, số chương cần học.
2. Nhập: *"Tôi có lịch thi [chi tiết]. Mỗi ngày rảnh 3 tiếng buổi tối. Lên thời gian biểu ôn tập chi tiết."*
3. Chép vào lịch cá nhân.

**Ví dụ:** 2 tuần thi cuối kỳ 3 môn → ChatGPT phân bổ: 2-4-6 ôn Toán, 3-5-7 học Triết+Tiếng Anh, Chủ nhật làm đề thử.

### Cách 7: Học lập trình miễn phí với AI tutor
**Công cụ:** ChatGPT/Claude + Replit | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Yêu cầu AI: *"Giải thích vòng lặp (loop) trong Python là gì, cho ví dụ dễ hiểu."*
2. Copy code mẫu AI tạo ra.
3. Mở Replit (IDE online miễn phí), dán code, bấm "Run".

**Ví dụ:** Gặp bug Python → copy code lỗi dán vào Claude → AI chỉ ra thiếu dấu `:` dòng 5, hướng dẫn sửa.

### Cách 8: Chuyển voice memo thành ghi chú text
**Công cụ:** Whisper (OpenAI) | **Mức độ:** Dễ

**Hướng dẫn:**
1. Ghi âm bài giảng bằng điện thoại.
2. Tải file âm thanh lên công cụ tích hợp Whisper.
3. Chờ vài phút → AI transcript toàn bộ thành văn bản.

**Ví dụ:** Ghi âm 45 phút → Whisper xuất trang văn bản đầy đủ thay vì nghe lại chép tay.

### Cách 9: Tạo bài thuyết trình PowerPoint tự động
**Công cụ:** Gamma hoặc Beautiful.ai | **Mức độ:** Dễ

**Hướng dẫn:**
1. Truy cập Gamma.app, tạo tài khoản miễn phí.
2. Chọn "Generate", gõ chủ đề (VD: "Tác động biến đổi khí hậu").
3. Chọn theme → AI tạo đủ slide kèm nội dung + hình ảnh trong 1 phút.
4. Xuất ra PDF hoặc PPT.

**Ví dụ:** Tối mới bắt đầu làm slide nhóm → Gamma tự dàn ý, viết chữ, tìm ảnh, sắp xếp bố cục chuyên nghiệp.

### Cách 10: Nghiên cứu với AI search engine
**Công cụ:** Perplexity AI | **Mức độ:** Dễ

**Hướng dẫn:**
1. Truy cập Perplexity.ai.
2. Đặt câu hỏi nghiên cứu bằng ngôn ngữ tự nhiên.
3. Đọc câu trả lời tổng hợp + nhấp chú thích [1] [2] để truy cập nguồn gốc.

**Ví dụ:** Làm tiểu luận → Perplexity trả lời + liệt kê link bài báo học thuật uy tín để trích dẫn.

### Cách 11: Viết email xin thực tập chuyên nghiệp
**Công cụ:** ChatGPT/Claude | **Mức độ:** Dễ

**Hướng dẫn:**
1. Liệt kê: tên, trường, công ty muốn xin, kỹ năng nổi bật.
2. Dán vào ChatGPT: *"Viết email xin thực tập tiếng Việt lịch sự, chuyên nghiệp, thuyết phục."*
3. Chỉnh sửa văn phong cho phù hợp.

**Ví dụ:** Sinh viên năm 3 lần đầu xin thực tập → AI viết email chỉn chu, tiêu đề rõ ràng, gây ấn tượng với HR.

### Cách 12: Tạo mindmap từ nội dung bài học
**Công cụ:** Markmap + ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Dán văn bản vào ChatGPT: *"Tóm tắt bài này dưới dạng Markdown (# và -) để làm sơ đồ tư duy."*
2. Copy đoạn Markdown.
3. Truy cập markmap.js.org, dán vào → biểu đồ tư duy tự hiện ra.

**Ví dụ:** Cấu trúc bộ máy nhà nước → AI chuyển thành Markdown → Markmap tạo sơ đồ rẽ nhánh rõ ràng.

### Cách 13: Luyện phỏng vấn xin việc với AI
**Công cụ:** ChatGPT Voice | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Tải app ChatGPT, nhấn biểu tượng tai nghe (Voice).
2. Giao việc: *"Đóng vai người phỏng vấn, hỏi tôi từng câu, đợi trả lời rồi nhận xét."*
3. Trả lời bằng giọng nói trực tiếp.

**Ví dụ:** Lo lắng nói lắp khi phỏng vấn → thực hành với ChatGPT Voice làm quen áp lực, sửa giọng điệu.

### Cách 14: Sửa lỗi chính tả và ngữ pháp
**Công cụ:** LanguageTool + ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cài extension LanguageTool miễn phí trên trình duyệt.
2. Tự động gạch chân lỗi khi gõ trên Google Docs/email.
3. (Tùy chọn) Bôi đen đoạn lủng củng, nhờ ChatGPT diễn đạt lại.

**Ví dụ:** Báo cáo 20 trang → LanguageTool quét toàn bộ, phát hiện gõ nhầm dấu câu, dùng từ sai ngữ cảnh.

### Cách 15: Tạo podcast học tập từ tài liệu
**Công cụ:** NotebookLM | **Mức độ:** Dễ

**Hướng dẫn:**
1. Đăng nhập Google NotebookLM, tạo Notebook mới.
2. Tải lên tài liệu PDF, bài viết liên quan môn học.
3. Nhấn "Audio Overview" → AI tạo podcast 2 MC ảo bàn luận về tài liệu.

**Ví dụ:** 3 chương sách Lịch sử khô khan → podcast 10 phút, cắm tai nghe vừa dọn phòng vừa nghe.

---

## PHẦN 2: GIÁO VIÊN & GIẢNG VIÊN (Cách 16–30)

*Giảm tải hồ sơ sổ sách, chấm bài nhanh chóng, tạo bài giảng sinh động.*

### Cách 16: Soạn giáo án tự động
**Công cụ:** ChatGPT hoặc Claude | **Mức độ:** Dễ

**Hướng dẫn:**
1. Liệt kê tên bài, mục tiêu, đối tượng học sinh.
2. Nhập: *"Soạn giáo án 45 phút môn [Tên môn], bài [Tên bài]. Chia rõ: khởi động, giảng bài mới, luyện tập, củng cố."*
3. Chỉnh sửa hoạt động cho phù hợp phong cách dạy.

**Ví dụ:** Bài "Hệ bài tiết" Sinh lớp 8 → AI gợi ý trò chơi khởi động, câu hỏi dẫn dắt, chia nhóm thực hành trong 30 giây.

### Cách 17: Tạo ngân hàng câu hỏi trắc nghiệm
**Công cụ:** Quizizz AI + ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Copy đoạn văn bản bài học.
2. Dán vào ChatGPT/Quizizz AI: *"Tạo 15 câu trắc nghiệm (4 đáp án A,B,C,D), đánh dấu đáp án đúng."*
3. Trích xuất vào Quizizz để học sinh làm trực tuyến.

**Ví dụ:** Nội dung bài đọc Ngữ Văn → AI tự động tạo bộ 20 câu hỏi đọc hiểu cực chuẩn.

### Cách 18: Chấm bài viết tự động và đưa ra nhận xét
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Gõ tiêu chí chấm điểm (barem) vào AI.
2. Copy bài luận học sinh dán vào.
3. Yêu cầu: *"Chấm bài dựa trên tiêu chí. Đưa ra điểm số dự kiến và 3 dòng nhận xét."*

**Ví dụ:** Chấm 40 bài luận tiếng Anh → Claude chỉ ra lỗi ngữ pháp lặp, gợi ý lời khen ngợi từng em.

### Cách 19: Tạo rubric đánh giá chuyên nghiệp
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Xác định bài tập cần đánh giá.
2. Yêu cầu: *"Lập bảng Rubric chấm điểm [Tên bài tập]. Chia 4 mức: Kém, Đạt, Khá, Tốt."*
3. Copy vào Word/Excel.

**Ví dụ:** Dự án "Bảo vệ môi trường" → AI chia thang điểm: Hình thức, sáng tạo, làm việc nhóm.

### Cách 20: Dịch tài liệu giảng dạy đa ngôn ngữ
**Công cụ:** DeepL + Gemini | **Mức độ:** Dễ

**Hướng dẫn:**
1. Tìm bài báo khoa học/tài liệu tiếng Anh.
2. Dán vào DeepL (cần sự tự nhiên) hoặc Gemini (dịch + tóm tắt).
3. Lọc ý hay đưa vào bài giảng.

**Ví dụ:** Báo cáo WHO về dinh dưỡng → DeepL dịch chuẩn thuật ngữ y khoa, không "ngô nghê" như Google Dịch.

### Cách 21: Tạo bài tập phân hóa theo năng lực
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cung cấp bài tập gốc.
2. Nhập: *"Biến đổi bài tập này thành 3 phiên bản: Dễ (học sinh yếu), Trung bình (khá), Khó (giỏi)."*
3. In ra cho từng nhóm.

**Ví dụ:** Phương trình bậc 2 → AI thiết kế dạng điền số cho HS yếu, toán đố ứng dụng cho HS giỏi.

### Cách 22: Tạo hình ảnh minh họa cho bài giảng
**Công cụ:** Canva AI / DALL-E | **Mức độ:** Dễ

**Hướng dẫn:**
1. Mở Canva → "Magic Media" hoặc dùng DALL-E trong ChatGPT.
2. Gõ mô tả: *"Bức ảnh hoạt hình cảnh chợ quê Việt Nam ngày xưa, màu tươi sáng."*
3. Lưu ảnh, chèn vào slide.

**Ví dụ:** Giáo viên Lịch sử không tìm được ảnh phù hợp → AI vẽ lại khung cảnh trận Bạch Đằng chân thực.

### Cách 23: Viết email phụ huynh chuyên nghiệp
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Gõ tóm tắt vấn đề: "Bé A hay nói chuyện riêng, điểm Toán giảm, nhưng năng nổ thể thao".
2. Yêu cầu: *"Viết email gửi phụ huynh. Văn phong khéo léo, đồng cảm nhưng nhắc nhở nghiêm túc."*
3. Chỉnh sửa tên, gửi.

**Ví dụ:** Tránh phụ huynh phật ý → ChatGPT dùng "lời hay ý đẹp", tiếp cận tích cực, phối hợp giáo dục.

### Cách 24: Tạo video hướng dẫn ngắn từ text
**Công cụ:** HeyGen / InVideo AI | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Chuẩn bị đoạn văn bản ngắn (VD: nhắc nộp bài).
2. Dán vào HeyGen, chọn nhân vật ảo (Avatar).
3. Bấm "Generate" → AI tạo video MC ảo đọc kịch bản.

**Ví dụ:** Thay vì trang điểm quay hình → AI tạo MC ảo đọc thông báo học bù cuối tuần.

### Cách 25: Phân tích kết quả thi cử
**Công cụ:** ChatGPT (Data Analysis) | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Tải bảng điểm Excel/CSV lên ChatGPT.
2. Nhập: *"Phân tích phổ điểm lớp. Tìm điểm trung bình, chỉ ra câu trắc nghiệm có tỷ lệ sai cao nhất."*
3. Nhận báo cáo điều chỉnh phương pháp dạy.

**Ví dụ:** Sau giữa kỳ → AI báo cáo: "60% học sinh sai câu 12 phần hình học" trong 3 giây.

### Cách 26: Tạo kịch bản bài giảng video
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nhập chủ đề video (VD: Giải thích Nhật Thực).
2. Yêu cầu: *"Viết kịch bản 5 phút. Chia 2 cột: Hình ảnh minh họa + Lời thoại."*
3. Lấy kịch bản quay dựng.

**Ví dụ:** Kênh YouTube giáo dục → AI đóng vai biên kịch, biết điểm nào chèn hiệu ứng âm thanh.

### Cách 27: Tạo quiz tương tác Kahoot-style
**Công cụ:** Quizizz / Kahoot AI | **Mức độ:** Dễ

**Hướng dẫn:**
1. Tải PDF bài giảng lên Kahoot/Quizizz.
2. Chọn "Create with AI".
3. Ứng dụng tự quét tài liệu, sinh trò chơi có nhạc, đếm ngược.

**Ví dụ:** Cuối tiết học → 2 cú click chuột, học sinh chơi game trả lời câu hỏi đua top trên điện thoại.

### Cách 28: Viết thư giới thiệu học sinh
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nhập: tên HS, GPA, 2-3 ưu điểm, trường muốn nộp đơn.
2. Yêu cầu: *"Viết thư giới thiệu (Letter of Recommendation) tiếng Anh chuyên nghiệp 400 chữ."*
3. Ký tên, đóng dấu.

**Ví dụ:** Giáo viên cấp 3 thường xuyên nhờ viết thư xin học bổng → ChatGPT biến gạch đầu dòng thành thư trang trọng.

### Cách 29: Tạo tài liệu hướng dẫn thực hành
**Công cụ:** ChatGPT + Markdown | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nêu tên bài thực hành (VD: cắt tỉa hoa quả).
2. Yêu cầu AI viết các bước rõ ràng dạng Markdown (in đậm, gạch đầu dòng).
3. Copy vào Word, in phát cho học sinh.

**Ví dụ:** Thí nghiệm Hóa → AI liệt kê dụng cụ, bước đong đếm, lưu ý an toàn cháy nổ rành mạch.

### Cách 30: Tạo câu hỏi thảo luận nhóm
**Công cụ:** Gemini / ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nhập tác phẩm/chủ đề tranh luận.
2. Yêu cầu: *"Tạo 5 câu hỏi mở kích thích tư duy phản biện, không có đáp án đúng sai tuyệt đối."*
3. Trình chiếu lên bảng.

**Ví dụ:** Dạy "Vợ nhặt" → AI gợi ý: *"Nếu Tràng sống thời hiện đại, quyết định nhặt vợ có được đánh giá khác không?"*

---

## PHẦN 3: NGƯỜI ĐI LÀM & DÂN VĂN PHÒNG (Cách 31–45)

*Tăng năng suất gấp đôi, tan làm đúng giờ.*

### Cách 31: Viết và tối ưu email công việc
**Công cụ:** ChatGPT hoặc Claude | **Mức độ:** Dễ

**Hướng dẫn:**
1. Gõ nháp ý lủng củng (VD: báo sếp dự án bị trễ).
2. Yêu cầu: *"Viết lại thành email công sở chuyên nghiệp, lịch sự, xin lỗi kèm hướng giải quyết."*
3. Copy gửi.

**Ví dụ:** Tránh email cọc cằn khi bực → AI làm "bộ lọc ngôn từ", trình bày mượt mà.

### Cách 32: Tạo biên bản họp tự động
**Công cụ:** Otter.ai | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cài Otter extension, mở khi họp Zoom/Meet.
2. Otter tự chuyển giọng nói thành văn bản.
3. Kết thúc → AI tóm tắt 3 hành động (Action items) tiếp theo.

**Ví dụ:** Họp 2 tiếng → Otter gỡ băng, chốt thành email tóm tắt hoàn hảo gửi cả phòng ban.

### Cách 33: Tóm tắt tài liệu PDF dài
**Công cụ:** ChatPDF hoặc Claude | **Mức độ:** Dễ

**Hướng dẫn:**
1. Tải PDF báo cáo/hợp đồng lên ChatPDF.
2. Đặt câu hỏi: *"Đâu là 3 điểm rủi ro nhất trong bản hợp đồng này?"*
3. Lọc ý chính làm báo cáo.

**Ví dụ:** Báo cáo 100 trang → ChatPDF tóm tắt 1 trang A4 các chỉ số quan trọng trong 1 phút.

### Cách 34: Phân tích dữ liệu Excel với AI
**Công cụ:** ChatGPT (Data Analysis) | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Kéo thả file Excel/CSV vào ChatGPT.
2. Yêu cầu: *"Phân tích file. Cho biết 3 sản phẩm bán chạy nhất, vẽ biểu đồ hình tròn."*
3. Tải biểu đồ về.

**Ví dụ:** Không cần VLOOKUP/Pivot Table → dùng ngôn ngữ nói bảo ChatGPT phân tích, AI làm toàn bộ.

### Cách 35: Tạo kế hoạch dự án (Gantt Chart)
**Công cụ:** ChatGPT + Mermaid Live | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Cung cấp timeline các công việc.
2. Yêu cầu: *"Tạo biểu đồ Gantt bằng cú pháp Markdown Mermaid."*
3. Copy code, dán vào Mermaid Live Editor lấy hình.

**Ví dụ:** Ra mắt sản phẩm mới → sơ đồ Gantt giúp sếp hiểu ngay ai làm gì, ngày nào.

### Cách 36: Dịch tài liệu công việc chuyên ngành
**Công cụ:** DeepL | **Mức độ:** Dễ

**Hướng dẫn:**
1. Mở DeepL.com.
2. Dán email/tài liệu kỹ thuật tiếng nước ngoài.
3. Chỉnh sửa từ ngữ cho hợp ngữ cảnh.

**Ví dụ:** Chứng từ Logistics chứa từ lóng hàng hải → DeepL dịch chuẩn ngữ cảnh chuyên ngành.

### Cách 37: Tạo PowerPoint chuyên nghiệp cực nhanh
**Công cụ:** Gamma hoặc Copilot | **Mức độ:** Dễ

**Hướng dẫn:**
1. Đăng nhập Gamma.app → "Generate Presentation".
2. Gõ nội dung (VD: Báo cáo kinh doanh Q3).
3. AI tự tạo dàn bài, viết chữ, tìm ảnh, dàn slide.

**Ví dụ:** Báo cáo sếp đột xuất 3h chiều, 2h mới bắt đầu → Gamma tạo 15 slide đẹp long lanh.

### Cách 38: Viết proposal và báo giá
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Nhập nhu cầu khách hàng, dịch vụ, mức giá.
2. Yêu cầu AI viết Proposal 3 phần: Nỗi đau khách → Giải pháp → Báo giá.
3. Điều chỉnh, xuất PDF.

**Ví dụ:** Dân sales mất nửa ngày nặn chào hàng → AI cấu trúc Benefits cực thuyết phục, chốt deal nhanh.

### Cách 39: Quản lý task và nhắc việc
**Công cụ:** Notion AI hoặc Todoist AI | **Mức độ:** Dễ

**Hướng dẫn:**
1. Tạo mục tiêu lớn (VD: Tổ chức Year End Party).
2. Nhấn AI Assist: *"Chia nhỏ mục tiêu này thành các task con."*
3. Gán ngày giờ, người phụ trách.

**Ví dụ:** "Làm tiệc cuối năm" → AI chẻ nhỏ: chốt địa điểm, thuê MC, đặt menu, gửi thiệp mời...

### Cách 40: Phân tích đối thủ cạnh tranh
**Công cụ:** Perplexity + ChatGPT | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Perplexity: *"Phân tích chiến lược marketing hiện tại của [Tên đối thủ]."*
2. Copy dữ liệu vào ChatGPT.
3. Yêu cầu vẽ bảng SWOT so sánh với công ty bạn.

**Ví dụ:** Perplexity "cào" dữ liệu mới nhất hôm nay, không phải dữ liệu cũ năm ngoái.

### Cách 41: Tạo template email marketing
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cung cấp chi tiết sản phẩm.
2. Yêu cầu: *"Viết chuỗi 3 email: Email 1 gây tò mò, Email 2 nêu lợi ích, Email 3 chốt sale FOMO."*
3. Copy vào nền tảng gửi mail.

**Ví dụ:** Tự tạo tiêu đề "giật gân" → tăng tỷ lệ mở thư khách hàng gấp đôi.

### Cách 42: Viết CV và cover letter
**Công cụ:** ChatGPT hoặc Rezi | **Mức độ:** Dễ

**Hướng dẫn:**
1. Copy JD công ty + kinh nghiệm làm việc cũ.
2. Dán vào ChatGPT: *"Viết lại kinh nghiệm nổi bật từ khóa trong JD, viết Cover Letter hấp dẫn."*
3. Gửi ứng tuyển.

**Ví dụ:** Vượt qua hệ thống lọc ATS → AI giúp CV "khớp 100%" từ khóa nhà tuyển dụng tìm.

### Cách 43: Tạo nội dung LinkedIn chuyên nghiệp
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Gõ ý tưởng ngắn: "Hoàn thành chứng chỉ Google Ads, rất vui".
2. Yêu cầu: *"Format phong cách LinkedIn: chuyên nghiệp, truyền cảm hứng, gạch đầu dòng, hashtag."*
3. Đăng kèm ảnh chứng chỉ.

**Ví dụ:** Biến dòng trạng thái cụt lủn thành bài chia sẻ hành trình đầy năng lượng, thu hút headhunters.

### Cách 44: Tự động hóa dữ liệu Google Sheets
**Công cụ:** ChatGPT + Google Apps Script | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Miêu tả: *"Mỗi khi có khách điền form Google Sheets, tự gửi email cảm ơn."*
2. Nhờ ChatGPT viết code Apps Script.
3. Google Sheets → Tiện ích mở rộng → Apps Script → Dán code → Chạy.

**Ví dụ:** Không biết code vẫn làm công cụ tự động trên Sheets, tiết kiệm hàng giờ copy/paste.

### Cách 45: Tạo quy trình chuẩn hóa (SOP)
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Liệt kê công việc thao tác lộn xộn.
2. Yêu cầu: *"Hệ thống hóa thành bộ SOP cho nhân viên mới. Bổ sung phòng ngừa rủi ro."*
3. Format, lưu vào kho kiến thức công ty.

**Ví dụ:** Trưởng phòng viết quy trình đào tạo → AI dàn khung từ Ngày 1 đến checklist thử việc tháng 2.

---

## PHẦN 4: NHÀ SÁNG TẠO NỘI DUNG (Cách 46–57)

*Làm nội dung nhanh hơn mà không cạn kiệt ý tưởng.*

### Cách 46: Viết kịch bản YouTube/TikTok
**Công cụ:** ChatGPT hoặc Claude | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cung cấp chủ đề + đối tượng người xem.
2. Nhập: *"Viết kịch bản TikTok 60 giây về [Chủ đề]. 2 cột: Hình ảnh + Âm thanh (Voiceover)."*
3. Chỉnh sửa văn phong, tiến hành quay.

**Ví dụ:** Review son môi → AI lên kịch bản: 3 giây hook, thân bài review chất, cuối kêu gọi thả tim.

### Cách 47: Tạo tiêu đề và thumbnail ideas
**Công cụ:** ChatGPT + Canva | **Mức độ:** Dễ

**Hướng dẫn:**
1. ChatGPT tạo 5 tiêu đề giật gân (clickbait nhẹ, không lừa đảo).
2. Yêu cầu AI miêu tả ý tưởng thumbnail.
3. Mở Canva, ghép theo ý tưởng AI.

**Ví dụ:** "Đi chơi Đà Lạt" → AI gợi ý "Cầm 2 triệu ăn sập Đà Lạt 24h" + thumbnail cầm tiền biểu cảm bất ngờ.

### Cách 48: Sinh ảnh minh họa miễn phí
**Công cụ:** DALL-E hoặc Leonardo.ai | **Mức độ:** Dễ

**Hướng dẫn:**
1. Đăng nhập Leonardo.ai hoặc DALL-E.
2. Gõ prompt tiếng Anh: *"A futuristic robot typing on a laptop, neon lights, 4k"*
3. Tải ảnh hoàn hảo nhất.

**Ví dụ:** Blog công nghệ không có ảnh đẹp → AI sinh ảnh xịn không lo bản quyền.

### Cách 49: Viết blog post SEO-friendly
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Nêu từ khóa (Keyword) muốn lên top Google.
2. Nhập: *"Viết blog 1000 chữ về [Từ khóa]. Cấu trúc H2, H3, tối ưu SEO."*
3. Thêm ảnh, rà soát, đăng bài.

**Ví dụ:** "Cách trị mụn tại nhà" → AI rải từ khóa tự nhiên vào mở/thân/kết bài, thân thiện Google.

### Cách 50: Tạo podcast từ bài viết
**Công cụ:** NotebookLM | **Mức độ:** Dễ

**Hướng dẫn:**
1. Tải bài viết blog/tài liệu lên NotebookLM.
2. Bấm "Audio Overview".
3. Tải MP3, đăng lên Spotify/YouTube.

**Ví dụ:** Bài đánh giá sách 2000 chữ → podcast 2 MC ảo thảo luận tung hứng về sách.

### Cách 51: Chỉnh sửa video với AI
**Công cụ:** CapCut AI hoặc Runway | **Mức độ:** Dễ

**Hướng dẫn:**
1. Tải video gốc lên CapCut.
2. Dùng Auto-captions tự tạo phụ đề từ giọng nói.
3. Dùng Remove Background hoặc Auto-cut khoảng lặng.

**Ví dụ:** Video 10 phút → AI tạo phụ đề tiếng Việt chuẩn xác chạy chữ theo lời nói trong 2 phút.

### Cách 52: Viết caption social media
**Công cụ:** ChatGPT hoặc Gemini | **Mức độ:** Dễ

**Hướng dẫn:**
1. Dán hình ảnh/miêu tả video.
2. Nhập: *"Viết 3 caption ngắn gọn, hài hước cho Facebook/Instagram kèm hashtag."*
3. Chọn caption ưng ý.

**Ví dụ:** Chụp ly cà phê sáng → AI "chế" câu thả thính/truyền động lực tăng tương tác.

### Cách 53: Tạo newsletter tự động
**Công cụ:** ChatGPT + beehiiv | **Mức độ:** Dễ

**Hướng dẫn:**
1. ChatGPT tóm tắt 3 tin tức nổi bật trong tuần.
2. Chỉnh sửa văn phong thân thiện.
3. Dán vào beehiiv, lên lịch gửi.

**Ví dụ:** Sáng thứ 2 → bản tin "Điểm tin Marketing tuần qua" gửi khách hàng, chỉ mất 15 phút.

### Cách 54: Thiết kế logo miễn phí
**Công cụ:** Hatchful hoặc Looka | **Mức độ:** Dễ

**Hướng dẫn:**
1. Truy cập Looka, nhập tên thương hiệu + ngành nghề.
2. Chọn màu sắc, phong cách thiết kế.
3. AI sinh hàng chục mẫu logo chuyên nghiệp.

**Ví dụ:** Tiệm bánh online nhỏ → logo xinh xắn, chuẩn màu nhận diện, không cần thuê designer.

### Cách 55: Tạo emoji/sticker tùy chỉnh
**Công cụ:** DALL-E hoặc Canva | **Mức độ:** Dễ

**Hướng dẫn:**
1. Yêu cầu DALL-E: *"Vẽ sticker chú mèo uống trà sữa, phong cách chibi, nền trắng."*
2. Mở Canva, xóa nền nếu cần.
3. Xuất PNG, đẩy lên Zalo/Telegram.

**Ví dụ:** Bộ sticker "Đang chạy deadline" độc quyền gửi trong nhóm chat công ty.

### Cách 56: Viết truyện với AI
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Xây cốt truyện: bối cảnh, tên nhân vật, tính cách.
2. Nhập: *"Viết chương 1, tập trung miêu tả nội tâm nhân vật."*
3. Đọc, yêu cầu AI sửa đoạn chưa hay.

**Ví dụ:** Ý tưởng truyện xuyên không nhưng văn phong hạn chế → Claude chắp bút, diễn đạt mượt mà.

### Cách 57: Tạo content calendar
**Công cụ:** ChatGPT + Buffer AI | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nhập: *"Lập lịch đăng bài 30 ngày cho TikTok về giảm cân. Bảng: Ngày, Chủ đề, Định dạng."*
2. Đưa nội dung lên Buffer tự động lên lịch.

**Ví dụ:** Không còn "Hôm nay đăng gì?" → AI cung cấp bức tranh toàn cảnh 1 tháng để quay dựng một lần.

---

## PHẦN 5: LẬP TRÌNH VIÊN & TECH (Cách 58–69)

*Trợ lý đắc lực cho dân IT.*

### Cách 58: Code review tự động
**Công cụ:** Claude Code hoặc Codex CLI | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Copy đoạn code vừa viết.
2. Dán vào AI: *"Review code này, chỉ ra rủi ro bảo mật, gợi ý tối ưu."*
3. Chỉnh sửa theo nhận xét.

**Ví dụ:** Trước khi push code → AI phát hiện leak biến môi trường hoặc hàm tốn quá nhiều bộ nhớ.

### Cách 59: Debug code với AI assistant
**Công cụ:** ChatGPT hoặc Claude | **Mức độ:** Dễ

**Hướng dẫn:**
1. Copy toàn bộ error log.
2. Dán vào ChatGPT cùng code lỗi: *"Tại sao lỗi này và cách sửa?"*
3. Áp dụng code đã sửa.

**Ví dụ:** "Null pointer exception" 2 tiếng không ra → AI chỉ đích danh dòng 45 chưa khởi tạo biến.

### Cách 60: Tạo boilerplate code
**Công cụ:** Cursor hoặc Copilot | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cài Cursor IDE.
2. Mở file mới, gọi AI: *"Tạo khung server Express.js có kết nối MongoDB."*
3. Code tự sinh ra trong IDE.

**Ví dụ:** Dự án mới không cần gõ lại cấu hình server, router, middleware → AI tạo khung sườn 5 giây.

### Cách 61: Viết unit test tự động
**Công cụ:** Codex CLI hoặc Claude | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Cung cấp hàm cần test.
2. Lệnh: *"Viết Unit Test bằng Jest. Bao phủ trường hợp thường và edge cases."*
3. Chạy test trong terminal.

**Ví dụ:** Claude tự đẻ ra 10 file test cho component React chỉ bằng một cú nhấp.

### Cách 62: Chuyển đổi code giữa ngôn ngữ
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Dán code cũ (VD: Python).
2. Lệnh: *"Dịch sang Go (Golang), giữ nguyên logic."*
3. Tích hợp code mới.

**Ví dụ:** Port thuật toán Java sang JavaScript mà không cần nắm vững cú pháp Java.

### Cách 63: Tạo API documentation
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Dán file chứa API endpoints.
2. Lệnh: *"Tạo tài liệu API chuẩn Swagger/OpenAPI, giải thích request body và response."*
3. Xuất ra YAML/Markdown.

**Ví dụ:** Làm xong tính năng, ngại viết tài liệu → AI mô tả chi tiết từng param siêu chuyên nghiệp.

### Cách 64: Refactor code
**Công cụ:** Claude Code | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Dán đoạn code dài, if-else phức tạp.
2. Lệnh: *"Refactor cho Clean Code, áp dụng Design Pattern phù hợp."*
3. Đọc kỹ logic mới.

**Ví dụ:** Code "Spaghetti" của thực tập sinh → cấu trúc Module gọn gàng, chuẩn Senior.

### Cách 65: Học framework mới
**Công cụ:** ChatGPT + Perplexity | **Mức độ:** Dễ

**Hướng dẫn:**
1. Perplexity: *"Cập nhật tính năng mới nhất Next.js 14."*
2. ChatGPT: *"App Router khác gì Pages Router? Cho ví dụ."*

**Ví dụ:** AI tóm tắt tinh hoa trang Document dài dằng dặc, học nhanh framework mới.

### Cách 66: Tạo regex bằng ngôn ngữ tự nhiên
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nêu định dạng muốn trích xuất.
2. Lệnh: *"Viết Regex JavaScript bắt số điện thoại VN (10 số, bắt đầu 0)."*
3. Dán vào source code.

**Ví dụ:** Không cần nhớ `\\d`, `^`, `$` → miêu tả bằng lời, AI trả Regex chính xác 100%.

### Cách 67: Tối ưu database queries
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Dán SQL chậm + cấu trúc bảng (Schema).
2. Lệnh: *"Query này chậm. Tối ưu hóa? Đánh Index ở cột nào?"*
3. Chạy lại query đo lường.

**Ví dụ:** Query bảng triệu dòng → AI gợi ý JOIN đúng + Index, tăng tốc từ 5s xuống 0.1s.

### Cách 68: Viết commit messages chuyên nghiệp
**Công cụ:** Claude Code | **Mức độ:** Dễ

**Hướng dẫn:**
1. Copy `git diff`.
2. Lệnh: *"Viết commit message chuẩn Conventional Commits."*
3. Dán vào Git.

**Ví dụ:** Thay vì "Fix bug" → AI viết: `fix(auth): resolve token expiration issue`.

### Cách 69: Tạo CI/CD pipeline templates
**Công cụ:** ChatGPT hoặc Claude | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Cung cấp thông tin dự án (VD: React, deploy AWS).
2. Lệnh: *"Tạo file GitHub Actions YAML tự động build+deploy khi push main."*
3. Copy `.yml` vào dự án.

**Ví dụ:** Tự động hóa triển khai không cần rành DevOps → AI tạo file cấu hình chuẩn bảo mật.

---

## PHẦN 6: TỰ ĐỘNG HÓA & NĂNG SUẤT (Cách 70–81)

*Làm việc thay bạn trong khi bạn ngủ.*

### Cách 70: Tạo chatbot trả lời khách hàng
**Công cụ:** ChatGPT + n8n | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Đăng ký n8n.io (công cụ tự động hóa).
2. Cài đặt: Tin nhắn Facebook → ChatGPT xử lý → Trả lời.
3. Tinh chỉnh prompt lịch sự.

**Ví dụ:** Cửa hàng online tự trả lời giá ship, tư vấn size 24/7 không cần nhân viên trực page.

### Cách 71: Tự động phân loại email
**Công cụ:** Gmail AI / Zapier | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Kết nối Gmail với Zapier.
2. Cài luồng: Quét email mới → AI đọc → Phân loại phàn nàn/rác/hỏi mua.
3. Tự động gắn nhãn (Label).

**Ví dụ:** Mở hộp thư → email khách cáu gắt đã vào mục "Cần xử lý Gấp" để ưu tiên.

### Cách 72: Tạo workflow automation
**Công cụ:** n8n hoặc Make.com | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Đăng nhập Make.com.
2. Kéo thả: Google Form → Google Sheets → Slack thông báo.
3. Bật "Run".

**Ví dụ:** Tiết kiệm hàng giờ copy-paste thông tin khách hàng giữa các nền tảng.

### Cách 73: Trích xuất dữ liệu từ invoices
**Công cụ:** ChatGPT Vision | **Mức độ:** Dễ

**Hướng dẫn:**
1. Chụp ảnh hóa đơn/biên lai.
2. Tải lên ChatGPT: *"Trích xuất tên cửa hàng, ngày, tổng tiền vào bảng."*
3. Lưu vào Excel.

**Ví dụ:** Kế toán không gõ tay → AI quét ảnh, bóc tách dữ liệu chính xác 99%.

### Cách 74: Tạo webhook thông báo
**Công cụ:** n8n + ChatGPT | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Cấu hình Webhook n8n nhận data từ website.
2. ChatGPT tóm tắt data.
3. Bắn tin nhắn Telegram.

**Ví dụ:** Báo mới nhắc tên thương hiệu → hệ thống tự bắt, gửi tóm tắt qua Telegram ngay.

### Cách 75: Tự động đăng bài social media
**Công cụ:** Buffer / Buffer AI | **Mức độ:** Dễ

**Hướng dẫn:**
1. Kết nối Facebook, LinkedIn, Twitter vào Buffer.
2. Tải nội dung cả tháng lên.
3. Set giờ đăng (VD: 8h tối mỗi ngày).

**Ví dụ:** Đi du lịch cả tuần nhưng trang social vẫn có bài lên đều đặn.

### Cách 76: Giám sát website uptime
**Công cụ:** n8n + AI | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Trigger n8n chạy mỗi 5 phút "ping" website.
2. Nếu lỗi (404, 500) → AI phân tích lỗi.
3. Gửi cảnh báo SMS.

**Ví dụ:** Hệ thống sập 2h sáng → nhận cảnh báo ngay thay vì sáng hôm sau mới biết.

### Cách 77: Tự động backup dữ liệu
**Công cụ:** Rclone + scripts | **Mức độ:** Trung bình

**Hướng dẫn:**
1. ChatGPT viết script shell nén thư mục tài liệu.
2. Rclone đẩy file lên Google Drive/OneDrive.
3. Cài hẹn giờ tự chạy.

**Ví dụ:** Mỗi 12h đêm → toàn bộ code + hợp đồng sao lưu lên mây tự động.

### Cách 78: Tạo personal assistant
**Công cụ:** Hermes Agent | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Cài framework AI Agent mã nguồn mở.
2. Cấp quyền truy cập Calendar, file ghi chú.
3. Trò chuyện, ra lệnh.

**Ví dụ:** Sáng hỏi: "Lịch trình hôm nay?" → trợ lý rà soát lịch, báo cuộc họp 9h + tài liệu tóm tắt.

### Cách 79: Tạo báo cáo định kỳ tự động
**Công cụ:** ChatGPT + Cron | **Mức độ:** Nâng cao

**Hướng dẫn:**
1. Python lấy dữ liệu bán hàng.
2. ChatGPT API viết email tổng kết.
3. Cron Job chạy 5h chiều thứ 6 hàng tuần.

**Ví dụ:** Báo cáo tuần không còn ác mộng → quy trình tự gom số liệu, viết, gửi email.

### Cách 80: Quản lý password thông minh
**Công cụ:** Bitwarden + AI | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cài Bitwarden miễn phí.
2. AI sinh Master Password mạnh dạng câu văn dễ nhớ.
3. Lưu toàn bộ mật khẩu vào két sắt ảo.

**Ví dụ:** Không bao giờ "Quên mật khẩu" hay dùng chung pass "123456" cho mọi trang.

### Cách 81: Tạo todo list AI-powered
**Công cụ:** Todoist AI hoặc Notion | **Mức độ:** Dễ

**Hướng dẫn:**
1. Gõ mục tiêu chung chung vào Notion.
2. Nhấn AI: *"Chia nhỏ thành đầu việc làm được trong ngày."*
3. Tick khi hoàn thành.

**Ví dụ:** AI bẻ gãy khối công việc khổng lồ thành nhiệm vụ nhỏ tí hon dễ bắt đầu.

---

## PHẦN 7: KINH DOANH & MARKETING (Cách 82–91)

*Tối ưu chi phí, đạt hiệu quả cao.*

### Cách 82: Phân tích thị trường
**Công cụ:** Perplexity + ChatGPT | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Perplexity: *"Quy mô + xu hướng thị trường cà phê đặc sản VN năm nay?"*
2. Copy dữ liệu vào ChatGPT.
3. Yêu cầu: *"Lập báo cáo phân tích: Cơ hội, Thách thức, Xu hướng."*

**Ví dụ:** Muốn mở quán cafe → AI cung cấp bức tranh thị hiếu giới trẻ trong 5 phút, không cần thuê công ty nghiên cứu.

### Cách 83: Tạo chiến dịch quảng cáo
**Công cụ:** ChatGPT hoặc Claude | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Cung cấp sản phẩm + ngân sách.
2. Nhập: *"Lên ý tưởng chiến dịch Facebook bán áo khoác đông. 3 góc độ (angles) + nội dung mỗi góc."*
3. Chỉnh sửa câu chữ.

**Ví dụ:** AI tạo phiên bản copy khác nhau (giá rẻ, chất lượng, thời trang) để A/B testing.

### Cách 84: Viết business plan
**Công cụ:** ChatGPT | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Gõ tóm tắt ý tưởng khởi nghiệp.
2. Yêu cầu: *"Viết Business Plan: Tóm tắt hành pháp, Phân tích thị trường, Chiến lược tiếp thị, Kế hoạch tài chính."*
3. Điền con số thực tế.

**Ví dụ:** Rủ bạn hùn vốn mở tiệm bánh → ChatGPT phác thảo kế hoạch logic, thuyết phục.

### Cách 85: Tạo customer persona
**Công cụ:** Claude hoặc ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nêu sản phẩm (VD: Khóa yoga online cho mẹ bỉm).
2. Lệnh: *"Vẽ 2 chân dung khách hàng chi tiết: Tên, tuổi, thu nhập, pain points, sở thích."*
3. Lưu làm kim chỉ nam marketing.

**Ví dụ:** Hiểu "chị Lan 30 tuổi, đau lưng, không có thời gian tới phòng tập" → target quảng cáo chuẩn.

### Cách 86: Phân tích feedback khách hàng
**Công cụ:** ChatGPT (Data Analysis) | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Tải Excel review khách hàng Shopee/TikTok Shop lên ChatGPT.
2. Lệnh: *"Phân loại Tích cực/Tiêu cực. Tìm 3 lời phàn nàn phổ biến nhất."*
3. Cải thiện sản phẩm.

**Ví dụ:** 1000 review → AI tóm tắt: "70% khen vải đẹp, 20% phàn nàn giao hàng chậm".

### Cách 87: Tạo landing page copy
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nhập thông tin dịch vụ.
2. Lệnh: *"Viết Landing Page: Tiêu đề giật tít, Nêu vấn đề, Giải pháp, Cảm nhận khách hàng, Call to action."*
3. Đưa cho bộ phận thiết kế web.

**Ví dụ:** ChatGPT cấu trúc theo mô hình thuyết phục tâm lý AIDA/PAS.

### Cách 88: Tối ưu SEO on-page
**Công cụ:** ChatGPT + Surfer SEO | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Cung cấp bài viết gốc.
2. Lệnh: *"SEO bài viết cho từ khóa 'Sữa rửa mặt trị mụn'. Tối ưu tiêu đề, Meta Description 150 chữ, rải từ khóa vào H2, H3."*
3. Chỉnh sửa trên website.

**Ví dụ:** Bài blog dễ leo trang 1 Google mà không cần thuê chuyên gia SEO.

### Cách 89: Tạo email sequence marketing
**Công cụ:** ChatGPT | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Nêu mục tiêu chuyển đổi khách hàng.
2. Lệnh: *"Viết chuỗi 5 email: Email 1 tặng quà, 2-3 chia sẻ giá trị, 4 giới thiệu khóa học, 5 chốt sale giảm giá."*
3. Đưa vào hệ thống gửi mail tự động.

**Ví dụ:** Đi ngủ, chuỗi email AI viết "chăm sóc" khách hàng thay bạn mỗi ngày.

### Cách 90: Phân tích đối thủ
**Công cụ:** Perplexity + Claude | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Perplexity: *"Liệt kê tính năng + mức giá [Tên đối thủ]."*
2. Dán vào Claude kèm thông tin sản phẩm bạn.
3. Lệnh: *"Lập bảng so sánh điểm mạnh/yếu."*

**Ví dụ:** Nhận ra USP (Điểm bán hàng độc nhất) để tập trung quảng bá.

### Cách 91: Tạo dự báo doanh thu
**Công cụ:** ChatGPT (Data Analysis) | **Mức độ:** Trung bình

**Hướng dẫn:**
1. Kéo thả Excel doanh thu 6 tháng vào ChatGPT.
2. Lệnh: *"Dựa xu hướng 6 tháng, dự báo doanh thu 3 tháng tới, vẽ biểu đồ đường."*
3. Lưu biểu đồ kế hoạch nhập hàng.

**Ví dụ:** AI dùng mô hình hồi quy dự báo mùa cao điểm → không bao giờ nhập thiếu hàng.

---

## PHẦN 8: ĐỜI SỐNG CÁ NHÂN & GIA ĐÌNH (Cách 92–101)

*Cuộc sống gọn gàng, thú vị, khoa học hơn.*

### Cách 92: Lập thực đơn nấu ăn hàng tuần
**Công cụ:** ChatGPT / Gemini | **Mức độ:** Dễ

**Hướng dẫn:**
1. Xem tủ lạnh còn nguyên liệu gì.
2. Lệnh: *"Nhà có thịt bò, trứng, cà chua, rau cải. Muốn ăn lành mạnh, nấu không quá 30 phút. Lên thực đơn 5 ngày."*
3. Lưu thực đơn kèm công thức.

**Ví dụ:** Tạm biệt "Hôm nay ăn gì?" → AI đóng vai chuyên gia dinh dưỡng, ăn ngon không lãng phí.

### Cách 93: Tạo kế hoạch tập luyện cá nhân
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nêu thể trạng + dụng cụ có (VD: 2 quả tạ đơn).
2. Lệnh: *"Lịch tập gym tại nhà 4 ngày/tuần. Chia bài tập, sets, reps."*
3. Xem YouTube cách tập nếu chưa biết.

**Ví dụ:** PT cá nhân thiết kế giáo án riêng miễn phí thay vì mua gói tập đắt đỏ.

### Cách 94: Lập kế hoạch tài chính cá nhân
**Công cụ:** ChatGPT / Gemini | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cung cấp mức lương thực nhận.
2. Lệnh: *"Lương 15 triệu. Phân bổ theo 50/30/20 (Nhu cầu/Sở thích/Tiết kiệm). Gợi ý danh mục chi tiết."*
3. Áp dụng vào sổ chi tiêu.

**Ví dụ:** Quản lý dòng tiền, không "cuối tháng ăn mì tôm" vì tiêu xài quá tay.

### Cách 95: Tạo lịch du lịch thông minh
**Công cụ:** ChatGPT + Google Maps | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nêu điểm đến, số ngày, gu du lịch.
2. Lệnh: *"Lịch trình Đà Nẵng 3 ngày 2 đêm nhóm bạn trẻ. Chi tiết từng buổi, tối ưu đường di chuyển, gợi ý đặc sản."*
3. Tra cứu quán ăn trên Google Maps.

**Ví dụ:** AI sắp xếp điểm cùng cung đường → không đi vòng vèo tốn taxi, thời gian nghỉ ngơi hợp lý.

### Cách 96: Viết thiệp chúc mừng cá nhân hóa
**Công cụ:** ChatGPT | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cung cấp: tên người nhận, mối quan hệ, kỷ niệm vui.
2. Lệnh: *"Viết lời chúc sinh nhật hài hước nhưng tình cảm 5 câu cho bạn tên Vy. Nhắc kỷ niệm bị dầm mưa năm ngoái."*
3. Viết tay vào thiệp.

**Ví dụ:** Biến "Happy Birthday" nhạt nhẽo thành kỷ niệm đáng nhớ.

### Cách 97: Tạo playlist theo tâm trạng
**Công cụ:** ChatGPT + Spotify | **Mức độ:** Dễ

**Hướng dẫn:**
1. Mô tả cảm xúc: *"Ngồi cà phê một mình ngày mưa, hơi buồn."*
2. Lệnh: *"Gợi ý 10 bài Indie VN hoặc acoustic nhẹ nhàng phù hợp."*
3. Tạo playlist Spotify.

**Ví dụ:** Khám phá nghệ sĩ mới, bài hát "đúng người đúng thời điểm".

### Cách 98: Học kỹ năng mới với AI
**Công cụ:** ChatGPT / YouTube AI | **Mức độ:** Dễ

**Hướng dẫn:**
1. Nhập: *"Muốn học Guitar đệm hát từ con số 0."*
2. Lệnh: *"Chia lộ trình 30 ngày. Mỗi ngày luyện tập bước nào?"*
3. Bám sát lộ trình.

**Ví dụ:** Học bất cứ gì: đan len, thiết kế, ngoại ngữ → AI bẻ nhỏ kiến thức thành từng bước.

### Cách 99: Quản lý sức khỏe tâm lý
**Công cụ:** Wysa hoặc Replika | **Mức độ:** Dễ

**Hướng dẫn:**
1. Tải Wysa (chatbot tâm lý) về điện thoại.
2. Nhắn tin khi áp lực, lo âu, căng thẳng.
3. Thực hành bài tập hít thở, chánh niệm AI hướng dẫn.

**Ví dụ:** Đêm khuya không có ai tâm sự → AI lắng nghe không phán xét, xoa dịu cảm xúc.

### Cách 100: Tạo kế hoạch đọc sách
**Công cụ:** ChatGPT / Goodreads AI | **Mức độ:** Dễ

**Hướng dẫn:**
1. Cung cấp 3 cuốn sách từng thích.
2. Lệnh: *"Dựa gu này, gợi ý 5 sách phi hư cấu tiếp theo, kèm tóm tắt 1 câu."*
3. Lên lịch đọc 20 trang/ngày.

**Ví dụ:** AI hiểu chính xác gu đọc → đề xuất "ẩn mình" cực chất lượng.

### Cách 101: Tạo bucket list và mục tiêu
**Công cụ:** ChatGPT / Notion AI | **Mức độ:** Dễ

**Hướng dẫn:**
1. Mở Notion AI hoặc ChatGPT.
2. Lệnh: *"Tôi 25 tuổi thích trải nghiệm. Gợi ý 20 ý tưởng Bucket List thử thách bản thân."*
3. Chọn lọc, lưu vào sổ tay.

**Ví dụ:** Từ "Chạy bộ 10km" đến "Học lặn biển" → AI mở rộng trí tưởng tượng, tạo động lực sống.

---

## KẾT LUẬN

Cuốn ebook *"101 Cách Dùng AI Miễn Phí"* kết thúc tại đây, nhưng hành trình của bạn với Trí tuệ Nhân tạo mới chỉ thực sự bắt đầu.

**Giá trị cốt lõi** mà cuốn sách muốn truyền tải: AI hoàn toàn không phải phép thuật xa vời chỉ dành cho kỹ sư ở Thung lũng Silicon. Chúng ta đang sống trong thời đại công nghệ tối tân đã được "bình dân hóa" — ai cũng có thể dùng, ai cũng nên dùng, và quan trọng nhất: **miễn phí**.

Dù bạn đang chật vật với bài luận ở trường, đau đầu vì hồ sơ công ty, hay chỉ đơn giản tìm thực đơn nấu tối — luôn có trợ lý ảo sẵn sàng giải quyết trong tích tắc.

> **AI sẽ không cướp công việc của bạn. Nhưng người biết dùng AI sẽ làm việc nhanh hơn, sống nhàn hơn, và có nhiều thời gian hơn cho những giá trị đích thực.**

Đừng ngại ngùng. Mở máy tính lên, chọn một cách bất kỳ từ cẩm nang này, và bắt đầu trải nghiệm phép màu ngay hôm nay!

---

*© 2026 — 101 Cách Dùng AI Miễn Phí. Tạo bằng Hermes Agent + NotebookLM + Antigravity CLI.*
"""

output_path = EBOOK_DIR / "full-ebook.md"
output_path.write_text(content, encoding='utf-8')

# Stats
word_count = len(content.split())
char_count = len(content)
line_count = content.count('\n')

print(f"✅ Ebook saved to: {output_path}")
print(f"📊 Words: {word_count:,}")
print(f"📊 Characters: {char_count:,}")
print(f"📊 Lines: {line_count:,}")
