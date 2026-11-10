# -*- coding: utf-8 -*-
"""Exercícios selecionados do capítulo 2 (adaptados de OpenStax, Calculus Volume 1)."""

EXERCICIOS = [
dict(id='2.1', origem='2.3, ex. 98', titulo='Da secante à tangente',
enunciado=r"""Calcule $\displaystyle\lim_{h\to0}\frac{\frac{1}{a+h}-\frac1a}{h}$, em que $a\neq0$ é constante.
Interprete o resultado em termos de retas secantes ao gráfico de $f(x)=1/x$.""",
resposta=r"""$-\dfrac{1}{a^2}$: é a inclinação da reta tangente a $y=1/x$ em $x=a$.""",
solucao=r"""Forma $0/0$ com fração composta: simplificamos o numerador.
$$\frac{\frac{1}{a+h}-\frac1a}{h}=\frac{\frac{a-(a+h)}{a(a+h)}}{h}=\frac{-h}{a(a+h)\,h}=\frac{-1}{a(a+h)}\quad(h\neq0).$$
Logo
$$\lim_{h\to0}\frac{-1}{a(a+h)}=-\frac{1}{a^2}.$$

**Interpretação.** A expressão é a inclinação da secante ao gráfico de $f(x)=1/x$ pelos pontos $(a,f(a))$ e $(a+h,f(a+h))$. Quando $h\to0$, as secantes tendem à **tangente**, cuja inclinação é $-1/a^2$. Esse é exatamente o cálculo da derivada de $1/x$, que veremos no capítulo 3.

**Animação.** Com $a=1$, as secantes giram até a tangente de inclinação $-1$ conforme $h\to0$, pela direita e pela esquerda.""",
),
dict(id='2.2', origem='2.2, ex. 35–37', titulo='O limite de $\\sin(ax)/x$',
enunciado=r"""(a) Use tabelas com $x=\pm0{,}1;\ \pm0{,}01;\ \pm0{,}001$ para estimar
$\lim_{x\to0}\frac{\sin2x}{x}$ e $\lim_{x\to0}\frac{\sin3x}{x}$.
(b) Conjecture o valor de $\lim_{x\to0}\frac{\sin ax}{x}$ para $a>0$ e prove-o com o
Teorema~2.7.""",
resposta=r"""(a) 2 e 3; (b) $\lim_{x\to0}\frac{\sin ax}{x}=a$.""",
solucao=r"""**(a)** Para $\frac{\sin2x}{x}$: $x=0{,}1\Rightarrow1{,}98669$; $x=0{,}01\Rightarrow1{,}99987$; $x=0{,}001\Rightarrow1{,}9999987$. A função é par, então os valores para $-x$ são iguais. O limite parece ser **2**.
Para $\frac{\sin3x}{x}$: $2{,}95520$; $2{,}99955$; $2{,}9999955$, que parecem tender a **3**.

**(b)** Conjectura: o limite é $a$. Prova: com $\theta=ax$, temos $\theta\to0$ quando $x\to0$, e
$$\frac{\sin ax}{x}=a\cdot\frac{\sin ax}{ax}=a\cdot\frac{\sin\theta}{\theta}\longrightarrow a\cdot1=a .$$

**Animação.** O gráfico de $\frac{\sin ax}{x}$ para $a=1,2,3$: o "buraco" em $x=0$ fica exatamente na altura $a$.""",
),
dict(id='2.3', origem='2.3, ex. 97', titulo='Conjugado com raiz',
enunciado=r"""Mostre que a substituição direta leva a uma forma indeterminada e calcule
$\displaystyle\lim_{t\to9}\frac{t-9}{\sqrt t-3}$.""",
resposta=r"""$0/0$; o limite é 6.""",
solucao=r"""Substituindo: $\frac{9-9}{3-3}=\frac00$, indeterminado.

**Caminho 1 (fatoração).** $t-9=(\sqrt t)^2-3^2=(\sqrt t-3)(\sqrt t+3)$. Para $t\neq9$:
$$\frac{t-9}{\sqrt t-3}=\sqrt t+3\ \Longrightarrow\ \lim_{t\to9}(\sqrt t+3)=6 .$$

**Caminho 2 (conjugado).** Multiplicar por $\frac{\sqrt t+3}{\sqrt t+3}$ dá $\frac{(t-9)(\sqrt t+3)}{t-9}=\sqrt t+3$, que é o mesmo resultado.

**Animação.** O gráfico é o de $\sqrt t+3$ com um buraco em $(9,6)$; pontos pela esquerda e pela direita se aproximam da altura 6.""",
),
dict(id='2.4', origem='2.3, ex. 100', titulo='Fatorando cubos',
enunciado=r"""Calcule $\displaystyle\lim_{x\to1}\frac{x^3-1}{x^2-1}$.""",
resposta=r"""$\dfrac32$.""",
solucao=r"""Forma $0/0$. Fatoramos com $a^3-b^3=(a-b)(a^2+ab+b^2)$ e $a^2-b^2=(a-b)(a+b)$:
$$\frac{x^3-1}{x^2-1}=\frac{(x-1)(x^2+x+1)}{(x-1)(x+1)}=\frac{x^2+x+1}{x+1}\quad(x\neq1).$$
Então $\lim_{x\to1}\frac{x^2+x+1}{x+1}=\frac{3}{2}$.

**Comentário.** Em $x=1$ há uma descontinuidade **removível** (o limite existe). Em $x=-1$, o fator $x+1$ permanece no denominador e o numerador vale 1: há uma assíntota vertical.

**Animação.** O ponto se aproxima de $x=1$ pelos dois lados, rumo ao buraco em $(1,\,3/2)$.""",
),
dict(id='2.5', origem='2.3, ex. 105–106', titulo='Limites laterais infinitos',
enunciado=r"""Calcule $\displaystyle\lim_{x\to1^-}\frac{2x^2+7x-4}{x^2+x-2}$ e
$\displaystyle\lim_{x\to1^+}\frac{2x^2+7x-4}{x^2+x-2}$.""",
resposta=r"""$-\infty$ pela esquerda e $+\infty$ pela direita.""",
solucao=r"""Substituindo $x=1$: numerador $2+7-4=5$, denominador $1+1-2=0$. Forma $K/0$ com $K\neq0$: o limite é infinito, e o **sinal** decide.

Fatoramos o denominador: $x^2+x-2=(x+2)(x-1)$. Perto de $x=1$, $x+2\approx3>0$, então o sinal é o de $x-1$:
- $x\to1^-$: $x-1<0$, logo o denominador $\to0^-$ e $\frac{5}{0^-}\to-\infty$;
- $x\to1^+$: $x-1>0$, logo o denominador $\to0^+$ e $\frac{5}{0^+}\to+\infty$.

Portanto $x=1$ é uma **assíntota vertical**.

**Animação.** Dois pontos se aproximam de $x=1$: o da esquerda despenca e o da direita dispara.""",
),
dict(id='2.6', origem='2.3, ex. 127', titulo='Teorema do Confronto',
enunciado=r"""Calcule $\displaystyle\lim_{\theta\to0}\theta^2\cos\!\left(\frac1\theta\right)$.""",
resposta=r"""0, pelo Teorema do Confronto.""",
solucao=r"""Não dá para usar a propriedade do produto, porque $\lim_{\theta\to0}\cos(1/\theta)$ **não existe** (oscila).
Mas $\cos$ é limitado: $-1\le\cos(1/\theta)\le1$. Multiplicando por $\theta^2\ge0$:
$$-\theta^2\le\theta^2\cos\left(\tfrac1\theta\right)\le\theta^2 .$$
Como $\lim_{\theta\to0}(-\theta^2)=0=\lim_{\theta\to0}\theta^2$, o Teorema do Confronto dá
$$\lim_{\theta\to0}\theta^2\cos\left(\tfrac1\theta\right)=0 .$$

**Padrão útil.** (algo que tende a 0) × (algo limitado) → 0.

**Animação.** Um zoom sucessivo em torno da origem: a função oscila cada vez mais rápido, mas sempre presa entre $-\theta^2$ e $\theta^2$.""",
),
dict(id='2.7', origem='2.4, ex. 145', titulo='Escolhendo $k$ para a continuidade (I)',
enunciado=r"""Encontre $k$ para que $f(x)=\begin{cases}3x+2, & x<k\\ 2x-3, & k\le x\le8\end{cases}$
seja contínua em todo o seu domínio.""",
resposta=r"""$k=-5$.""",
solucao=r"""Cada parte é um polinômio, logo contínua. O único ponto a verificar é a emenda $x=k$:
- $\lim_{x\to k^-}f(x)=3k+2$;
- $\lim_{x\to k^+}f(x)=f(k)=2k-3$.

Precisamos de $3k+2=2k-3$, isto é, $k=-5$. Com isso, $f(-5)=-13$ e as duas retas se encontram em $(-5,-13)$.

**Animação.** Enquanto $k$ varia, o salto entre as duas partes muda de tamanho; ele desaparece exatamente em $k=-5$.""",
),
dict(id='2.8', origem='2.4, ex. 148', titulo='Escolhendo $k$ para a continuidade (II)',
enunciado=r"""Encontre $k$ para que $f(x)=\begin{cases}e^{kx}, & 0\le x<4\\ x+3, & 4\le x\le8\end{cases}$
seja contínua em $[0,8]$.""",
resposta=r"""$k=\dfrac{\ln7}{4}\approx0{,}4865$.""",
solucao=r"""As partes são contínuas; resta a emenda em $x=4$:
- $\lim_{x\to4^-}e^{kx}=e^{4k}$;
- $f(4)=\lim_{x\to4^+}(x+3)=7$.

Logo $e^{4k}=7\iff4k=\ln7\iff k=\frac{\ln7}{4}\approx0{,}4865$.

**Animação.** A exponencial muda de inclinação com $k$ até se encaixar no ponto $(4,7)$.""",
),
dict(id='2.9', origem='2.4, ex. 151', titulo='TVI: duas partículas',
enunciado=r"""Uma partícula se move numa reta com posição $s(t)$ contínua, e $s(2)=5$, $s(5)=2$. Outra
partícula tem posição $h(t)=s(t)-t$. Explique por que existe um instante $t\in[2,5]$ em que
$h(t)=0$. O que isso significa para a primeira partícula?""",
resposta=r"""$h(2)=3>0$ e $h(5)=-3<0$; pelo TVI, $h(c)=0$ para algum $c\in[2,5]$, ou seja, $s(c)=c$.""",
solucao=r"""$h(t)=s(t)-t$ é contínua, pois é a diferença de funções contínuas. Calculando nas extremidades:
$$h(2)=5-2=3>0,\qquad h(5)=2-5=-3<0 .$$
Como $0$ está entre $h(2)$ e $h(5)$, o **Teorema do Valor Intermediário** garante que existe $c\in[2,5]$ com $h(c)=0$.

**Significado.** $h(c)=0\iff s(c)=c$: em algum instante a posição da primeira partícula coincide numericamente com o tempo. Graficamente, o gráfico de $s$ cruza a reta $y=t$.

**Animação.** Uma possível $s(t)$ (qualquer curva contínua de $(2,5)$ a $(5,2)$) é desenhada; ela é obrigada a cruzar a reta $y=t$.""",
),
dict(id='2.10', origem='2.4, ex. 153', titulo='TVI: localizando uma raiz',
enunciado=r"""Use o TVI para decidir se $2^x=x^3$ tem solução em $[1{,}25;\,1{,}375]$ ou em
$[1{,}375;\,1{,}5]$. Justifique para cada intervalo.""",
resposta=r"""Com $g(x)=2^x-x^3$: $g(1{,}25)>0$ e $g(1{,}375)<0$, logo há raiz no 1º intervalo; no 2º, $g$ não muda de sinal e o TVI nada garante.""",
solucao=r"""Seja $g(x)=2^x-x^3$, contínua. Uma solução de $2^x=x^3$ é um zero de $g$.
- $g(1{,}25)=2^{1{,}25}-1{,}25^3\approx2{,}3784-1{,}9531=0{,}425>0$;
- $g(1{,}375)\approx2{,}5937-2{,}5996=-0{,}006<0$;
- $g(1{,}5)\approx2{,}8284-3{,}375=-0{,}547<0$.

**Em $[1{,}25;\,1{,}375]$:** $g$ muda de sinal, logo pelo TVI **há** uma solução (de fato, $x\approx1{,}3735$).

**Em $[1{,}375;\,1{,}5]$:** $g$ é negativa nas duas extremidades. O TVI **não garante** nada. (Pode haver zero ou não; o teorema só fala de valores intermediários. Aqui, de fato, não há.)

**Animação.** Zoom sucessivo sobre a raiz, reduzindo o intervalo pela metade a cada passo (método da bissecção).""",
),
dict(id='2.11', origem='2.5, ex. 192', titulo='Prova $\\varepsilon$-$\\delta$',
enunciado=r"""Use a definição precisa de limite para provar que $\displaystyle\lim_{x\to2}(x^2+2x)=8$.""",
resposta=r"""Escolha $\delta=\min\{1,\varepsilon/7\}$.""",
solucao=r"""**Rascunho.** Queremos $|(x^2+2x)-8|<\varepsilon$. Fatorando: $|x^2+2x-8|=|x-2|\,|x+4|$.
Controlamos $|x+4|$ restringindo $x$: se $|x-2|<1$, então $1<x<3$, logo $5<x+4<7$ e $|x+4|<7$.
Basta então $|x-2|<\varepsilon/7$.

**Prova.** Seja $\varepsilon>0$. Escolha $\delta=\min\{1,\varepsilon/7\}$. Suponha $0<|x-2|<\delta$.
Então $|x-2|<1$, donde $|x+4|<7$, e também $|x-2|<\varepsilon/7$. Logo
$$|(x^2+2x)-8|=|x-2|\,|x+4|<\frac\varepsilon7\cdot7=\varepsilon .$$
Portanto $\lim_{x\to2}(x^2+2x)=8$. $\blacksquare$

**Animação.** Para $\varepsilon$ cada vez menor, a faixa vertical de largura $\delta=\min\{1,\varepsilon/7\}$ mantém o gráfico dentro da faixa horizontal $(8-\varepsilon,8+\varepsilon)$.""",
),
dict(id='2.12', origem='2.5, ex. 200', titulo='Provando que um limite não existe',
enunciado=r"""Use a definição precisa para provar que $\displaystyle\lim_{x\to1}\frac{|x-1|}{x-1}$ não existe.""",
resposta=r"""Tome $\varepsilon=\tfrac12$: perto de 1 a função vale $-1$ e $1$, que não cabem juntos em nenhuma faixa de largura 1.""",
solucao=r"""A função vale $f(x)=1$ para $x>1$ e $f(x)=-1$ para $x<1$.

Suponha, por absurdo, que $\lim_{x\to1}f(x)=L$. Tome $\varepsilon=\frac12$. Deveria existir $\delta>0$ tal que $0<|x-1|<\delta\Rightarrow|f(x)-L|<\frac12$.
Escolha $x_1=1+\frac\delta2$ e $x_2=1-\frac\delta2$, ambos com $0<|x-1|<\delta$. Então
$$|1-L|<\tfrac12\quad\text{e}\quad|-1-L|<\tfrac12 .$$
Pela desigualdade triangular,
$$2=|1-(-1)|\le|1-L|+|L-(-1)|<\tfrac12+\tfrac12=1,$$
o que é absurdo. Logo o limite não existe. $\blacksquare$

**Animação.** Testamos vários candidatos $L$: a faixa $(L-\frac12,L+\frac12)$ nunca contém ao mesmo tempo os valores $-1$ e $1$.""",
),
]
