# Cálculo I — edição condensada em português

Adaptação e tradução de **Calculus Volume 1**, de Gilbert Strang (MIT) e Edwin "Jed" Herman
(University of Wisconsin–Stevens Point), publicado pela OpenStax (Rice University).
A meta é ter, em até 150 páginas, o essencial do Cálculo I para **revisar** o conteúdo:
definições, teoremas, exemplos-chave e figuras. Cada capítulo traz 65 exercícios, com a dificuldade indicada por pontos (• fácil, •• médio,
••• difícil, •••• desafio) e
respostas. Os marcados com ★ têm solução completa e animação do gráfico neste repositório.

📘 **[Baixar o PDF](Calculo_I.pdf)**

## Conteúdo

| Capítulo | Tema | Livro | Exercícios resolvidos |
|---|---|---|---|
| 1 | Funções e gráficos | ✅ | [65 exercícios, 11 resolvidos](exercicios/cap1/README.md) |
| 2 | Limites | ✅ | [65 exercícios, 12 resolvidos](exercicios/cap2/README.md) |
| 3 | Derivadas | ✅ | [65 exercícios, 11 resolvidos](exercicios/cap3/README.md) |
| 4 | Aplicações das derivadas | ✅ | [65 exercícios, 12 resolvidos](exercicios/cap4/README.md) |
| 5 | Integração | ✅ | [65 exercícios, 11 resolvidos](exercicios/cap5/README.md) |
| 6 | Aplicações da integração | ✅ | [65 exercícios, 11 resolvidos](exercicios/cap6/README.md) |
| 7 | Técnicas de integração | ✅ | [65 exercícios, 11 resolvidos](exercicios/cap7/README.md) |
| A | Formulário (apêndice) | ✅ | — |

Versão **1.0** (novembro de 2026): 107 páginas, 455 exercícios, todas as figuras em português, apêndice de fórmulas e índice remissivo.

Cada solução completa segue o mesmo roteiro: a **estratégia**, a resolução passo a passo, um
comentário sobre erros comuns ou interpretações e uma **animação** do gráfico do problema.

![Exemplo: secantes tendendo à tangente](exercicios/cap2/anim/ex-2.40.gif)

## Estrutura

```
Calculo_I.pdf          livro compilado
livro/                 fontes LaTeX (calculo1.tex, capN.tex, apendice.tex); figuras em TikZ/pgfplots
  exercicios_capN.tex  gerado automaticamente; não edite à mão
exercicios/capN/       soluções (README.md) e animações (anim/*.gif)
ferramentas/
  ex_capN.py           lista de 65 exercícios por capítulo, com respostas
  sol_capN.py          soluções completas dos exercícios ★
  anim_capN.py         animações (matplotlib)
  gerar.py             gera o .tex dos exercícios, os README e as animações
```

## Como compilar

```bash
pip install -r ferramentas/requirements.txt
python3 ferramentas/gerar.py            # exercícios + animações dos capítulos prontos
cd livro && latexmk -pdf calculo1.tex   # requer TeX Live com babel-portuges, pgfplots, tcolorbox e makeindex
```

Para gerar só os textos, sem refazer as animações: `python3 ferramentas/gerar.py --sem-animacoes`.

## Licença e créditos

Este trabalho é uma obra derivada de *Calculus Volume 1*, © 2016 Rice University,
disponível gratuitamente em <https://openstax.org/details/books/calculus-volume-1>,
licenciado sob [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
O capítulo 7 (Técnicas de integração) adapta o capítulo 3 de *Calculus Volume 2*, © 2016 Rice University
(<https://openstax.org/details/books/calculus-volume-2>), sob a mesma licença.
Esta adaptação (tradução, condensação, figuras redesenhadas, soluções e animações) é
distribuída sob a **mesma licença**, apenas para uso não comercial. Veja [LICENSE](LICENSE).

**Alterações em relação ao original:** tradução; condensação do texto; remoção dos pontos
de verificação, dos projetos e dos exercícios do original; listas de exercícios novas, por nível,
com soluções e animações; todas as figuras redesenhadas em português; apêndice de fórmulas e
índice remissivo.

Esta versão não é endossada pela OpenStax nem pela Rice University. Os nomes e logotipos
OpenStax e Rice University são marcas registradas e não fazem parte da licença.
*Access for free at openstax.org.*
