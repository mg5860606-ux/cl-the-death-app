import base64
import os

app_dir = r"C:\xereca017\.japa\workspace\cl_the_death_app"
bg_path = os.path.join(app_dir, "bg_morte.jpg")
audio_path = os.path.join(app_dir, "musica.opus")
out_html = os.path.join(app_dir, "index.html")

b64_bg = ""
if os.path.exists(bg_path):
    with open(bg_path, "rb") as f:
        b64_bg = base64.b64encode(f.read()).decode("utf-8")

b64_audio = ""
if os.path.exists(audio_path):
    with open(audio_path, "rb") as f:
        b64_audio = base64.b64encode(f.read()).decode("utf-8")

template = """<!--
==============================================================================
⚡ CRIADO POR: CORVO (MARCOS) ⚡
DESENVOLVIDO POR: JAPA IA // 2026
PROJETO: CL THE DEATH // O CAVALEIRO PÁLIDO
==============================================================================
-->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CL THE DEATH</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;900&family=Cinzel+Decorative:wght@700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: #050507;
    color: #e5e5e5;
    font-family: 'Inter', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
  }

  /* SPLASH SCREEN (O Cavaleiro Pálido) */
  #splash-screen {
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    background: #020202 url('data:image/jpeg;base64,__BG_IMG__') no-repeat center top;
    background-size: cover;
    z-index: 9999;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
    padding: 40px 20px 60px;
    transition: opacity 0.8s ease, visibility 0.8s ease;
  }
  #splash-screen::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 100%;
    background: linear-gradient(180deg, rgba(3,3,5,0.2) 0%, rgba(3,3,5,0.7) 60%, rgba(3,3,5,0.98) 100%);
    z-index: 1;
  }
  .splash-content {
    position: relative;
    z-index: 2;
    text-align: center;
    max-width: 420px;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 16px;
  }
  .skull-logo {
    width: 64px;
    height: 64px;
    margin-bottom: 4px;
    filter: drop-shadow(0 0 15px rgba(255,255,255,0.4));
  }
  .splash-title {
    font-family: 'Cinzel', serif;
    font-size: 2.2rem;
    font-weight: 900;
    letter-spacing: 5px;
    color: #ffffff;
    text-shadow: 0 0 20px rgba(255,255,255,0.3);
  }
  .splash-sub {
    font-size: 0.95rem;
    color: #a0a0a0;
    font-style: italic;
    letter-spacing: 1px;
    margin-bottom: 20px;
  }
  .btn-enter {
    background: rgba(138, 14, 26, 0.4);
    color: #ff334b;
    border: 1.5px solid #8a0e1a;
    padding: 16px 40px;
    font-family: 'Cinzel', serif;
    font-size: 1.1rem;
    font-weight: 700;
    letter-spacing: 4px;
    text-transform: uppercase;
    cursor: pointer;
    width: 100%;
    max-width: 280px;
    border-radius: 4px;
    transition: all 0.3s ease;
    box-shadow: 0 0 20px rgba(138, 14, 26, 0.3);
  }
  .btn-enter:hover {
    background: #8a0e1a;
    color: #fff;
    box-shadow: 0 0 35px rgba(255, 51, 75, 0.6);
    transform: translateY(-2px);
  }

  /* MAIN DASHBOARD */
  #main-dashboard {
    width: 100%;
    max-width: 480px;
    margin: 0 auto;
    min-height: 100vh;
    padding: 24px 16px 50px;
    display: flex;
    flex-direction: column;
    gap: 20px;
    opacity: 0;
    transform: translateY(15px);
    transition: opacity 0.8s ease, transform 0.8s ease;
  }
  #main-dashboard.active {
    opacity: 1;
    transform: translateY(0);
  }

  /* HEADER */
  .dash-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    padding-bottom: 12px;
    border-bottom: 1px solid #1a1520;
  }
  .dash-title-wrap {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .dash-title {
    font-family: 'Cinzel', serif;
    font-size: 1.6rem;
    font-weight: 900;
    letter-spacing: 3px;
    color: #fff;
  }
  .dash-hint {
    font-size: 0.8rem;
    color: #71717a;
  }
  .audio-btn {
    background: transparent;
    border: none;
    color: #a1a1aa;
    font-size: 1.4rem;
    cursor: pointer;
    padding: 6px;
    transition: color 0.2s;
  }
  .audio-btn:hover {
    color: #ff334b;
  }

  /* ADD NEW ITEM */
  .add-item-box {
    display: flex;
    gap: 10px;
  }
  .add-input {
    flex: 1;
    background: #0f0d14;
    border: 1px solid #272230;
    border-radius: 8px;
    padding: 12px 14px;
    color: #fff;
    font-family: inherit;
    font-size: 0.9rem;
    outline: none;
    transition: border-color 0.2s;
  }
  .add-input:focus {
    border-color: #8a0e1a;
  }
  .btn-add {
    background: #8a0e1a;
    border: none;
    border-radius: 8px;
    color: #fff;
    font-family: inherit;
    font-weight: 600;
    font-size: 0.9rem;
    padding: 0 18px;
    cursor: pointer;
    transition: background 0.2s;
  }
  .btn-add:hover {
    background: #b11322;
  }

  /* COUNTERS LIST */
  .counter-card {
    background: #0d0b12;
    border: 1px solid #1e1926;
    border-radius: 12px;
    padding: 16px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }
  .counter-top {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .counter-name {
    font-size: 0.95rem;
    font-weight: 600;
    color: #f4f4f5;
  }
  .counter-controls {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .btn-step {
    background: #181422;
    border: 1px solid #2d263b;
    color: #d4d4d8;
    width: 32px;
    height: 32px;
    border-radius: 6px;
    font-size: 1.1rem;
    font-weight: bold;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: all 0.2s;
  }
  .btn-step:hover {
    background: #8a0e1a;
    border-color: #8a0e1a;
    color: #fff;
  }
  .counter-val {
    font-family: 'Cinzel', serif;
    font-size: 1.3rem;
    font-weight: 700;
    min-width: 24px;
    text-align: center;
    color: #fff;
  }

  /* EXPANDABLE NAMES DROPDOWN */
  .names-toggle {
    font-size: 0.8rem;
    color: #a1a1aa;
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: 4px;
    user-select: none;
    transition: color 0.2s;
  }
  .names-toggle:hover {
    color: #e4e4e7;
  }
  .names-drawer {
    display: none;
    flex-direction: column;
    gap: 8px;
    padding-top: 8px;
    border-top: 1px solid #181422;
  }
  .names-drawer.open {
    display: flex;
  }
  .name-entry-row {
    display: flex;
    gap: 8px;
  }
  .name-input {
    flex: 1;
    background: #14101c;
    border: 1px solid #261f33;
    border-radius: 6px;
    padding: 6px 10px;
    color: #fff;
    font-size: 0.8rem;
    outline: none;
  }
  .btn-name-add {
    background: #1f192b;
    border: 1px solid #362c4a;
    color: #a1a1aa;
    border-radius: 6px;
    padding: 0 10px;
    font-size: 0.75rem;
    cursor: pointer;
  }
  .btn-name-add:hover {
    color: #fff;
    border-color: #8a0e1a;
  }
  .names-list {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  .name-tag {
    background: #181422;
    border: 1px solid #2d263b;
    color: #d4d4d8;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 0.75rem;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .name-tag span {
    cursor: pointer;
    color: #71717a;
  }
  .name-tag span:hover {
    color: #ff334b;
  }
</style>
</head>
<body>

  <!-- TELA INICIAL (SPLASH) -->
  <div id="splash-screen">
    <div class="splash-content">
      <svg class="skull-logo" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
        <path d="M12 2C7.58 2 4 5.58 4 10c0 2.5 1.15 4.73 2.95 6.22L7 20h10l.05-3.78C18.85 14.73 20 12.5 20 10c0-4.42-3.58-8-8-8z"/>
        <circle cx="9" cy="10" r="1.5" fill="#ffffff"/>
        <circle cx="15" cy="10" r="1.5" fill="#ffffff"/>
        <path d="M9 16h6"/>
        <path d="M10 16v3"/>
        <path d="M12 16v3"/>
        <path d="M14 16v3"/>
      </svg>
      <div class="splash-title">CL THE DEATH</div>
      <div class="splash-sub">"O Cavaleiro Pálido aguarda"</div>
      <button class="btn-enter" onclick="openDashboard()">ENTRAR</button>
    </div>
  </div>

  <!-- DASHBOARD PRINCIPAL -->
  <div id="main-dashboard">
    <div class="dash-header">
      <div class="dash-title-wrap">
        <div class="dash-title">CL THE DEATH</div>
        <div class="dash-hint">Toque em + ou – para registrar.</div>
      </div>
      <button id="audio-btn" class="audio-btn" onclick="toggleSound()">🔊</button>
    </div>

    <!-- CRIAR NOVO ITEM -->
    <div class="add-item-box">
      <input type="text" id="new-item-input" class="add-input" placeholder="Novo item..." onkeydown="if(event.key==='Enter') createItem()">
      <button class="btn-add" onclick="createItem()">Adicionar</button>
    </div>

    <!-- LISTA DE CONTADORES -->
    <div id="counters-container" style="display: flex; flex-direction: column; gap: 14px;">
      <!-- Itens gerados dinamicamente via JS -->
    </div>
  </div>

  <audio id="bg-music" loop preload="auto">
    <source src="data:audio/ogg;base64,__AUDIO_B64__" type="audio/ogg">
  </audio>

<script>
  const DEFAULT_ITEMS = [
    { id: 'grupos', name: 'Grupos derrubados', count: 0, names: [] },
    { id: 'numeros', name: 'Números derrubados', count: 0, names: [] },
    { id: 'aliancas', name: 'Alianças feitas', count: 0, names: [] },
    { id: 'membros', name: 'Quantidade de membros', count: 0, names: [] },
    { id: 'amigos', name: 'Quantidade de amigos do grupo', count: 0, names: [] }
  ];

  let items = [];

  function loadState() {
    const saved = localStorage.getItem('cl_counters_v2');
    if (saved) {
      try {
        items = JSON.parse(saved);
      } catch(e) {
        items = DEFAULT_ITEMS;
      }
    } else {
      items = DEFAULT_ITEMS;
    }
    renderCounters();
  }

  function saveState() {
    localStorage.setItem('cl_counters_v2', JSON.stringify(items));
  }

  function renderCounters() {
    const container = document.getElementById('counters-container');
    container.innerHTML = '';

    items.forEach((item, idx) => {
      const card = document.createElement('div');
      card.className = 'counter-card';
      card.innerHTML = `
        <div class="counter-top">
          <span class="counter-name">${item.name}</span>
          <div class="counter-controls">
            <button class="btn-step" onclick="changeCount(${idx}, -1)">–</button>
            <span class="counter-val">${item.count}</span>
            <button class="btn-step" onclick="changeCount(${idx}, 1)">+</button>
          </div>
        </div>
        <div class="names-toggle" onclick="toggleDrawer(${idx})">
          <span id="drawer-arrow-${idx}">▼</span> Nomes (${item.names.length})
        </div>
        <div id="drawer-${idx}" class="names-drawer">
          <div class="name-entry-row">
            <input type="text" id="name-input-${idx}" class="name-input" placeholder="Adicionar nome..." onkeydown="if(event.key==='Enter') addName(${idx})">
            <button class="btn-name-add" onclick="addName(${idx})">+</button>
          </div>
          <div class="names-list">
            ${item.names.map((n, nIdx) => `
              <div class="name-tag">
                ${n} <span onclick="removeName(${idx}, ${nIdx})">&times;</span>
              </div>
            `).join('')}
          </div>
        </div>
      `;
      container.appendChild(card);
    });
  }

  function changeCount(idx, delta) {
    items[idx].count = Math.max(0, items[idx].count + delta);
    saveState();
    renderCounters();
  }

  function toggleDrawer(idx) {
    const drawer = document.getElementById(`drawer-${idx}`);
    drawer.classList.toggle('open');
    const arrow = document.getElementById(`drawer-arrow-${idx}`);
    arrow.innerText = drawer.classList.contains('open') ? '▲' : '▼';
  }

  function addName(idx) {
    const input = document.getElementById(`name-input-${idx}`);
    const val = input.value.trim();
    if (val) {
      items[idx].names.push(val);
      saveState();
      renderCounters();
      setTimeout(() => {
        const d = document.getElementById(`drawer-${idx}`);
        if (d) d.classList.add('open');
      }, 50);
    }
  }

  function removeName(idx, nIdx) {
    items[idx].names.splice(nIdx, 1);
    saveState();
    renderCounters();
    setTimeout(() => {
      const d = document.getElementById(`drawer-${idx}`);
      if (d) d.classList.add('open');
    }, 50);
  }

  function createItem() {
    const input = document.getElementById('new-item-input');
    const name = input.value.trim();
    if (!name) return;
    items.push({
      id: 'custom_' + Date.now(),
      name: name,
      count: 0,
      names: []
    });
    input.value = '';
    saveState();
    renderCounters();
  }

  // Audio Controls
  const music = document.getElementById('bg-music');
  const audioBtn = document.getElementById('audio-btn');

  function openDashboard() {
    const splash = document.getElementById('splash-screen');
    const dash = document.getElementById('main-dashboard');

    splash.style.opacity = '0';
    setTimeout(() => { splash.style.display = 'none'; }, 800);
    dash.classList.add('active');

    music.play().catch(e => {
      console.log('Autoplay bloqueado:', e);
      audioBtn.innerText = '🔇';
    });
  }

  function toggleSound() {
    if (music.paused) {
      music.play();
      audioBtn.innerText = '🔊';
    } else {
      music.pause();
      audioBtn.innerText = '🔇';
    }
  }

  loadState();
</script>
</body>
</html>"""

html_final = template.replace("__BG_IMG__", b64_bg).replace("__AUDIO_B64__", b64_audio)

with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_final)

print("SUCESSO V2! Arquivo gerado em:", out_html, "Tamanho:", os.path.getsize(out_html))
