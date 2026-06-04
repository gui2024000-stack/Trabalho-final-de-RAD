'use strict';
const canvas = document.getElementById('jogo');
const ctx = canvas.getContext('2d');
const margem = 30;
const pista = {
  x: margem,
  y: 0,
  w: canvas.width - margem * 2,
  h: canvas.height
};
const carro = {
  w: 40,
  h: 70,
  x: 0,
  y: 0,
  vel: 360,
  cor: '#22d3ee'
};
const obstaculos = [];
let faixaOffset = 0;
let pontos = 0;
let recorde = Number(localStorage.getItem('recorde_corrida') || 0);
let nivel = 1;
let velBase = 220;

let spawnMin = 0.45;
let spawnMax = 1.0;
let spawnTimer = 0.6;
const teclas = { esquerda: false, direita: false };
let estado = 'menu';
let ultimoTempo = 0;
function aleatorio(min, max) { return Math.random() * (max - min) + min; }
function clamp(v, a, b) { return Math.max(a, Math.min(b,v)); }
function retangulosColidem(a, b) {
  return !(a.x + a.w < b.x || a.x > b.x + b.w || a.y + a.h < b.y || a.y > b.y + b.h);
}
function iniciar() {
  carro.x = pista.x + pista.w / 2 - carro.w / 2;
  carro.y = pista.h - carro.h - 16;
  obstaculos.length = 0;
  faixaOffset = 0;
  pontos = 0;
  nivel = 1;
  velBase = 220;
  spawnTimer = 0.6;
  estado = 'jogando';
}
function criarObstaculos() {
  const faixas = 3;
  const larguraFaixa = pista.w / faixas;
  const faixaEscolhida = Math.floor(Math.random() * faixas);
  const baseW = 44;
  const w = clamp(baseW + Math.floor(aleatorio(-4, 8) * nivel * 0.1), 36, 58);
  const h = 70;
  const x = pista.x + faixaEscolhida * larguraFaixa + larguraFaixa / 2 - w / 2;
  const y = -h;
  obstaculos.push({ x, y, w, h, cor: '#ef4444' });
}
function atualizar(dt) {
  if (teclas.esquerda) carro.x -= carro.vel * dt;
  if (teclas.direita) carro.x += carro.vel * dt;
  carro.x = clamp(carro.x, pista.x + 8, pista.x + pista.w - carro.w - 8);
  const alturaMarca = 30;
  faixaOffset += (velBase + pontos * 0.35) * dt;
  if (faixaOffset > alturaMarca * 2) faixaOffset = 0;
  velBase += 6 * dt;
  nivel = 1 + Math.floor(pontos / 150);
  spawnTimer -= dt;
  if (spawnTimer <= 0) {
        criarObstaculos();
        if (nivel >= 3 && Math.random() < 0.25) criarObstaculos();
        const dificuldade = Math.max(0.22, spawnMin - pontos * 0.0015);
        spawnTimer = aleatorio(dificuldade, dificuldade + 0.55);
    }
for (let i = obstaculos.length - 1; i >= 0; i--) {
    const o = obstaculos[i];
    o.y += (velBase + pontos * 0.22 + nivel * 6) * dt;
    if (retangulosColidem({ x: carro.x, y: carro.y, w: carro.w, h: carro.h }, o)) {
        estado = 'fim';
        recorde = Math.max(recorde, Math.floor(pontos));
        localStorage.setItem('recorde_corrida', recorde);
    }
    if (o.y > canvas.height) {
      obstaculos.splice(i, 1);
      pontos += 12;
    }
  }
}
function desenhar() {
  ctx.fillStyle = '#1f2937';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = '#065f46';
  ctx.fillRect(0, 0, pista.x, canvas.height);
  ctx.fillRect(pista.x + pista.w, 0, pista.x, canvas.height);
  ctx.fillStyle = '#d1d5db';
  ctx.fillRect(pista.x + 4,0, 4, canvas.height);
  ctx.fillRect(pista.x + pista.w - 8, 0, 4, canvas.height);
  ctx.fillStyle = '#e5e7eb';
  const faixas = 3;
  const larguraFaixa = pista.w / faixas;
  const alturaMarca = 30;
  for (let i = 1; i < faixas; i++) {
    const x = pista.x + i * larguraFaixa - 2;
    for (let y = -alturaMarca; y < canvas.height + alturaMarca; y += alturaMarca * 2) {
      ctx.fillRect(x, y + faixaOffset, 4, alturaMarca);
    }
  }
ctx.fillStyle = carro.cor;
ctx.fillRect(carro.x, carro.y, carro.w, carro.h);
ctx.fillStyle = '#0ea5e9';
ctx.fillRect(carro.x + 6, carro.y + 8, carro.w - 12, 10);
ctx.fillRect(carro.x + 6, carro.y + carro.h - 18, carro.w - 12, 10);
for (const o of obstaculos) {
  ctx.fillStyle = o.cor;
  ctx.fillRect(o.x, o.y, o.w, o.h);
  ctx.fillStyle = '#991b1b';
  ctx.fillRect(o.x + 6, o.y + 8, o.w - 12, 10);
  ctx.fillRect(o.x + 6, o.y + o.h - 18, o.w - 12, 10);
}
ctx.fillStyle = '#ffffff';
ctx.font = '16px system-ui, Arial';
ctx.fillText('Pontos: ' + Math.floor(pontos), pista.x + 10, 24);
ctx.fillText('Recoede: ' + recorde, pista.x + pista.w - 120, 24);
ctx.fillText('Nível: ' + nivel, pista.x + 10, 44);
if (estado === 'menu') {
  ctx.fillStyle = 'rgba(0,0,0,0.6)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = '#ffffff';
  ctx.textAlign = 'center';
  ctx.font = '22px system-ui, Arial';
  ctx.fillText('Corrida Didática', canvas.width / 2, canvas.height / 2 - 40);
  ctx.font = '16px system-ui, Arial';
  ctx.fillText('Setas ou A e D para mover', canvas.width / 2, canvas.height / 2);
  ctx.fillText('Pressione Enter para começar', canvas.width / 2, canvas.height / 2 + 28);
  ctx.textAlign = 'left';
}
if (estado === 'fim') {
  ctx.fillStyle = 'rgba(0,0,0,0.6)';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = '#ffffff';
  ctx.textAlign = 'center';
  ctx.font = '22px system-ui, Arial';
  ctx.fillText('Colisão. Jogo encerrado.', canvas.width / 2, canvas.height / 2 - 20);
  ctx.font = '16px system-ui, Arial';
  ctx.fillText('Pontos: ' + Math.floor(pontos) + '    Recorde: ' + recorde, canvas.width / 2, canvas.height / 2 + 10);
  ctx.fillText('Pressione Enter para reiniciar', canvas.width / 2, canvas.height / 2 + 36);
  ctx.textAlign = 'left';
}
}
function loop(tempoAgora) {
  const dt = Math.min(0.33, (tempoAgora - ultimoTempo) / 1000 || 0);
  ultimoTempo = tempoAgora;
  if (estado === 'jogando') atualizar(dt);
  desenhar();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
window.addEventListener('keydown', (e) => {
  if (['ArrowLeft','ArrowRight','Space'].includes(e.key)) e.preventDefault();
  if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') teclas.esquerda = true;
  if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') teclas.direita = true;
  if (e.key === 'Enter' && estado !== 'jogando') iniciar();
});
window.addEventListener('keyup', (e) => {
    if (e.key === 'ArrowLeft' || e.key.toLowerCase() === 'a') teclas.esquerda = false;
    if (e.key === 'ArrowRight' || e.key.toLowerCase() === 'd') teclas.direita = false;
  });