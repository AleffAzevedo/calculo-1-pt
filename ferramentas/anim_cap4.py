# -*- coding: utf-8 -*-
"""Animações das soluções completas do capítulo 4."""
import numpy as np
import matplotlib.pyplot as plt
from anim_base import *


def a_escada(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8, 4))
    ts = np.linspace(0, 9.2, 70); x = lambda t: 0.2 + 0.5 * t
    a1.set_xlim(-0.6, 5.6); a1.set_ylim(-0.6, 5.6); a1.set_aspect('equal'); a1.axis('off')
    a1.fill_between([-0.4, 0], 0, 5.4, color=CINZA, alpha=0.3); a1.plot([0, 0], [0, 5.4], 'w'); a1.plot([0, 5.5], [0, 0], 'w')
    esc, = a1.plot([], [], color=AZUL, lw=4); t1 = a1.text(1.2, 5.3, '', fontsize=9)
    a2.set_xlim(0, 5); a2.set_ylim(0, 2.5); a2.grid(alpha=0.3); a2.set_xlabel('x (m)'); a2.set_title('rapidez do topo |dy/dt| (m/s)')
    a2.axhline(0.5, ls='--', color=CINZA); a2.text(0.2, 0.55, 'rapidez da base', fontsize=8, color=CINZA)
    tr, = a2.plot([], [], color=LARANJA, lw=2); fig.tight_layout()
    xs, vs = [], []
    def up(i):
        X = x(ts[i]); Y = np.sqrt(max(25 - X ** 2, 1e-6)); v = 0.5 * X / Y
        esc.set_data([0, X], [Y, 0]); t1.set_text(f'x={X:.2f}  y={Y:.2f}  dy/dt={-v:.3f}'.replace('.', ','))
        xs.append(X); vs.append(min(v, 3)); tr.set_data(xs, vs)
    salvar(fig, up, len(ts), path)


def a_sombra(path):
    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    ax.set_xlim(-0.5, 16); ax.set_ylim(-0.3, 6.6); ax.set_aspect('equal'); ax.axis('off')
    ax.plot([0, 0], [0, 6], color=TINTA, lw=3); ax.plot([0], [6], 'o', color='#E8A33D', ms=12); ax.plot([-0.5, 16], [0, 0], 'w')
    pes, = ax.plot([], [], color=AZUL, lw=5); som, = ax.plot([], [], color=LARANJA, lw=5, alpha=0.7)
    raio, = ax.plot([], [], ':', color='#E8A33D'); txt = ax.text(6, 5.5, '', fontsize=10)
    ts = np.linspace(0, 6, 60)
    def up(i):
        X = 1 + 1.5 * ts[i]; s = 3 * X / 7
        pes.set_data([X, X], [0, 1.8]); som.set_data([X, X + s], [0, 0]); raio.set_data([0, X + s], [6, 0])
        txt.set_text(f'x = {X:.1f} m   sombra = {s:.2f} m'.replace('.', ','))
    salvar(fig, up, len(ts), path)


def a_aviao(path):
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.4), gridspec_kw={'height_ratios': [1.1, 1]})
    a1.set_xlim(-12, 12); a1.set_ylim(-0.5, 5.5); a1.set_aspect('equal'); a1.axis('off'); a1.plot([-12, 12], [0, 0], 'w')
    a1.plot([0], [0], '^', color=TINTA, ms=10); av, = a1.plot([], [], '>', color=AZUL, ms=12); lin, = a1.plot([], [], '--', color=LARANJA)
    eixos(a2, (-10, 10), (-700, 700)); a2.set_xlabel('x (km)'); a2.set_title("D'(x) = 600·x/√(x²+16)  (km/h)")
    xx = np.linspace(-10, 10, 300); a2.plot(xx, 600 * xx / np.sqrt(xx ** 2 + 16), color=CINZA, lw=1, ls=':')
    a2.plot([3], [360], 'o', color=VERDE); a2.annotate('360 km/h em x = 3', (3, 360), (4.5, 150), arrowprops=dict(arrowstyle='->'), fontsize=9)
    tr, = a2.plot([], [], color=LARANJA, lw=2); fig.tight_layout()
    X = np.linspace(-10, 10, 70)
    def up(i):
        x = X[i]; av.set_data([x], [4]); lin.set_data([0, x], [0, 4])
        tr.set_data(X[:i + 1], 600 * X[:i + 1] / np.sqrt(X[:i + 1] ** 2 + 16))
    salvar(fig, up, len(X), path)


def a_extremos(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); eixos(ax, (-0.2, 4.2), (-0.1, 0.5))
    xx = np.linspace(0, 4, 300); f = xx * np.exp(-xx); ax.plot(xx, f, color=AZUL, lw=2); ax.set_title(r'$f(x)=x\,e^{-x}$ em $[0,4]$')
    hl, = ax.plot([], [], color=LARANJA, lw=1.5); N = 60
    ys = np.concatenate([np.linspace(0.48, 1 / np.e, 30), np.linspace(-0.08, 0, 30)])
    def up(i):
        y = ys[i]; hl.set_data([0, 4], [y, y])
        if i == 29: ax.plot([1], [1 / np.e], 'o', color=VERDE, ms=8); ax.text(1.1, 0.39, 'máx. absoluto 1/e', color=VERDE)
        if i == N - 1: ax.plot([0], [0], 'o', color=VERDE, ms=8); ax.text(0.1, 0.02, 'mín. absoluto 0', color=VERDE)
    salvar(fig, up, N, path)


def a_tvm(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); eixos(ax, (-0.3, 2.3), (-1, 7))
    f = lambda x: x ** 3 - x; xx = np.linspace(-0.3, 2.3, 300)
    ax.plot(xx, f(xx), color=AZUL, lw=2); ax.plot([0, 2], [0, 6], color=LARANJA, lw=1.5); ax.plot([0, 2], [0, 6], 'o', color=LARANJA)
    c0 = 2 / np.sqrt(3); xs = np.concatenate([np.linspace(0.1, c0, 45)])
    tan, = ax.plot([], [], lw=1.6); p, = ax.plot([], [], 'o'); tt = ax.set_title('')
    def up(i):
        a = xs[i]; m = 3 * a ** 2 - 1; ok = abs(a - c0) < 1e-9; c = VERDE if ok else CINZA
        tan.set_data(xx, f(a) + m * (xx - a)); tan.set_color(c); p.set_data([a], [f(a)]); p.set_color(c)
        tt.set_text(f"c = {a:.3f}: f'(c) = {m:.2f}  (secante: 3)".replace('.', ',') + ('  ✔' if ok else ''))
    salvar(fig, up, len(xs), path)


def a_lhopital_e(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); ax.set_xscale('log'); ax.set_xlim(0.8, 2e4); ax.set_ylim(1.8, 2.9); ax.grid(alpha=0.3)
    ax.axhline(np.e, ls='--', color=LARANJA); ax.text(1, 2.75, 'y = e ≈ 2,71828', color=LARANJA)
    xx = np.geomspace(1, 2e4, 400); l, = ax.plot([], [], color=AZUL, lw=2); ax.set_title(r'$(1+1/x)^x$')
    pts = [1, 10, 100, 1000, 10000]; N = 60; tx = []
    def up(i):
        k = int(len(xx) * (i + 1) / N); l.set_data(xx[:k], (1 + 1 / xx[:k]) ** xx[:k])
        for p in pts:
            if xx[k - 1] >= p and p not in tx:
                tx.append(p); v = (1 + 1 / p) ** p; ax.plot([p], [v], 'o', color=VERDE)
                ax.annotate(f'{v:.5f}'.replace('.', ','), (p, v), (p * 0.7, v - 0.12), fontsize=8)
    salvar(fig, up, N, path)


def a_esboco(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); eixos(ax, (-6, 6), (-0.8, 0.8))
    f = lambda x: x / (x ** 2 + 1); xx = np.linspace(-6, 6, 400); N = 60; ax.set_title(r'$f(x)=x/(x^2+1)$')
    l, = ax.plot([], [], color=AZUL, lw=2)
    def up(i):
        if i == 5: ax.axhline(0, color=LARANJA, ls='--'); ax.text(3.5, 0.05, 'assíntota y = 0', color=LARANJA, fontsize=9)
        if i == 15:
            ax.plot([1, -1], [0.5, -0.5], 'wo'); ax.text(1.1, 0.55, 'máx (1, 1/2)', fontsize=9); ax.text(-3.4, -0.6, 'mín (−1, −1/2)', fontsize=9)
        if i == 25:
            r3 = np.sqrt(3)
            ax.plot([0, r3, -r3], [0, f(r3), f(-r3)], 'o', color=VERDE); ax.text(r3 + 0.1, f(r3) - 0.1, 'inflexão', color=VERDE, fontsize=9)
        if i >= 30:
            k = int(len(xx) * (i - 29) / (N - 30)); l.set_data(xx[:k], f(xx[:k]))
    salvar(fig, up, N, path)


def a_cerca(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 3.8))
    A = lambda x: x * (600 - 3 * x); xs = np.concatenate([np.linspace(20, 180, 40), np.linspace(180, 100, 25)])
    a2.set_xlim(0, 200); a2.set_ylim(0, 33000); a2.grid(alpha=0.3); a2.set_xlabel('x (m)'); a2.set_title('A(x) = x(600 − 3x)')
    xx = np.linspace(0, 200, 200); a2.plot(xx, A(xx), color=CINZA, ls=':'); p, = a2.plot([], [], 'o', color=LARANJA)
    fig.tight_layout(); tt = a1.set_title('')
    def up(i):
        x = xs[i]; y = 600 - 3 * x; a1.cla(); a1.set_xlim(-20, 620); a1.set_ylim(-60, 220); a1.set_aspect('equal'); a1.axis('off')
        a1.fill_between([-20, 620], 0, -50, color='#9EC5E8'); a1.text(250, -40, 'rio', fontsize=9)
        a1.plot([0, 0, y, y], [0, x, x, 0], color=AZUL, lw=2); a1.plot([y / 2, y / 2], [0, x], color=AZUL, lw=2)
        a1.set_title(f'x = {x:.0f} m, y = {y:.0f} m, A = {A(x):,.0f} m²'.replace(',', '.'), fontsize=9)
        p.set_data([x], [A(x)])
    salvar(fig, up, len(xs), path)


def a_proximo(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 3.9))
    eixos(a1, (-2.6, 2.6), (-0.3, 5)); a1.set_aspect('equal')
    xx = np.linspace(-2.3, 2.3, 300); a1.plot(xx, xx ** 2, color=AZUL, lw=2); a1.plot([0], [3], 'ws')
    seg, = a1.plot([], [], color=LARANJA); pt, = a1.plot([], [], 'o', color=LARANJA)
    d = lambda x: np.sqrt(x ** 2 + (x ** 2 - 3) ** 2)
    eixos(a2, (-2.3, 2.3), (0, 3.5)); a2.plot(xx, d(xx), color=CINZA, ls=':'); a2.set_title('distância d(x)')
    q, = a2.plot([], [], 'o', color=LARANJA); fig.tight_layout()
    xs = np.linspace(-2.2, 2.2, 70); r = np.sqrt(2.5)
    a1.plot([r, -r], [2.5, 2.5], 'o', color=VERDE); a2.plot([r, -r], [d(r), d(r)], 'o', color=VERDE)
    def up(i):
        x = xs[i]; seg.set_data([0, x], [3, x ** 2]); pt.set_data([x], [x ** 2]); q.set_data([x], [d(x)])
    salvar(fig, up, len(xs), path)


def a_cabo(path):
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.2), gridspec_kw={'height_ratios': [1, 1.3]})
    a1.set_xlim(-0.3, 3.4); a1.set_ylim(-0.3, 1.4); a1.set_aspect('equal'); a1.axis('off')
    a1.fill_between([-0.3, 3.4], 0, 1, color='#9EC5E8', alpha=0.6); a1.plot([0], [0], 'ws'); a1.plot([3], [1], 'w^', ms=9)
    a1.text(-0.25, -0.25, 'usina', fontsize=8); a1.text(2.8, 1.12, 'fábrica', fontsize=8)
    agua, = a1.plot([], [], color=LARANJA, lw=2); terra, = a1.plot([], [], color=AZUL, lw=2)
    C = lambda x: 5 * np.sqrt(1 + x ** 2) + 4 * (3 - x)
    eixos(a2, (0, 3), (14, 17.5)); xx = np.linspace(0, 3, 200); a2.plot(xx, C(xx), color=CINZA, ls=':'); a2.set_xlabel('x (km)'); a2.set_title('custo C(x) (mil R$)')
    q, = a2.plot([], [], 'o', color=LARANJA); fig.tight_layout()
    xs = np.concatenate([np.linspace(0, 3, 45), np.linspace(3, 4 / 3, 25)])
    def up(i):
        x = xs[i]; agua.set_data([0, x], [0, 1]); terra.set_data([x, 3], [1, 1]); q.set_data([x], [C(x)])
        if i == len(xs) - 1: q.set_color(VERDE); a2.annotate('mínimo: x = 4/3, C = 15', (4 / 3, 15), (1.7, 16.3), arrowprops=dict(arrowstyle='->'), fontsize=9)
    salvar(fig, up, len(xs), path)


def a_newton(path):
    f = lambda x: np.cos(x) - x; df = lambda x: -np.sin(x) - 1
    xs = [1.0]
    for _ in range(4): xs.append(xs[-1] - f(xs[-1]) / df(xs[-1]))
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); N = 4 * 12
    def up(i):
        k = min(i // 12, 3); a, b = xs[k], xs[k + 1]; w = max(abs(a - 0.739085) * 2.2, 2e-4)
        ax.cla(); xx = np.linspace(0.739085 - w, 0.739085 + w, 300)
        ax.plot(xx, f(xx), color=AZUL, lw=2); ax.axhline(0, color=TINTA, lw=0.7)
        ax.plot(xx, f(a) + df(a) * (xx - a), color=LARANJA, lw=1.4)
        ax.plot([a], [f(a)], 'o', color=LARANJA); ax.plot([b], [0], 'o', color=VERDE)
        ax.set_xlim(xx[0], xx[-1]); ax.set_title(f'x{k} = {a:.9f}  →  x{k+1} = {b:.9f}'.replace('.', ','), fontsize=10)
    salvar(fig, up, N, path)


def a_lancamento(path):
    s = lambda t: -4.9 * t ** 2 + 15 * t + 2; v = lambda t: 15 - 9.8 * t
    T = (15 + np.sqrt(225 + 39.2)) / 9.8; ts = np.linspace(0, T, 70)
    fig = plt.figure(figsize=(8, 4)); a0 = fig.add_subplot(1, 3, 1); a1 = fig.add_subplot(1, 3, (2, 3))
    a0.set_xlim(-1, 1); a0.set_ylim(0, 15); a0.set_xticks([]); a0.set_title('altura (m)'); a0.axhline(13.48, ls=':', color=CINZA)
    bola, = a0.plot([], [], 'o', color=LARANJA, ms=12)
    eixos(a1, (0, 3.3), (-18, 16)); a1.set_xlabel('t (s)')
    ls_, = a1.plot([], [], color=AZUL, lw=2, label='s(t)'); lv, = a1.plot([], [], color=LARANJA, lw=2, label='v(t)'); a1.legend(loc='lower left')
    fig.tight_layout()
    def up(i):
        t = ts[i]; bola.set_data([0], [s(t)]); ls_.set_data(ts[:i + 1], s(ts[:i + 1])); lv.set_data(ts[:i + 1], v(ts[:i + 1]))
    salvar(fig, up, len(ts), path)


ANIM = {'escada': a_escada, 'sombra': a_sombra, 'aviao': a_aviao, 'extremos': a_extremos, 'tvm': a_tvm,
        'lhopital_e': a_lhopital_e, 'esboco': a_esboco, 'cerca': a_cerca, 'proximo': a_proximo, 'cabo': a_cabo,
        'newton': a_newton, 'lancamento': a_lancamento}
