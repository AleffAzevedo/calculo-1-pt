#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera, a partir de ex_capN.py (lista) e sol_capN.py (soluções completas):
  - livro/exercicios_capN.tex  (lista por nível + respostas, no livro)
  - exercicios/capN/README.md   (lista com respostas ocultas + soluções completas)
  - exercicios/capN/anim/*.gif  (animações das soluções completas)
Uso: python3 gerar.py [N ...] [--sem-animacoes]
"""
import sys, os, re, glob, importlib
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

REPO_URL = os.environ.get('REPO_URL', 'https://github.com/AleffAzevedo/calculo-1-pt')
TITULOS = {1: 'Funções e gráficos', 2: 'Limites'}
PONTOS = {'F': 1, 'M': 2, 'D': 3, 'X': 4}


def chaves(s):
    return s.replace(r'\{', r'\lbrace ').replace(r'\}', r'\rbrace ')


def tex_para_md(s):
    s = chaves(s).replace(r'R\$\,', r'R\$ ').replace(r'\%', '%').replace('~', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def montar(n):
    lista = importlib.import_module(f'ex_cap{n}').LISTA
    sols = {s['id']: s for s in importlib.import_module(f'sol_cap{n}').SOLUCOES}
    itens = []
    for k, (nivel, enun, resp) in enumerate(lista, 1):
        it = dict(num=f'{n}.{k}', nivel=nivel, sol=None, titulo=None)
        if enun.startswith('sol:'):
            s = sols[enun[4:]]
            it.update(enunciado=s['enunciado'], resposta=s['resposta'], titulo=s['titulo'],
                      sol=s, chave=s['id'])
        else:
            it.update(enunciado=enun, resposta=resp)
        itens.append(it)
    return itens


def gerar(n, animar=True):
    itens = montar(n)
    pasta = os.path.join(RAIZ, 'exercicios', f'cap{n}')
    os.makedirs(os.path.join(pasta, 'anim'), exist_ok=True)
    url = f'{REPO_URL}/blob/main/exercicios/cap{n}/README.md'

    # ---------------- LaTeX
    t = ['% Gerado por ferramentas/gerar.py; não edite à mão.',
         '\\section*{Exercícios}', '\\addcontentsline{toc}{section}{Exercícios}',
         'Os pontos antes de cada número indicam a dificuldade: \\nivel{1} fácil, \\nivel{2} médio, '
         '\\nivel{3} difícil e \\nivel{4} desafio. Os exercícios marcados com \\estrela{} têm solução completa, '
         f'com animação do gráfico, no repositório do livro: \\url{{{url}}}. '
         'As respostas estão no fim do capítulo.\n',
         '\\begin{itemize}[leftmargin=5.2em,labelsep=0.6em,itemsep=4pt]']
    for i in itens:
        est = '\\estrela\\ ' if i['sol'] else ''
        tit = f'\\textbf{{{i["titulo"]}.}} ' if i['titulo'] else ''
        t.append(f'\\item[\\exnum{{{PONTOS[i["nivel"]]}}}{{{i["num"]}}}] {est}{tit}{i["enunciado"]}')
    t.append('\\end{itemize}')
    t.append('\\subsection*{Respostas}\n{\\small\\begin{multicols}{2}\\raggedright')
    t.append('\\begin{itemize}[leftmargin=2.7em,labelsep=0.5em,itemsep=1pt]')
    for i in itens:
        t.append(f'\\item[\\textbf{{{i["num"]}}}] {i["resposta"]}')
    t.append('\\end{itemize}\\end{multicols}}\n')
    open(os.path.join(RAIZ, 'livro', f'exercicios_cap{n}.tex'), 'w').write('\n'.join(t))

    # ---------------- Markdown
    md = [f'# Capítulo {n} — {TITULOS[n]}: exercícios\n',
          'São 65 exercícios. Os pontos antes de cada número indicam a dificuldade: '
          '**•** fácil, **••** médio, **•••** difícil e **••••** desafio. '
          'Tente resolver antes de abrir a resposta. Os marcados com ★ têm '
          '[solução completa com animação](#soluções-completas).\n',
          'Muitos enunciados são adaptados de *Calculus Volume 1* (OpenStax, CC BY-NC-SA 4.0).\n',
          '## Lista\n']
    for i in itens:
        est = f' ★ [ver solução](#ex-{i["num"].replace(".", "-")})' if i['sol'] else ''
        tit = f'**{i["titulo"]}.** ' if i['titulo'] else ''
        md.append(f'`{"•" * PONTOS[i["nivel"]]}` **{i["num"]}** {tit}{tex_para_md(i["enunciado"])}{est}\n')
        md.append(f'<details><summary>Resposta</summary>\n\n{tex_para_md(i["resposta"])}\n\n</details>\n')
    md.append('## Soluções completas\n')
    for i in [i for i in itens if i['sol']]:
        s = i['sol']
        md.append(f'<a id="ex-{i["num"].replace(".", "-")}"></a>\n')
        md.append(f'### {i["num"]} — {s["titulo"]}\n')
        md.append(f'*Origem: OpenStax, {s["origem"]}.*\n')
        md.append('> ' + tex_para_md(s['enunciado']) + '\n')
        md.append(f'![Animação do exercício {i["num"]}](anim/ex-{i["num"]}.gif)\n')
        md.append(chaves(s['solucao']).replace(r'R\$\,', r'R\$ ') + '\n')
        md.append('---\n')
    open(os.path.join(pasta, 'README.md'), 'w').write('\n'.join(md))

    # ---------------- animações
    if animar:
        an = importlib.import_module(f'anim_cap{n}').ANIM
        for f in glob.glob(os.path.join(pasta, 'anim', '*.gif')):
            os.remove(f)
        for i in [i for i in itens if i['sol']]:
            caminho = os.path.join(pasta, f'anim/ex-{i["num"]}.gif')
            an[i['chave']](caminho)
            print('  animação', os.path.relpath(caminho, RAIZ))


if __name__ == '__main__':
    animar = '--sem-animacoes' not in sys.argv
    caps = [int(a) for a in sys.argv[1:] if a.isdigit()] or [1, 2]
    for n in caps:
        print(f'Capítulo {n}')
        gerar(n, animar)
