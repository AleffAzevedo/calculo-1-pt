# -*- coding: utf-8 -*-
"""Soluções completas (★) do capítulo 5."""

SOLUCOES = [
dict(id='riemann', origem='inspirado no Exemplo 5.1', titulo='Somas de Riemann convergindo',
enunciado=r"""Para $f(x)=4-x^2$ em $[0,2]$, calcule $L_4$ e $R_4$, escreva $R_n$ em função de $n$ e
encontre a área exata como $\lim_{n\to\infty}R_n$.""",
resposta=r"""$L_4=6{,}25$; $R_4=4{,}25$; $R_n=8-\tfrac{4(n+1)(2n+1)}{3n^2}$; área $\tfrac{16}3$.""",
solucao=r"""$\Delta x=\frac2n$ e $x_i=\frac{2i}n$.

**$n=4$** ($\Delta x=0{,}5$): valores de $f$ em $0;\,0{,}5;\,1;\,1{,}5;\,2$: $4;\ 3{,}75;\ 3;\ 1{,}75;\ 0$.
$L_4=0{,}5(4+3{,}75+3+1{,}75)=6{,}25$ e $R_4=0{,}5(3{,}75+3+1{,}75+0)=4{,}25$.
Como $f$ é **decrescente**, agora $L_n$ superestima e $R_n$ subestima.

**$R_n$ geral:**
$$R_n=\sum_{i=1}^n\Big(4-\frac{4i^2}{n^2}\Big)\frac2n=\frac8n\cdot n-\frac{8}{n^3}\cdot\frac{n(n+1)(2n+1)}6=8-\frac{4(n+1)(2n+1)}{3n^2}.$$

**Limite:** $\frac{(n+1)(2n+1)}{n^2}\to2$, logo $R_n\to8-\frac83=\frac{16}3\approx5{,}333$.

**Conferência pelo TFC:** $\int_0^2(4-x^2)\,dx=\left[4x-\frac{x^3}3\right]_0^2=8-\frac83=\frac{16}3$. ✓

**Animação.** $n$ cresce de 2 a 64; os retângulos (pela direita) preenchem a região e $R_n$ se aproxima de $16/3$.""",
),
dict(id='limite_soma', origem='inspirado na seção 5.2', titulo='Integral pela definição',
enunciado=r"""Use a definição (limite de somas de Riemann com extremidades direitas) para calcular
$\int_0^1x^3\,dx$.""",
resposta=r"""$\tfrac14$.""",
solucao=r"""$\Delta x=\frac1n$, $x_i=\frac in$:
$$R_n=\sum_{i=1}^n\Big(\frac in\Big)^3\frac1n=\frac1{n^4}\sum_{i=1}^ni^3=\frac1{n^4}\cdot\frac{n^2(n+1)^2}{4}=\frac{(n+1)^2}{4n^2}.$$
Quando $n\to\infty$, $\frac{(n+1)^2}{n^2}\to1$, então $\int_0^1x^3\,dx=\frac14$.

**Valores intermediários:** $R_4=\frac{25}{64}\approx0{,}391$; $R_{10}=0{,}3025$; $R_{100}=0{,}255025$.

**Lição.** O cálculo pela definição exige a fórmula de $\sum i^3$; o TFC dá o mesmo resultado em uma linha, $\left[\frac{x^4}4\right]_0^1=\frac14$. Os dois caminhos concordam, e é exatamente isso que o teorema garante.

**Animação.** Os retângulos ficam cada vez mais finos e o valor de $R_n$ desce até $0{,}25$.""",
),
dict(id='funcao_area', origem='inspirado na seção 5.3', titulo='A função área',
enunciado=r"""Seja $g(x)=\displaystyle\int_0^x(t-1)(t-3)\,dt$ para $0\le x\le4$. Use o TFC para encontrar
$g'(x)$, os intervalos em que $g$ cresce e decresce, e os extremos locais de $g$. Calcule
$g(1)$, $g(3)$ e $g(4)$.""",
resposta=r"""$g'(x)=(x-1)(x-3)$; máx. local $g(1)=\tfrac43$; mín. local $g(3)=0$; $g(4)=\tfrac43$.""",
solucao=r"""**TFC 1:** $g'(x)=(x-1)(x-3)$.

- $g'>0$ em $[0,1)$ e $(3,4]$: $g$ cresce (a área acumulada aumenta, pois o integrando é positivo);
- $g'<0$ em $(1,3)$: $g$ decresce (o integrando é negativo e "desconta" área).

**Extremos locais:** máximo em $x=1$ e mínimo em $x=3$.

**Valores** (pelo TFC 2, com $\int(t^2-4t+3)\,dt=\frac{t^3}3-2t^2+3t$):
$g(1)=\frac13-2+3=\frac43$; $g(3)=9-18+9=0$; $g(4)=\frac{64}3-32+12=\frac43$.

**Leitura geométrica.** De 0 a 1 acumulamos $\frac43$ de área positiva; de 1 a 3 perdemos $\frac43$ (a região abaixo do eixo); de 3 a 4 ganhamos $\frac43$ de novo.

**Animação.** À esquerda, a região sob $f$ é varrida (azul onde $f>0$, laranja onde $f<0$); à direita, o gráfico de $g(x)$ é desenhado ao mesmo tempo.""",
),
dict(id='tfc_cadeia', origem='inspirado na seção 5.3', titulo='TFC com limites variáveis',
enunciado=r"""Calcule $\dfrac{d}{dx}\displaystyle\int_x^{x^2}e^{t^2}\,dt$.""",
resposta=r"""$2x\,e^{x^4}-e^{x^2}$.""",
solucao=r"""**Ideia.** Dividimos a integral num ponto fixo (qualquer, por exemplo $0$):
$$\int_x^{x^2}e^{t^2}dt=\int_0^{x^2}e^{t^2}dt-\int_0^{x}e^{t^2}dt .$$

**Derivando cada parte (TFC 1 + cadeia):**
- $\frac{d}{dx}\int_0^{x^2}e^{t^2}dt=e^{(x^2)^2}\cdot2x=2x\,e^{x^4}$;
- $\frac{d}{dx}\int_0^{x}e^{t^2}dt=e^{x^2}$.

**Resultado:** $2x\,e^{x^4}-e^{x^2}$.

**Regra geral:** $\frac{d}{dx}\int_{a(x)}^{b(x)}f(t)\,dt=f(b(x))\,b'(x)-f(a(x))\,a'(x)$.

**Observação.** $e^{t^2}$ **não tem antiderivada elementar**, mas o TFC nos dá a derivada da integral mesmo assim.

**Animação.** A faixa entre $x$ e $x^2$ sob $e^{t^2}$ muda de tamanho conforme $x$ varia (para $1\le x\le1{,}3$); a taxa de variação da área é a derivada calculada.""",
),
dict(id='deslocamento', origem='inspirado no Exemplo 5.3 e na seção 5.4', titulo='Deslocamento e distância',
enunciado=r"""Uma partícula tem velocidade $v(t)=3t^2-12t+9$ m/s para $0\le t\le4$. Calcule o
deslocamento e a distância percorrida. Se $s(0)=2$, onde ela está em $t=4$?""",
resposta=r"""Deslocamento 4 m; distância 12 m; $s(4)=6$.""",
solucao=r"""$v(t)=3(t-1)(t-3)$; uma antiderivada é $s_0(t)=t^3-6t^2+9t$.

**Deslocamento:** $\int_0^4v\,dt=s_0(4)-s_0(0)=64-96+36=4$ m.

**Distância:** separamos os intervalos de sinal:
- $\int_0^1v=s_0(1)-s_0(0)=4$ (para a frente);
- $\int_1^3v=s_0(3)-s_0(1)=0-4=-4$ (para trás);
- $\int_3^4v=s_0(4)-s_0(3)=4-0=4$ (para a frente).

Distância $=4+4+4=12$ m.

**Posição final:** $s(4)=s(0)+\int_0^4v=2+4=6$ (Teorema da Variação Total).

**Animação.** Em cima, o gráfico de $v(t)$ com as áreas acumuladas (azul positiva, laranja negativa); embaixo, a partícula se movendo na reta.""",
),
dict(id='valor_medio', origem='inspirado na seção 5.2', titulo='Valor médio de uma função',
enunciado=r"""Calcule o valor médio de $f(x)=\sin x$ em $[0,\pi]$ e encontre todos os $c$ garantidos pelo
TVM para integrais.""",
resposta=r"""$f_{\text{méd}}=\tfrac2\pi\approx0{,}637$; $c=\sin^{-1}\tfrac2\pi\approx0{,}690$ ou $c=\pi-0{,}690\approx2{,}451$.""",
solucao=r"""$$f_{\text{méd}}=\frac1{\pi-0}\int_0^\pi\sin x\,dx=\frac{[-\cos x]_0^\pi}{\pi}=\frac2\pi\approx0{,}6366 .$$

**Pontos $c$:** $\sin c=\frac2\pi\Rightarrow c=\sin^{-1}\frac2\pi\approx0{,}6901$ ou $c=\pi-0{,}6901\approx2{,}4515$ (ambos em $[0,\pi]$).

**Interpretação geométrica.** O retângulo de base $[0,\pi]$ e altura $\frac2\pi$ tem área $2$, a mesma da região sob o arco do seno. A parte do arco acima do retângulo compensa exatamente os "cantos" vazios.

**Aplicação.** Se uma tensão alternada é $V_p\sin\omega t$, a média de $|V|$ num semiciclo é $\frac2\pi V_p\approx0{,}637V_p$.

**Animação.** A altura de um retângulo varia até que sua área iguale a área sob o seno; os pontos $c$ aparecem no fim.""",
),
dict(id='substituicao', origem='inspirado na seção 5.5', titulo='Substituição em integral definida',
enunciado=r"""Calcule $\displaystyle\int_0^2x\sqrt{4-x^2}\,dx$ trocando os limites de integração, e interprete
a substituição geometricamente.""",
resposta=r"""$\tfrac83$.""",
solucao=r"""**Substituição:** $u=4-x^2$, $du=-2x\,dx\Rightarrow x\,dx=-\frac12du$.

**Limites:** $x=0\mapsto u=4$; $x=2\mapsto u=0$.
$$\int_0^2x\sqrt{4-x^2}\,dx=-\frac12\int_4^0u^{1/2}du=\frac12\int_0^4u^{1/2}du=\frac12\cdot\frac23\left[u^{3/2}\right]_0^4=\frac13\cdot8=\frac83 .$$

**Erro comum.** Esquecer de trocar os limites (ou trocar e depois voltar para $x$ sem querer). Escolha **um** caminho: ou troca os limites e fica em $u$, ou volta para $x$ e usa os limites originais.

**Interpretação.** A substituição transforma a região sob $x\sqrt{4-x^2}$ em $[0,2]$ na região sob $\frac12\sqrt u$ em $[0,4]$: formatos diferentes, **mesma área**.

**Animação.** As duas regiões aparecem lado a lado, sendo preenchidas em sincronia ($x\mapsto u=4-x^2$); as áreas acumuladas são sempre iguais.""",
),
dict(id='simetria', origem='inspirado na seção 5.4', titulo='Simetria salva contas',
enunciado=r"""Calcule $\displaystyle\int_{-\pi}^{\pi}\big(x^3\cos x+2\cos x+x\big)\,dx$ usando simetria.""",
resposta=r"""$0$.""",
solucao=r"""Separamos em partes ímpares e pares:
- $x^3\cos x$ é **ímpar** (ímpar × par) e $x$ é **ímpar**: suas integrais em $[-\pi,\pi]$ são $0$;
- $2\cos x$ é **par**: $\int_{-\pi}^\pi2\cos x\,dx=2\cdot2\int_0^\pi\cos x\,dx=4[\sin x]_0^\pi=0$.

Logo a integral vale $0$.

**Atenção.** O resultado $0$ **não** significa que não há área: a área total é positiva. As áreas acima e abaixo do eixo apenas se cancelam.

**Por que a parte ímpar some?** Para $f$ ímpar, a substituição $u=-x$ mostra que $\int_{-a}^0f=-\int_0^af$.

**Animação.** As áreas de $x^3\cos x$ são varridas simetricamente a partir da origem: cada pedaço à direita é cancelado pelo seu reflexo à esquerda.""",
),
dict(id='pi_arctan', origem='inspirado no Exemplo 5.6', titulo='Calculando $\\pi$ com uma integral',
enunciado=r"""Mostre que $\displaystyle\int_0^1\frac{4}{1+x^2}\,dx=\pi$ e use a regra do ponto médio com $n=4$ para
estimar $\pi$.""",
resposta=r"""$4\tan^{-1}1=\pi$; $M_4\approx3{,}14680$.""",
solucao=r"""**Exato:** $\int_0^1\frac4{1+x^2}dx=4\left[\tan^{-1}x\right]_0^1=4\cdot\frac\pi4=\pi$.

**Ponto médio com $n=4$** ($\Delta x=\frac14$; pontos $\frac18,\frac38,\frac58,\frac78$):
$$M_4=\frac14\left(\frac{4}{1+\frac1{64}}+\frac{4}{1+\frac9{64}}+\frac{4}{1+\frac{25}{64}}+\frac{4}{1+\frac{49}{64}}\right)\approx\frac14(3{,}93846+3{,}50685+2{,}87640+2{,}26549)\approx3{,}14680 .$$
O erro é $\approx0{,}0052$ com apenas 4 retângulos.

**Desempenho:** $M_{10}\approx3{,}14243$ e $M_{100}\approx3{,}1416010$ (erro $\approx8\times10^{-6}$).

**Animação.** A regra do ponto médio com $n=1,2,4,8,\dots,128$, mostrando o valor aproximado de $\pi$ a cada passo.""",
),
dict(id='tanque', origem='inspirado na seção 5.4', titulo='Vazão e volume',
enunciado=r"""Água entra num tanque à taxa $r(t)=200-4t$ L/min, $0\le t\le50$, que inicialmente tem
1000 L. Quanto há no tanque em $t=50$? Em que instante o volume cresce mais rapidamente?
Esboce $V(t)$.""",
resposta=r"""$6000$ L; em $t=0$; $V(t)=1000+200t-2t^2$, parábola crescente até o vértice em $t=50$.""",
solucao=r"""**Variação total:** $\int_0^{50}(200-4t)\,dt=\left[200t-2t^2\right]_0^{50}=10000-5000=5000$ L.
Volume final: $1000+5000=6000$ L.

**Volume em cada instante:** $V(t)=1000+\int_0^t(200-4s)\,ds=1000+200t-2t^2$.

**Crescimento mais rápido:** $V'(t)=r(t)$, máxima quando $t=0$ ($200$ L/min). Em $t=50$, $r=0$: o tanque para de encher, e $V$ tem tangente horizontal (vértice da parábola).

**Geometricamente**, os 5000 L são a área do triângulo sob $r(t)$: $\frac12\cdot50\cdot200=5000$. ✓

**Animação.** A área sob $r(t)$ é acumulada (em cima) enquanto o nível do tanque sobe (embaixo).""",
),
dict(id='log_tan', origem='inspirado no Exemplo 5.5', titulo='Integral da tangente e da secante',
enunciado=r"""Mostre que $\int\tan x\,dx=\ln|\sec x|+C$ e que $\int\sec x\,dx=\ln|\sec x+\tan x|+C$.
Calcule $\int_0^{\pi/4}\sec x\,dx$.""",
resposta=r"""$\ln(\sqrt2+1)\approx0{,}8814$.""",
solucao=r"""**Tangente.** $\int\frac{\sin x}{\cos x}dx$ com $u=\cos x$, $du=-\sin x\,dx$:
$-\int\frac{du}u=-\ln|\cos x|+C=\ln|\sec x|+C$.

**Secante (truque).** Multiplicamos e dividimos por $\sec x+\tan x$:
$$\int\sec x\,dx=\int\frac{\sec^2x+\sec x\tan x}{\sec x+\tan x}\,dx .$$
O numerador é exatamente a derivada do denominador! Com $u=\sec x+\tan x$: $\int\frac{du}u=\ln|\sec x+\tan x|+C$.

(Verifique derivando: $\frac{\sec x\tan x+\sec^2x}{\sec x+\tan x}=\sec x$. ✓)

**Valor:** $\int_0^{\pi/4}\sec x\,dx=\ln(\sqrt2+1)-\ln(1+0)=\ln(1+\sqrt2)\approx0{,}8814$.

**Curiosidade.** Essa integral aparece na projeção de Mercator: a distância vertical de um paralelo de latitude $\varphi$ até o equador, no mapa, é proporcional a $\int_0^\varphi\sec t\,dt$.

**Animação.** A região sob $\sec x$ em $[0,\pi/4]$ é preenchida, e o valor acumulado é comparado com $\ln|\sec x+\tan x|$.""",
),
]
