# -*- coding: utf-8 -*-
"""Animações das soluções completas do capítulo 7."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from math import factorial
from anim_base import *


def _br(v, nd=4):
    return f'{v:.{nd}f}'.replace('.', ',')


def _acumula(path, f, a, b, valor, titulo, ylim, xlim=None, n=60):
    fig, ax = plt.subplots(figsize=(6.4, 4.4)); eixos(ax, xlim or (a - 0.1 * (b - a), b + 0.1 * (b - a)), ylim)
    xx = np.linspace(*(xlim or (a, b)), 400); ax.plot(xx, f(xx), color=AZUL, lw=2)
    xs = np.linspace(a, b, n); arts = []; fig.subplots_adjust(top=0.82)
    def up(i):
        for p in arts: p.remove()
        arts.clear(); t = np.linspace(a, xs[i], 300)
        arts.append(ax.fill_between(t, 0, f(t), color=LARANJA, alpha=0.35))
        A = np.trapezoid(f(t), t)
        ax.set_title(f'{titulo}\nárea acumulada = {_br(A)}   (valor exato {_br(valor)})', fontsize=10)
    salvar(fig, up, n, path)


def a_partes(path):
    e = np.e; fig, ax = plt.subplots(figsize=(6.4, 3.6)); eixos(ax, (-0.1, 3.0), (-0.1, 1.25))
    xx = np.linspace(0.5, 2.9, 300); ax.plot(xx, np.log(xx), color=AZUL, lw=2)
    ax.plot([0, e, e], [1, 1, 0], 'k--', lw=1); ax.set_aspect('equal'); arts = []; N = 70
    def up(i):
        for p in arts: p.remove()
        arts.clear()
        s = min(i / 35, 1); x1 = 1 + (e - 1) * s; t = np.linspace(1, x1, 200)
        arts.append(ax.fill_between(t, 0, np.log(t), color=AZUL, alpha=0.35))
        A1 = x1 * np.log(x1) - x1 + 1; txt = f'∫₁ˣ ln t dt = {_br(A1, 3)}'
        if i >= 35:
            s2 = min((i - 35) / 30, 1); y1 = s2; yy = np.linspace(0, y1, 200)
            arts.append(ax.fill_betweenx(yy, 0, np.exp(yy), color=LARANJA, alpha=0.35))
            txt += f'    ∫₀ʸ eᵘ du = {_br(np.exp(y1) - 1, 3)}'
            if s2 >= 1: txt += '\nsoma = e ≈ 2,718 (retângulo)'
        ax.set_title(txt, fontsize=10)
    salvar(fig, up, N, path)


def a_ciclica(path):
    _acumula(path, lambda x: np.exp(x) * np.sin(x), 0, np.pi, (np.exp(np.pi) + 1) / 2, '$\\int_0^x e^t\\sin t\\,dt$', (-0.5, 9))


def a_sec3(path):
    _acumula(path, lambda x: 1 / np.cos(x) ** 3, 0, np.pi / 4, (np.sqrt(2) + np.log(1 + np.sqrt(2))) / 2, '$\\int_0^x\\sec^3 t\\,dt$', (0, 3.2))


def a_elipse(path):
    a, b = 3, 2; fig, ax = plt.subplots(figsize=(6.4, 4.6)); eixos(ax, (-3.6, 3.6), (-2.6, 2.6)); ax.set_aspect('equal')
    th = np.linspace(0, 2 * np.pi, 300); ax.plot(a * np.cos(th), b * np.sin(th), color=AZUL, lw=2)
    ths = np.linspace(-np.pi / 2, np.pi / 2, 60); arts = []
    def up(i):
        for p in arts: p.remove()
        arts.clear(); T = ths[i]; x1 = a * np.sin(T); x = np.linspace(-a, x1, 300); y = b / a * np.sqrt(np.clip(a * a - x * x, 0, None))
        arts.append(ax.fill_between(x, -y, y, color=LARANJA, alpha=0.35))
        y1 = b / a * np.sqrt(max(a * a - x1 * x1, 0)); arts.extend(ax.plot([x1, x1], [-y1, y1], color=VERDE, lw=3))
        A = a * b * (T + np.sin(T) * np.cos(T) + np.pi / 2)
        ax.set_title(f'θ = {_br(np.degrees(T), 0)}°,  x = 3 sen θ = {_br(x1, 2)}:  área = {_br(A, 3)}  (6π ≈ 18,850)', fontsize=10)
    salvar(fig, up, len(ths), path)


def a_fracoes(path):
    f = lambda x: (5 * x ** 2 + 3 * x - 2) / (x ** 3 + 2 * x ** 2)
    comps = [(lambda x: 2 / x, '$2/x$'), (lambda x: -1 / x ** 2, '$-1/x^2$'), (lambda x: 3 / (x + 2), '$3/(x+2)$')]
    fig, ax = plt.subplots(figsize=(6.4, 4.4)); xx = np.linspace(0.35, 3, 300); cores = [VERDE, LARANJA, CINZA]
    def up(k):
        ax.cla(); eixos(ax, (0, 3.1), (-4, 6)); ax.plot(xx, f(xx), color=AZUL, lw=3, alpha=0.35, label='$f(x)$')
        m = min(k, 3); soma = np.zeros_like(xx)
        for j in range(m):
            g, lab = comps[j]; ax.plot(xx, g(xx), color=cores[j], lw=1.2, ls='--', label=lab); soma += g(xx)
        if m: ax.plot(xx, soma, color=AZUL, lw=1.6, label='soma das parcelas')
        if k >= 4:
            t = np.linspace(1, 2, 200); ax.fill_between(t, 0, f(t), color=AZUL, alpha=0.25)
            ax.set_title('$\\int_1^2 f = 2\\ln2-\\frac{1}{2}+3\\ln\\frac{4}{3}\\approx1{,}749$')
        else:
            ax.set_title(f'{m} de 3 parcelas somadas')
        ax.legend(fontsize=8, loc='upper right')
    salvar(fig, up, 5, path, fps=1, pausa_final=3)


def a_simpson(path):
    f = lambda x: np.exp(-x ** 2); exato = 0.7468241328; ns = [2, 4, 8, 16]
    fig, ax = plt.subplots(figsize=(6.4, 4.4)); xx = np.linspace(0, 1, 300)
    def up(i):
        n = ns[i]; ax.cla(); eixos(ax, (-0.05, 1.08), (0, 1.12)); ax.plot(xx, f(xx), color=AZUL, lw=2)
        p = np.linspace(0, 1, n + 1); h = 1 / n
        for j in range(n):
            ax.add_patch(Polygon([[p[j], 0], [p[j], f(p[j])], [p[j + 1], f(p[j + 1])], [p[j + 1], 0]], fc=LARANJA, ec=LARANJA, alpha=0.3))
        T = h * (f(p).sum() - (f(0) + f(1)) / 2); w = np.array([1] + [4 if j % 2 else 2 for j in range(1, n)] + [1]); S = h / 3 * (w * f(p)).sum()
        ax.set_title(f'n = {n}:  T = {_br(T, 6)} (erro {abs(T - exato):.1e})\nS = {_br(S, 6)} (erro {abs(S - exato):.1e});  exato 0,746824'.replace('e-0', 'e-'), fontsize=10)
    salvar(fig, up, len(ns), path, fps=1, pausa_final=3)


def a_arco_parabola(path):
    fig, ax = plt.subplots(figsize=(5.6, 4.6)); xx = np.linspace(0, 1.05, 200); ns = [1, 2, 3, 4, 6, 8, 16, 32]
    def up(i):
        n = ns[i]; ax.cla(); eixos(ax, (-0.05, 1.1), (-0.05, 1.12)); ax.set_aspect('equal'); ax.plot(xx, xx ** 2, color=AZUL, lw=2)
        p = np.linspace(0, 1, n + 1); ax.plot(p, p ** 2, 'o-', color=LARANJA, ms=3, lw=1.4)
        L = np.hypot(np.diff(p), np.diff(p ** 2)).sum()
        ax.set_title(f'{n} segmento(s): {_br(L, 5)}   (exato 1,47894)', fontsize=10)
    salvar(fig, up, len(ns), path, fps=2, pausa_final=4)


def a_gabriel(path):
    fig = plt.figure(figsize=(6.6, 4.4)); ax = fig.add_subplot(projection='3d'); Rs = np.geomspace(1.5, 60, 45)
    def S(R):
        x = np.linspace(1, R, 4000); return 2 * np.pi * np.trapezoid(np.sqrt(1 + x ** -4) / x, x)
    def up(i):
        R = Rs[i]; ax.cla(); xv = np.geomspace(1, min(R, 12), 60); ph = np.linspace(0, 2 * np.pi, 40)
        X, P = np.meshgrid(xv, ph); r = 1 / X
        ax.plot_surface(X, r * np.cos(P), r * np.sin(P), color=AZUL, alpha=0.5, linewidth=0)
        ax.set_xlim(1, 12); ax.set_ylim(-1, 1); ax.set_zlim(-1, 1); ax.set_box_aspect((4, 1, 1)); ax.view_init(18, -60)
        ax.set_yticks([]); ax.set_zticks([])
        ax.set_title(f'R = {_br(R, 1)}:   V = π(1 − 1/R) = {_br(np.pi * (1 - 1 / R), 4)}  →  π\nS(R) = {_br(S(R), 2)}  →  ∞', fontsize=10)
    salvar(fig, up, len(Rs), path, fps=8, pausa_final=10)


def a_gama(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.4)); t = np.linspace(0, 16, 600); N = 6
    fig.subplots_adjust(top=0.85)
    def up(n):
        ax.cla(); top = max(1.0, n ** n * np.exp(-n)) * 1.15; eixos(ax, (0, 16), (0, top))
        y = t ** n * np.exp(-t); ax.plot(t, y, color=AZUL, lw=2); ax.fill_between(t, 0, y, color=LARANJA, alpha=0.35)
        ax.set_title(f'$\\Gamma({n + 1})=\\int_0^\\infty t^{{{n}}}e^{{-t}}\\,dt={factorial(n)}={n}!$', fontsize=12)
    salvar(fig, up, N, path, fps=1, pausa_final=2)


def a_weierstrass(path):
    f = lambda x: 1 / (2 + np.cos(x)); g = lambda t: 2 / (3 + t ** 2)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.4, 3.6)); eixos(a1, (0, 1.7), (0, 0.8)); eixos(a2, (0, 1.1), (0, 0.8))
    x = np.linspace(0, np.pi / 2, 300); a1.plot(x, f(x), color=AZUL, lw=2); a1.set_title('$1/(2+\\cos x)$, $x\\in[0,\\pi/2]$', fontsize=10)
    tt = np.linspace(0, 1, 300); a2.plot(tt, g(tt), color=AZUL, lw=2); a2.set_title('$2/(3+t^2)$, $t\\in[0,1]$', fontsize=10)
    fig.subplots_adjust(top=0.78, wspace=0.3); arts = []; ts = np.linspace(0, 1, 50)
    def up(i):
        for p in arts: p.remove()
        arts.clear(); T = ts[i]; X = 2 * np.arctan(T)
        u = np.linspace(0, X, 200); v = np.linspace(0, T, 200)
        arts.append(a1.fill_between(u, 0, f(u), color=LARANJA, alpha=0.35)); arts.append(a2.fill_between(v, 0, g(v), color=LARANJA, alpha=0.35))
        fig.suptitle(f't = tan(x/2) = {_br(T, 2)}:  as duas áreas valem {_br(np.trapezoid(g(v), v))}\n(total π/(3√3) ≈ 0,6046)', fontsize=10)
    salvar(fig, up, len(ts), path)


def a_logistica(path):
    P = lambda t: 1000 / (1 + 9 * np.exp(-t / 2)); fig, ax = plt.subplots(figsize=(6.4, 4.4))
    T, Y = np.meshgrid(np.linspace(0.5, 15.5, 16), np.linspace(50, 1150, 12)); dY = 0.5 * Y * (1 - Y / 1000); dT = np.ones_like(dY)
    nrm = np.hypot(dT, dY / 75); ts = np.linspace(0, 16, 60); ti = 2 * np.log(9)
    def up(i):
        ax.cla(); eixos(ax, (0, 16.2), (0, 1200)); ax.quiver(T, Y, 0.6 * dT / nrm, 0.6 * dY / nrm, color=CINZA, alpha=0.45, angles='xy', scale_units='xy', scale=1, width=0.003)
        ax.axhline(1000, color=VERDE, ls='--', lw=1); t = np.linspace(0, ts[i], 300); ax.plot(t, P(t), color=AZUL, lw=2.2)
        ax.plot([ts[i]], [P(ts[i])], 'o', color=AZUL)
        if ts[i] >= ti: ax.plot([ti], [500], 's', color=LARANJA, ms=8); ax.annotate('inflexão (P = 500)', (ti, 500), (ti + 1, 330), color=LARANJA, fontsize=9)
        ax.set_xlabel('t'); ax.set_title(f't = {_br(ts[i], 2)}:  P = {P(ts[i]):.0f}'.replace('.', ','), fontsize=10)
    salvar(fig, up, len(ts), path)


ANIM = {'partes': a_partes, 'ciclica': a_ciclica, 'sec3': a_sec3, 'elipse': a_elipse, 'fracoes': a_fracoes,
        'simpson': a_simpson, 'arco_parabola': a_arco_parabola, 'gabriel': a_gabriel, 'gama': a_gama,
        'weierstrass': a_weierstrass, 'logistica': a_logistica}
