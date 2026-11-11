# -*- coding: utf-8 -*-
"""Animações dos exercícios selecionados do capítulo 2."""
import numpy as np
import matplotlib.pyplot as plt
from anim_base import *


def furo(ax, x, y, cor=AZUL):
    ax.plot([x], [y], 'o', mfc=FUNDO, mec=cor, ms=8, zorder=6)


def a2_1(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (0, 3.2), (0, 2.6))
    x = np.linspace(0.3, 3.2, 300); ax.plot(x, 1 / x, color=AZUL, lw=2)
    ax.plot([1], [1], 'wo', zorder=5)
    xt = np.linspace(0, 3.2, 10); tang, = ax.plot([], [], ':', color=CINZA, lw=1.5)
    sec, = ax.plot([], [], color=LARANJA, lw=1.8); q, = ax.plot([], [], 'o', color=LARANJA)
    tt = ax.set_title('')
    hs = np.concatenate([np.geomspace(1.8, 0.01, 40), -np.geomspace(0.6, 0.01, 30)]); N = len(hs)
    def up(i):
        h = hs[i]; m = (1 / (1 + h) - 1) / h
        sec.set_data(xt, 1 + m * (xt - 1)); q.set_data([1 + h], [1 / (1 + h)])
        tt.set_text(f'h = {h:+.3f}   inclinação da secante = {m:.4f}'.replace('.', ','))
        if i > N - 12: tang.set_data(xt, 1 - (xt - 1))
    salvar(fig, up, N, path)


def a2_2(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (-4, 4), (-1, 3.6))
    x = np.linspace(-4, 4, 800); x = x[np.abs(x) > 1e-3]
    linhas = []
    for a, c in zip((1, 2, 3), (CINZA, AZUL, LARANJA)):
        l, = ax.plot([], [], color=c, lw=2, label=f'a = {a}'); linhas.append((a, l, c))
    ax.legend(loc='upper right'); ax.set_title(r'$\dfrac{\operatorname{sen}(ax)}{x}\to a$ quando $x\to0$')
    N = 60
    def up(i):
        for j, (a, l, c) in enumerate(linhas):
            s = np.clip((i + 1) / N * 3 - j, 0, 1)
            if s > 0:
                k = int(len(x) * s); l.set_data(x[:k], np.sin(a * x[:k]) / x[:k])
            if s >= 1 and not hasattr(l, 'f'):
                furo(ax, 0, a, c); l.f = 1
    salvar(fig, up, N, path)


def a2_3(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (0, 16), (0, 8))
    t = np.linspace(0, 16, 400); ax.plot(t, np.sqrt(t) + 3, color=AZUL, lw=2); furo(ax, 9, 6)
    ax.set_title(r'$\dfrac{t-9}{\sqrt{t}-3}=\sqrt{t}+3$  para $t\neq9$')
    pe, = ax.plot([], [], 'o', color=LARANJA); pd, = ax.plot([], [], 'o', color=VERDE)
    ax.axhline(6, ls=':', color=CINZA); txt = ax.text(10.5, 2, '', fontsize=10)
    ds = np.geomspace(5, 0.02, 50); N = len(ds)
    g = lambda t: (t - 9) / (np.sqrt(t) - 3)
    def up(i):
        d = ds[i]; pe.set_data([9 - d], [g(9 - d)]); pd.set_data([9 + d], [g(9 + d)])
        txt.set_text(f'g(9−{d:.2f}) = {g(9-d):.3f}\ng(9+{d:.2f}) = {g(9+d):.3f}'.replace('.', ','))
    salvar(fig, up, N, path)


def a2_4(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (-3, 3), (-6, 6))
    f = lambda x: (x ** 2 + x + 1) / (x + 1)
    x1 = np.linspace(-3, -1.05, 200); x2 = np.linspace(-0.95, 3, 300)
    ax.plot(x1, f(x1), color=AZUL, lw=2); ax.plot(x2, f(x2), color=AZUL, lw=2)
    ax.axvline(-1, ls='--', color=LARANJA, lw=1); furo(ax, 1, 1.5)
    ax.set_title(r'$\dfrac{x^3-1}{x^2-1}$: buraco em $(1,\,3/2)$ e assíntota $x=-1$')
    pe, = ax.plot([], [], 'o', color=LARANJA); pd, = ax.plot([], [], 'o', color=VERDE)
    ds = np.geomspace(1.5, 0.01, 50); N = len(ds); txt = ax.text(1.2, -4, '')
    def up(i):
        d = ds[i]; pe.set_data([1 - d], [f(1 - d)]); pd.set_data([1 + d], [f(1 + d)])
        txt.set_text(f'f(1±{d:.2f}) → {f(1-d):.3f}, {f(1+d):.3f}'.replace('.', ','))
    salvar(fig, up, N, path)


def a2_5(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (-1, 3), (-60, 60))
    f = lambda x: (2 * x ** 2 + 7 * x - 4) / (x ** 2 + x - 2)
    for xs in (np.linspace(-1, 0.99, 300), np.linspace(1.01, 3, 300)):
        ax.plot(xs, f(xs), color=AZUL, lw=2)
    ax.axvline(1, ls='--', color=LARANJA)
    ax.set_title(r'$\dfrac{2x^2+7x-4}{(x+2)(x-1)}$ perto de $x=1$')
    pe, = ax.plot([], [], 'o', color=LARANJA, ms=8); pd, = ax.plot([], [], 'o', color=VERDE, ms=8)
    txt = ax.text(1.6, -45, '', fontsize=10)
    ds = np.geomspace(0.8, 0.08, 50); N = len(ds)
    def up(i):
        d = ds[i]; pe.set_data([1 - d], [f(1 - d)]); pd.set_data([1 + d], [f(1 + d)])
        txt.set_text(f'esq.: {f(1-d):.1f}\ndir.: {f(1+d):.1f}'.replace('.', ','))
    salvar(fig, up, N, path)


def a2_6(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    tt = ax.set_title(''); N = 60
    def up(i):
        ax.cla(); w = 1.0 * 0.92 ** i
        x = np.linspace(-w, w, 4000); x = x[x != 0]
        ax.plot(x, x ** 2 * np.cos(1 / x), color=AZUL, lw=1)
        ax.plot(x, x ** 2, '--', color=LARANJA); ax.plot(x, -x ** 2, '--', color=LARANJA)
        ax.axhline(0, color=TINTA, lw=0.6); ax.axvline(0, color=TINTA, lw=0.6)
        ax.set_xlim(-w, w); ax.set_ylim(-1.2 * w ** 2, 1.2 * w ** 2)
        ax.set_title(r'$-\theta^2\leq\theta^2\cos(1/\theta)\leq\theta^2$   (zoom ×' + f'{1/w:.0f})')
    salvar(fig, up, N, path)


def a2_7(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    tt = ax.set_title(''); ks = np.concatenate([np.linspace(3, -5, 50)]); N = len(ks)
    def up(i):
        k = ks[i]; ax.cla(); eixos(ax, (-12, 9), (-40, 20))
        x1 = np.linspace(-12, k, 100); x2 = np.linspace(k, 8, 100)
        ax.plot(x1, 3 * x1 + 2, color=AZUL, lw=2); ax.plot(x2, 2 * x2 - 3, color=LARANJA, lw=2)
        salto = (3 * k + 2) - (2 * k - 3)
        if abs(salto) > 1e-9: furo(ax, k, 3 * k + 2)
        ax.plot([k], [2 * k - 3], 'o', color=LARANJA)
        ax.set_title(f'k = {k:.2f}:  salto = {salto:.2f}'.replace('.', ',') + ('  ✔ contínua' if abs(salto) < 1e-9 else ''))
    salvar(fig, up, N, path)


def a2_8(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    ks = np.linspace(0.2, np.log(7) / 4, 50); N = len(ks)
    def up(i):
        k = ks[i]; ax.cla(); eixos(ax, (0, 8.5), (0, 12))
        x1 = np.linspace(0, 4, 100); x2 = np.linspace(4, 8, 50)
        ax.plot(x1, np.exp(k * x1), color=AZUL, lw=2); ax.plot(x2, x2 + 3, color=LARANJA, lw=2)
        if i < N - 1: furo(ax, 4, np.exp(4 * k))
        ax.plot([4], [7], 'o', color=LARANJA)
        ok = '  ✔' if i == N - 1 else ''
        ax.set_title(f'k = {k:.4f}:  e^(4k) = {np.exp(4*k):.3f}  (precisa ser 7){ok}'.replace('.', ','))
    salvar(fig, up, N, path)


def a2_9(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eixos(ax, (1.5, 5.5), (0, 6.5)); ax.set_xlabel('t')
    t = np.linspace(2, 5, 300)
    s = 5 - (t - 2) + 1.2 * np.sin(2.2 * (t - 2)) * (t - 2) * (5 - t) / 2.25
    ax.plot([1.5, 5.5], [1.5, 5.5], '--', color=LARANJA, label='$y=t$')
    l, = ax.plot([], [], color=AZUL, lw=2, label='$s(t)$ (exemplo)'); ax.legend(loc='upper right')
    ax.plot([2, 5], [5, 2], 'wo'); ax.set_title('TVI: $h(t)=s(t)-t$ muda de sinal em $[2,5]$')
    pt, = ax.plot([], [], 'o', color=VERDE, ms=9); N = 60
    idx = np.argmin(np.abs(s - t))
    def up(i):
        k = int(len(t) * (i + 1) / N); l.set_data(t[:k], s[:k])
        if k > idx: pt.set_data([t[idx]], [s[idx]])
    salvar(fig, up, N, path)


def a2_10(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    g = lambda x: 2 ** x - x ** 3
    lo, hi = 1.25, 1.375; passos = []
    for _ in range(10):
        passos.append((lo, hi)); m = (lo + hi) / 2
        if g(m) > 0: lo = m
        else: hi = m
    N = len(passos) * 6
    def up(i):
        a, b = passos[min(i // 6, len(passos) - 1)]; ax.cla()
        pad = (b - a) * 0.6; x = np.linspace(a - pad, b + pad, 300)
        ax.plot(x, g(x), color=AZUL, lw=2); ax.axhline(0, color=TINTA, lw=0.7)
        ax.axvspan(a, b, color=LARANJA, alpha=0.26)
        ax.plot([a, b], [g(a), g(b)], 'o', color=LARANJA)
        ax.set_title(f'g(x)=2^x − x³ em [{a:.5f}; {b:.5f}]'.replace('.', ','))
    salvar(fig, up, N, path)


def a2_11(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    eps = np.geomspace(4, 0.3, 40); N = len(eps)
    f = lambda x: x ** 2 + 2 * x
    def up(i):
        e = eps[i]; d = min(1, e / 7); ax.cla()
        w = 5 * d; x = np.linspace(2 - w, 2 + w, 300)
        ax.axhspan(8 - e, 8 + e, color=LARANJA, alpha=0.26); ax.axvspan(2 - d, 2 + d, color=AZUL, alpha=0.31)
        ax.plot(x, f(x), color=AZUL, lw=2); ax.plot([2], [8], 'wo')
        ax.set_xlim(2 - w, 2 + w); ax.set_ylim(8 - 2.5 * e, 8 + 2.5 * e)
        ax.set_title(f'ε = {e:.3f}   δ = min(1, ε/7) = {d:.4f}'.replace('.', ','))
    salvar(fig, up, N, path)


def a2_12(path):
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    Ls = np.concatenate([np.linspace(-1, 1, 40), np.linspace(1, 0, 20)]); N = len(Ls)
    def up(i):
        L = Ls[i]; ax.cla(); eixos(ax, (-1, 3), (-2, 2))
        ax.plot([-1, 1], [-1, -1], color=AZUL, lw=2); ax.plot([1, 3], [1, 1], color=AZUL, lw=2)
        furo(ax, 1, -1); furo(ax, 1, 1)
        ax.axhspan(L - 0.5, L + 0.5, color=LARANJA, alpha=0.2)
        ax.axhline(L, color=LARANJA, ls='--', lw=1)
        ax.set_title(f'candidato L = {L:.2f}: a faixa (L−½, L+½) não contém −1 e 1'.replace('.', ','))
    salvar(fig, up, N, path)


ANIM = {'2.1': a2_1, '2.2': a2_2, '2.3': a2_3, '2.4': a2_4, '2.5': a2_5, '2.6': a2_6,
        '2.7': a2_7, '2.8': a2_8, '2.9': a2_9, '2.10': a2_10, '2.11': a2_11, '2.12': a2_12}
