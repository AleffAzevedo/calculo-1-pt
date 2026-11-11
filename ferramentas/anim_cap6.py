# -*- coding: utf-8 -*-
"""Animações das soluções completas do capítulo 6."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, FancyArrowPatch
from anim_base import *


def _br(v, nd=3):
    return f'{v:,.{nd}f}'.replace(',', ' ').replace('.', ',')


# --------------------------------------------------------------- áreas
def a_area_cruzam(path):
    f = lambda x: x ** 3 - 3 * x; g = lambda x: x
    fig, ax = plt.subplots(figsize=(6.4, 4.4)); eixos(ax, (-2.6, 2.6), (-3.2, 3.2))
    xx = np.linspace(-2.4, 2.4, 400)
    ax.plot(xx, f(xx), color=AZUL, lw=2, label='$y=x^3-3x$'); ax.plot(xx, g(xx), color=LARANJA, lw=2, label='$y=x$')
    ax.legend(loc='lower right', fontsize=9); xs = np.linspace(-2, 2, 61); arts = []
    def up(i):
        for a in arts: a.remove()
        arts.clear(); x = xs[i]; t = np.linspace(-2, x, 300)
        arts.append(ax.fill_between(t, f(t), g(t), where=t <= 0, color=AZUL, alpha=0.25))
        arts.append(ax.fill_between(t, f(t), g(t), where=t >= 0, color=LARANJA, alpha=0.42))
        lo, hi = sorted([f(x), g(x)]); arts.append(ax.add_patch(Rectangle((x - 0.04, lo), 0.08, hi - lo, color=VERDE, alpha=0.8)))
        A = np.trapezoid(np.abs(f(t) - g(t)), t) if x > -2 else 0
        ax.set_title(f'área acumulada = {_br(A)}   (total 8)')
    salvar(fig, up, len(xs), path)


# --------------------------------------------------------------- sólidos de revolução
def _revolve(path, curva, eixo, c, sinal, lims, titulo, regiao=None, n=36):
    """curva: (s, t) fechada; s ao longo do eixo, t = distância ao eixo.
    eixo 'h': pontos (s, c + sinal*t cos φ, t sin φ); eixo 'v': (c + sinal*t cos φ, t sin φ, s)."""
    s, t = curva
    fig = plt.figure(figsize=(6.0, 5.0)); ax = fig.add_subplot(projection='3d')
    def coords(S, T, P):
        a = c + sinal * T * np.cos(P); b = T * np.sin(P)
        return (S, a, b) if eixo == 'h' else (a, b, S)
    def up(k):
        ax.cla(); th = 2 * np.pi * (k + 1) / n
        P, S = np.meshgrid(np.linspace(0, th, 40), s); T = np.meshgrid(np.linspace(0, th, 40), t)[1]
        X, Y, Z = coords(S, T, P)
        ax.plot_surface(X, Y, Z, color=AZUL, alpha=0.35, linewidth=0, shade=True)
        for ph, cor in [(0, LARANJA), (th, LARANJA)]:
            X0, Y0, Z0 = coords(s, t, np.full_like(s, ph)); ax.plot(X0, Y0, Z0, color=cor, lw=1.6)
        # eixo de rotação
        L = np.array([lims[0][0], lims[0][1]]) if eixo == 'h' else np.array([lims[2][0], lims[2][1]])
        if eixo == 'h': ax.plot(L, [c, c], [0, 0], 'w--', lw=1)
        else: ax.plot([c, c], [0, 0], L, 'w--', lw=1)
        ax.set_xlim(*lims[0]); ax.set_ylim(*lims[1]); ax.set_zlim(*lims[2])
        ax.set_xlabel('x'); ax.set_ylabel('y' if eixo == 'h' else 'z'); ax.set_zlabel('z' if eixo == 'h' else 'y')
        ax.view_init(elev=22, azim=-60)
        if eixo == 'h': ax.set_xticks([0, 1])
        ax.set_box_aspect((lims[0][1] - lims[0][0], lims[1][1] - lims[1][0], lims[2][1] - lims[2][0]))
        ax.set_title(f'{titulo}   ângulo = {np.degrees(th):.0f}°', fontsize=10)
    salvar(fig, up, n, path, fps=10, pausa_final=15)


def a_arruela(path):
    x = np.linspace(0, 1, 60)
    s = np.concatenate([x, x[::-1]]); y = np.concatenate([x ** 2, x[::-1]]); t = 2 - y
    _revolve(path, (s, t), 'h', 2, -1, ((-0.2, 1.2), (-0.2, 4.2), (-2.2, 2.2)), 'Giro em torno de $y=2$: $V=8\\pi/15$')


def a_cascas(path):
    x = np.linspace(0, 1, 60)
    xs = np.concatenate([x, x[::-1]]); ys = np.concatenate([x ** 2, x[::-1]])
    _revolve(path, (ys, xs + 1), 'v', -1, 1, ((-3.2, 1.2), (-2.2, 2.2), (-0.1, 1.1)), 'Giro em torno de $x=-1$: $V=\\pi/2$')


def a_toro(path):
    u = np.linspace(0, 2 * np.pi, 80)
    _revolve(path, (np.sin(u), 3 + np.cos(u)), 'v', 0, 1, ((-4.2, 4.2), (-4.2, 4.2), (-1.5, 1.5)), 'Toro: $V=6\\pi^2\\approx59{,}22$')


# --------------------------------------------------------------- comprimento de arco
def a_arco(path):
    f = lambda x: x ** 3 / 6 + 1 / (2 * x)
    fig, ax = plt.subplots(figsize=(6.4, 4.4)); xx = np.linspace(0.8, 3.2, 300); ns = [1, 2, 4, 8, 16, 32, 64]
    def up(i):
        n = ns[i]; ax.cla(); eixos(ax, (0, 3.4), (0, 5.6)); ax.plot(xx, f(xx), color=AZUL, lw=2)
        p = np.linspace(1, 3, n + 1); ax.plot(p, f(p), 'o-', color=LARANJA, ms=3, lw=1.4)
        L = np.sum(np.hypot(np.diff(p), np.diff(f(p))))
        ax.set_title(f'{n} segmento(s): comprimento = {_br(L, 4)}   (exato 14/3 ≈ 4,6667)', fontsize=10)
    salvar(fig, up, len(ns), path, fps=2, pausa_final=4)


# --------------------------------------------------------------- centroide
def a_centroide(path):
    fig, ax = plt.subplots(figsize=(5.6, 5.0)); eixos(ax, (-0.1, 1.1), (-0.1, 1.1))
    xx = np.linspace(0, 1, 200); ax.plot(xx, xx, color=AZUL, lw=2); ax.plot(xx, xx ** 2, color=AZUL, lw=2)
    ax.set_aspect('equal'); xs = np.linspace(0.04, 1, 50); arts = []; trilha = []
    def up(i):
        for a in arts: a.remove()
        arts.clear(); X = xs[i]; t = np.linspace(0, X, 300); h = t - t ** 2
        A = np.trapezoid(h, t); xb = np.trapezoid(t * h, t) / A; yb = np.trapezoid((t ** 2 - t ** 4) / 2, t) / A
        trilha.append((xb, yb))
        arts.append(ax.fill_between(t, t ** 2, t, color=LARANJA, alpha=0.51))
        arts.extend(ax.plot(*zip(*trilha), color=CINZA, lw=1))
        arts.extend(ax.plot([xb], [yb], "o", color=VERDE, ms=9))
        ax.set_title(f'centroide da parte varrida: ({_br(xb)}; {_br(yb)})\nfinal: (1/2; 2/5)', fontsize=10)
    salvar(fig, up, len(xs), path)


# --------------------------------------------------------------- crescimento
def a_crescimento(path):
    k = np.log(3) / 2; T2 = np.log(2) / k; y = lambda t: 1000 * np.exp(k * t)
    fig, ax = plt.subplots(figsize=(6.4, 4.4)); ts = np.linspace(0, 5, 60)
    def up(i):
        ax.cla(); eixos(ax, (0, 5.2), (0, 17000)); T = ts[i]; tt = np.linspace(0, T, 200)
        ax.plot(tt, y(tt), color=AZUL, lw=2); ax.plot([T], [y(T)], 'o', color=AZUL)
        m = 1
        while m * T2 <= T + 1e-9:
            ax.axhline(1000 * 2 ** m, color=LARANJA, ls=':', lw=1); ax.axvline(m * T2, color=LARANJA, ls=':', lw=1); m += 1
        if T >= 2 * np.log(10) / np.log(3): ax.plot([2 * np.log(10) / np.log(3)], [10000], 's', color=VERDE)
        ax.set_xlabel('t (h)'); ax.set_title(f't = {_br(T, 2)} h:  y = ' + f'{y(T):,.0f}'.replace(',', ' ') + f'   (dobra a cada {_br(T2, 3)} h)', fontsize=10)
    salvar(fig, up, len(ts), path)


# --------------------------------------------------------------- bombeamento
def a_bombeamento(path):
    fig, ax = plt.subplots(figsize=(5.4, 5.4)); niv = np.linspace(6, 0, 50)
    W = lambda h: 2450 * np.pi * ((7 * 216 / 3 - 1296 / 4) - (7 * h ** 3 / 3 - h ** 4 / 4))
    def up(i):
        ax.cla(); ax.set_xlim(-4, 4); ax.set_ylim(-0.5, 8); ax.set_aspect('equal'); ax.axis('off')
        h = niv[i]
        ax.add_patch(Polygon([[0, 0], [-h / 2, h], [h / 2, h]], color=AZUL, alpha=0.4))
        ax.plot([-3, 0, 3], [6, 0, 6], color=TINTA, lw=2); ax.plot([-3, 3], [6, 6], color=TINTA, lw=0.6, ls=':')
        ax.plot([0, 0], [6, 7], color=CINZA, lw=3); ax.plot([0, 1], [7, 7], color=CINZA, lw=3)
        ax.annotate('', (0.5, 7.0), (0.5, h), arrowprops=dict(arrowstyle='->', color=LARANJA, lw=1.5))
        ax.text(0.65, (h + 7) / 2, f'sobe {_br(7 - h, 2)} m', color=LARANJA, fontsize=9)
        ax.set_title(f'nível = {_br(h, 2)} m\ntrabalho acumulado = {W(h) / 1e6:.3f} MJ (total 1,385 MJ)'.replace('.', ','), fontsize=10)
    salvar(fig, up, len(niv), path)


# --------------------------------------------------------------- comporta
def a_comporta(path):
    fig, ax = plt.subplots(figsize=(6.0, 4.8)); hs = np.linspace(0, 3, 31)
    def up(i):
        ax.cla(); ax.set_xlim(-4.2, 3.2); ax.set_ylim(-3.4, 0.6); ax.set_aspect('equal'); ax.axis('off')
        ax.fill_between([-4.2, 3.2], -3.4, 0, color=AZUL, alpha=0.08); ax.axhline(0, color=AZUL, lw=1)
        ax.add_patch(Polygon([[-2, 0], [2, 0], [0, -3]], fc='#4A4A4A', ec=TINTA, lw=1.5))
        H = hs[i]
        for h in np.arange(0.05, H, 0.1):
            w = 4 / 3 * (3 - h); ax.add_patch(Rectangle((-w / 2, -h - 0.05), w, 0.1, color=LARANJA, alpha=0.59, lw=0))
            if abs((h * 10) % 5 - 0.5) < 0.06:
                ax.annotate('', (-w / 2, -h), (-w / 2 - 0.35 * h - 0.05, -h), arrowprops=dict(arrowstyle='->', color=VERDE))
        F = 9800 * 4 / 3 * (1.5 * H ** 2 - H ** 3 / 3)
        ax.set_title(f'profundidade somada: {_br(H, 1)} m    força = {F:,.0f} N'.replace(',', ' ') + '\n(total 58 800 N)', fontsize=10)
    salvar(fig, up, len(hs), path, fps=8)


# --------------------------------------------------------------- faixa esférica
def a_superficie(path):
    R, h = 1.0, 0.3; fig = plt.figure(figsize=(5.4, 5.0)); ax = fig.add_subplot(projection='3d')
    a_s = np.concatenate([np.linspace(R - h, -R, 30), np.linspace(-R, R - h, 30)])
    def up(i):
        ax.cla(); a = a_s[i]; ph = np.linspace(0, 2 * np.pi, 50)
        X, P = np.meshgrid(np.linspace(-R, R, 40), ph); r = np.sqrt(np.clip(R ** 2 - X ** 2, 0, None))
        ax.plot_wireframe(X, r * np.cos(P), r * np.sin(P), color=CINZA, lw=0.3, alpha=0.5)
        X, P = np.meshgrid(np.linspace(a, a + h, 12), ph); r = np.sqrt(np.clip(R ** 2 - X ** 2, 0, None))
        ax.plot_surface(X, r * np.cos(P), r * np.sin(P), color=LARANJA, alpha=0.8, linewidth=0)
        for lim in (-1, 1): pass
        ax.set_xlim(-1, 1); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1); ax.set_box_aspect((1, 1, 1)); ax.axis('off')
        ax.view_init(elev=15, azim=-70)
        ax.set_title(f'faixa de x = {_br(a, 2)} a {_br(a + h, 2)}\nárea = 2πRh = {2 * np.pi * R * h:.4f}'.replace('.', ','), fontsize=10)
    salvar(fig, up, len(a_s), path, fps=10, pausa_final=5)


# --------------------------------------------------------------- catenária
def a_catenaria(path):
    fig, ax = plt.subplots(figsize=(6.6, 4.4)); As = np.concatenate([np.geomspace(80, 12, 35), np.geomspace(12, 20, 15)[1:]])
    def up(i):
        a = As[i]; ax.cla(); x = np.linspace(-20, 20, 300); y = a * np.cosh(x / a); top = a * np.cosh(20 / a)
        ax.plot(x, y - top, color=AZUL, lw=2.2)
        ax.plot([-20, -20], [-25, 0], color=TINTA, lw=4); ax.plot([20, 20], [-25, 0], color=TINTA, lw=4)
        ax.plot([-20, 20], [0, 0], color=CINZA, ls=':')
        ax.set_xlim(-24, 24); ax.set_ylim(-26, 3); ax.set_aspect('equal'); ax.grid(alpha=0.2)
        L = 2 * a * np.sinh(20 / a); fl = top - a
        ax.set_title(f'a = {_br(a, 1)} m:   L = {_br(L, 2)} m,   flecha = {_br(fl, 2)} m', fontsize=10)
    salvar(fig, up, len(As), path, fps=10)


ANIM = {'area_cruzam': a_area_cruzam, 'arruela': a_arruela, 'cascas': a_cascas, 'arco': a_arco,
        'centroide': a_centroide, 'crescimento': a_crescimento, 'bombeamento': a_bombeamento,
        'comporta': a_comporta, 'superficie': a_superficie, 'catenaria': a_catenaria, 'toro': a_toro}
