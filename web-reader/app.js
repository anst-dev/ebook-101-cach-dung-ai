// Đảm bảo Marked.js đã được cấu hình an toàn
marked.setOptions({
  gfm: true,
  breaks: true,
  headerIds: true
});

// Trạng thái ứng dụng
const state = {
  currentChapterIndex: 0,
  theme: 'light',
  fontSize: 18,
  fontFamily: 'sans',
  sidebarOpen: false,
  settingsOpen: false,
  tocDrawerOpen: false,
  searchQuery: ''
};

// Các phần tử DOM chính
const DOM = {
  body: document.body,
  chapterList: document.getElementById('chapters-list'),
  readerContent: document.getElementById('reader-content'),
  prevBtn: document.getElementById('prev-btn'),
  nextBtn: document.getElementById('next-btn'),
  progressBar: document.getElementById('progress-bar'),
  readerContainer: document.getElementById('reader-container'),
  sidebar: document.getElementById('sidebar'),
  sidebarToggle: document.getElementById('sidebar-toggle'),
  settingsToggle: document.getElementById('settings-toggle'),
  settingsPanel: document.getElementById('settings-panel'),
  overlay: document.getElementById('overlay'),
  
  // Font/Theme controls
  themeBtns: document.querySelectorAll('.theme-btn'),
  fontBtns: document.querySelectorAll('.font-btn'),
  fontSizeDec: document.getElementById('font-size-dec'),
  fontSizeInc: document.getElementById('font-size-inc'),
  fontSizeVal: document.getElementById('font-size-val'),
  
  // Search
  searchInput: document.getElementById('search-input'),
  
  // Quick TOC
  tocTrigger: document.getElementById('toc-trigger'),
  tocDrawer: document.getElementById('toc-drawer'),
  tocDrawerClose: document.getElementById('toc-drawer-close'),
  tocDrawerList: document.getElementById('toc-drawer-list')
};

// --- Khởi tạo ứng dụng ---
function init() {
  loadSettings();
  renderSidebar();
  setupEventListeners();
  
  // Load chương đầu tiên (hoặc chương đã lưu)
  const savedChapterId = localStorage.getItem('saved_chapter_id');
  if (savedChapterId) {
    const idx = EBOOK_DATA.chapters.findIndex(ch => ch.id === savedChapterId);
    if (idx !== -1) {
      state.currentChapterIndex = idx;
    }
  }
  
  loadChapter(state.currentChapterIndex, true);
  
  // Đồng bộ giao diện
  updateThemeUI();
  updateFontUI();
  updateFontSizeUI();
}

// --- Cài đặt & Trạng thái ---
function loadSettings() {
  state.theme = localStorage.getItem('reader_theme') || 'light';
  state.fontSize = parseInt(localStorage.getItem('reader_font_size')) || 18;
  state.fontFamily = localStorage.getItem('reader_font_family') || 'sans';
}

function saveSettings() {
  localStorage.setItem('reader_theme', state.theme);
  localStorage.setItem('reader_font_size', state.fontSize);
  localStorage.setItem('reader_font_family', state.fontFamily);
}

function updateThemeUI() {
  DOM.body.setAttribute('data-theme', state.theme);
  DOM.themeBtns.forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-val') === state.theme);
  });
}

function updateFontUI() {
  DOM.body.setAttribute('data-font', state.fontFamily);
  DOM.fontBtns.forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-val') === state.fontFamily);
  });
}

function updateFontSizeUI() {
  DOM.body.style.setProperty('--font-size', `${state.fontSize}px`);
  DOM.fontSizeVal.textContent = `${state.fontSize}px`;
}

// --- Render Sidebar ---
function renderSidebar(filteredChapters = null) {
  const chaptersToRender = filteredChapters || EBOOK_DATA.chapters;
  DOM.chapterList.innerHTML = '';
  
  if (chaptersToRender.length === 0) {
    DOM.chapterList.innerHTML = `
      <div style="padding: 2rem; text-align: center; color: var(--text-secondary); font-size: 0.9rem;">
        Không tìm thấy chương nào phù hợp.
      </div>
    `;
    return;
  }
  
  chaptersToRender.forEach(ch => {
    // Tìm index thực tế trong EBOOK_DATA
    const actualIndex = EBOOK_DATA.chapters.findIndex(orig => orig.id === ch.id);
    const isActive = actualIndex === state.currentChapterIndex;
    
    // Đếm số lượng "Cách" trong chương này
    const waysCount = (ch.content.match(/### Cách \d+/g) || []).length;
    let subtitle = '';
    if (ch.id === 'intro') subtitle = 'Giới thiệu & hướng dẫn';
    else if (ch.id === 'conclusion') subtitle = 'Lời kết cuốn sách';
    else if (waysCount > 0) subtitle = `${waysCount} cách ứng dụng AI`;
    
    const item = document.createElement('div');
    item.className = `chapter-item ${isActive ? 'active' : ''}`;
    item.innerHTML = `
      <span class="chapter-title">${ch.title}</span>
      <span class="chapter-subtitle">${subtitle}</span>
    `;
    
    item.addEventListener('click', () => {
      loadChapter(actualIndex);
      if (window.innerWidth < 1024) {
        closeSidebar();
      }
    });
    
    DOM.chapterList.appendChild(item);
  });
}

// --- Tải & hiển thị chương ---
function loadChapter(index, isFirstLoad = false) {
  if (index < 0 || index >= EBOOK_DATA.chapters.length) return;
  
  state.currentChapterIndex = index;
  const chapter = EBOOK_DATA.chapters[index];
  
  // Lưu chương hiện tại
  localStorage.setItem('saved_chapter_id', chapter.id);
  
  // Render Markdown sang HTML
  // Đổi dấu tiêu đề từ markdown sang HTML
  DOM.readerContent.innerHTML = marked.parse(chapter.content);
  
  // Post-processing: Trang trí các tiêu đề Cách
  decorateChapters();
  
  // Build Quick TOC (Drawer di động)
  buildQuickTOC(chapter);
  
  // Cập nhật trạng thái Active trong Sidebar
  const items = DOM.chapterList.querySelectorAll('.chapter-item');
  items.forEach((item, idx) => {
    // Chỉ active nếu index khớp với index thực tế
    item.classList.toggle('active', idx === index);
  });
  
  // Cuộn trang về đầu (hoặc vị trí cũ nếu là First Load)
  if (isFirstLoad) {
    const savedScroll = parseFloat(localStorage.getItem(`scroll_${chapter.id}`)) || 0;
    setTimeout(() => {
      const scrollHeight = DOM.readerContainer.scrollHeight - DOM.readerContainer.clientHeight;
      DOM.readerContainer.scrollTop = scrollHeight * savedScroll;
      updateProgressBar();
    }, 100);
  } else {
    DOM.readerContainer.scrollTop = 0;
    updateProgressBar();
  }
  
  // Cập nhật trạng thái nút Prev/Next
  DOM.prevBtn.disabled = index === 0;
  DOM.nextBtn.disabled = index === EBOOK_DATA.chapters.length - 1;
  
  // Đóng các drawer phụ
  closeSettings();
  closeTOCDrawer();
}

// Trang trí thêm class và icon cho đẹp trong HTML đã render
function decorateChapters() {
  // Tìm tất cả các tiêu đề h3
  const h3Elements = DOM.readerContent.querySelectorAll('h3');
  h3Elements.forEach(h3 => {
    const text = h3.textContent.trim();
    if (text.startsWith('Cách ')) {
      h3.id = text.toLowerCase().replace(/[^a-z0-9àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]/g, '-');
      // Thêm class css đặc biệt
      h3.classList.add('way-header');
      h3.innerHTML = `<span style="display:flex;align-items:center;gap:0.5rem;"><i data-lucide="sparkles" style="width:18px;height:18px"></i> ${text}</span>`;
    }
  });
  
  // Cập nhật các icon Lucide mới nếu được sinh ra
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
}

// Xây dựng Mục lục nhanh (TOC) của chương
function buildQuickTOC(chapter) {
  DOM.tocDrawerList.innerHTML = '';
  
  // Tìm tất cả dòng chứa "### Cách X:"
  const regex = /### (Cách \d+: .+)/g;
  let match;
  const ways = [];
  
  while ((match = regex.exec(chapter.content)) !== null) {
    ways.push(match[1]);
  }
  
  if (ways.length === 0) {
    DOM.tocTrigger.style.display = 'none';
    return;
  }
  
  DOM.tocTrigger.style.display = 'flex';
  
  ways.forEach(way => {
    const parts = way.split(':');
    const wayNum = parts[0].trim();
    const wayName = parts.slice(1).join(':').trim();
    
    const item = document.createElement('div');
    item.className = 'toc-drawer-item';
    item.innerHTML = `
      <strong style="color:var(--accent-color)">${wayNum}:</strong> ${wayName}
    `;
    
    item.addEventListener('click', () => {
      // Tìm phần tử h3 tương ứng và cuộn tới đó
      const targetId = wayNum.toLowerCase().replace(/[^a-z0-9àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ]/g, '-');
      const targetEl = document.getElementById(targetId);
      if (targetEl) {
        // Cuộn smooth trong main
        DOM.readerContainer.scrollTo({
          top: targetEl.offsetTop - 20,
          behavior: 'smooth'
        });
      }
      closeTOCDrawer();
    });
    
    DOM.tocDrawerList.appendChild(item);
  });
}

// Cập nhật thanh tiến trình đọc & lưu vị trí
function updateProgressBar() {
  const scrollTop = DOM.readerContainer.scrollTop;
  const scrollHeight = DOM.readerContainer.scrollHeight - DOM.readerContainer.clientHeight;
  
  let percentage = 0;
  if (scrollHeight > 0) {
    percentage = (scrollTop / scrollHeight) * 100;
  }
  
  DOM.progressBar.style.width = `${percentage}%`;
  
  // Lưu phần trăm cuộn của chương hiện tại
  const currentChapter = EBOOK_DATA.chapters[state.currentChapterIndex];
  if (currentChapter) {
    localStorage.setItem(`scroll_${currentChapter.id}`, scrollHeight > 0 ? (scrollTop / scrollHeight).toString() : '0');
  }
}

// --- Tìm kiếm ---
function handleSearch(e) {
  const query = e.target.value.toLowerCase().trim();
  state.searchQuery = query;
  
  if (!query) {
    renderSidebar();
    return;
  }
  
  // Tìm kiếm trong tiêu đề chương hoặc nội dung
  const filtered = EBOOK_DATA.chapters.filter(ch => {
    return ch.title.toLowerCase().includes(query) || ch.content.toLowerCase().includes(query);
  });
  
  renderSidebar(filtered);
}

// --- Toggle Panels & Menu ---
function openSidebar() {
  state.sidebarOpen = true;
  DOM.sidebar.classList.add('open');
  DOM.sidebarToggle.classList.add('active');
  if (window.innerWidth < 1024) {
    DOM.overlay.classList.add('active');
  }
}

function closeSidebar() {
  state.sidebarOpen = false;
  DOM.sidebar.classList.remove('open');
  DOM.sidebarToggle.classList.remove('active');
  DOM.overlay.classList.remove('active');
}

function toggleSidebar() {
  if (state.sidebarOpen) closeSidebar();
  else openSidebar();
}

function openSettings() {
  state.settingsOpen = true;
  DOM.settingsPanel.classList.add('open');
  DOM.settingsToggle.classList.add('active');
}

function closeSettings() {
  state.settingsOpen = false;
  DOM.settingsPanel.classList.remove('open');
  DOM.settingsToggle.classList.remove('active');
}

function toggleSettings() {
  if (state.settingsOpen) closeSettings();
  else openSettings();
}

function openTOCDrawer() {
  state.tocDrawerOpen = true;
  DOM.tocDrawer.classList.add('open');
  DOM.overlay.classList.add('active');
}

function closeTOCDrawer() {
  state.tocDrawerOpen = false;
  DOM.tocDrawer.classList.remove('open');
  // Chỉ đóng overlay nếu sidebar cũng đóng
  if (!state.sidebarOpen) {
    DOM.overlay.classList.remove('active');
  }
}

// --- Xử lý Sự kiện ---
function setupEventListeners() {
  // Cuộn trang
  DOM.readerContainer.addEventListener('scroll', updateProgressBar);
  
  // Navigation
  DOM.prevBtn.addEventListener('click', () => loadChapter(state.currentChapterIndex - 1));
  DOM.nextBtn.addEventListener('click', () => loadChapter(state.currentChapterIndex + 1));
  
  // Sidebar & Settings toggle
  DOM.sidebarToggle.addEventListener('click', toggleSidebar);
  DOM.settingsToggle.addEventListener('click', toggleSettings);
  
  // Nút đóng overlay (ở điện thoại)
  DOM.overlay.addEventListener('click', () => {
    closeSidebar();
    closeTOCDrawer();
  });
  
  // Thay đổi cài đặt Theme
  DOM.themeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      state.theme = btn.getAttribute('data-val');
      updateThemeUI();
      saveSettings();
    });
  });
  
  // Thay đổi cài đặt Font
  DOM.fontBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      state.fontFamily = btn.getAttribute('data-val');
      updateFontUI();
      saveSettings();
    });
  });
  
  // Cỡ chữ
  DOM.fontSizeDec.addEventListener('click', () => {
    if (state.fontSize > 14) {
      state.fontSize -= 1;
      updateFontSizeUI();
      saveSettings();
    }
  });
  
  DOM.fontSizeInc.addEventListener('click', () => {
    if (state.fontSize < 28) {
      state.fontSize += 1;
      updateFontSizeUI();
      saveSettings();
    }
  });
  
  // Tìm kiếm
  DOM.searchInput.addEventListener('input', handleSearch);
  
  // Quick TOC
  DOM.tocTrigger.addEventListener('click', openTOCDrawer);
  DOM.tocDrawerClose.addEventListener('click', closeTOCDrawer);
  
  // Close popups on click outside
  document.addEventListener('click', (e) => {
    if (!DOM.settingsPanel.contains(e.target) && !DOM.settingsToggle.contains(e.target)) {
      closeSettings();
    }
  });
}

// Khởi chạy khi tài liệu sẵn sàng
document.addEventListener('DOMContentLoaded', () => {
  init();
  // Khởi tạo lucide icons
  if (typeof lucide !== 'undefined') {
    lucide.createIcons();
  }
});
