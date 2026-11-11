# -*- coding: utf-8 -*-
"""Utilidades comuns para as animações dos exercícios."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np

# Identidade visual Nexus BI: fundo grafite, curvas em branco, destaques em verde-nexus.
# (Os nomes AZUL/LARANJA/VERDE ficaram por compatibilidade com os scripts antigos.)
FUNDO = '#353535'     # grafite (cor institucional)
TINTA = '#E6E6E6'     # eixos, textos e marcadores
AZUL = '#FFFFFF'      # curva principal
LARANJA = '#AFE213'   # verde-nexus (cor institucional): destaques, áreas, tangentes
VERDE = '#B0B0B0'     # terceira série (cinza claro)
CINZA = '#808080'     # referências e tracejados

plt.rcParams.update({
    'font.size': 11, 'axes.titlesize': 12, 'axes.spines.top': False,
    'axes.spines.right': False, 'figure.dpi': 100, 'mathtext.fontset': 'cm',
    'axes.formatter.use_locale': False,
    'figure.facecolor': FUNDO, 'axes.facecolor': FUNDO, 'savefig.facecolor': FUNDO,
    'text.color': TINTA, 'axes.labelcolor': TINTA, 'axes.titlecolor': TINTA,
    'xtick.color': TINTA, 'ytick.color': TINTA, 'axes.edgecolor': '#8A8A8A',
    'grid.color': '#FFFFFF', 'legend.facecolor': '#2B2B2B', 'legend.edgecolor': '#5A5A5A',
    'legend.labelcolor': TINTA, 'patch.edgecolor': TINTA,
    'axes3d.xaxis.panecolor': (0.25, 0.25, 0.25, 1.0), 'axes3d.yaxis.panecolor': (0.23, 0.23, 0.23, 1.0),
    'axes3d.zaxis.panecolor': (0.27, 0.27, 0.27, 1.0),
})


def eixos(ax, xlim, ylim, grade=True):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.axhline(0, color=TINTA, lw=0.8); ax.axvline(0, color=TINTA, lw=0.8)
    if grade:
        ax.grid(alpha=0.12)


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
