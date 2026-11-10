# Capítulo 1 — Funções e gráficos: exercícios

São 65 exercícios. Os pontos antes de cada número indicam a dificuldade: **•** fácil, **••** médio, **•••** difícil e **••••** desafio. Tente resolver antes de abrir a resposta. Os marcados com ★ têm [solução completa com animação](#soluções-completas).

Muitos enunciados são adaptados de *Calculus Volume 1* (OpenStax, CC BY-NC-SA 4.0).

## Lista

`•` **1.1** Esboce o gráfico de $f(x)=|x-2|-1$, indicando o vértice, os zeros e o intercepto $y$.

<details><summary>Resposta</summary>

Vértice $(2,-1)$; zeros $x=1$ e $x=3$; intercepto $(0,1)$.

</details>

`•` **1.2** Determine domínio, imagem, zeros e intercepto $y$ de $f(x)=\sqrt{x+3}-1$ e esboce o gráfico a partir de $y=\sqrt x$.

<details><summary>Resposta</summary>

Domínio $[-3,\infty)$; imagem $[-1,\infty)$; zero $x=-2$; intercepto $(0,\sqrt3-1)$; translação de 3 para a esquerda e 1 para baixo.

</details>

`•` **1.3** Determine o domínio de $f(x)=\sqrt{x^2-5x+6}$ por estudo de sinais.

<details><summary>Resposta</summary>

$(-\infty,2]\cup[3,\infty)$.

</details>

`•` **1.4** Determine o domínio e a imagem de $f(x)=\ln(4-x^2)$.

<details><summary>Resposta</summary>

Domínio $(-2,2)$; imagem $(-\infty,\ln4]$.

</details>

`•` **1.5** Esboce $f(x)=\begin{cases}-x,&x<0\\x^2,&0\le x\le2\\6-x,&x>2\end{cases}$. Qual é a imagem? Quantas soluções tem $f(x)=3$?

<details><summary>Resposta</summary>

Imagem $\mathbb R$; três soluções: $x=-3$, $\sqrt3$ e $3$.

</details>

`•` **1.6** Encontre os zeros de $f(x)=x^3-5x^2+6x$, faça o estudo de sinais e esboce o gráfico.

<details><summary>Resposta</summary>

Zeros $0$, $2$, $3$; $f>0$ em $(0,2)\cup(3,\infty)$ e $f<0$ em $(-\infty,0)\cup(2,3)$.

</details>

`•` **1.7** Encontre a reta que passa por $(-1,4)$ e é perpendicular a $2x-3y=6$.

<details><summary>Resposta</summary>

$y=-\tfrac32x+\tfrac52$.

</details>

`•` **1.8** Complete o quadrado em $f(x)=2x^2-8x+5$, dê o vértice e os zeros e esboce a parábola.

<details><summary>Resposta</summary>

$f(x)=2(x-2)^2-3$; vértice $(2,-3)$; zeros $2\pm\sqrt{3/2}$.

</details>

`•` **1.9** Classifique como par, ímpar ou nenhuma: (a) $x^2\cos x$; (b) $x\sin x$; (c) $\dfrac{x}{x^2+1}$; (d) $e^x-e^{-x}$; (e) $x^2+x$.

<details><summary>Resposta</summary>

(a) par; (b) par; (c) ímpar; (d) ímpar; (e) nenhuma.

</details>

`•` **1.10** Sejam $f(x)=x^2+1$ e $g(x)=\sqrt{x-1}$. Encontre $f\circ g$ e $g\circ f$ com os domínios. Por que as fórmulas são ``quase'' inversas?

<details><summary>Resposta</summary>

$(f\circ g)(x)=x$, $x\ge1$; $(g\circ f)(x)=|x|$, $x\in\mathbb R$.

</details>

`•` **1.11** Escreva $h(x)=\sqrt{1+\cos^2x}$ como composição de três funções mais simples.

<details><summary>Resposta</summary>

$h=f\circ g\circ k$, com $k(x)=\cos x$, $g(u)=1+u^2$, $f(v)=\sqrt v$ (há outras).

</details>

`•` **1.12** Resolva $|2x-3|\le5$ e $|x+1|>2$, escrevendo as soluções em notação de intervalos.

<details><summary>Resposta</summary>

$[-1,4]$; $(-\infty,-3)\cup(1,\infty)$.

</details>

`•` **1.13** Encontre todos os $\theta\in[0,2\pi)$ com $\cos\theta=-\tfrac12$ e todos com $\tan\theta=\sqrt3$.

<details><summary>Resposta</summary>

$\tfrac{2\pi}3,\tfrac{4\pi}3$; $\tfrac\pi3,\tfrac{4\pi}3$.

</details>

`•` **1.14** Esboce um período de $y=2\sin\!\big(x-\tfrac\pi4\big)$, marcando amplitude, período, zeros e máximos.

<details><summary>Resposta</summary>

Amplitude 2, período $2\pi$; zeros $\tfrac\pi4,\tfrac{5\pi}4,\tfrac{9\pi}4$; máximo em $x=\tfrac{3\pi}4$.

</details>

`•` **1.15** Encontre a inversa de $f(x)=\dfrac{x+1}{x-2}$, com domínio e imagem, e confira que $f(f^{-1}(x))=x$.

<details><summary>Resposta</summary>

$f^{-1}(x)=\dfrac{2x+1}{x-1}$; $\operatorname{Dom}f^{-1}=\lbrace x\neq1\rbrace $, $\operatorname{Im}f^{-1}=\lbrace y\neq2\rbrace $.

</details>

`•` **1.16** Calcule, desenhando um triângulo retângulo: $\sin\!\big(\cos^{-1}\tfrac35\big)$, $\tan\!\big(\sin^{-1}(-\tfrac12)\big)$ e $\cos(\tan^{-1}2)$.

<details><summary>Resposta</summary>

$\tfrac45$, $-\tfrac{\sqrt3}3$ e $\tfrac1{\sqrt5}$.

</details>

`•` **1.17** Simplifique (a) $\ln\!\big(e^2\sqrt e\big)$; (b) $\log_2\dfrac{8}{\sqrt2}$; (c) $e^{2\ln3-\ln2}$.

<details><summary>Resposta</summary>

(a) $\tfrac52$; (b) $\tfrac52$; (c) $\tfrac92$.

</details>

`•` **1.18** Resolva (a) $3^{2x-1}=27$; (b) $\log_3(x+1)=2$; (c) $5^x=2\cdot3^x$.

<details><summary>Resposta</summary>

(a) $x=2$; (b) $x=8$; (c) $x=\dfrac{\ln2}{\ln5-\ln3}\approx1{,}357$.

</details>

`•` **1.19** Esboce $y=2^{-x}+1$ a partir de $y=2^x$, indicando a assíntota, o intercepto $y$ e a imagem.

<details><summary>Resposta</summary>

Reflexão no eixo $y$ e translação de 1 para cima; assíntota $y=1$; intercepto $(0,2)$; imagem $(1,\infty)$.

</details>

`•` **1.20** Esboce $y=-\ln(x-1)$ a partir de $y=\ln x$, indicando domínio, assíntota e zero.

<details><summary>Resposta</summary>

Domínio $(1,\infty)$; assíntota $x=1$; zero $x=2$; é decrescente.

</details>

`••` **1.21** **Composição e domínio.** Sejam $f(x)=\dfrac{3}{2x+1}$ e $g(x)=\dfrac{2}{x}$. Encontre $(f\circ g)(x)$ e $(g\circ f)(x)$ e determine o domínio de cada composta. ★ [ver solução](#ex-1-21)

<details><summary>Resposta</summary>

$(f\circ g)(x)=\dfrac{3x}{x+4}$, com $x\neq0,-4$;\quad $(g\circ f)(x)=\dfrac{2(2x+1)}{3}$, com $x\neq-\tfrac12$.

</details>

`••` **1.22** Sejam $f(x)=\dfrac1{x-1}$ e $g(x)=\dfrac{x+1}{x}$. Encontre $f\circ g$ e seu domínio. O resultado surpreende?

<details><summary>Resposta</summary>

$(f\circ g)(x)=x$, com domínio $x\neq0$ (a fórmula simplificada esconde a restrição).

</details>

`••` **1.23** Esboce $f(x)=x|x|$. Mostre que $f$ é ímpar e injetora e encontre $f^{-1}$.

<details><summary>Resposta</summary>

$f(x)=x^2$ para $x\ge0$ e $-x^2$ para $x<0$; $f^{-1}(x)=\sqrt x$ se $x\ge0$ e $-\sqrt{-x}$ se $x<0$.

</details>

`••` **1.24** Descreva as transformações que levam $y=x^2$ em $y=-(x+1)^2+3$ e dê o vértice da parábola.

<details><summary>Resposta</summary>

Translação de 1 para a esquerda, reflexão no eixo $x$, translação de 3 para cima; vértice $(-1,3)$.

</details>

`••` **1.25** Determine o domínio e a imagem de $f(x)=\sqrt{4-x^2}$ e descreva seu gráfico.

<details><summary>Resposta</summary>

Domínio $[-2,2]$; imagem $[0,2]$; semicircunferência superior de raio 2.

</details>

`••` **1.26** **Custo e ponto de equilíbrio.** Uma confeitaria vende cupcakes em festivais. Montar a barraca custa R\$ 125,00 e cada cupcake custa R\$ 0,75 para ser produzido. (a) Escreva o custo total $C$ em função do número $x$ de cupcakes. (b) Quanto custa produzir 160 cupcakes? (c) Vendendo cada cupcake a R\$ 1,50, quantos ela precisa vender para começar a ter lucro? ★ [ver solução](#ex-1-26)

<details><summary>Resposta</summary>

(a) $C(x)=0{,}75x+125$; (b) R\$ 245,00; (c) 167 cupcakes.

</details>

`••` **1.27** Resolva $2\sin^2\theta-\sin\theta-1=0$ para $\theta\in[0,2\pi)$.

<details><summary>Resposta</summary>

$\theta=\tfrac\pi2$, $\tfrac{7\pi}6$ e $\tfrac{11\pi}6$.

</details>

`••` **1.28** **Identidade trigonométrica.** Verifique a identidade $\dfrac{1}{1-\sin\alpha}+\dfrac{1}{1+\sin\alpha}=2\sec^2\alpha$. ★ [ver solução](#ex-1-28)

<details><summary>Resposta</summary>

Some as frações: o denominador comum é $1-\sin^2\alpha=\cos^2\alpha$.

</details>

`••` **1.29** Verifique a identidade $\dfrac{\tan\theta-\cot\theta}{\sin\theta\cos\theta}=\sec^2\theta-\csc^2\theta$.

<details><summary>Resposta</summary>

Escreva $\tan$ e $\cot$ em senos e cossenos e separe a fração.

</details>

`••` **1.30** Escreva $3\cos t+4\sin t$ na forma $A\cos(t-\varphi)$, com $A>0$.

<details><summary>Resposta</summary>

$A=5$, $\varphi=\tan^{-1}\tfrac43\approx0{,}927$.

</details>

`••` **1.31** Mostre que $f(x)=\dfrac{2x+1}{x-3}$ é injetora e encontre $f^{-1}$, com domínio e imagem.

<details><summary>Resposta</summary>

$f^{-1}(x)=\tfrac{3x+1}{x-2}$; domínio $x\neq2$, imagem $y\neq3$.

</details>

`••` **1.32** Restrinja o domínio de $f(x)=(x-2)^2$ para torná-la injetora e encontre a inversa.

<details><summary>Resposta</summary>

Em $[2,\infty)$: $f^{-1}(x)=2+\sqrt x$, $x\ge0$.

</details>

`••` **1.33** Calcule $\cos^{-1}\!\big(\cos\tfrac{5\pi}3\big)$, $\sin^{-1}\!\big(\sin\tfrac{3\pi}4\big)$ e $\tan\!\big(\cos^{-1}\tfrac35\big)$.

<details><summary>Resposta</summary>

$\tfrac\pi3$, $\tfrac\pi4$ e $\tfrac43$.

</details>

`••` **1.34** Resolva $\log_2x+\log_2(x-2)=3$.

<details><summary>Resposta</summary>

$x=4$ ($x=-2$ é solução estranha).

</details>

`••` **1.35** Resolva $\ln(x+1)-\ln x=1$.

<details><summary>Resposta</summary>

$x=\dfrac1{e-1}\approx0{,}582$.

</details>

`••` **1.36** Mostre que $f(x)=x^3+x$ é estritamente crescente (logo injetora) e calcule $f^{-1}(2)$ e $f^{-1}(10)$ sem achar a fórmula da inversa.

<details><summary>Resposta</summary>

$f^{-1}(2)=1$ e $f^{-1}(10)=2$.

</details>

`••` **1.37** **Expressões hiperbólicas.** Reescreva em termos de exponenciais e simplifique: (a) $2\cosh(\ln x)$; (b) $\cosh 4x+\sinh 4x$; (c) $\cosh 2x-\sinh 2x$; (d) $\ln(\cosh x+\sinh x)+\ln(\cosh x-\sinh x)$. ★ [ver solução](#ex-1-37)

<details><summary>Resposta</summary>

(a) $x+\frac1x$ ($x>0$); (b) $e^{4x}$; (c) $e^{-2x}$; (d) $0$.

</details>

`••` **1.38** **Decaimento do iodo-131.** O iodo-131 decai segundo $Q(t)=Q_0e^{-0{,}08664t}$, com $t$ em dias. Quanto tempo leva (arredondando para o dia mais próximo) para 95% de uma amostra decair? ★ [ver solução](#ex-1-38)

<details><summary>Resposta</summary>

$t=\dfrac{\ln 20}{0{,}08664}\approx35$ dias.

</details>

`••` **1.39** **Escala Richter.** O terremoto de 1906 em São Francisco teve magnitude 8,3 na escala Richter. No mesmo período, um terremoto de magnitude 4,9 no Japão causou poucos danos. Quantas vezes o de São Francisco foi mais intenso? ★ [ver solução](#ex-1-39)

<details><summary>Resposta</summary>

$10^{3{,}4}\approx2512$ vezes.

</details>

`••` **1.40** Resolva $2^{x+1}=3^x$ e $\log_2x+\log_4x=6$.

<details><summary>Resposta</summary>

$x=\dfrac{\ln2}{\ln3-\ln2}\approx1{,}7095$; $x=16$.

</details>

`•••` **1.41** **Horas de luz do dia.** O número de horas de luz do dia em uma cidade é modelado por $N(t)=12+3\sin\!\left[\frac{2\pi}{365}(t-79)\right]$, em que $t$ é o número de dias após 1º de janeiro. (a) Encontre a amplitude e o período. (b) Quantas horas de luz há no dia mais longo do ano? E no mais curto? (c) Quantas horas de luz há 90 dias após 1º de janeiro? ★ [ver solução](#ex-1-41)

<details><summary>Resposta</summary>

(a) Amplitude 3, período 365 dias; (b) 15 h e 9 h; (c) $\approx12{,}56$ h.

</details>

`•••` **1.42** **Custo de remoção de uma toxina.** O custo (em milhares de reais) para remover $p$ partes por bilhão (ppb) de uma toxina de um lago é $C(p)=\dfrac{75p}{85-p}$, válido para $0\le p<85$. (a) Calcule o custo para remover 25, 40 e 50 ppb. (b) Encontre a função inversa $p=C^{-1}(C)$. (c) Quanto da toxina se remove com R\$ 50 mil? ★ [ver solução](#ex-1-42)

<details><summary>Resposta</summary>

(a) $\approx$ R\$ 31,25 mil, R\$ 66,67 mil e R\$ 107,14 mil; (b) $p=\dfrac{85C}{C+75}$; (c) 34 ppb.

</details>

`•••` **1.43** **Profundidade da maré.** A profundidade (em pés) da água em um cais é $D(t)=5\sin\!\left(\frac{\pi}{6}t-\frac{7\pi}{6}\right)+8$, em que $t$ é o número de horas após a meia-noite. Determine o primeiro instante após a meia-noite em que a profundidade é 11,75 pés. ★ [ver solução](#ex-1-43)

<details><summary>Resposta</summary>

$t=7+\frac6\pi\sin^{-1}(0{,}75)\approx8{,}62$ h, por volta de 8h37.

</details>

`•••` **1.44** **Crescimento de bactérias.** Uma colônia de bactérias dobra a cada 12 horas e começa com 1000 bactérias. (a) Usando $Q=Q_0e^{kt}$, determine $k$ (quatro casas decimais). (b) Aproximadamente quanto tempo leva para haver 200\,000 bactérias? ★ [ver solução](#ex-1-44)

<details><summary>Resposta</summary>

(a) $k=\frac{\ln2}{12}\approx0{,}0578$ por hora; (b) $\approx92$ horas.

</details>

`•••` **1.45** **População sazonal.** A população de uma cidade litorânea, em milhares, é modelada por $P(t)=82{,}5-67{,}5\cos\!\left(\frac\pi6t\right)$, com $t$ em meses ($t=0$ é 1º de janeiro). Em que intervalos do ano a população é menor que 20 mil? E maior que 140 mil? ★ [ver solução](#ex-1-45)

<details><summary>Resposta</summary>

$P<20$ para $t\in[0;\,0{,}74)\cup(11{,}26;\,12]$ (início de dez. a fim de jan.); $P>140$ para $t\in(4{,}95;\,7{,}05)$ (fim de maio ao início de ago.).

</details>

`•••` **1.46** Mostre que toda $f:\mathbb R\to\mathbb R$ é a soma de uma função par e uma ímpar. Aplique a $f(x)=e^x$.

<details><summary>Resposta</summary>

$f=\tfrac12[f(x)+f(-x)]+\tfrac12[f(x)-f(-x)]$; $e^x=\cosh x+\sinh x$.

</details>

`•••` **1.47** Encontre todas as soluções de $\sin(2\theta)=\cos\theta$.

<details><summary>Resposta</summary>

$\theta=\tfrac\pi2+n\pi$, $\tfrac\pi6+2n\pi$ ou $\tfrac{5\pi}6+2n\pi$, $n\in\mathbb Z$.

</details>

`•••` **1.48** Encontre a inversa de $f(x)=x^2-4x+5$ restrita a $x\ge2$, com domínio e imagem.

<details><summary>Resposta</summary>

$f^{-1}(x)=2+\sqrt{x-1}$; domínio $[1,\infty)$, imagem $[2,\infty)$.

</details>

`•••` **1.49** Resolva $y=\sinh x$ para $x$ e mostre que $\sinh^{-1}y=\ln\!\big(y+\sqrt{y^2+1}\big)$.

<details><summary>Resposta</summary>

Com $u=e^x$: $u^2-2yu-1=0$, logo $u=y+\sqrt{y^2+1}$ (a raiz positiva).

</details>

`•••` **1.50** Determine o domínio de $f(x)=\dfrac{\ln(x^2-4)}{\sqrt{5-x}}$.

<details><summary>Resposta</summary>

$(-\infty,-2)\cup(2,5)$.

</details>

`•••` **1.51** Um carro comprado por R\$ 26\,000 perde R\$ 1\,500 por ano. (a) Escreva o valor $V(t)$. (b) Calcule $V(2)$. (c) Em quanto tempo o valor zera?

<details><summary>Resposta</summary>

(a) $V(t)=26000-1500t$; (b) R\$ 23\,000; (c) $\approx17{,}3$ anos.

</details>

`•••` **1.52** A função $C(F)=\tfrac59(F-32)$ converte Fahrenheit em Celsius. Encontre a inversa e a temperatura em que as duas escalas coincidem.

<details><summary>Resposta</summary>

$F=\tfrac95C+32$; coincidem em $-40^\circ$.

</details>

`•••` **1.53** Uma roda-gigante tem raio 20 m, centro a 22 m do solo, e dá uma volta a cada 4 min, partindo do ponto mais baixo. Escreva a altura $h(t)$ e encontre o primeiro instante em que $h=32$ m.

<details><summary>Resposta</summary>

$h(t)=22-20\cos\tfrac{\pi t}2$; $t=\tfrac43$ min (80 s).

</details>

`•••` **1.54** R\$ 1000 rendem 4% ao ano: $A(t)=1000(1{,}04)^t$. Calcule $A(5)$ e $A(10)$ e o tempo para o capital dobrar.

<details><summary>Resposta</summary>

R\$ 1216{,}65; R\$ 1480{,}24; $\approx17{,}7$ anos.

</details>

`•••` **1.55** O pH é $-\log_{10}[\mathrm H^+]$. (a) Quantas vezes uma solução de pH 3 é mais ácida que uma de pH 5? (b) Qual é $[\mathrm H^+]$ para pH $2{,}5$?

<details><summary>Resposta</summary>

(a) 100 vezes; (b) $10^{-2{,}5}\approx3{,}16\times10^{-3}$ mol/L.

</details>

`•••` **1.56** Uma população de coelhos dobra a cada 6 meses e começa com 120. Escreva $P(t)=120\,a^t$ ($t$ em meses) e estime quando chega a 1000.

<details><summary>Resposta</summary>

$a=2^{1/6}\approx1{,}1225$; $t\approx18{,}4$ meses.

</details>

`•••` **1.57** O ângulo de Mach é $\mu=2\sin^{-1}(1/M)$. Calcule $\mu$ para $M=2$ e $M=1{,}5$, e o número de Mach para $\mu=\pi/6$.

<details><summary>Resposta</summary>

$60^\circ$; $\approx83{,}6^\circ$; $M=1/\sin\tfrac\pi{12}\approx3{,}86$.

</details>

`•••` **1.58** O ângulo de visão de um quadro é $\theta=\tan^{-1}\tfrac{5{,}5}{x}-\tan^{-1}\tfrac{2{,}5}{x}$, com $x$ em pés. Calcule $\theta$ para $x=5$.

<details><summary>Resposta</summary>

$\approx0{,}369$ rad $\approx21{,}2^\circ$.

</details>

`•••` **1.59** Resolva $\cosh x=2$.

<details><summary>Resposta</summary>

$x=\pm\ln(2+\sqrt3)\approx\pm1{,}317$.

</details>

`•••` **1.60** Mostre que $\cosh(2x)=\cosh^2x+\sinh^2x$ e deduza que $\cosh^2x=\tfrac12(1+\cosh2x)$.

<details><summary>Resposta</summary>

Use a fórmula de adição e $\cosh^2x-\sinh^2x=1$.

</details>

`••••` **1.61** Encontre todas as funções afins $f(x)=ax+b$ tais que $f(f(x))=4x+3$ para todo $x$.

<details><summary>Resposta</summary>

$f(x)=2x+1$ ou $f(x)=-2x-3$.

</details>

`••••` **1.62** Mostre que $f(x)=\dfrac{ax+b}{cx+d}$ ($c\neq0$, $ad-bc\neq0$) é a própria inversa se, e somente se, $a=-d$. Interprete geometricamente.

<details><summary>Resposta</summary>

$f=f^{-1}$ equivale a $(a+d)(cx^2+(d-a)x-b)\equiv0$; o gráfico é simétrico em relação a $y=x$.

</details>

`••••` **1.63** Resolva $4^x-3\cdot2^{x+1}+8=0$.

<details><summary>Resposta</summary>

$x=1$ ou $x=2$.

</details>

`••••` **1.64** Prove que $\log_2 3$ é irracional.

<details><summary>Resposta</summary>

Se $\log_23=p/q$, então $3^q=2^p$: ímpar = par, absurdo.

</details>

`••••` **1.65** Quantas soluções reais tem a equação $\sin x=\dfrac{x}{10}$? Justifique com um esboço.

<details><summary>Resposta</summary>

7 soluções (todas em $[-10,10]$; uma é $x=0$, e as demais são simétricas).

</details>

## Soluções completas

<a id="ex-1-21"></a>

### 1.21 — Composição e domínio

*Origem: OpenStax, 1.1, ex. 47.*

> Sejam $f(x)=\dfrac{3}{2x+1}$ e $g(x)=\dfrac{2}{x}$. Encontre $(f\circ g)(x)$ e $(g\circ f)(x)$ e determine o domínio de cada composta.

![Animação do exercício 1.21](anim/ex-1.21.gif)

**Estratégia.** Na composta $f\circ g$, primeiro aplicamos $g$; o domínio é formado pelos $x$
do domínio de $g$ cuja imagem $g(x)$ está no domínio de $f$. Simplificar a fórmula no fim
**não** apaga as restrições do caminho.

**(a)** $(f\circ g)(x)=f\!\left(\frac2x\right)=\dfrac{3}{2\cdot\frac2x+1}=\dfrac{3}{\frac{4+x}{x}}=\dfrac{3x}{x+4}.$

Restrições: $x\neq0$ (para $g$ existir) e $g(x)\neq-\tfrac12$, isto é, $\tfrac2x\neq-\tfrac12 \iff x\neq-4$
(para $f$ existir). Domínio: $\lbrace x\mid x\neq0,\ x\neq-4\rbrace $.

Observe que a fórmula final $\frac{3x}{x+4}$ "aceita" $x=0$, mas a composta não: em $x=0$ há um **buraco** no gráfico.

**(b)** $(g\circ f)(x)=g\!\left(\frac{3}{2x+1}\right)=\dfrac{2}{\frac{3}{2x+1}}=\dfrac{2(2x+1)}{3}=\dfrac{4x+2}{3}.$

Restrições: $x\neq-\tfrac12$ (para $f$ existir) e $f(x)\neq0$, o que nunca acontece. Domínio: $\lbrace x\mid x\neq-\tfrac12\rbrace $.

**Animação.** O ponto percorre o gráfico de $f\circ g$: note a assíntota vertical em $x=-4$ e o buraco em $x=0$.

---

<a id="ex-1-26"></a>

### 1.26 — Custo e ponto de equilíbrio

*Origem: OpenStax, 1.2, ex. 105.*

> Uma confeitaria vende cupcakes em festivais. Montar a barraca custa R\$ 125,00 e cada cupcake custa R\$ 0,75 para ser produzido. (a) Escreva o custo total $C$ em função do número $x$ de cupcakes. (b) Quanto custa produzir 160 cupcakes? (c) Vendendo cada cupcake a R\$ 1,50, quantos ela precisa vender para começar a ter lucro?

![Animação do exercício 1.26](anim/ex-1.26.gif)

**(a)** Custo fixo mais custo por unidade: $C(x)=0{,}75x+125$.

**(b)** $C(160)=0{,}75\cdot160+125=120+125=245$ reais.

**(c)** A receita é $R(x)=1{,}50x$. Há lucro quando $R(x)>C(x)$:
$$1{,}50x>0{,}75x+125\iff 0{,}75x>125\iff x>166{,}\overline{6}.$$
Como $x$ é inteiro, ela precisa vender **167 cupcakes**.

**Animação.** As retas de custo e de receita se cruzam no ponto de equilíbrio $x\approx166{,}7$; à direita dele, a área entre as retas é o lucro.

---

<a id="ex-1-28"></a>

### 1.28 — Identidade trigonométrica

*Origem: OpenStax, 1.3, ex. 153.*

> Verifique a identidade $\dfrac{1}{1-\sin\alpha}+\dfrac{1}{1+\sin\alpha}=2\sec^2\alpha$.

![Animação do exercício 1.28](anim/ex-1.28.gif)

**Estratégia.** Trabalhe com o lado mais complicado (o esquerdo) até chegar ao outro.

$$\frac{1}{1-\sin\alpha}+\frac{1}{1+\sin\alpha}
=\frac{(1+\sin\alpha)+(1-\sin\alpha)}{(1-\sin\alpha)(1+\sin\alpha)}
=\frac{2}{1-\sin^2\alpha}=\frac{2}{\cos^2\alpha}=2\sec^2\alpha .$$

Usamos o produto da soma pela diferença, $(1-s)(1+s)=1-s^2$, e a identidade pitagórica $\sin^2\alpha+\cos^2\alpha=1$.

A identidade vale onde os dois lados estão definidos: $\sin\alpha\neq\pm1$, isto é, $\cos\alpha\neq0$.

**Animação.** O lado esquerdo (curva) e o lado direito (pontos) coincidem para todo $\alpha$; nas retas tracejadas $\cos\alpha=0$ e nenhum dos lados existe.

---

<a id="ex-1-37"></a>

### 1.37 — Expressões hiperbólicas

*Origem: OpenStax, 1.5, ex. 298.*

> Reescreva em termos de exponenciais e simplifique: (a) $2\cosh(\ln x)$; (b) $\cosh 4x+\sinh 4x$; (c) $\cosh 2x-\sinh 2x$; (d) $\ln(\cosh x+\sinh x)+\ln(\cosh x-\sinh x)$.

![Animação do exercício 1.37](anim/ex-1.37.gif)

Use $\cosh u=\frac{e^u+e^{-u}}2$ e $\sinh u=\frac{e^u-e^{-u}}2$.

**(a)** $2\cosh(\ln x)=e^{\ln x}+e^{-\ln x}=x+\frac1x$, para $x>0$.

**(b)** $\cosh 4x+\sinh 4x=\frac{e^{4x}+e^{-4x}+e^{4x}-e^{-4x}}2=e^{4x}$.

**(c)** $\cosh 2x-\sinh 2x=\frac{e^{2x}+e^{-2x}-e^{2x}+e^{-2x}}2=e^{-2x}$.

**(d)** Pelos itens anteriores, $\cosh x+\sinh x=e^x$ e $\cosh x-\sinh x=e^{-x}$. Logo
$\ln e^x+\ln e^{-x}=x-x=0$. (Alternativa: o produto é $\cosh^2x-\sinh^2x=1$, e $\ln1=0$.)

**Animação.** As curvas de $\cosh kx$ e $\sinh kx$ somadas coincidem sempre com $e^{kx}$, enquanto $k$ varia.

---

<a id="ex-1-38"></a>

### 1.38 — Decaimento do iodo-131

*Origem: OpenStax, 1.5, ex. 304.*

> O iodo-131 decai segundo $Q(t)=Q_0e^{-0{,}08664t}$, com $t$ em dias. Quanto tempo leva (arredondando para o dia mais próximo) para 95% de uma amostra decair?

![Animação do exercício 1.38](anim/ex-1.38.gif)

Se 95% decaiu, restam 5%: $Q(t)=0{,}05\,Q_0$.
$$e^{-0{,}08664t}=0{,}05\iff -0{,}08664\,t=\ln0{,}05\iff t=\frac{-\ln0{,}05}{0{,}08664}=\frac{\ln20}{0{,}08664}\approx\frac{2{,}996}{0{,}08664}\approx34{,}6 .$$
Resposta: **cerca de 35 dias**.

**Comentário.** A meia-vida é $\frac{\ln2}{0{,}08664}\approx8$ dias. Como $0{,}05\approx2^{-4{,}3}$, são necessárias cerca de 4,3 meias-vidas, ou seja, $4{,}3\times8\approx35$ dias.

**Animação.** A curva de decaimento é traçada até cruzar o nível de 5%.

---

<a id="ex-1-39"></a>

### 1.39 — Escala Richter

*Origem: OpenStax, 1.5, ex. 309.*

> O terremoto de 1906 em São Francisco teve magnitude 8,3 na escala Richter. No mesmo período, um terremoto de magnitude 4,9 no Japão causou poucos danos. Quantas vezes o de São Francisco foi mais intenso?

![Animação do exercício 1.39](anim/ex-1.39.gif)

Pela escala Richter, $R_1-R_2=\log_{10}\frac{A_1}{A_2}$. Então
$$\log_{10}\frac{A_1}{A_2}=8{,}3-4{,}9=3{,}4\Rightarrow\frac{A_1}{A_2}=10^{3{,}4}\approx2512 .$$
O terremoto de São Francisco foi **cerca de 2500 vezes** mais intenso.

**Intuição.** Cada ponto a mais na escala multiplica a intensidade por 10. Uma diferença de 3,4 pontos é $10^3\cdot10^{0{,}4}\approx1000\cdot2{,}5$.

**Animação.** A magnitude sobe de 4,9 a 8,3 enquanto a barra de intensidade relativa cresce (em escala logarítmica).

---

<a id="ex-1-41"></a>

### 1.41 — Horas de luz do dia

*Origem: OpenStax, 1.3, ex. 180.*

> O número de horas de luz do dia em uma cidade é modelado por $N(t)=12+3\sin\!\left[\frac{2\pi}{365}(t-79)\right]$, em que $t$ é o número de dias após 1º de janeiro. (a) Encontre a amplitude e o período. (b) Quantas horas de luz há no dia mais longo do ano? E no mais curto? (c) Quantas horas de luz há 90 dias após 1º de janeiro?

![Animação do exercício 1.41](anim/ex-1.41.gif)

**(a)** Na forma $A\sin(B(t-\alpha))+C$: $A=3$ (amplitude), $B=\frac{2\pi}{365}$, logo o período é
$\frac{2\pi}{B}=365$ dias. A defasagem é $\alpha=79$ (por volta de 20 de março, o equinócio) e o deslocamento vertical, $C=12$.

**(b)** O seno varia entre $-1$ e $1$, então $N$ varia entre $12-3=9$ e $12+3=15$.
Dia mais longo: **15 horas**. Dia mais curto: **9 horas**.

O máximo ocorre quando $\frac{2\pi}{365}(t-79)=\frac\pi2$, isto é, $t=79+\frac{365}{4}\approx170$ (por volta de 20 de junho).

**(c)** $N(90)=12+3\sin\!\left(\frac{2\pi\cdot11}{365}\right)=12+3\sin(0{,}1894)\approx12+3(0{,}188)\approx12{,}56$ horas.

**Animação.** O ponto percorre o ano; as linhas tracejadas marcam 9 h e 15 h.

---

<a id="ex-1-42"></a>

### 1.42 — Custo de remoção de uma toxina

*Origem: OpenStax, 1.4, ex. 219.*

> O custo (em milhares de reais) para remover $p$ partes por bilhão (ppb) de uma toxina de um lago é $C(p)=\dfrac{75p}{85-p}$, válido para $0\le p<85$. (a) Calcule o custo para remover 25, 40 e 50 ppb. (b) Encontre a função inversa $p=C^{-1}(C)$. (c) Quanto da toxina se remove com R\$ 50 mil?

![Animação do exercício 1.42](anim/ex-1.42.gif)

**(a)** $C(25)=\frac{75\cdot25}{60}=31{,}25$; $C(40)=\frac{3000}{45}\approx66{,}67$; $C(50)=\frac{3750}{35}\approx107{,}14$ (milhares de reais).
Note como o custo cresce cada vez mais rápido: remover os últimos ppb é caríssimo, e $C\to\infty$ quando $p\to85^-$.

**(b)** Isolamos $p$ em $C=\frac{75p}{85-p}$:
$$C(85-p)=75p\iff 85C=75p+Cp=p(75+C)\iff p=\frac{85C}{C+75}.$$

**(c)** $p=\frac{85\cdot50}{125}=34$ ppb.

**Animação.** O gráfico de $C$ é refletido em torno da reta $y=x$ para formar o gráfico da inversa. A assíntota vertical $p=85$ de $C$ vira a assíntota horizontal da inversa.

---

<a id="ex-1-43"></a>

### 1.43 — Profundidade da maré

*Origem: OpenStax, 1.4, ex. 224.*

> A profundidade (em pés) da água em um cais é $D(t)=5\sin\!\left(\frac{\pi}{6}t-\frac{7\pi}{6}\right)+8$, em que $t$ é o número de horas após a meia-noite. Determine o primeiro instante após a meia-noite em que a profundidade é 11,75 pés.

![Animação do exercício 1.43](anim/ex-1.43.gif)

Queremos $D(t)=11{,}75$:
$$5\sin\!\left(\tfrac{\pi}{6}t-\tfrac{7\pi}{6}\right)+8=11{,}75\iff \sin\!\left(\tfrac{\pi}{6}(t-7)\right)=0{,}75 .$$

Seja $u=\frac\pi6(t-7)$. Para $t\ge0$, $u\ge-\frac{7\pi}{6}$. As soluções de $\sin u=0{,}75$ são
$u=\sin^{-1}(0{,}75)+2k\pi\approx0{,}8481+2k\pi$ e $u=\pi-0{,}8481+2k\pi\approx2{,}2935+2k\pi$.

Procuramos o **menor** $u\ge-\frac{7\pi}6\approx-3{,}665$:
- $0{,}8481-2\pi\approx-5{,}435$ (antes da meia-noite, descartado);
- $2{,}2935-2\pi\approx-3{,}990$ (também antes, pois $<-3{,}665$);
- $0{,}8481$ ✓.

Então $\frac\pi6(t-7)=0{,}8481\Rightarrow t=7+\frac{6(0{,}8481)}{\pi}\approx8{,}62$ h, ou seja, **por volta de 8h37**.

**Cuidado.** A função $\sin^{-1}$ dá apenas *uma* solução (entre $-\frac\pi2$ e $\frac\pi2$). Em problemas com tempo, liste todas as soluções e escolha a que respeita o intervalo pedido.

**Animação.** A curva da maré é desenhada a partir da meia-noite até tocar a linha de 11,75 pés.

---

<a id="ex-1-44"></a>

### 1.44 — Crescimento de bactérias

*Origem: OpenStax, 1.5, ex. 307.*

> Uma colônia de bactérias dobra a cada 12 horas e começa com 1000 bactérias. (a) Usando $Q=Q_0e^{kt}$, determine $k$ (quatro casas decimais). (b) Aproximadamente quanto tempo leva para haver 200\,000 bactérias?

![Animação do exercício 1.44](anim/ex-1.44.gif)

**(a)** Em $t=12$, $Q=2Q_0$: $e^{12k}=2\Rightarrow k=\frac{\ln2}{12}\approx0{,}0578$ por hora.

**(b)** $1000e^{kt}=200\,000\iff e^{kt}=200\iff t=\frac{\ln200}{k}=\frac{12\ln200}{\ln2}\approx\frac{12\cdot5{,}298}{0{,}6931}\approx91{,}7$ h.
Resposta: **cerca de 92 horas**. (Conferência: $2^{91{,}7/12}=2^{7{,}64}\approx200$.)

**Animação.** À esquerda, a escala linear: o crescimento parece "explodir". À direita, a escala logarítmica: a exponencial vira uma reta de inclinação $k$.

---

<a id="ex-1-45"></a>

### 1.45 — População sazonal

*Origem: OpenStax, Revisão, ex. 333.*

> A população de uma cidade litorânea, em milhares, é modelada por $P(t)=82{,}5-67{,}5\cos\!\left(\frac\pi6t\right)$, com $t$ em meses ($t=0$ é 1º de janeiro). Em que intervalos do ano a população é menor que 20 mil? E maior que 140 mil?

![Animação do exercício 1.45](anim/ex-1.45.gif)

**Menor que 20 mil.**
$$82{,}5-67{,}5\cos\left(\tfrac\pi6t\right)<20\iff\cos\left(\tfrac\pi6t\right)>\tfrac{62{,}5}{67{,}5}\approx0{,}9259 .$$
Como $\cos^{-1}(0{,}9259)\approx0{,}3873$ rad, precisamos de $\frac\pi6t<0{,}3873$ ou $\frac\pi6t>2\pi-0{,}3873$, isto é,
$t<0{,}74$ ou $t>11{,}26$ meses: **de por volta de 8 de dezembro a 23 de janeiro**.

**Maior que 140 mil.**
$$\cos\left(\tfrac\pi6t\right)<-\tfrac{57{,}5}{67{,}5}\approx-0{,}8519 .$$
Como $\cos^{-1}(-0{,}8519)\approx2{,}5903$ rad, precisamos de $2{,}5903<\frac\pi6t<2\pi-2{,}5903$, isto é,
$4{,}95<t<7{,}05$: **de por volta de 29 de maio a 2 de agosto**.

**Animação.** As faixas sombreadas mostram os períodos abaixo de 20 mil (azul) e acima de 140 mil (laranja).

---
