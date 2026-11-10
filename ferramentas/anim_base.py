# -*- coding: utf-8 -*-
"""Utilidades comuns para as animações dos exercícios."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

AZUL = '#1F4E79'
LARANJA = '#C55A11'
VERDE = '#2E7D32'
CINZA = '#7f7f7f'

plt.rcParams.update({
    'font.size': 11, 'axes.titlesize': 12, 'axes.spines.top': False,
    'axes.spines.right': False, 'figure.dpi': 100, 'mathtext.fontset': 'cm',
    'axes.formatter.use_locale': False,
})


def eixos(ax, xlim, ylim, grade=True):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.axhline(0, color='black', lw=0.8); ax.axvline(0, color='black', lw=0.8)
    if grade:
        ax.grid(alpha=0.25)


def salvar(fig, update, n, caminho, fps=15, pausa_final=20):
    """Gera GIF com n quadros + pausa no último quadro."""
    frames = list(range(n)) + [n - 1] * pausa_final
    anim = FuncAnimation(fig, update, frames=frames, blit=False)
    anim.save(caminho, writer=PillowWriter(fps=fps))
    plt.close(fig)


def segmentos(x, y, salto=8.0):
    """Insere NaN onde y dá saltos grandes (assíntotas) para não ligar ramos."""
    y = np.array(y, dtype=float)
    d = np.abs(np.diff(y))
    y[1:][d > salto] = np.nan
    return y
