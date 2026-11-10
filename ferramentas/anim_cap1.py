# -*- coding: utf-8 -*-
"""Animações dos exercícios selecionados do capítulo 1."""
import numpy as np
import matplotlib.pyplot as plt
from anim_base import *


def a1_1(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (-10, 6), (-8, 12))
    f = lambda x: 3 * x / (x + 4)
    ax.axvline(-4, ls='--', color=LARANJA, lw=1)
    ax.axhline(3, ls=':', color=CINZA, lw=1)
    xs1 = np.linspace(-10, -4.05, 300); xs2 = np.linspace(-3.95, 6, 300)
    ax.plot(xs1, f(xs1), color=AZUL, alpha=0.25); ax.plot(xs2, f(xs2), color=AZUL, alpha=0.25)
    ax.plot([0], [0], 'o', mfc='white', mec=AZUL, ms=8, zorder=5)
    ax.set_title(r'$(f\circ g)(x)=\dfrac{3x}{x+4}$,  $x\neq0,\,-4$')
    ax.text(-3.8, 10.5, 'assíntota $x=-4$', color=LARANJA, fontsize=9)
    ax.text(0.3, -1.3, 'buraco em $x=0$', color=AZUL, fontsize=9)
    trilha, = ax.plot([], [], color=AZUL, lw=2.2); pt, = ax.plot([], [], 'o', color=AZUL)
    xs = np.concatenate([xs1, xs2]); N = 80
    def up(i):
        k = int(len(xs) * (i + 1) / N)
        x = xs[:k]; y = f(x).astype(float)
        y[(x > -4.1) & (x < -3.9)] = np.nan
        x2 = x[np.abs(x) > 0.03]; y2 = f(x2)
        trilha.set_data(x, y)
        if k: pt.set_data([xs[k - 1]], [f(xs[k - 1])])
    salvar(fig, up, N, path)


def a1_2(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (0, 300), (0, 460))
    C = lambda x: 0.75 * x + 125; R = lambda x: 1.5 * x
    ax.set_xlabel('cupcakes $x$'); ax.set_ylabel('R$')
    ax.set_title('Custo $C=0{,}75x+125$  ×  Receita $R=1{,}50x$')
    lc, = ax.plot([], [], color=AZUL, lw=2, label='custo'); lr, = ax.plot([], [], color=LARANJA, lw=2, label='receita')
    ax.legend(loc='upper left')
    fill = []
    N = 70; xe = 500 / 3
    txt = ax.text(180, 60, '', fontsize=10)
    def up(i):
        x = np.linspace(0, 300 * (i + 1) / N, 200)
        lc.set_data(x, C(x)); lr.set_data(x, R(x))
        for f_ in fill: f_.remove()
        fill.clear()
        m = x > xe
        if m.any():
            fill.append(ax.fill_between(x[m], C(x[m]), R(x[m]), color=VERDE, alpha=0.2))
            if not hasattr(up, 'm'):
                ax.plot([xe], [C(xe)], 'ko'); ax.annotate('equilíbrio\n$x\\approx166{,}7$', (xe, C(xe)), (60, 330),
                    arrowprops=dict(arrowstyle='->'), fontsize=9); up.m = 1
            txt.set_text('lucro'); txt.set_color(VERDE)
    salvar(fig, up, N, path)


def a1_3(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (-2 * np.pi, 2 * np.pi), (0, 12))
    ax.set_xticks(np.arange(-2, 2.5, 0.5) * np.pi)
    ax.set_xticklabels([r'$-2\pi$', '', r'$-\pi$', '', '0', '', r'$\pi$', '', r'$2\pi$'])
    for k in (-1.5, -0.5, 0.5, 1.5): ax.axvline(k * np.pi, ls='--', color=LARANJA, lw=0.8)
    ax.set_title(r'$\frac{1}{1-\sin\alpha}+\frac{1}{1+\sin\alpha}$ (curva) e $2\sec^2\alpha$ (pontos)')
    a = np.linspace(-2 * np.pi, 2 * np.pi, 1500)
    L = 1 / (1 - np.sin(a)) + 1 / (1 + np.sin(a)); L = segmentos(a, L, 3)
    l1, = ax.plot([], [], color=AZUL, lw=2); p2, = ax.plot([], [], 'o', color=LARANJA, ms=4)
    ap = np.linspace(-2 * np.pi, 2 * np.pi, 120); R = 2 / np.cos(ap) ** 2
    N = 70
    def up(i):
        k = int(len(a) * (i + 1) / N); l1.set_data(a[:k], L[:k])
        kk = int(len(ap) * (i + 1) / N); p2.set_data(ap[:kk], R[:kk])
    salvar(fig, up, N, path)


def a1_4(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    N_ = lambda t: 12 + 3 * np.sin(2 * np.pi / 365 * (t - 79))
    eixos(ax, (0, 365), (6, 17)); ax.axhline(6, color='black')
    ax.axhline(15, ls='--', color=LARANJA, lw=1); ax.axhline(9, ls='--', color=LARANJA, lw=1)
    ax.text(5, 15.3, 'dia mais longo: 15 h', color=LARANJA, fontsize=9)
    ax.text(5, 8.3, 'dia mais curto: 9 h', color=LARANJA, fontsize=9)
    ax.set_xlabel('dias após 1º de janeiro'); ax.set_ylabel('horas de luz')
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    ax.set_xticks(np.arange(12) * 30.4); ax.set_xticklabels(meses, fontsize=8)
    ax.set_title(r'$N(t)=12+3\sin\left[\frac{2\pi}{365}(t-79)\right]$')
    l, = ax.plot([], [], color=AZUL, lw=2); p, = ax.plot([], [], 'o', color=AZUL)
    txt = ax.text(250, 10, '', fontsize=10)
    t = np.linspace(0, 365, 400); N = 80
    def up(i):
        k = int(len(t) * (i + 1) / N); l.set_data(t[:k], N_(t[:k])); p.set_data([t[k - 1]], [N_(t[k - 1])])
        txt.set_text(f'dia {int(t[k-1])}: {N_(t[k-1]):.2f} h'.replace('.', ','))
    salvar(fig, up, N, path)


def a1_5(path):
    fig, ax = plt.subplots(figsize=(5.4, 5.0))
    eixos(ax, (0, 160), (0, 160)); ax.set_aspect('equal')
    C = lambda p: 75 * p / (85 - p)
    p = np.linspace(0, 70, 300); c = C(p)
    ax.plot([0, 160], [0, 160], ':', color=CINZA)
    ax.plot(p, c, color=AZUL, lw=2, label='$C(p)=75p/(85-p)$')
    ax.axvline(85, ls='--', color=AZUL, lw=0.8)
    lr, = ax.plot([], [], color=LARANJA, lw=2, label='$C^{-1}$: $p=85C/(C+75)$')
    asy, = ax.plot([], [], ls='--', color=LARANJA, lw=0.8)
    ax.legend(loc='upper left', fontsize=9); ax.set_title('Reflexão em torno de $y=x$')
    N = 60
    def up(i):
        s = (i + 1) / N
        # interpola cada ponto (p,c) -> (c,p)
        X = (1 - s) * p + s * c; Y = (1 - s) * c + s * p
        lr.set_data(X, Y)
        if s > 0.98:
            asy.set_data([0, 160], [85, 85])
    salvar(fig, up, N, path)


def a1_6(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    D = lambda t: 5 * np.sin(np.pi / 6 * t - 7 * np.pi / 6) + 8
    eixos(ax, (0, 24), (0, 14))
    ax.axhline(11.75, ls='--', color=LARANJA, lw=1); ax.text(0.3, 12.1, '11,75 pés', color=LARANJA, fontsize=9)
    ax.set_xlabel('horas após a meia-noite'); ax.set_ylabel('profundidade (pés)')
    ax.set_title(r'$D(t)=5\sin\left(\frac{\pi}{6}t-\frac{7\pi}{6}\right)+8$')
    t1 = 7 + 6 * np.arcsin(0.75) / np.pi
    tt = np.linspace(0, 24, 500)
    ax.plot(tt, D(tt), color=AZUL, alpha=0.15)
    l, = ax.plot([], [], color=AZUL, lw=2); p, = ax.plot([], [], 'o', color=AZUL)
    N = 60; txt = ax.text(14, 2, '', fontsize=10)
    def up(i):
        T = t1 * (i + 1) / N; t = np.linspace(0, T, 200)
        l.set_data(t, D(t)); p.set_data([T], [D(T)])
        if i == N - 1:
            p.set_color(LARANJA); txt.set_text(f't ≈ 8,62 h  (≈ 8h37)')
    salvar(fig, up, N, path)


def a1_7(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (-2, 2), (-4, 8))
    x = np.linspace(-2, 2, 400)
    lc, = ax.plot([], [], color=AZUL, lw=1.5, ls='--', label=r'$\cosh kx$')
    ls_, = ax.plot([], [], color=VERDE, lw=1.5, ls='--', label=r'$\sinh kx$')
    le, = ax.plot([], [], color=LARANJA, lw=3, alpha=0.6, label=r'$e^{kx}$')
    lsum, = ax.plot([], [], color='black', lw=1.2, label=r'$\cosh kx+\sinh kx$')
    ax.legend(loc='upper left', fontsize=9); tt = ax.set_title('')
    ks = np.concatenate([np.linspace(0.3, 2, 40), np.linspace(2, -1, 40)]); N = len(ks)
    def up(i):
        k = ks[i]
        lc.set_data(x, np.cosh(k * x)); ls_.set_data(x, np.sinh(k * x))
        le.set_data(x, np.exp(k * x)); lsum.set_data(x, np.cosh(k * x) + np.sinh(k * x))
        tt.set_text(f'k = {k:.2f}'.replace('.', ','))
    salvar(fig, up, N, path)


def a1_8(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    k = 0.08664; T = np.log(20) / k
    eixos(ax, (0, 50), (0, 105))
    ax.axhline(5, ls='--', color=LARANJA, lw=1); ax.text(38, 8, 'restam 5%', color=LARANJA, fontsize=9)
    for j in range(1, 6):
        ax.axvline(j * np.log(2) / k, color=CINZA, lw=0.6, ls=':')
    ax.text(8.3, 95, 'meias-vidas (≈ 8 dias)', color=CINZA, fontsize=8)
    ax.set_xlabel('dias'); ax.set_ylabel('% restante'); ax.set_title(r'$Q(t)=Q_0\,e^{-0{,}08664\,t}$')
    l, = ax.plot([], [], color=AZUL, lw=2); p, = ax.plot([], [], 'o', color=AZUL); txt = ax.text(30, 50, '')
    N = 70
    def up(i):
        t = np.linspace(0, T * (i + 1) / N, 200); l.set_data(t, 100 * np.exp(-k * t))
        p.set_data([t[-1]], [100 * np.exp(-k * t[-1])])
        txt.set_text(f't = {t[-1]:.1f} dias'.replace('.', ','))
    salvar(fig, up, N, path)


def a1_9(path):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8, 3.8))
    k = np.log(2) / 12; T = np.log(200) / k
    for a in (a1, a2):
        a.set_xlim(0, 100); a.grid(alpha=0.25); a.set_xlabel('horas')
        a.axhline(200000, ls='--', color=LARANJA, lw=1)
    a1.set_ylim(0, 220000); a1.set_title('escala linear')
    a2.set_yscale('log'); a2.set_ylim(800, 300000); a2.set_title('escala logarítmica')
    l1, = a1.plot([], [], color=AZUL, lw=2); l2, = a2.plot([], [], color=AZUL, lw=2)
    fig.suptitle(r'$Q(t)=1000\,e^{kt}$,  $k=\ln 2/12\approx0{,}0578$; 200 mil em $t\approx91{,}7$ h', fontsize=11)
    fig.tight_layout(); N = 70
    def up(i):
        t = np.linspace(0, T * (i + 1) / N, 200); q = 1000 * np.exp(k * t)
        l1.set_data(t, q); l2.set_data(t, q)
    salvar(fig, up, N, path)


def a1_10(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ax.set_yscale('log'); ax.set_ylim(0.5, 5000); ax.set_xlim(-0.6, 1.6)
    ax.set_xticks([0, 1]); ax.set_xticklabels(['Japão\n(4,9)', 'terremoto\nvariável'])
    ax.set_ylabel('intensidade relativa'); ax.grid(axis='y', alpha=0.3)
    ax.bar([0], [1], color=CINZA, width=0.6)
    b = ax.bar([1], [1], color=AZUL, width=0.6)[0]
    txt = ax.set_title('')
    Ms = np.linspace(4.9, 8.3, 60); N = len(Ms)
    def up(i):
        r = 10 ** (Ms[i] - 4.9); b.set_height(r)
        if i == N - 1: b.set_color(LARANJA)
        txt.set_text(f'magnitude {Ms[i]:.1f}:  {r:,.0f} vezes mais intenso'.replace(',', 'X').replace('.', ',').replace('X', '.'))
    salvar(fig, up, N, path)


def a1_11(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    P = lambda t: 82.5 - 67.5 * np.cos(np.pi / 6 * t)
    eixos(ax, (0, 12), (0, 160)); ax.set_xlabel('meses (0 = 1º de janeiro)'); ax.set_ylabel('mil habitantes')
    ax.set_title(r'$P(t)=82{,}5-67{,}5\cos\left(\frac{\pi}{6}t\right)$')
    ax.axhline(20, ls='--', color=AZUL, lw=0.8); ax.axhline(140, ls='--', color=LARANJA, lw=0.8)
    a = np.arccos(62.5 / 67.5) * 6 / np.pi; b = np.arccos(-57.5 / 67.5) * 6 / np.pi
    l, = ax.plot([], [], color='black', lw=2); N = 70; st = {}
    def up(i):
        T = 12 * (i + 1) / N; t = np.linspace(0, T, 300); l.set_data(t, P(t))
        if T > 12 - b and 'o' not in st:
            st['o'] = 1; ax.axvspan(b, 12 - b, color=LARANJA, alpha=0.15)
            ax.text(5.1, 148, '> 140 mil', color=LARANJA, fontsize=9)
        if T > 12 - a and 'b' not in st:
            st['b'] = 1; ax.axvspan(0, a, color=AZUL, alpha=0.15); ax.axvspan(12 - a, 12, color=AZUL, alpha=0.15)
            ax.text(0.1, 25, '< 20 mil', color=AZUL, fontsize=9)
    salvar(fig, up, N, path)


ANIM = {'1.1': a1_1, '1.2': a1_2, '1.3': a1_3, '1.4': a1_4, '1.5': a1_5, '1.6': a1_6,
        '1.7': a1_7, '1.8': a1_8, '1.9': a1_9, '1.10': a1_10, '1.11': a1_11}
