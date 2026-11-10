# -*- coding: utf-8 -*-
"""Soluções completas (★) do capítulo 4."""

SOLUCOES = [
dict(id='escada', origem='inspirado no Exemplo 4.2', titulo='A escada escorregando',
enunciado=r"""Uma escada de 5 m está apoiada numa parede vertical. A base se afasta da parede a
$0{,}5$ m/s. (a) Com que rapidez o topo desce quando a base está a 3 m da parede?
(b) Em que posição as duas extremidades se movem com a mesma rapidez?""",
resposta=r"""(a) $0{,}375$ m/s; (b) quando $x=y=\tfrac{5}{\sqrt2}\approx3{,}54$ m.""",
solucao=r"""**Modelo.** $x$ = distância da base à parede, $y$ = altura do topo: $x^2+y^2=25$.

**Derivando em $t$:** $2x\,x'+2y\,y'=0\Rightarrow y'=-\dfrac{x}{y}\,x'$.

**(a)** $x=3\Rightarrow y=4$. Com $x'=0{,}5$: $y'=-\frac34(0{,}5)=-0{,}375$ m/s. O topo **desce** a $0{,}375$ m/s.

**(b)** $|y'|=|x'|\iff\frac xy=1\iff x=y=\frac5{\sqrt2}\approx3{,}54$ m.

**Observação.** Quando $y\to0$, $|y'|=\frac xy\,x'\to\infty$: o modelo prevê que o topo cai "infinitamente rápido" no fim. Na prática, a escada perde contato com a parede antes disso.

**Animação.** A escada escorrega; as setas mostram as velocidades da base (constante) e do topo (cada vez maior).""",
),
dict(id='sombra', origem='problema clássico de taxas relacionadas', titulo='A sombra no poste',
enunciado=r"""Uma pessoa de $1{,}8$ m se afasta de um poste de luz de 6 m de altura a $1{,}5$ m/s.
(a) Com que rapidez sua sombra aumenta? (b) Com que rapidez a ponta da sombra se move?""",
resposta=r"""(a) $\tfrac{9}{14}\approx0{,}64$ m/s; (b) $\tfrac{15}{7}\approx2{,}14$ m/s.""",
solucao=r"""**Modelo.** $x$ = distância da pessoa ao poste, $s$ = comprimento da sombra. Por semelhança de triângulos (poste e pessoa, ambos com a ponta da sombra como vértice):
$$\frac{s}{1{,}8}=\frac{x+s}{6}\iff6s=1{,}8x+1{,}8s\iff s=\frac{3}{7}x .$$

**(a)** $s'=\frac37x'=\frac37(1{,}5)=\frac9{14}\approx0{,}64$ m/s (constante!).

**(b)** A ponta está em $x+s$: $(x+s)'=1{,}5+0{,}64=\frac{15}7\approx2{,}14$ m/s.

**Observação.** As taxas não dependem de onde a pessoa está, porque a relação entre $s$ e $x$ é **linear**.

**Animação.** A pessoa caminha, e a sombra (em laranja) cresce proporcionalmente à distância ao poste.""",
),
dict(id='aviao', origem='inspirado no Exemplo 4.2 (avião)', titulo='Avião e radar',
enunciado=r"""Um avião voa horizontalmente a 4 km de altitude, a 600 km/h, numa trajetória que passa
diretamente acima de uma estação de radar. Com que rapidez a distância avião–radar aumenta
quando essa distância é 5 km (e o avião já passou da estação)?""",
resposta=r"""360 km/h.""",
solucao=r"""**Modelo.** $x$ = distância horizontal do avião à estação, $D$ = distância avião–radar: $D^2=x^2+16$.

**Derivando:** $2D\,D'=2x\,x'\Rightarrow D'=\dfrac{x}{D}\,x'$.

Quando $D=5$: $x=3$. Com $x'=600$: $D'=\frac35(600)=360$ km/h.

**Interpretação.** $\frac xD=\cos\theta$, onde $\theta$ é o ângulo entre a horizontal e a linha de visada: só a componente da velocidade **ao longo** da linha de visada afasta o avião do radar. Bem acima da estação, $x=0$ e $D'=0$; muito longe, $\frac xD\to1$ e $D'\to600$.

**Animação.** O avião passa sobre o radar; o gráfico mostra $D'(t)$ subindo de $-600$ a $600$ km/h.""",
),
dict(id='extremos', origem='inspirado no Exemplo 4.13', titulo='Método do intervalo fechado',
enunciado=r"""Encontre os valores máximo e mínimo absolutos de $f(x)=x\,e^{-x}$ em $[0,4]$.""",
resposta=r"""Máximo $\tfrac1e\approx0{,}368$ em $x=1$; mínimo $0$ em $x=0$.""",
solucao=r"""**Pontos críticos.** $f'(x)=e^{-x}-xe^{-x}=e^{-x}(1-x)$. Como $e^{-x}>0$, $f'=0\iff x=1$.

**Tabela de valores:**

| $x$ | $f(x)$ |
|---|---|
| $0$ (extremidade) | $0$ |
| $1$ (crítico) | $e^{-1}\approx0{,}368$ |
| $4$ (extremidade) | $4e^{-4}\approx0{,}073$ |

**Máximo absoluto:** $\frac1e$ em $x=1$. **Mínimo absoluto:** $0$ em $x=0$.

**Por que funciona?** $f$ é contínua em $[0,4]$ (Teorema do Valor Extremo: os extremos existem) e eles só podem estar em pontos críticos ou nas extremidades.

**Animação.** Uma reta horizontal desce desde o topo até tocar o gráfico (máximo) e sobe desde baixo até tocá-lo (mínimo).""",
),
dict(id='tvm', origem='inspirado no Exemplo 4.15', titulo='Teorema do Valor Médio',
enunciado=r"""Verifique as hipóteses do TVM para $f(x)=x^3-x$ em $[0,2]$ e encontre todos os $c$ garantidos
pelo teorema.""",
resposta=r"""$c=\tfrac{2}{\sqrt3}\approx1{,}155$.""",
solucao=r"""**Hipóteses.** $f$ é polinômio: contínua em $[0,2]$ e derivável em $(0,2)$. ✓

**Inclinação média:** $\dfrac{f(2)-f(0)}{2-0}=\dfrac{6-0}{2}=3$.

**Condição:** $f'(c)=3c^2-1=3\iff c^2=\frac43\iff c=\pm\frac2{\sqrt3}$. Só $c=\frac2{\sqrt3}\approx1{,}155$ está em $(0,2)$.

**Interpretação.** Nesse ponto a tangente é paralela à secante que liga $(0,0)$ a $(2,6)$.

**Animação.** A tangente percorre o gráfico; ela fica verde exatamente quando sua inclinação iguala a da secante.""",
),
dict(id='lhopital_e', origem='inspirado no Exemplo 4.43', titulo='O limite $(1+a/x)^x$',
enunciado=r"""Mostre, com L'Hôpital, que $\displaystyle\lim_{x\to\infty}\Big(1+\frac ax\Big)^x=e^a$ para
qualquer constante $a$. Use o resultado para calcular o montante de R\$\,1000 a 6\% ao ano
com capitalização contínua por 10 anos.""",
resposta=r"""$e^a$; $1000e^{0{,}6}\approx$ R\$\,1822{,}12.""",
solucao=r"""**Forma $1^\infty$.** Seja $y=\left(1+\frac ax\right)^x$. Então
$$\ln y=x\ln\!\left(1+\frac ax\right)=\frac{\ln(1+a/x)}{1/x}\quad\left(\text{forma }\tfrac00\right).$$
Por L'Hôpital (derivando em $x$):
$$\lim_{x\to\infty}\frac{\frac{1}{1+a/x}\cdot\left(-\frac a{x^2}\right)}{-\frac1{x^2}}=\lim_{x\to\infty}\frac{a}{1+a/x}=a .$$
Logo $\ln y\to a$ e $y\to e^a$.

**Juros.** Com capitalização $n$ vezes ao ano, o montante é $P\left(1+\frac rn\right)^{nt}=P\left[\left(1+\frac rn\right)^n\right]^t\to Pe^{rt}$.
Para $P=1000$, $r=0{,}06$, $t=10$: $1000e^{0{,}6}\approx1822{,}12$ reais.

**Animação.** O gráfico de $(1+a/x)^x$ para $a=1$ se aproxima da assíntota $y=e$; marcamos os valores para $x=1,10,100,\dots$""",
),
dict(id='esboco', origem='inspirado na seção 4.6', titulo='Esboço completo de um gráfico',
enunciado=r"""Faça o estudo completo e esboce $f(x)=\dfrac{x}{x^2+1}$: domínio, simetria, assíntotas,
crescimento, extremos, concavidade e inflexões.""",
resposta=r"""Ímpar; assíntota $y=0$; máx. $(1,\tfrac12)$, mín. $(-1,-\tfrac12)$; inflexões em $x=0$ e $x=\pm\sqrt3$.""",
solucao=r"""**1. Domínio e simetria.** $\mathbb R$ (o denominador nunca zera). $f(-x)=-f(x)$: **ímpar**, simétrica em relação à origem. Intercepto $(0,0)$.

**2. Assíntotas.** Não há verticais. $\lim_{x\to\pm\infty}\frac{x}{x^2+1}=0$: **assíntota horizontal $y=0$**.

**3. Primeira derivada.** $f'(x)=\dfrac{(x^2+1)-2x^2}{(x^2+1)^2}=\dfrac{1-x^2}{(x^2+1)^2}$.
Crescente em $(-1,1)$, decrescente em $(-\infty,-1)$ e $(1,\infty)$. **Máximo** $f(1)=\frac12$, **mínimo** $f(-1)=-\frac12$.

**4. Segunda derivada.** $f''(x)=\dfrac{2x(x^2-3)}{(x^2+1)^3}$. Sinal:
- $(-\infty,-\sqrt3)$: $-$ (côncava para baixo); $(-\sqrt3,0)$: $+$ (para cima);
- $(0,\sqrt3)$: $-$; $(\sqrt3,\infty)$: $+$.

**Inflexões** em $x=0$ e $x=\pm\sqrt3$, com $f(\pm\sqrt3)=\pm\frac{\sqrt3}{4}$.

**Animação.** O esboço é montado em camadas: assíntota, extremos, inflexões e, por fim, a curva.""",
),
dict(id='cerca', origem='inspirado no Exemplo 4.32', titulo='Cercado junto ao rio',
enunciado=r"""Um fazendeiro tem 600 m de cerca para construir um cercado retangular junto a um rio reto
(sem cerca do lado do rio), dividido em dois currais por uma cerca perpendicular ao rio. Que
dimensões maximizam a área total?""",
resposta=r"""100 m (perpendicular ao rio) por 300 m (paralelo); área 30\,000 m².""",
solucao=r"""**Variáveis.** $x$ = lado perpendicular ao rio (há **três** desses segmentos: as duas laterais e a divisória), $y$ = lado paralelo ao rio (um segmento).

**Restrição:** $3x+y=600\Rightarrow y=600-3x$, com $0\le x\le200$.

**Área:** $A(x)=x(600-3x)=600x-3x^2$.

**Otimização:** $A'(x)=600-6x=0\iff x=100$. Como $A''=-6<0$ (ou $A(0)=A(200)=0$), é máximo.

Dimensões: $x=100$ m e $y=300$ m. Área máxima $30\,000$ m².

**Padrão.** No ótimo, a cerca total "paralela" ($y=300$) é igual à cerca total "perpendicular" ($3x=300$): metade da cerca para cada direção.

**Animação.** O retângulo muda de forma com a cerca total fixa; ao lado, o gráfico de $A(x)$ é traçado até o máximo.""",
),
dict(id='proximo', origem='inspirado na seção 4.7', titulo='Ponto mais próximo',
enunciado=r"""Encontre os pontos da parábola $y=x^2$ mais próximos do ponto $(0,3)$ e a distância mínima.""",
resposta=r"""$\big(\pm\sqrt{5/2},\,\tfrac52\big)$; distância $\tfrac{\sqrt{11}}{2}\approx1{,}658$.""",
solucao=r"""**Truque.** Minimizar $d$ é o mesmo que minimizar $d^2$ (sem a raiz, as contas ficam mais simples).

$$g(x)=d^2=x^2+(x^2-3)^2=x^4-5x^2+9 .$$

$g'(x)=4x^3-10x=2x(2x^2-5)=0\iff x=0$ ou $x=\pm\sqrt{5/2}$.

- $g(0)=9$ (é **máximo local** de $g$: o vértice da parábola está a distância 3);
- $g(\pm\sqrt{5/2})=\frac{25}4-\frac{25}2+9=\frac{11}4$.

Como $g\to\infty$ quando $|x|\to\infty$, o mínimo absoluto é $\frac{11}4$: os pontos são $\left(\pm\sqrt{\tfrac52},\tfrac52\right)$ e a distância mínima é $\frac{\sqrt{11}}2\approx1{,}658$.

**Geometria.** No ponto mais próximo, o segmento até $(0,3)$ é **perpendicular** à tangente: inclinação da tangente $2x=\sqrt{10}$, inclinação do segmento $\frac{5/2-3}{\sqrt{5/2}}=-\frac1{\sqrt{10}}$; o produto é $-1$. ✓

**Animação.** Um ponto percorre a parábola ligado a $(0,3)$; o gráfico de $d(x)$ mostra os dois mínimos.""",
),
dict(id='cabo', origem='inspirado no Exemplo 4.34', titulo='O cabo mais barato',
enunciado=r"""Uma usina fica numa margem de um rio de 1 km de largura. Uma fábrica fica na outra
margem, 3 km rio abaixo. O cabo custa R\$\,5 mil/km sob a água e R\$\,4 mil/km em terra.
Qual é o trajeto mais barato (atravessar em diagonal até um ponto e seguir pela margem)?""",
resposta=r"""Atravessar até o ponto a $\tfrac43$ km rio abaixo; custo mínimo R\$\,15 mil.""",
solucao=r"""**Variável.** $x$ = distância rio abaixo, na outra margem, até o ponto onde o cabo sai da água ($0\le x\le3$).

**Custo:** trecho na água $\sqrt{1+x^2}$, trecho em terra $3-x$:
$$C(x)=5\sqrt{1+x^2}+4(3-x).$$

$C'(x)=\dfrac{5x}{\sqrt{1+x^2}}-4=0\iff5x=4\sqrt{1+x^2}\iff25x^2=16+16x^2\iff x=\tfrac43 .$

**Comparação:** $C(0)=5+12=17$; $C(\tfrac43)=5\cdot\tfrac53+4\cdot\tfrac53=15$; $C(3)=5\sqrt{10}\approx15{,}81$.

O mínimo é **R\$ 15 mil**, atravessando até $\frac43$ km rio abaixo.

**Observação (lei de Snell).** No ótimo, $\frac{x}{\sqrt{1+x^2}}=\frac45$: o seno do ângulo de travessia é a razão entre os custos, como na refração da luz.

**Animação.** O ponto de saída desliza ao longo da margem; o gráfico de $C(x)$ registra o custo.""",
),
dict(id='newton', origem='inspirado no Exemplo 4.46', titulo='Método de Newton para $\\cos x=x$',
enunciado=r"""Use o método de Newton com $x_0=1$ para aproximar a solução de $\cos x=x$ com 9 casas
decimais. Quantas iterações são necessárias?""",
resposta=r"""$x\approx0{,}739085133$; 3 iterações (a 4ª só confirma).""",
solucao=r"""**Função.** $f(x)=\cos x-x$, $f'(x)=-\sin x-1$. Iteração:
$$x_{n+1}=x_n-\frac{\cos x_n-x_n}{-\sin x_n-1}=x_n+\frac{\cos x_n-x_n}{\sin x_n+1}.$$

| $n$ | $x_n$ |
|---|---|
| 0 | 1 |
| 1 | 0,750363868 |
| 2 | 0,739112891 |
| 3 | 0,739085133 |
| 4 | 0,739085133 |

A partir de $x_3$, as 9 casas se estabilizam: $x\approx0{,}739085133$.

**Convergência quadrática.** Os erros são aproximadamente $2{,}6\times10^{-1}$, $1{,}1\times10^{-2}$, $2{,}8\times10^{-5}$, $1{,}8\times10^{-10}$: o número de casas corretas **dobra** a cada passo.

**Animação.** Cada passo traça a tangente em $(x_n,f(x_n))$ e desce até o eixo, revelando $x_{n+1}$; o gráfico é ampliado a cada iteração.""",
),
dict(id='lancamento', origem='inspirado no Exemplo 4.54', titulo='Lançamento vertical',
enunciado=r"""Uma bola é lançada para cima a partir de 2 m de altura com velocidade de 15 m/s
($g=9{,}8$ m/s²). Partindo de $a(t)=-9{,}8$, encontre $v(t)$ e $s(t)$, a altura máxima e o
instante em que a bola atinge o chão.""",
resposta=r"""$s(t)=-4{,}9t^2+15t+2$; altura máx. $\approx13{,}48$ m em $t\approx1{,}53$ s; chão em $t\approx3{,}19$ s.""",
solucao=r"""**Antiderivando.** $v(t)=\int-9{,}8\,dt=-9{,}8t+C_1$; $v(0)=15\Rightarrow v(t)=15-9{,}8t$.
$s(t)=\int v\,dt=15t-4{,}9t^2+C_2$; $s(0)=2\Rightarrow s(t)=-4{,}9t^2+15t+2$.

**Altura máxima.** $v=0\iff t=\frac{15}{9{,}8}\approx1{,}531$ s, com $s\approx2+\frac{15^2}{2\cdot9{,}8}\approx13{,}48$ m.

**Chão.** $-4{,}9t^2+15t+2=0\Rightarrow t=\dfrac{15+\sqrt{225+39{,}2}}{9{,}8}\approx3{,}19$ s (a raiz negativa é descartada).

**Velocidade de impacto:** $v(3{,}19)\approx-16{,}25$ m/s, um pouco maior em módulo que a de lançamento, porque a bola caiu 2 m a mais do que subiu.

**Animação.** A bola sobe e desce; ao lado, os gráficos de $s(t)$ e $v(t)$ são traçados juntos.""",
),
]
