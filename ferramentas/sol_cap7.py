# -*- coding: utf-8 -*-
"""Soluções completas (★) do capítulo 7."""

SOLUCOES = [
dict(id='partes', origem='inspirado no Exemplo 7.1', titulo='Partes com logaritmo (e a figura do retângulo)',
enunciado=r"""Calcule $\int_1^e\ln x\,dx$ e $\int_1^ex\ln x\,dx$ por partes. Interprete o primeiro resultado como
uma diferença de áreas num retângulo.""",
resposta=r"""$1$; $\tfrac{e^2+1}4\approx2{,}097$.""",
solucao=r"""**Primeira.** $u=\ln x$ (L de LIATE), $dv=dx$: $du=\frac{dx}x$, $v=x$.
$$\int_1^e\ln x\,dx=\big[x\ln x\big]_1^e-\int_1^e x\cdot\frac1x\,dx=(e-0)-(e-1)=1 .$$

**Geometria.** O gráfico de $y=\ln x$ entre $(1,0)$ e $(e,1)$ é o mesmo que $x=e^y$ para $0\le y\le1$. A região *sob* $\ln x$ e a região *à esquerda* da curva (entre o eixo $y$ e $x=e^y$) preenchem o retângulo $[0,e]\times[0,1]$, de área $e$. Como a segunda vale $\int_0^1e^y\,dy=e-1$, sobra $1$ para a primeira. Partes é exatamente isto: $\int u\,dv+\int v\,du=uv$.

**Segunda.** $u=\ln x$, $dv=x\,dx$: $v=\frac{x^2}2$.
$$\int_1^ex\ln x\,dx=\Big[\frac{x^2}2\ln x\Big]_1^e-\int_1^e\frac x2\,dx=\frac{e^2}2-\Big[\frac{x^2}4\Big]_1^e=\frac{e^2}2-\frac{e^2}4+\frac14=\frac{e^2+1}4 .$$

**Por que não $u=x$?** Teríamos $dv=\ln x\,dx$, e integrar $\ln x$ é justamente o problema. O logaritmo simplifica ao derivar ($\frac1x$), por isso vai para $u$.

**Animação.** A área sob $\ln x$ (azul) e a área $\int_0^1e^y\,dy$ (laranja) preenchem juntas o retângulo $e\times1$.""",
),
dict(id='ciclica', origem='inspirado na seção 7.1', titulo='Uma integral que volta a si mesma',
enunciado=r"""Calcule $\int e^x\sen x\,dx$ e depois $\int_0^\pi e^x\sen x\,dx$.""",
resposta=r"""$\tfrac12e^x(\sen x-\cos x)+C$; $\tfrac{e^\pi+1}2\approx12{,}070$.""",
solucao=r"""Seja $I=\int e^x\sen x\,dx$.

**Primeira vez** ($u=\sen x$, $dv=e^xdx$): $I=e^x\sen x-\int e^x\cos x\,dx$.

**Segunda vez** ($u=\cos x$, $dv=e^xdx$, mantendo a escolha!): $\int e^x\cos x\,dx=e^x\cos x+\int e^x\sen x\,dx=e^x\cos x+I$.

**Juntando:** $I=e^x\sen x-e^x\cos x-I$, logo
$$I=\tfrac12e^x(\sen x-\cos x)+C .$$

**Atenção.** Se na segunda vez escolhermos $u=e^x$, as partes se desfazem e chegamos a $I=I$. A escolha de $dv$ tem de ser a mesma nas duas etapas.

**Definida:** $\Big[\tfrac12e^x(\sen x-\cos x)\Big]_0^\pi=\tfrac12e^\pi(0+1)-\tfrac12(0-1)=\frac{e^\pi+1}2\approx12{,}070$.

**Conferência derivando:** $\tfrac12\big[e^x(\sen x-\cos x)+e^x(\cos x+\sen x)\big]=e^x\sen x$. ✓

**Animação.** A área sob $e^x\sen x$ é acumulada de $0$ a $\pi$ e comparada com a fórmula.""",
),
dict(id='sec3', origem='inspirado no Exemplo 7.2', titulo='A integral da secante ao cubo',
enunciado=r"""Mostre que $\int\sec^3x\,dx=\frac12\big(\sec x\tg x+\ln|\sec x+\tg x|\big)+C$ e calcule
$\int_0^{\pi/4}\sec^3x\,dx$.""",
resposta=r"""$\tfrac12\big(\sqrt2+\ln(1+\sqrt2)\big)\approx1{,}1478$.""",
solucao=r"""**Partes:** $u=\sec x$, $dv=\sec^2x\,dx$, então $du=\sec x\tg x\,dx$, $v=\tg x$.
$$\int\sec^3x\,dx=\sec x\tg x-\int\sec x\tg^2x\,dx .$$

**Identidade** $\tg^2x=\sec^2x-1$:
$$\int\sec^3x\,dx=\sec x\tg x-\int\sec^3x\,dx+\int\sec x\,dx .$$
A integral reapareceu (cíclica). Passando para a esquerda e usando $\int\sec x\,dx=\ln|\sec x+\tg x|$ (capítulo 5):
$$2\int\sec^3x\,dx=\sec x\tg x+\ln|\sec x+\tg x|+C .$$

**Valor:** em $x=\frac\pi4$, $\sec=\sqrt2$, $\tg=1$; em $0$, $\sec=1$, $\tg=0$:
$$\int_0^{\pi/4}\sec^3x\,dx=\tfrac12\big(\sqrt2+\ln(\sqrt2+1)\big)-\tfrac12(0+\ln1)\approx1{,}1478 .$$

**Onde aparece.** Essa integral surge na substituição $x=a\tg\theta$ em $\int\sqrt{a^2+x^2}\,dx$, por exemplo no comprimento de arco da parábola (outro exercício resolvido desta lista).

**Animação.** A área sob $\sec^3x$ cresce até $\pi/4$; o valor acumulado coincide com a fórmula.""",
),
dict(id='elipse', origem='inspirado no Exemplo 7.3', titulo='A área da elipse',
enunciado=r"""Use substituição trigonométrica para mostrar que a elipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}\le1$ tem área $\pi ab$.""",
resposta=r"""$\pi ab$.""",
solucao=r"""**Montagem.** A metade de cima é $y=\frac ba\sqrt{a^2-x^2}$. Por simetria, a área é quatro vezes a do primeiro quadrante:
$$A=4\int_0^a\frac ba\sqrt{a^2-x^2}\,dx .$$

**Substituição** $x=a\sen\theta$: $dx=a\cos\theta\,d\theta$, $\sqrt{a^2-x^2}=a\cos\theta$; limites $x=0\mapsto\theta=0$, $x=a\mapsto\theta=\frac\pi2$.
$$A=4\cdot\frac ba\int_0^{\pi/2}a^2\cos^2\theta\,d\theta=4ab\int_0^{\pi/2}\frac{1+\cos2\theta}2\,d\theta=4ab\cdot\frac\pi4=\pi ab .$$

**Conferências.** $a=b=r$ dá $\pi r^2$ (círculo). A elipse é o círculo unitário esticado por $a$ na horizontal e por $b$ na vertical, e áreas se multiplicam por $ab$.

**Exemplo numérico:** $a=3$, $b=2$: $A=6\pi\approx18{,}85$.

**Animação.** O ângulo $\theta$ vai de $-\pi/2$ a $\pi/2$; a faixa vertical em $x=3\sen\theta$ varre a elipse e a área acumulada chega a $6\pi$.""",
),
dict(id='fracoes', origem='inspirado no Exemplo 7.4', titulo='Frações parciais com fator repetido',
enunciado=r"""Calcule $\displaystyle\int\frac{5x^2+3x-2}{x^3+2x^2}\,dx$ e depois a integral de $1$ a $2$.""",
resposta=r"""$2\ln|x|+\frac1x+3\ln|x+2|+C$; $2\ln2-\tfrac12+3\ln\tfrac43\approx1{,}749$.""",
solucao=r"""**Fatoração:** $x^3+2x^2=x^2(x+2)$: fator $x$ repetido e fator linear $x+2$. A fração é própria (grau 2 < grau 3).

**Forma:**
$$\frac{5x^2+3x-2}{x^2(x+2)}=\frac Ax+\frac B{x^2}+\frac C{x+2}\iff5x^2+3x-2=Ax(x+2)+B(x+2)+Cx^2 .$$

**Constantes:**
- $x=0$: $-2=2B\Rightarrow B=-1$;
- $x=-2$: $20-6-2=12=4C\Rightarrow C=3$;
- coeficiente de $x^2$: $A+C=5\Rightarrow A=2$.

**Integral:**
$$\int\Big(\frac2x-\frac1{x^2}+\frac3{x+2}\Big)dx=2\ln|x|+\frac1x+3\ln|x+2|+C .$$

**De 1 a 2:** $\big(2\ln2+\tfrac12+3\ln4\big)-\big(0+1+3\ln3\big)=2\ln2-\tfrac12+3\ln\tfrac43\approx1{,}749$.

**Por que precisa de $\frac B{x^2}$?** Só com $\frac Ax+\frac C{x+2}$ o denominador comum seria $x(x+2)$, de grau 2, e não haveria como reproduzir o $x^2$ do denominador original.

**Animação.** As três parcelas são desenhadas e somadas uma a uma até reproduzirem a função original.""",
),
dict(id='simpson', origem='inspirado no Exemplo 7.5', titulo='Trapézio e Simpson para $e^{-x^2}$',
enunciado=r"""A função $e^{-x^2}$ não tem antiderivada elementar. Calcule $T_4$ e $S_4$ para $\int_0^1e^{-x^2}dx$ e
use os limitantes de erro (com $|f''|\le2$ e $|f^{(4)}|\le12$ em $[0,1]$) para dizer quantas casas são confiáveis.""",
resposta=r"""$T_4\approx0{,}742984$; $S_4\approx0{,}746855$; valor $\approx0{,}746824$.""",
solucao=r"""**Valores** ($\Delta x=0{,}25$): $f(0)=1$; $f(0{,}25)\approx0{,}939413$; $f(0{,}5)\approx0{,}778801$; $f(0{,}75)\approx0{,}569783$; $f(1)\approx0{,}367879$.

**Trapézio:**
$$T_4=\tfrac{0{,}25}2\big[1+2(0{,}939413+0{,}778801+0{,}569783)+0{,}367879\big]\approx0{,}742984 .$$

**Simpson:**
$$S_4=\tfrac{0{,}25}3\big[1+4(0{,}939413)+2(0{,}778801)+4(0{,}569783)+0{,}367879\big]\approx0{,}746855 .$$

**Cotas de erro:**
- $|E_T|\le\frac{2\cdot1^3}{12\cdot4^2}\approx0{,}0104$;
- $|E_S|\le\frac{12\cdot1^5}{180\cdot4^4}\approx0{,}00026$.

Logo $S_4$ garante $\int_0^1e^{-x^2}dx\in[0{,}7466;\,0{,}7471]$. O valor real é $0{,}746824$: os erros efetivos são $0{,}0038$ (trapézio) e $0{,}00003$ (Simpson).

**Tendência:** com $n=8$, $T_8\approx0{,}745866$ e $S_8\approx0{,}746826$. O erro do trapézio cai cerca de 4 vezes; o de Simpson, cerca de 16.

**Animação.** Os trapézios para $n=2,4,8,16$ se ajustam à curva e o título compara $T_n$ e $S_n$ com o valor exato.""",
),
dict(id='arco_parabola', origem='inspirado nas seções 6.4 e 7.3', titulo='O comprimento da parábola',
enunciado=r"""Calcule o comprimento de arco de $y=x^2$ para $0\le x\le1$.""",
resposta=r"""$\tfrac14\big(2\sqrt5+\ln(2+\sqrt5)\big)\approx1{,}4789$.""",
solucao=r"""**Integral:** $y'=2x$, então $L=\int_0^1\sqrt{1+4x^2}\,dx$. É o caso $\sqrt{a^2+u^2}$, com $u=2x$.

**Substituição** $2x=\tg\theta$: $dx=\frac12\sec^2\theta\,d\theta$, $\sqrt{1+4x^2}=\sec\theta$. Limites: $x=0\mapsto\theta=0$; $x=1\mapsto\theta=\alpha$, com $\tg\alpha=2$, $\sec\alpha=\sqrt5$.
$$L=\frac12\int_0^\alpha\sec^3\theta\,d\theta=\frac14\Big[\sec\theta\tg\theta+\ln|\sec\theta+\tg\theta|\Big]_0^\alpha=\frac14\big(2\sqrt5+\ln(2+\sqrt5)\big).$$
(Usamos a integral de $\sec^3$ do exercício da secante ao cubo.)

**Valor:** $\frac14(4{,}4721+1{,}4436)\approx1{,}4789$.

**Conferência:** a corda de $(0,0)$ a $(1,1)$ mede $\sqrt2\approx1{,}4142<1{,}4789$; e o caminho pelos catetos mede $2$. O arco fica entre os dois, como deve.

**Lição.** Até a parábola, a curva mais simples depois da reta, exige substituição trigonométrica e uma integral cíclica para ter o comprimento calculado.

**Animação.** Poligonais com cada vez mais lados se aproximam da parábola; o comprimento converge para $1{,}4789$.""",
),
dict(id='gabriel', origem='inspirado na seção 7.6', titulo='A trombeta de Gabriel',
enunciado=r"""Gire $y=\frac1x$, $x\ge1$, em torno do eixo $x$. Mostre que o sólido tem volume finito, mas a
superfície tem área infinita.""",
resposta=r"""$V=\pi$; $S=\infty$.""",
solucao=r"""**Volume (discos):**
$$V=\pi\int_1^\infty\frac{dx}{x^2}=\pi\lim_{t\to\infty}\Big(1-\frac1t\Big)=\pi .$$

**Área de superfície:**
$$S=2\pi\int_1^\infty\frac1x\sqrt{1+\frac1{x^4}}\,dx .$$
Não precisamos calculá-la: como $\sqrt{1+\frac1{x^4}}\ge1$,
$$\frac1x\sqrt{1+\frac1{x^4}}\ge\frac1x,\qquad\text{e}\qquad\int_1^\infty\frac{dx}x=\infty .$$
Pelo **teste da comparação**, $S=\infty$.

**O paradoxo do pintor.** A trombeta ``cabe'' em $\pi$ unidades de tinta (o volume), mas a parede interna teria área infinita, e nenhuma quantidade de tinta a cobriria. A saída: uma camada de tinta com espessura constante não cabe no tubo, que fica mais fino que qualquer espessura. Encher o volume não é o mesmo que pintar a superfície.

**Truncando em $x=R$:** $V(R)=\pi(1-\frac1R)\to\pi$, enquanto $S(R)\ge2\pi\ln R\to\infty$.

**Animação.** A trombeta se estende até $R$ cada vez maior; o título mostra $V(R)$ estabilizando em $\pi$ e $S(R)$ crescendo sem limite.""",
),
dict(id='gama', origem='inspirado na seção 7.6', titulo='A função gama',
enunciado=r"""Seja $\Gamma(x)=\int_0^\infty t^{x-1}e^{-t}\,dt$ para $x>0$. Mostre que $\Gamma(1)=1$, que
$\Gamma(x+1)=x\,\Gamma(x)$ e conclua que $\Gamma(n+1)=n!$.""",
resposta=r"""$\Gamma(n+1)=n!$.""",
solucao=r"""**Convergência.** Perto de $t=0$, $t^{x-1}e^{-t}\le t^{x-1}$, integrável se $x-1>-1$, isto é, $x>0$. Para $t$ grande, $t^{x-1}e^{-t/2}\to0$, então $t^{x-1}e^{-t}\le e^{-t/2}$ a partir de algum ponto, e $\int^\infty e^{-t/2}$ converge.

**$\Gamma(1)=\int_0^\infty e^{-t}dt=\lim_{b\to\infty}(1-e^{-b})=1$.**

**Recorrência (partes):** $u=t^x$, $dv=e^{-t}dt$:
$$\Gamma(x+1)=\int_0^\infty t^xe^{-t}dt=\Big[-t^xe^{-t}\Big]_0^\infty+x\int_0^\infty t^{x-1}e^{-t}dt=0+x\,\Gamma(x) .$$
(O termo de fronteira some: $t^xe^{-t}\to0$ quando $t\to\infty$, e vale $0$ em $t=0$ porque $x>0$.)

**Fatorial:** $\Gamma(2)=1\cdot\Gamma(1)=1$, $\Gamma(3)=2\cdot1$, $\Gamma(4)=3\cdot2\cdot1$, e por indução $\Gamma(n+1)=n!$.

**Significado.** $\Gamma$ estende o fatorial a números não inteiros: por exemplo $\Gamma(\tfrac12)=\sqrt\pi$, que é o desafio 7.64.

**Animação.** Para $n=0,1,\dots,5$, a área sob $t^ne^{-t}$ é preenchida e vale $n!$: $1,1,2,6,24,120$.""",
),
dict(id='weierstrass', origem='inspirado na seção 7.4', titulo='A substituição universal $t=\\tg(x/2)$',
enunciado=r"""Com $t=\tg\frac x2$, mostre que $\cos x=\frac{1-t^2}{1+t^2}$ e $dx=\frac{2\,dt}{1+t^2}$, e calcule
$\displaystyle\int_0^{\pi/2}\frac{dx}{2+\cos x}$.""",
resposta=r"""$\tfrac{\pi}{3\sqrt3}\approx0{,}6046$.""",
solucao=r"""**Fórmulas.** $\cos x=\cos^2\frac x2-\sen^2\frac x2=\frac{1-\tg^2(x/2)}{\sec^2(x/2)}=\frac{1-t^2}{1+t^2}$. De $x=2\arctg t$: $dx=\frac{2\,dt}{1+t^2}$. (Analogamente, $\sen x=\frac{2t}{1+t^2}$.)

**Transformando:** $2+\cos x=\frac{2(1+t^2)+1-t^2}{1+t^2}=\frac{3+t^2}{1+t^2}$. Limites: $x=0\mapsto t=0$; $x=\frac\pi2\mapsto t=1$.
$$\int_0^{\pi/2}\frac{dx}{2+\cos x}=\int_0^1\frac{1+t^2}{3+t^2}\cdot\frac{2\,dt}{1+t^2}=\int_0^1\frac{2\,dt}{3+t^2}=\frac2{\sqrt3}\Big[\arctg\frac t{\sqrt3}\Big]_0^1=\frac2{\sqrt3}\cdot\frac\pi6=\frac\pi{3\sqrt3}.$$

**Valor:** $\approx0{,}6046$. Conferência: o integrando fica entre $\frac13$ e $\frac12$, então a integral está entre $\frac\pi6\approx0{,}52$ e $\frac\pi4\approx0{,}79$. ✓

**Por que ``universal''.** Toda função racional de $\sen x$ e $\cos x$ vira uma função racional de $t$, que sempre pode ser integrada por frações parciais (embora nem sempre seja o caminho mais curto).

**Animação.** As áreas sob $\frac1{2+\cos x}$ em $[0,\pi/2]$ e sob $\frac2{3+t^2}$ em $[0,1]$ são preenchidas juntas e têm sempre o mesmo valor.""",
),
dict(id='logistica', origem='inspirado na seção 7.4', titulo='Crescimento logístico',
enunciado=r"""Uma população segue $\dfrac{dP}{dt}=0{,}5\,P\Big(1-\dfrac P{1000}\Big)$, com $P(0)=100$. Separe as variáveis,
use frações parciais e encontre $P(t)$. Quando a população chega a $500$? Quando cresce mais rápido?""",
resposta=r"""$P(t)=\dfrac{1000}{1+9e^{-t/2}}$; $t=2\ln9\approx4{,}39$; crescimento máximo quando $P=500$.""",
solucao=r"""**Separando:** $\displaystyle\int\frac{1000\,dP}{P(1000-P)}=\int0{,}5\,dt$.

**Frações parciais:** $\frac{1000}{P(1000-P)}=\frac1P+\frac1{1000-P}$ (verifique somando).

**Integrando:** $\ln P-\ln(1000-P)=0{,}5t+C$, isto é, $\frac P{1000-P}=Ke^{t/2}$. Com $P(0)=100$: $K=\frac{100}{900}=\frac19$.

**Isolando $P$:**
$$P(t)=\frac{1000}{1+9e^{-t/2}} .$$

**$P=500$:** $9e^{-t/2}=1\Rightarrow t=2\ln9\approx4{,}39$.

**Crescimento mais rápido:** $P'=0{,}5P(1-\frac P{1000})$ é uma parábola em $P$ com máximo em $P=500$, onde $P'=125$ por unidade de tempo. Portanto o ponto de inflexão da curva é $(2\ln9;\,500)$.

**Comportamento:** $P\to1000$ (capacidade de suporte). No início, $P\ll1000$ e $P'\approx0{,}5P$: crescimento quase exponencial.

**Animação.** A curva logística é desenhada sobre o campo de inclinações; o ponto de inflexão é marcado em $P=500$.""",
),
]
