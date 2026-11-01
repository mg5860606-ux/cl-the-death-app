import base64
import os

app_dir = r"C:\xereca017\.japa\workspace\cl_the_death_app"
f1_path = os.path.join(app_dir, "foto1.jpg")
f2_path = os.path.join(app_dir, "foto2.webp")
audio_path = os.path.join(app_dir, "musica.opus")
out_html = os.path.join(app_dir, "index.html")

with open(f1_path, "rb") as f:
    b64_f1 = base64.b64encode(f.read()).decode("utf-8")

with open(f2_path, "rb") as f:
    b64_f2 = base64.b64encode(f.read()).decode("utf-8")

with open(audio_path, "rb") as f:
    b64_audio = base64.b64encode(f.read()).decode("utf-8")

template = """<!--
==============================================================================
⚡ CRIADO POR: CORVO (MARCOS) ⚡
DESENVOLVIDO POR: JAPA IA // 2026
PROJETO: CL THE DEATH // ORDEM ILLUMINATI
==============================================================================
-->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CL THE DEATH // ILLUMINATI</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: #030305;
    color: #e0e0e0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    overflow-x: hidden;
  }

  /* INTRO OVERLAY */
  #intro-screen {
    position: fixed;
    top: 0; left: 0; width: 100vw; height: 100vh;
    background: radial-gradient(circle, #100b1a 0%, #020203 100%);
    z-index: 9999;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    cursor: pointer;
    transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1);
  }
  .intro-symbol {
    width: 140px;
    height: 140px;
    margin-bottom: 25px;
    filter: drop-shadow(0 0 25px #00ffcc);
    animation: pulse 2.5s infinite alternate;
  }
  @keyframes pulse {
    0% { transform: scale(0.95); filter: drop-shadow(0 0 10px #7928ca); }
    100% { transform: scale(1.05); filter: drop-shadow(0 0 35px #00ffcc); }
  }
  .intro-btn {
    background: transparent;
    color: #00ffcc;
    border: 2px solid #00ffcc;
    padding: 16px 36px;
    font-size: 1.1rem;
    font-family: inherit;
    font-weight: bold;
    letter-spacing: 4px;
    text-transform: uppercase;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.3);
    cursor: pointer;
    border-radius: 4px;
    transition: 0.3s;
  }
  .intro-btn:hover {
    background: #00ffcc;
    color: #000;
    box-shadow: 0 0 40px #00ffcc;
  }

  /* MAIN APP */
  #main-app {
    width: 100%;
    max-width: 500px;
    min-height: 100vh;
    padding: 20px 16px 40px;
    display: flex;
    flex-direction: column;
    gap: 18px;
    opacity: 0;
    transform: translateY(20px);
    transition: opacity 0.8s ease, transform 0.8s ease;
  }
  #main-app.active {
    opacity: 1;
    transform: translateY(0);
  }

  /* HEADER */
  .brand-card {
    background: rgba(18, 14, 28, 0.85);
    border: 1px solid #7928ca;
    box-shadow: 0 0 25px rgba(121, 40, 202, 0.3);
    border-radius: 14px;
    padding: 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  .brand-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; width: 100%; height: 3px;
    background: linear-gradient(90deg, #00ffcc, #7928ca, #ff0055);
  }
  .brand-title {
    font-size: 1.8rem;
    font-weight: 900;
    letter-spacing: 3px;
    color: #fff;
    text-shadow: 0 0 10px #7928ca, 0 0 20px #00ffcc;
  }
  .brand-sub {
    color: #00ffcc;
    font-size: 0.85rem;
    letter-spacing: 2px;
    margin-top: 6px;
    text-transform: uppercase;
  }

  /* GALLERY CAROUSEL */
  .gallery-card {
    background: #09080e;
    border: 1px solid #231d33;
    border-radius: 14px;
    overflow: hidden;
    position: relative;
    box-shadow: 0 8px 30px rgba(0,0,0,0.8);
  }
  .gallery-img {
    width: 100%;
    height: 380px;
    object-fit: cover;
    display: block;
    transition: opacity 0.4s ease;
  }
  .gallery-nav {
    position: absolute;
    bottom: 12px;
    width: 100%;
    display: flex;
    justify-content: center;
    gap: 10px;
  }
  .gallery-dot {
    width: 12px; height: 12px;
    border-radius: 50%;
    background: rgba(255,255,255,0.3);
    cursor: pointer;
    border: 1px solid #000;
  }
  .gallery-dot.active {
    background: #00ffcc;
    box-shadow: 0 0 10px #00ffcc;
  }

  /* AUDIO CONTROLLER */
  .player-card {
    background: rgba(18, 14, 28, 0.9);
    border: 1px solid #00ffcc;
    border-radius: 12px;
    padding: 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
  }
  .player-info {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .track-name {
    color: #fff;
    font-weight: bold;
    font-size: 0.95rem;
    letter-spacing: 1px;
  }
  .track-status {
    color: #00ffcc;
    font-size: 0.75rem;
    letter-spacing: 1px;
  }
  .audio-toggle-btn {
    background: #00ffcc;
    color: #000;
    border: none;
    border-radius: 50%;
    width: 44px; height: 44px;
    font-size: 1.2rem;
    font-weight: bold;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 0 15px #00ffcc;
    transition: 0.2s;
  }
  .audio-toggle-btn:hover {
    transform: scale(1.08);
  }

  /* CONTADORES (LOCALSTORAGE) */
  .stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
  }
  .stat-card {
    background: #0c0916;
    border: 1px solid #7928ca;
    border-radius: 12px;
    padding: 16px;
    text-align: center;
    box-shadow: 0 0 15px rgba(121, 40, 202, 0.15);
  }
  .stat-val {
    font-size: 2rem;
    font-weight: 900;
    color: #fff;
    text-shadow: 0 0 10px #7928ca;
    margin-bottom: 4px;
  }
  .stat-lbl {
    font-size: 0.75rem;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 12px;
  }
  .stat-btn {
    background: transparent;
    border: 1px solid #7928ca;
    color: #00ffcc;
    padding: 8px 14px;
    font-family: inherit;
    font-size: 0.8rem;
    font-weight: bold;
    border-radius: 6px;
    cursor: pointer;
    transition: 0.2s;
    width: 100%;
  }
  .stat-btn:hover {
    background: #7928ca;
    color: #fff;
    box-shadow: 0 0 15px #7928ca;
  }

  /* FOOTER ASSINATURAS */
  .signatures-card {
    text-align: center;
    padding: 18px;
    border-top: 1px solid #1a1726;
    margin-top: 10px;
  }
  .sig-corvo {
    font-size: 1.05rem;
    font-weight: 900;
    color: #ff0055;
    letter-spacing: 2px;
    text-shadow: 0 0 15px rgba(255, 0, 85, 0.6);
    margin-bottom: 6px;
  }
  .sig-japa {
    font-size: 0.8rem;
    color: #777;
    letter-spacing: 1.5px;
  }
</style>
</head>
<body>

  <!-- TELA INICIAL -->
  <div id="intro-screen" onclick="enterApp()">
    <svg class="intro-symbol" viewBox="0 0 100 100">
      <polygon points="50,10 90,85 10,85" fill="none" stroke="#00ffcc" stroke-width="3" stroke-linejoin="round"/>
      <path d="M28,52 Q50,30 72,52 Q50,74 28,52 Z" fill="none" stroke="#7928ca" stroke-width="2.5"/>
      <circle cx="50" cy="52" r="7" fill="#00ffcc"/>
      <circle cx="50" cy="52" r="3" fill="#030305"/>
    </svg>
    <button class="intro-btn">INICIAR EXPERIÊNCIA</button>
  </div>

  <!-- APLICATIVO PRINCIPAL -->
  <div id="main-app">
    <div class="brand-card">
      <div class="brand-title">CL THE DEATH</div>
      <div class="brand-sub">ORDEM ILLUMINATI // ELITE</div>
    </div>

    <!-- CAROUSEL DE FOTOS -->
    <div class="gallery-card">
      <img id="gallery-view" class="gallery-img" src="data:image/jpeg;base64,__FOTO1__" alt="CL Photo">
      <div class="gallery-nav">
        <div class="gallery-dot active" onclick="setPhoto(0)"></div>
        <div class="gallery-dot" onclick="setPhoto(1)"></div>
      </div>
    </div>

    <!-- PLAYER DE ÁUDIO -->
    <div class="player-card">
      <div class="player-info">
        <div class="track-name">TRILHA DE COMBATE CL</div>
        <div id="track-status" class="track-status">REPRODUZINDO TRILHA</div>
      </div>
      <button id="play-btn" class="audio-toggle-btn" onclick="toggleAudio()">⏸</button>
    </div>

    <!-- CONTADORES -->
    <div class="stats-grid">
      <div class="stat-card">
        <div id="kills-val" class="stat-val">0</div>
        <div class="stat-lbl">Kills Computadas</div>
        <button class="stat-btn" onclick="addStat('kills')">+1 ALVO</button>
      </div>
      <div class="stat-card">
        <div id="respect-val" class="stat-val">0</div>
        <div class="stat-lbl">Respeito / Honra</div>
        <button class="stat-btn" onclick="addStat('respect')">+1 RESPEITO</button>
      </div>
    </div>
  </div>

  <audio id="bg-audio" loop preload="auto">
    <source src="data:audio/ogg;base64,__AUDIO__" type="audio/ogg">
  </audio>

<script>
  const photos = [
    'data:image/jpeg;base64,__FOTO1__',
    'data:image/webp;base64,__FOTO2__'
  ];
  let curPhoto = 0;

  function setPhoto(idx) {
    curPhoto = idx;
    const img = document.getElementById('gallery-view');
    img.style.opacity = '0';
    setTimeout(() => {
      img.src = photos[idx];
      img.style.opacity = '1';
    }, 200);
    const dots = document.querySelectorAll('.gallery-dot');
    dots.forEach((d, i) => d.classList.toggle('active', i === idx));
  }

  setInterval(() => {
    curPhoto = (curPhoto + 1) % photos.length;
    setPhoto(curPhoto);
  }, 4000);

  const audio = document.getElementById('bg-audio');
  const playBtn = document.getElementById('play-btn');
  const trackStatus = document.getElementById('track-status');

  function enterApp() {
    const intro = document.getElementById('intro-screen');
    const main = document.getElementById('main-app');
    
    intro.style.opacity = '0';
    setTimeout(() => { intro.style.display = 'none'; }, 800);
    main.classList.add('active');

    audio.play().catch(e => {
      console.log('Audio autoplay prevented:', e);
      trackStatus.innerText = 'CLIQUE NO PLAY';
      playBtn.innerText = '▶';
    });
  }

  function toggleAudio() {
    if (audio.paused) {
      audio.play();
      playBtn.innerText = '⏸';
      trackStatus.innerText = 'REPRODUZINDO TRILHA';
    } else {
      audio.pause();
      playBtn.innerText = '▶';
      trackStatus.innerText = 'PAUSADO';
    }
  }

  function loadStats() {
    const kills = localStorage.getItem('cl_kills') || 0;
    const respect = localStorage.getItem('cl_respect') || 0;
    document.getElementById('kills-val').innerText = kills;
    document.getElementById('respect-val').innerText = respect;
  }

  function addStat(type) {
    if (type === 'kills') {
      let val = parseInt(localStorage.getItem('cl_kills') || 0) + 1;
      localStorage.setItem('cl_kills', val);
      document.getElementById('kills-val').innerText = val;
    } else if (type === 'respect') {
      let val = parseInt(localStorage.getItem('cl_respect') || 0) + 1;
      localStorage.setItem('cl_respect', val);
      document.getElementById('respect-val').innerText = val;
    }
  }

  loadStats();
</script>
</body>
</html>"""

html_final = template.replace("__FOTO1__", b64_f1).replace("__FOTO2__", b64_f2).replace("__AUDIO__", b64_audio)

with open(out_html, "w", encoding="utf-8") as f:
    f.write(html_final)

print("SUCESSO! Arquivo gerado em:", out_html, "Tamanho:", os.path.getsize(out_html))
