# -*- coding: utf-8 -*-
"""Soluções completas (★) do capítulo 3."""

SOLUCOES = [
dict(id='tangente', origem='inspirado na seção 3.1', titulo='Retas tangente e normal',
enunciado=r"""Encontre as retas tangente e normal à parábola $y=x^2-4x+5$ no ponto de abscissa
$x=3$ e esboce as três curvas.""",
resposta=r"""Tangente $y=2x-4$; normal $y=-\tfrac12x+\tfrac72$.""",
solucao=r"""**Ponto.** $y(3)=9-12+5=2$, logo o ponto é $(3,2)$.

**Inclinação da tangente.** $y'=2x-4$, então $m=y'(3)=2$. Tangente: $y-2=2(x-3)$, isto é, $y=2x-4$.

**Normal.** É perpendicular à tangente no mesmo ponto, então tem inclinação $-\frac1m=-\frac12$:
$y-2=-\frac12(x-3)$, isto é, $y=-\frac12x+\frac72$.

**Conferência.** A parábola é $y=(x-2)^2+1$, com vértice $(2,1)$. À direita do vértice ela sobe, e a tangente com inclinação positiva faz sentido.

**Animação.** A tangente percorre a parábola; sua inclinação $2x-4$ é negativa à esquerda do vértice, zero no vértice e positiva à direita.""",
),
dict(id='grafico_derivada', origem='inspirado na seção 3.2', titulo='Construindo o gráfico de $f\'$',
enunciado=r"""Para $f(x)=x^3-3x^2$, determine onde $f'(x)>0$, $f'(x)<0$ e $f'(x)=0$, e esboce
o gráfico de $f'$ alinhado com o de $f$.""",
resposta=r"""$f'(x)=3x(x-2)$: positiva em $(-\infty,0)\cup(2,\infty)$, negativa em $(0,2)$, nula em $x=0$ e $x=2$.""",
solucao=r"""$f'(x)=3x^2-6x=3x(x-2)$, uma parábola com zeros em $0$ e $2$ e vértice em $x=1$ (onde $f'(1)=-3$).

- $f'>0$ em $(-\infty,0)\cup(2,\infty)$: ali $f$ é **crescente**;
- $f'<0$ em $(0,2)$: ali $f$ é **decrescente**;
- $f'=0$ em $x=0$ e $x=2$: **tangentes horizontais**, em $(0,0)$ (máximo local) e $(2,-4)$ (mínimo local).

O ponto em que $f$ decresce mais rápido é $x=1$, o vértice de $f'$.

**Animação.** A reta tangente percorre o gráfico de $f$ (em cima); embaixo, o valor da sua inclinação vai desenhando, ponto a ponto, o gráfico de $f'$.""",
),
dict(id='por_partes', origem='inspirado no Exemplo 3.14', titulo='Função por partes derivável',
enunciado=r"""Encontre $a$ e $b$ para que $f(x)=\begin{cases}x^2,&x\le1\\ax+b,&x>1\end{cases}$
seja derivável em todo $\mathbb R$.""",
resposta=r"""$a=2$, $b=-1$.""",
solucao=r"""**Continuidade em $x=1$.** $\lim_{x\to1^-}x^2=1$ e $\lim_{x\to1^+}(ax+b)=a+b$. Precisamos de $a+b=1$.

**Derivabilidade em $x=1$.** As derivadas laterais são
$$\lim_{h\to0^-}\frac{(1+h)^2-1}{h}=2,\qquad \lim_{h\to0^+}\frac{a(1+h)+b-1}{h}=\lim_{h\to0^+}\frac{ah+(a+b-1)}{h}=a\ \ (\text{usando }a+b=1).$$
Logo $a=2$ e $b=-1$.

**Interpretação.** A reta $y=2x-1$ é exatamente a **tangente** à parábola em $(1,1)$: a emenda fica "lisa", sem bico.

**Por que a continuidade vem primeiro?** Derivável implica contínua. Se $a+b\neq1$, a derivada lateral direita seria infinita.

**Animação.** Variamos $a$ (mantendo a continuidade, $b=1-a$): só quando $a=2$ as duas partes se encaixam sem bico.""",
),
dict(id='movimento', origem='inspirado no Exemplo 3.36', titulo='Partícula em movimento',
enunciado=r"""Uma partícula tem posição $s(t)=t^3-9t^2+24t$ (metros, $t\ge0$ em segundos).
(a) Quando ela está em repouso? (b) Quando se move para a frente e para trás?
(c) Qual é a distância total percorrida em $[0,5]$? (d) Quando está acelerando?""",
resposta=r"""(a) $t=2$ e $t=4$; (b) frente em $[0,2)\cup(4,\infty)$, trás em $(2,4)$; (c) 28 m; (d) em $(2,3)$ e $(4,\infty)$.""",
solucao=r"""$v(t)=s'(t)=3t^2-18t+24=3(t-2)(t-4)$ e $a(t)=v'(t)=6t-18$.

**(a)** Repouso: $v=0\iff t=2$ ou $t=4$.

**(b)** $v>0$ em $[0,2)$ e $(4,\infty)$ (para a frente); $v<0$ em $(2,4)$ (para trás).

**(c)** A distância **não** é $s(5)-s(0)$, porque a partícula volta no caminho. Somamos cada trecho:
$s(0)=0$, $s(2)=20$, $s(4)=16$, $s(5)=20$. Distância $=|20-0|+|16-20|+|20-16|=20+4+4=28$ m.
(O deslocamento é $s(5)-s(0)=20$ m.)

**(d)** A rapidez $|v|$ aumenta quando $v$ e $a$ têm o mesmo sinal:
- $(0,2)$: $v>0$, $a<0$, desacelera;
- $(2,3)$: $v<0$, $a<0$, acelera;
- $(3,4)$: $v<0$, $a>0$, desacelera;
- $(4,\infty)$: $v>0$, $a>0$, acelera.

**Animação.** A partícula anda sobre a reta enquanto o gráfico de $v(t)$ é traçado; a cor indica se ela vai para a frente (azul) ou para trás (laranja).""",
),
dict(id='derivada_seno', origem='inspirado na seção 3.5', titulo='O quociente de diferenças do seno',
enunciado=r"""Para $h=1$, $0{,}5$ e $0{,}1$, esboce $q_h(x)=\dfrac{\sen(x+h)-\sen x}{h}$ junto com
$\cos x$. O que acontece quando $h\to0$? Prove o resultado.""",
resposta=r"""$q_h\to\cos x$; usa $\lim\frac{\sen h}h=1$ e $\lim\frac{\cos h-1}h=0$.""",
solucao=r"""**Observação.** Para cada $h$, $q_h(x)$ é a inclinação de uma secante. Para $h=1$ a curva já parece uma cossenoide, mas deslocada; para $h=0{,}1$ quase coincide com $\cos x$.

Na verdade, pela identidade $\sen A-\sen B=2\cos\frac{A+B}2\sen\frac{A-B}2$,
$$q_h(x)=\frac{\sen(h/2)}{h/2}\,\cos\!\left(x+\frac h2\right),$$
ou seja, $q_h$ é **exatamente** uma cossenoide, com amplitude $\frac{\sen(h/2)}{h/2}<1$ e deslocada de $h/2$ para a esquerda. As duas distorções somem quando $h\to0$.

**Prova (como no texto).**
$$q_h(x)=\sen x\cdot\frac{\cos h-1}{h}+\cos x\cdot\frac{\sen h}{h}\ \xrightarrow{h\to0}\ \sen x\cdot0+\cos x\cdot1=\cos x .$$

**Animação.** $h$ diminui de 2 até 0,01, e $q_h$ (azul) se encaixa sobre $\cos x$ (laranja).""",
),
dict(id='cadeia_tangente', origem='inspirado no Exemplo 3.50', titulo='Regra da cadeia e tangente',
enunciado=r"""Encontre a reta tangente a $y=\sen(x^2)$ em $x=\sqrt{\pi}$.""",
resposta=r"""$y=-2\sqrt\pi\,(x-\sqrt\pi)$.""",
solucao=r"""**Ponto.** $y(\sqrt\pi)=\sen\pi=0$.

**Derivada (cadeia).** Fora: $\sen u$, com derivada $\cos u$. Dentro: $u=x^2$, com derivada $2x$.
$$y'=\cos(x^2)\cdot2x\quad\Rightarrow\quad y'(\sqrt\pi)=\cos\pi\cdot2\sqrt\pi=-2\sqrt\pi\approx-3{,}545 .$$

**Tangente.** $y=-2\sqrt\pi\,(x-\sqrt\pi)$.

**Observação.** Perto de $x=\sqrt\pi$, $\sen(x^2)$ oscila cada vez mais rápido à medida que $x$ cresce: o fator $2x$ da regra da cadeia mede justamente essa "aceleração" das oscilações.

**Animação.** A tangente percorre a curva $\sen(x^2)$; a inclinação $2x\cos(x^2)$ fica cada vez maior em módulo.""",
),
dict(id='inversa', origem='inspirado no Exemplo 3.61', titulo='Derivada de uma inversa sem a fórmula',
enunciado=r"""Seja $f(x)=x+e^x$. Mostre que $f$ é inversível e calcule $(f^{-1})'(1)$ e a reta
tangente ao gráfico de $f^{-1}$ no ponto $(1,0)$.""",
resposta=r"""$(f^{-1})'(1)=\tfrac12$; tangente $y=\tfrac12(x-1)$.""",
solucao=r"""**Inversível.** $f'(x)=1+e^x>0$ para todo $x$, então $f$ é estritamente crescente, logo injetora.

**Ponto correspondente.** Precisamos de $f^{-1}(1)$: $x+e^x=1$ tem solução $x=0$ (pois $0+e^0=1$). Logo $f^{-1}(1)=0$.

**Teorema da inversa.**
$$(f^{-1})'(1)=\frac{1}{f'(f^{-1}(1))}=\frac1{f'(0)}=\frac1{1+1}=\frac12 .$$

**Tangente.** No ponto $(1,0)$ do gráfico de $f^{-1}$: $y=\frac12(x-1)$.

**Observação.** Não existe fórmula elementar para $f^{-1}$, mas a derivada sai mesmo assim.

**Animação.** O gráfico de $f$ e sua tangente em $(0,1)$ (inclinação 2) são refletidos em torno de $y=x$, virando o gráfico de $f^{-1}$ e a tangente em $(1,0)$ (inclinação $\frac12$).""",
),
dict(id='implicita', origem='inspirado na seção 3.8', titulo='Tangentes horizontais numa elipse',
enunciado=r"""Encontre os pontos da curva $x^2-xy+y^2=3$ onde a reta tangente é horizontal e onde é
vertical.""",
resposta=r"""Horizontal em $(1,2)$ e $(-1,-2)$; vertical em $(2,1)$ e $(-2,-1)$.""",
solucao=r"""**Derivação implícita.** $2x-(y+xy')+2yy'=0\Rightarrow y'(2y-x)=y-2x\Rightarrow y'=\dfrac{y-2x}{2y-x}$.

**Horizontal ($y'=0$):** numerador nulo, $y=2x$. Na curva: $x^2-2x^2+4x^2=3\Rightarrow x^2=1$. Pontos $(1,2)$ e $(-1,-2)$ (o denominador $2y-x=3x\neq0$ ✓).

**Vertical:** denominador nulo, $x=2y$. Na curva: $4y^2-2y^2+y^2=3\Rightarrow y^2=1$. Pontos $(2,1)$ e $(-2,-1)$ (numerador $y-2x=-3y\neq0$ ✓).

**Sobre a curva.** É uma elipse inclinada a $45^\circ$ (o termo $-xy$ gira os eixos). Os quatro pontos são os "extremos" da elipse nas direções vertical e horizontal.

**Animação.** A tangente percorre a elipse; os pontos de tangente horizontal (laranja) e vertical (verde) ficam marcados.""",
),
dict(id='xx', origem='inspirado no Exemplo 3.83', titulo='O mínimo de $x^x$',
enunciado=r"""Use derivação logarítmica para encontrar $\dfrac{d}{dx}x^x$ ($x>0$) e determine o ponto onde
o gráfico de $y=x^x$ tem tangente horizontal.""",
resposta=r"""$y'=x^x(\ln x+1)$; tangente horizontal em $x=1/e$, com $y=e^{-1/e}\approx0{,}692$.""",
solucao=r"""**Derivação logarítmica.** $\ln y=x\ln x\Rightarrow\frac{y'}{y}=\ln x+1\Rightarrow y'=x^x(\ln x+1)$.

**Tangente horizontal.** Como $x^x>0$, $y'=0\iff\ln x=-1\iff x=\frac1e\approx0{,}368$. O valor é $y=\left(\frac1e\right)^{1/e}=e^{-1/e}\approx0{,}692$.

**Sinal de $y'$.** Para $x<\frac1e$, $\ln x+1<0$, e a função decresce; para $x>\frac1e$, ela cresce. Logo $x=1/e$ é um **mínimo** (no capítulo 4 isso fica sistemático).

**Erros comuns.** $\frac{d}{dx}x^x\neq x\cdot x^{x-1}$ (regra da potência, que exige expoente constante) e $\neq x^x\ln x$ (regra da exponencial, que exige base constante). A resposta correta é a **soma** das duas: $x^x\ln x+x\cdot x^{x-1}$.

**Animação.** A tangente percorre $y=x^x$ e fica horizontal em $x=1/e$.""",
),
dict(id='custo_marginal', origem='inspirado no Exemplo 3.38', titulo='Custo marginal',
enunciado=r"""O custo (em mil reais) de produzir $x$ unidades é $C(x)=0{,}01x^3-0{,}6x^2+15x+200$.
Calcule o custo marginal em $x=20$ e compare com o custo real de produzir a 21ª unidade.""",
resposta=r"""$C'(20)=3$; o custo real é $C(21)-C(20)=3{,}01$.""",
solucao=r"""$C'(x)=0{,}03x^2-1{,}2x+15$, então $C'(20)=12-24+15=3$ mil reais por unidade.

Custo real da 21ª unidade: $C(20)=80-240+300+200=340$ e $C(21)=92{,}61-264{,}6+315+200=343{,}01$. Logo $C(21)-C(20)=3{,}01$.

**Por que são próximos?** $C(21)-C(20)$ é a inclinação da secante entre $x=20$ e $x=21$; $C'(20)$ é a inclinação da tangente em $x=20$. Para $h=1$ (pequeno em relação à escala do problema), $C(20+1)\approx C(20)+C'(20)\cdot1$.

**Observação.** $C'$ é mínimo em $x=20$ (vértice de $0{,}03x^2-1{,}2x+15$): é o nível de produção em que cada unidade extra é mais barata.

**Animação.** A secante entre $x=20$ e $x=20+h$ gira até a tangente quando $h$ vai de 10 a 0.""",
),
dict(id='tangentes_por_ponto', origem='problema clássico', titulo='Tangentes por um ponto externo',
enunciado=r"""Encontre todas as retas tangentes à parábola $y=x^2$ que passam pelo ponto $(1,-3)$,
que não está na parábola.""",
resposta=r"""$y=6x-9$ (tangente em $x=3$) e $y=-2x-1$ (tangente em $x=-1$).""",
solucao=r"""**Ideia.** Não sabemos o ponto de tangência; chamamos de $(a,a^2)$ e impomos a condição.

A tangente em $(a,a^2)$ tem inclinação $2a$: $y=a^2+2a(x-a)=2ax-a^2$.

Ela passa por $(1,-3)$ se $-3=2a-a^2$, isto é, $a^2-2a-3=0\Rightarrow(a-3)(a+1)=0$.

- $a=3$: $y=6x-9$;
- $a=-1$: $y=-2x-1$.

**Verificação.** $6(1)-9=-3$ ✓ e $-2(1)-1=-3$ ✓.

**Observação.** De um ponto **abaixo** da parábola partem duas tangentes; de um ponto **sobre** ela, uma; de um ponto **acima**, nenhuma (a equação em $a$ não tem raiz real).

**Animação.** A tangente percorre a parábola; ela "acende" nas duas posições em que passa pelo ponto $(1,-3)$.""",
),
]
