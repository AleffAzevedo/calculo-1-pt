#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera, a partir de ex_capN.py:
  - livro/exercicios_capN.tex  (enunciados + respostas curtas, no livro)
  - exercicios/capN/README.md   (soluções completas, com animações)
  - exercicios/capN/anim/*.gif  (animações)
Uso: python3 gerar.py [N ...] [--sem-animacoes]
"""
import sys, os, re, importlib
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

REPO_URL = os.environ.get('REPO_URL', 'https://github.com/AleffAzevedo/calculo-1-pt')
TITULOS = {1: 'Funções e gráficos', 2: 'Limites'}


def chaves(s):
    return s.replace(r'\{', r'\lbrace ').replace(r'\}', r'\rbrace ')


def tex_para_md(s):
    s = chaves(s)
    s = s.replace(r'R\$\,', r'R\$ ').replace(r'\%', '%').replace('~', ' ')
    s = s.replace('\n', ' ')
    s = re.sub(r'\s+\(([a-d])\)\s', r'\n\n**(\1)** ', ' ' + s + ' ').strip()
    return s


def gerar(n, animar=True):
    ex = importlib.import_module(f'ex_cap{n}').EXERCICIOS
    an = importlib.import_module(f'anim_cap{n}').ANIM if animar else {}
    pasta = os.path.join(RAIZ, 'exercicios', f'cap{n}')
    os.makedirs(os.path.join(pasta, 'anim'), exist_ok=True)

    # ---------- LaTeX (livro)
    url = f'{REPO_URL}/tree/main/exercicios/cap{n}'
    t = ['% Gerado por ferramentas/gerar.py; não edite à mão.',
         '\\section*{Exercícios selecionados}',
         f'\\addcontentsline{{toc}}{{section}}{{Exercícios selecionados}}',
         'Problemas escolhidos para desenvolver a resolução de problemas. As soluções completas,',
         'com animações dos gráficos, estão no repositório do livro: '
         f'\\url{{{url}}}.\n',
         '\\begin{enumerate}[label=\\textbf{\\thechapter.\\arabic*}, leftmargin=2.6em, itemsep=6pt]']
    for e in ex:
        t.append(f'\\item \\textbf{{{e["titulo"]}.}} {e["enunciado"]}')
    t.append('\\end{enumerate}\n')
    t.append('\\subsection*{Respostas}\n{\\small\\begin{enumerate}[label=\\textbf{\\thechapter.\\arabic*}, leftmargin=2.6em, itemsep=2pt]')
    for e in ex:
        t.append(f'\\item {e["resposta"]}')
    t.append('\\end{enumerate}}\n')
    open(os.path.join(RAIZ, 'livro', f'exercicios_cap{n}.tex'), 'w').write('\n'.join(t))

    # ---------- Markdown (soluções)
    md = [f'# Capítulo {n} — {TITULOS[n]}: soluções dos exercícios selecionados\n',
          'Exercícios adaptados de *Calculus Volume 1* (OpenStax, CC BY-NC-SA 4.0). '
          'A numeração de origem indica a seção e o número do exercício no original.\n',
          '| Nº | Exercício | Origem |', '|---|---|---|']
    for e in ex:
        ancora = 'exercicio-' + e['id'].replace('.', '')
        md.append(f'| {e["id"]} | [{e["titulo"]}](#{ancora}) | {e["origem"]} |')
    md.append('')
    for e in ex:
        md.append(f'<a id="exercicio-{e["id"].replace(".", "")}"></a>\n')
        md.append(f'## {e["id"]} — {e["titulo"]}\n')
        md.append('> ' + tex_para_md(e['enunciado']).replace('\n\n', '\n>\n> ') + '\n')
        gif = f'anim/ex-{e["id"]}.gif'
        if e['id'] in an or os.path.exists(os.path.join(pasta, gif)):
            md.append(f'![Animação do exercício {e["id"]}]({gif})\n')
        md.append(chaves(e['solucao']).replace(r'R\$\,', r'R\$ ') + '\n')
        md.append('---\n')
    open(os.path.join(pasta, 'README.md'), 'w').write('\n'.join(md))

    # ---------- animações
    for e in ex:
        if e['id'] in an:
            caminho = os.path.join(pasta, f'anim/ex-{e["id"]}.gif')
            an[e['id']](caminho)
            print('  animação', caminho, f'{os.path.getsize(caminho)//1024} KB')


if __name__ == '__main__':
    animar = '--sem-animacoes' not in sys.argv
    caps = [int(a) for a in sys.argv[1:] if a.isdigit()] or [1, 2]
    for n in caps:
        print(f'Capítulo {n}')
        gerar(n, animar)
