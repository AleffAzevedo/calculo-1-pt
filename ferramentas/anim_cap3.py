# -*- coding: utf-8 -*-
"""Animações das soluções completas do capítulo 3."""
import numpy as np
import matplotlib.pyplot as plt
from anim_base import *


def _tangente_movel(path, f, df, xlim, ylim, titulo, xs, marcar=None, extra=None):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, xlim, ylim)
    xx = np.linspace(*xlim, 600); ax.plot(xx, f(xx), color=AZUL, lw=2)
    if extra: extra(ax)
    tan, = ax.plot([], [], color=LARANJA, lw=1.6); p, = ax.plot([], [], 'o', color=LARANJA)
    tt = ax.set_title(''); N = len(xs)
    def up(i):
        a = xs[i]; m = df(a)
        tan.set_data(xx, f(a) + m * (xx - a)); p.set_data([a], [f(a)])
        tt.set_text(titulo + f'   x = {a:.2f},  inclinação = {m:.2f}'.replace('.', ','))
        if marcar: marcar(ax, a, m, tan)
    salvar(fig, up, N, path)


def a_tangente(path):
    f = lambda x: x ** 2 - 4 * x + 5; df = lambda x: 2 * x - 4
    xs = np.concatenate([np.linspace(-0.5, 3, 50)])
    def extra(ax):
        ax.plot([3], [2], 'wo')
    fig_t = None
    def marcar(ax, a, m, tan):
        if abs(a - 3) < 1e-9 and not hasattr(marcar, 'ok'):
            xx = np.linspace(-1, 6, 10); ax.plot(xx, -0.5 * xx + 3.5, color=VERDE, lw=1.6, label='normal')
            ax.legend(loc='upper center'); marcar.ok = 1
    _tangente_movel(path, f, df, (-1, 6), (-2, 10), '$y=x^2-4x+5$', xs, marcar, extra)


def a_grafico_derivada(path):
    f = lambda x: x ** 3 - 3 * x ** 2; df = lambda x: 3 * x ** 2 - 6 * x
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.6), sharex=True)
    eixos(a1, (-1.2, 3.2), (-6, 3)); eixos(a2, (-1.2, 3.2), (-4, 10))
    xx = np.linspace(-1.2, 3.2, 400); a1.plot(xx, f(xx), color=AZUL, lw=2)
    a2.plot(xx, df(xx), color=CINZA, lw=1, ls=':')
    a1.set_title("$f(x)=x^3-3x^2$ e a tangente"); a2.set_title("$f'(x)$: a inclinação, ponto a ponto")
    tan, = a1.plot([], [], color=LARANJA, lw=1.5); p1, = a1.plot([], [], 'o', color=LARANJA)
    tr, = a2.plot([], [], color=LARANJA, lw=2); p2, = a2.plot([], [], 'o', color=LARANJA)
    xs = np.linspace(-1.1, 3.1, 70); fig.tight_layout()
    def up(i):
        a = xs[i]; m = df(a)
        tan.set_data(xx, f(a) + m * (xx - a)); p1.set_data([a], [f(a)])
        tr.set_data(xs[:i + 1], df(xs[:i + 1])); p2.set_data([a], [m])
    salvar(fig, up, len(xs), path)


def a_por_partes(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    As = np.concatenate([np.linspace(-1, 4, 40), np.linspace(4, 2, 20)]); N = len(As)
    def up(i):
        a = As[i]; b = 1 - a; ax.cla(); eixos(ax, (-1.5, 3), (-1, 5))
        x1 = np.linspace(-1.5, 1, 100); x2 = np.linspace(1, 3, 100)
        ax.plot(x1, x1 ** 2, color=AZUL, lw=2); ax.plot(x2, a * x2 + b, color=LARANJA, lw=2)
        ax.plot(np.linspace(0, 2.5, 10), 1 + 2 * (np.linspace(0, 2.5, 10) - 1), ':', color=CINZA)
        ax.plot([1], [1], 'wo')
        ok = '  ✔ sem bico' if abs(a - 2) < 1e-9 else ''
        ax.set_title(f'a = {a:.2f}, b = 1 − a = {b:.2f}{ok}'.replace('.', ','))
    salvar(fig, up, N, path)


def a_movimento(path):
    s = lambda t: t ** 3 - 9 * t ** 2 + 24 * t; v = lambda t: 3 * t ** 2 - 18 * t + 24
    fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.0), gridspec_kw={'height_ratios': [1, 2.2]})
    a1.set_xlim(-2, 24); a1.set_ylim(-1, 1); a1.set_yticks([]); a1.axhline(0, color=TINTA, lw=0.8)
    a1.set_title('posição na reta (m)')
    eixos(a2, (0, 5.2), (-6, 26)); a2.set_xlabel('t (s)'); a2.set_title('$v(t)=3(t-2)(t-4)$')
    pt, = a1.plot([], [], 'o', ms=12); tr, = a2.plot([], [], lw=2, color=AZUL)
    txt = a1.text(15, 0.4, '', fontsize=9); ts = np.linspace(0, 5, 80); fig.tight_layout()
    def up(i):
        t = ts[i]; c = AZUL if v(t) >= 0 else LARANJA
        pt.set_data([s(t)], [0]); pt.set_color(c)
        tr.set_data(ts[:i + 1], v(ts[:i + 1])); tr.set_color(c)
        txt.set_text(f't={t:.2f}  s={s(t):.1f}  v={v(t):.1f}'.replace('.', ','))
    salvar(fig, up, len(ts), path)


def a_derivada_seno(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (-2 * np.pi, 2 * np.pi), (-1.4, 1.4))
    xx = np.linspace(-2 * np.pi, 2 * np.pi, 500); ax.plot(xx, np.cos(xx), color=LARANJA, lw=3, alpha=0.6, label='cos x')
    l, = ax.plot([], [], color=AZUL, lw=1.8, label='$q_h(x)$'); ax.legend(loc='upper right')
    hs = np.geomspace(2, 0.01, 50); tt = ax.set_title('')
    def up(i):
        h = hs[i]; l.set_data(xx, (np.sin(xx + h) - np.sin(xx)) / h)
        tt.set_text(f'h = {h:.3f}'.replace('.', ','))
    salvar(fig, up, len(hs), path)


def a_cadeia_tangente(path):
    f = lambda x: np.sin(x ** 2); df = lambda x: 2 * x * np.cos(x ** 2)
    xs = np.linspace(0, np.sqrt(np.pi), 60)
    _tangente_movel(path, f, df, (0, 3), (-1.6, 1.6), r'$y=\operatorname{sen}(x^2)$', xs)


def a_inversa(path):
    fig, ax = plt.subplots(figsize=(5.4, 5.2))
    eixos(ax, (-3, 4), (-3, 4)); ax.set_aspect('equal')
    ax.plot([-3, 4], [-3, 4], ':', color=CINZA)
    x = np.linspace(-3, 1.2, 300); y = x + np.exp(x)
    ax.plot(x, y, color=AZUL, lw=2, label='$f(x)=x+e^x$')
    xt = np.linspace(-1.5, 1.5, 10); ax.plot(xt, 1 + 2 * xt, color=AZUL, ls='--', lw=1)
    ax.plot([0], [1], 'o', color=AZUL)
    lr, = ax.plot([], [], color=LARANJA, lw=2, label='$f^{-1}$'); lt, = ax.plot([], [], color=LARANJA, ls='--', lw=1)
    pr, = ax.plot([], [], 'o', color=LARANJA); ax.legend(loc='upper left', fontsize=9)
    tt = ax.set_title(''); N = 50
    def up(i):
        s = (i + 1) / N
        lr.set_data((1 - s) * x + s * y, (1 - s) * y + s * x)
        X = (1 - s) * xt + s * (1 + 2 * xt); Y = (1 - s) * (1 + 2 * xt) + s * xt
        lt.set_data(X, Y); pr.set_data([s], [1 - s])
        if i == N - 1: tt.set_text('inclinações: 2 em (0,1)  e  1/2 em (1,0)')
    salvar(fig, up, N, path)


def a_implicita(path):
    t = np.linspace(0, 2 * np.pi, 400)
    # parametrização: x^2 - xy + y^2 = 3 -> girar elipse u^2/6 + v^2/2 = 1 por 45°
    u = np.sqrt(6) * np.cos(t); w = np.sqrt(2) * np.sin(t)
    X = (u - w) / np.sqrt(2); Y = (u + w) / np.sqrt(2)
    fig, ax = plt.subplots(figsize=(5.6, 5.2)); eixos(ax, (-3.2, 3.2), (-3.2, 3.2)); ax.set_aspect('equal')
    ax.plot(X, Y, color=AZUL, lw=2); ax.set_title('$x^2-xy+y^2=3$')
    for (a, b) in [(1, 2), (-1, -2)]: ax.plot([a], [b], 'o', color=LARANJA, ms=8)
    for (a, b) in [(2, 1), (-2, -1)]: ax.plot([a], [b], 'o', color=VERDE, ms=8)
    tan, = ax.plot([], [], color=LARANJA, lw=1.4); p, = ax.plot([], [], 'wo')
    idx = np.linspace(0, len(t) - 2, 70).astype(int)
    def up(i):
        k = idx[i]; a, b = X[k], Y[k]; dx, dy = X[k + 1] - a, Y[k + 1] - b
        L = 1.5 / np.hypot(dx, dy); tan.set_data([a - L * dx, a + L * dx], [b - L * dy, b + L * dy]); p.set_data([a], [b])
    salvar(fig, up, len(idx), path)


def a_xx(path):
    f = lambda x: x ** x; df = lambda x: x ** x * (np.log(x) + 1)
    xs = np.concatenate([np.linspace(0.05, 1 / np.e, 30), np.linspace(1 / np.e, 1.6, 25)])
    def marcar(ax, a, m, tan):
        if abs(a - 1 / np.e) < 1e-9 and not hasattr(marcar, 'ok'):
            ax.plot([1 / np.e], [np.exp(-1 / np.e)], 'o', color=VERDE, ms=8)
            ax.annotate('mínimo em x = 1/e', (1 / np.e, np.exp(-1 / np.e)), (0.6, 0.35), arrowprops=dict(arrowstyle='->'))
            marcar.ok = 1
    _tangente_movel(path, f, df, (0.01, 1.7), (0, 2.5), '$y=x^x$', xs, marcar)


def a_custo_marginal(path):
    C = lambda x: 0.01 * x ** 3 - 0.6 * x ** 2 + 15 * x + 200
    fig, ax = plt.subplots(figsize=(6.4, 4.2)); eixos(ax, (0, 40), (150, 600))
    xx = np.linspace(0, 40, 300); ax.plot(xx, C(xx), color=AZUL, lw=2); ax.plot([20], [C(20)], 'wo')
    ax.set_xlabel('unidades'); ax.set_ylabel('mil R$')
    ax.plot(xx, C(20) + 3 * (xx - 20), color=LARANJA, ls='--', lw=1, label="tangente: C'(20) = 3")
    sec, = ax.plot([], [], color=VERDE, lw=1.6, label='secante'); q, = ax.plot([], [], 'o', color=VERDE)
    ax.legend(loc='upper left', fontsize=9); tt = ax.set_title('')
    hs = np.concatenate([np.linspace(15, 1, 50), [1] * 1]); N = len(hs)
    def up(i):
        h = hs[i]; m = (C(20 + h) - C(20)) / h
        sec.set_data(xx, C(20) + m * (xx - 20)); q.set_data([20 + h], [C(20 + h)])
        tt.set_text(f'h = {h:.1f}:  [C(20+h) − C(20)]/h = {m:.3f}'.replace('.', ','))
    salvar(fig, up, N, path)


def a_tangentes_por_ponto(path):
    f = lambda x: x ** 2; df = lambda x: 2 * x
    xs = np.sort(np.concatenate([np.linspace(-2.5, 4, 68), [-1.0, 3.0]]))
    def extra(ax):
        ax.plot([1], [-3], 's', color=TINTA, ms=7); ax.text(1.15, -3.4, '(1, −3)')
    def marcar(ax, a, m, tan):
        passa = abs(f(a) + m * (1 - a) + 3) < 1e-9
        tan.set_color(VERDE if passa else LARANJA); tan.set_linewidth(2.4 if passa else 1.4)
        if passa:
            ax.plot(np.linspace(-3, 5, 10), f(a) + m * (np.linspace(-3, 5, 10) - a), color=VERDE, lw=1, alpha=0.5)
    _tangente_movel(path, f, df, (-3, 5), (-5, 12), '$y=x^2$', xs, marcar, extra)


ANIM = {'tangente': a_tangente, 'grafico_derivada': a_grafico_derivada, 'por_partes': a_por_partes,
        'movimento': a_movimento, 'derivada_seno': a_derivada_seno, 'cadeia_tangente': a_cadeia_tangente,
        'inversa': a_inversa, 'implicita': a_implicita, 'xx': a_xx, 'custo_marginal': a_custo_marginal,
        'tangentes_por_ponto': a_tangentes_por_ponto}
