# -*- coding: utf-8 -*-
"""Animações das soluções completas do capítulo 5."""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from anim_base import *


def _riemann(path, f, a, b, ns, exato, titulo, regra='dir', ylim=None):
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); N = len(ns)
    xx = np.linspace(a, b, 400)
    def up(i):
        n = ns[i]; ax.cla(); eixos(ax, (a - 0.05 * (b - a), b + 0.05 * (b - a)), ylim or (0, 1.15 * f(xx).max()))
        dx = (b - a) / n; xs = a + dx * np.arange(n)
        pts = {'dir': xs + dx, 'esq': xs, 'med': xs + dx / 2}[regra]
        for x0, p in zip(xs, pts):
            ax.add_patch(Rectangle((x0, 0), dx, f(p), fc=LARANJA, ec=LARANJA, alpha=0.51, lw=0.6))
        ax.plot(xx, f(xx), color=AZUL, lw=2); s = (f(pts) * dx).sum()
        ax.set_title(f'{titulo}   n = {n}:  soma = {s:.5f}   (exato {exato:.5f})'.replace('.', ','), fontsize=10)
    salvar(fig, up, N, path, fps=3, pausa_final=4)


def a_riemann(path):
    _riemann(path, lambda x: 4 - x ** 2, 0, 2, [2, 4, 8, 16, 32, 64], 16 / 3, '$4-x^2$', 'dir')


def a_limite_soma(path):
    _riemann(path, lambda x: x ** 3, 0, 1, [2, 4, 8, 16, 32, 64, 128], 0.25, '$x^3$', 'dir')


def a_funcao_area(path):
    f = lambda t: (t - 1) * (t - 3); g = lambda x: x ** 3 / 3 - 2 * x ** 2 + 3 * x
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.6), sharex=True)
    eixos(a1, (0, 4.1), (-1.5, 3.5)); eixos(a2, (0, 4.1), (-0.3, 1.8))
    tt = np.linspace(0, 4, 400); a1.plot(tt, f(tt), color=AZUL, lw=2); a1.set_title('$f(t)=(t-1)(t-3)$')
    a2.set_title('$g(x)=\\int_0^x f(t)\\,dt$'); a2.plot(tt, g(tt), color=CINZA, ls=':')
    lg, = a2.plot([], [], color=AZUL, lw=2); pg, = a2.plot([], [], 'o', color=AZUL); fig.tight_layout()
    xs = np.linspace(0.02, 4, 60); fills = []
    def up(i):
        x = xs[i]
        for p in fills: p.remove()
        fills.clear(); t = np.linspace(0, x, 200); y = f(t)
        fills.append(a1.fill_between(t, 0, y, where=y >= 0, color=AZUL, alpha=0.3))
        fills.append(a1.fill_between(t, 0, y, where=y < 0, color=LARANJA, alpha=0.68))
        lg.set_data(xs[:i + 1], g(xs[:i + 1])); pg.set_data([x], [g(x)])
    salvar(fig, up, len(xs), path)


def a_tfc_cadeia(path):
    f = lambda t: np.exp(t ** 2)
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); xs = np.linspace(1.0, 1.3, 40)
    def up(i):
        x = xs[i]; ax.cla(); eixos(ax, (0.8, 1.8), (0, 25))
        tt = np.linspace(0.8, 1.8, 300); ax.plot(tt, f(tt), color=AZUL, lw=2)
        t = np.linspace(x, x ** 2, 100); ax.fill_between(t, 0, f(t), color=LARANJA, alpha=0.59)
        ax.axvline(x, color=VERDE, ls='--', lw=1); ax.axvline(x ** 2, color=VERDE, ls='--', lw=1)
        der = 2 * x * np.exp(x ** 4) - np.exp(x ** 2)
        ax.set_title(f'x = {x:.3f}: faixa de x até x²;  taxa = 2x·e^(x⁴) − e^(x²) = {der:.2f}'.replace('.', ','), fontsize=10)
    salvar(fig, up, len(xs), path)


def a_deslocamento(path):
    v = lambda t: 3 * (t - 1) * (t - 3); s = lambda t: 2 + t ** 3 - 6 * t ** 2 + 9 * t
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.2), gridspec_kw={'height_ratios': [2, 1]})
    eixos(a1, (0, 4.1), (-4, 10)); tt = np.linspace(0, 4, 300); a1.plot(tt, v(tt), color=AZUL, lw=2); a1.set_title('v(t) = 3(t−1)(t−3)')
    a2.set_xlim(0, 8); a2.set_ylim(-1, 1); a2.set_yticks([]); a2.axhline(0, color=TINTA, lw=0.8); a2.set_title('posição s(t)')
    pt, = a2.plot([], [], 'o', ms=12, color=AZUL); txt = a2.text(4.5, 0.4, '', fontsize=9); fig.tight_layout()
    ts = np.linspace(0.02, 4, 60); fills = []
    def up(i):
        t = ts[i]
        for p in fills: p.remove()
        fills.clear(); u = np.linspace(0, t, 200); y = v(u)
        fills.append(a1.fill_between(u, 0, y, where=y >= 0, color=AZUL, alpha=0.3))
        fills.append(a1.fill_between(u, 0, y, where=y < 0, color=LARANJA, alpha=0.68))
        pt.set_data([s(t)], [0]); txt.set_text(f't = {t:.2f}  s = {s(t):.2f}'.replace('.', ','))
    salvar(fig, up, len(ts), path)


def a_valor_medio(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); eixos(ax, (-0.1, 3.3), (0, 1.15))
    xx = np.linspace(0, np.pi, 300); ax.plot(xx, np.sin(xx), color=AZUL, lw=2); ax.fill_between(xx, 0, np.sin(xx), color=AZUL, alpha=0.15)
    rect = Rectangle((0, 0), np.pi, 0, fc=LARANJA, alpha=0.51, ec=LARANJA); ax.add_patch(rect)
    hs = np.concatenate([np.linspace(0.1, 1, 25), np.linspace(1, 2 / np.pi, 20)]); tt = ax.set_title('')
    def up(i):
        h = hs[i]; rect.set_height(h)
        tt.set_text(f'altura {h:.3f}: área do retângulo {np.pi*h:.3f}  (área sob o seno: 2)'.replace('.', ','))
        if i == len(hs) - 1:
            c = np.arcsin(2 / np.pi); ax.plot([c, np.pi - c], [2 / np.pi] * 2, 'o', color=VERDE, ms=8)
    salvar(fig, up, len(hs), path)


def a_substituicao(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 3.8))
    f = lambda x: x * np.sqrt(4 - x ** 2); g = lambda u: 0.5 * np.sqrt(u)
    eixos(a1, (0, 2.1), (0, 2.2)); eixos(a2, (0, 4.2), (0, 1.2))
    xx = np.linspace(0, 2, 300); uu = np.linspace(0, 4, 300)
    a1.plot(xx, f(xx), color=AZUL, lw=2); a1.set_title(r'$x\sqrt{4-x^2}$ em $[0,2]$')
    a2.plot(uu, g(uu), color=LARANJA, lw=2); a2.set_title(r'$\frac{1}{2}\sqrt{u}$ em $[0,4]$  ($u=4-x^2$)')
    fig.tight_layout(); fig.subplots_adjust(top=0.80); xs = np.linspace(2, 0.001, 50); fl = []; tt = fig.suptitle('')
    def up(i):
        x = xs[i]; u = 4 - x ** 2
        for p in fl: p.remove()
        fl.clear(); t = np.linspace(x, 2, 100); fl.append(a1.fill_between(t, 0, f(t), color=AZUL, alpha=0.3))
        w = np.linspace(0, u, 100); fl.append(a2.fill_between(w, 0, g(w), color=LARANJA, alpha=0.51))
        A = ((4 - x ** 2) ** 1.5) / 3
        tt.set_text(f'áreas acumuladas iguais: {A:.4f}  (total 8/3 ≈ 2,6667)'.replace('.', ','))
    salvar(fig, up, len(xs), path)


def a_simetria(path):
    f = lambda x: x ** 3 * np.cos(x)
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); eixos(ax, (-3.3, 3.3), (-25, 25))
    xx = np.linspace(-np.pi, np.pi, 400); ax.plot(xx, f(xx), color=AZUL, lw=2); ax.set_title(r'$x^3\cos x$ é ímpar: as áreas se cancelam')
    ws = np.linspace(0.05, np.pi, 50); fl = []
    def up(i):
        w = ws[i]
        for p in fl: p.remove()
        fl.clear(); t = np.linspace(-w, w, 300); y = f(t)
        fl.append(ax.fill_between(t, 0, y, where=y >= 0, color=AZUL, alpha=0.3))
        fl.append(ax.fill_between(t, 0, y, where=y < 0, color=LARANJA, alpha=0.68))
    salvar(fig, up, len(ws), path)


def a_pi_arctan(path):
    _riemann(path, lambda x: 4 / (1 + x ** 2), 0, 1, [1, 2, 4, 8, 16, 32, 64, 128], np.pi, r'$4/(1+x^2)$', 'med', (0, 4.4))


def a_tanque(path):
    r = lambda t: 200 - 4 * t; V = lambda t: 1000 + 200 * t - 2 * t ** 2
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 3.8), gridspec_kw={'width_ratios': [2, 1]})
    eixos(a1, (0, 52), (0, 220)); a1.set_xlabel('t (min)'); a1.set_title('r(t) = 200 − 4t  (L/min)')
    tt = np.linspace(0, 50, 200); a1.plot(tt, r(tt), color=AZUL, lw=2)
    a2.set_xlim(0, 1); a2.set_ylim(0, 6500); a2.set_xticks([]); a2.set_title('volume (L)')
    agua = Rectangle((0.15, 0), 0.7, 1000, fc='#7FB3E0'); a2.add_patch(agua); a2.add_patch(Rectangle((0.15, 0), 0.7, 6500, fill=False, ec=TINTA))
    txt = a2.text(0.2, 6100, '', fontsize=9); fig.tight_layout(); ts = np.linspace(0.5, 50, 50); fl = []
    def up(i):
        t = ts[i]
        for p in fl: p.remove()
        fl.clear(); u = np.linspace(0, t, 100); fl.append(a1.fill_between(u, 0, r(u), color=LARANJA, alpha=0.59))
        agua.set_height(V(t)); txt.set_text(f'{V(t):.0f} L')
    salvar(fig, up, len(ts), path)


def a_log_tan(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); eixos(ax, (0, 1.0), (0, 1.6))
    xx = np.linspace(0, np.pi / 4, 300); ax.plot(np.linspace(0, 0.95, 300), 1 / np.cos(np.linspace(0, 0.95, 300)), color=AZUL, lw=2)
    ax.axvline(np.pi / 4, color=CINZA, ls=':'); ws = np.linspace(0.02, np.pi / 4, 45); fl = []; tt = ax.set_title('')
    def up(i):
        w = ws[i]
        for p in fl: p.remove()
        fl.clear(); t = np.linspace(0, w, 100); fl.append(ax.fill_between(t, 0, 1 / np.cos(t), color=LARANJA, alpha=0.59))
        val = np.log(1 / np.cos(w) + np.tan(w))
        tt.set_text(f'∫₀^x sec t dt = ln|sec x + tan x| = {val:.4f}'.replace('.', ','))
    salvar(fig, up, len(ws), path)


ANIM = {'riemann': a_riemann, 'limite_soma': a_limite_soma, 'funcao_area': a_funcao_area,
        'tfc_cadeia': a_tfc_cadeia, 'deslocamento': a_deslocamento, 'valor_medio': a_valor_medio,
        'substituicao': a_substituicao, 'simetria': a_simetria, 'pi_arctan': a_pi_arctan,
        'tanque': a_tanque, 'log_tan': a_log_tan}
