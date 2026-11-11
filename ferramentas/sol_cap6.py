# -*- coding: utf-8 -*-
"""Soluções completas (★) do capítulo 6."""

SOLUCOES = [
dict(id='area_cruzam', origem='inspirado no Exemplo 6.1', titulo='Área quando as curvas se cruzam',
enunciado=r"""Calcule a área total da região limitada por $y=x^3-3x$ e $y=x$.""",
resposta=r"""$8$.""",
solucao=r"""**Interseções:** $x^3-3x=x\iff x^3-4x=0\iff x(x-2)(x+2)=0$, ou seja, $x=-2,\,0,\,2$.

**Quem está por cima?** Teste um ponto de cada intervalo:
- em $x=-1$: cúbica $=2$, reta $=-1$ → a cúbica está por cima em $[-2,0]$;
- em $x=1$: cúbica $=-2$, reta $=1$ → a reta está por cima em $[0,2]$.

**Área:**
$$A=\int_{-2}^0\big[(x^3-3x)-x\big]dx+\int_0^2\big[x-(x^3-3x)\big]dx=\int_{-2}^0(x^3-4x)\,dx+\int_0^2(4x-x^3)\,dx.$$
Cada parcela vale $\left[2x^2-\frac{x^4}4\right]_0^2=8-4=4$ (a primeira pela simetria: $x^3-4x$ é ímpar). Logo $A=8$.

**Cuidado.** $\int_{-2}^2\big[(x^3-3x)-x\big]dx=0$: as duas partes se cancelam porque o integrando é ímpar. Área é $\int|f-g|$, nunca a integral com sinal quando as curvas se cruzam.

**Animação.** Uma faixa vertical percorre $[-2,2]$; a área acumulada cresce nas duas metades (cores diferentes conforme quem está por cima).""",
),
dict(id='arruela', origem='inspirado no Exemplo 6.3', titulo='Arruelas em torno de uma reta horizontal',
enunciado=r"""Gire a região entre $y=x$ e $y=x^2$ ($0\le x\le1$) em torno da reta $y=2$. Calcule o volume.""",
resposta=r"""$\tfrac{8\pi}{15}$.""",
solucao=r"""**Raios.** O eixo $y=2$ fica *acima* da região. A distância de um ponto de altura $y$ até o eixo é $2-y$. Na fatia em $x$:
- a curva mais **longe** do eixo é a de baixo, $y=x^2$: raio externo $R=2-x^2$;
- a mais **perto** é a de cima, $y=x$: raio interno $r=2-x$.

**Volume:**
$$V=\pi\int_0^1\big[(2-x^2)^2-(2-x)^2\big]dx=\pi\int_0^1(x^4-5x^2+4x)\,dx=\pi\Big(\tfrac15-\tfrac53+2\Big)=\frac{8\pi}{15}\approx1{,}676.$$

**Erro comum:** usar $R=x$ e $r=x^2$ (raios medidos a partir do eixo $x$). Isso daria o giro em torno de $y=0$, que vale $\tfrac{2\pi}{15}$, quatro vezes menos.

**Conferência por Pappus.** O centroide da região está em $\bar y=\tfrac25$ (exercício do centroide), a distância $2-\tfrac25=\tfrac85$ do eixo, e a área é $\tfrac16$: $V=2\pi\cdot\tfrac85\cdot\tfrac16=\tfrac{8\pi}{15}$. ✓

**Animação.** A região gira em torno de $y=2$ e o sólido (um anel de parede curva) vai se formando.""",
),
dict(id='cascas', origem='inspirado no Exemplo 6.4', titulo='Cascas e arruelas: dois caminhos',
enunciado=r"""Gire a região entre $y=x$ e $y=x^2$ ($0\le x\le1$) em torno da reta $x=-1$. Calcule o volume pelo
método das cascas e confira com arruelas.""",
resposta=r"""$\tfrac\pi2$.""",
solucao=r"""**Cascas** (faixas verticais, paralelas ao eixo $x=-1$): raio $=x-(-1)=x+1$, altura $=x-x^2$.
$$V=2\pi\int_0^1(x+1)(x-x^2)\,dx=2\pi\int_0^1(x-x^3)\,dx=2\pi\Big(\tfrac12-\tfrac14\Big)=\frac\pi2 .$$

**Arruelas** (faixas horizontais, perpendiculares ao eixo): para $0\le y\le1$, a região vai de $x=y$ (reta) até $x=\sqrt y$ (parábola). Distâncias ao eixo: $R=\sqrt y+1$, $r=y+1$.
$$V=\pi\int_0^1\big[(\sqrt y+1)^2-(y+1)^2\big]dy=\pi\int_0^1\big(2\sqrt y-y-y^2\big)dy=\pi\Big(\tfrac43-\tfrac12-\tfrac13\Big)=\frac\pi2 . \ ✓$$

**Qual escolher?** As cascas usaram as funções na forma dada ($y$ em função de $x$); as arruelas exigiram inverter as curvas. Em geral, escolha a fatia que **não** obriga a resolver equações.

**Animação.** A região gira em torno de $x=-1$; o sólido é desenhado à medida que o ângulo vai de $0$ a $2\pi$.""",
),
dict(id='arco', origem='inspirado na seção 6.4', titulo='Um comprimento de arco que dá certo',
enunciado=r"""Calcule o comprimento de arco de $y=\dfrac{x^3}6+\dfrac1{2x}$ para $1\le x\le3$.""",
resposta=r"""$\tfrac{14}3$.""",
solucao=r"""**Derivada:** $f'(x)=\frac{x^2}2-\frac1{2x^2}$.

**O truque do quadrado perfeito:**
$$1+f'^2=1+\frac{x^4}4-\frac12+\frac1{4x^4}=\frac{x^4}4+\frac12+\frac1{4x^4}=\Big(\frac{x^2}2+\frac1{2x^2}\Big)^2 .$$
O ``$-\frac12$'' do produto cruzado virou ``$+\frac12$'' ao somar $1$. Essa é a marca das funções feitas para ter comprimento de arco elementar.

**Integral:**
$$L=\int_1^3\Big(\frac{x^2}2+\frac1{2x^2}\Big)dx=\Big[\frac{x^3}6-\frac1{2x}\Big]_1^3=\Big(\frac{27}6-\frac16\Big)-\Big(\frac16-\frac12\Big)=\frac{13}3+\frac13=\frac{14}3\approx4{,}667.$$

**Conferência.** A corda de $(1,\tfrac23)$ a $(3,\tfrac{14}3)$ mede $\sqrt{4+16}\approx4{,}472<4{,}667$, como deve ser.

**Animação.** Poligonais com $1,2,4,\dots,64$ segmentos se aproximam da curva; seus comprimentos crescem até $14/3$.""",
),
dict(id='centroide', origem='inspirado no Exemplo 6.7', titulo='Centroide e Pappus',
enunciado=r"""Encontre o centroide da região entre $y=x$ e $y=x^2$ e use o Teorema de Pappus para recalcular o
volume do giro em torno do eixo $x$ (Exemplo 6.3b).""",
resposta=r"""$(\bar x,\bar y)=\big(\tfrac12,\tfrac25\big)$; $V=\tfrac{2\pi}{15}$.""",
solucao=r"""**Área:** $A=\int_0^1(x-x^2)\,dx=\frac12-\frac13=\frac16$.

**$\bar x$:**
$$\bar x=\frac1A\int_0^1x(x-x^2)\,dx=6\Big(\frac13-\frac14\Big)=\frac12 .$$
(Não é por simetria em relação a $x=\tfrac12$: a região *não* é simétrica, mas a altura $x-x^2$ é. Isso basta para $\bar x$.)

**$\bar y$:**
$$\bar y=\frac1A\int_0^1\frac{x^2-x^4}2\,dx=6\cdot\frac12\Big(\frac13-\frac15\Big)=\frac25 .$$

**Pappus:** girando em torno do eixo $x$, o centroide percorre uma circunferência de raio $\bar y=\tfrac25$:
$$V=2\pi\cdot\frac25\cdot\frac16=\frac{2\pi}{15}, $$
igual ao resultado por arruelas. ✓

**Animação.** A região é varrida da esquerda para a direita; o ponto mostra o centroide da parte já varrida e para em $(\tfrac12,\tfrac25)$.""",
),
dict(id='crescimento', origem='inspirado na seção 6.8', titulo='Crescimento de uma cultura',
enunciado=r"""Uma cultura de bactérias cresce a uma taxa proporcional ao seu tamanho e passa de $1000$ para $3000$
indivíduos em $2$ h. Encontre $k$, o tempo de duplicação, o tamanho após $5$ h e quando ela chega a $10\,000$.""",
resposta=r"""$k=\tfrac{\ln3}2\approx0{,}549$/h; $T_2\approx1{,}26$ h; $\approx15\,588$; $\approx4{,}19$ h.""",
solucao=r"""**Modelo:** $y'=ky\Rightarrow y=1000\,e^{kt}$.

**$k$:** $3000=1000e^{2k}\Rightarrow k=\frac{\ln3}2\approx0{,}5493$ por hora.

**Tempo de duplicação:** $T_2=\frac{\ln2}k=\frac{2\ln2}{\ln3}\approx1{,}262$ h $\approx$ 1 h 16 min.

**Após 5 h:** $y(5)=1000e^{5\ln3/2}=1000\cdot3^{5/2}=1000\cdot9\sqrt3\approx15\,588$.

**Quando $y=10\,000$:** $e^{kt}=10\Rightarrow t=\frac{\ln10}k=\frac{2\ln10}{\ln3}\approx4{,}19$ h.

**Forma alternativa.** $y=1000\cdot3^{t/2}$: ``triplica a cada 2 h''. Toda exponencial pode ser escrita com a base que for mais conveniente; $e^{kt}$ é a que torna a derivada simples.

**Animação.** A curva cresce e marcas horizontais mostram as duplicações sucessivas, igualmente espaçadas no tempo.""",
),
dict(id='bombeamento', origem='inspirado no Exemplo 6.6', titulo='Esvaziando um tanque cônico',
enunciado=r"""Um tanque cônico (vértice para baixo) tem $3$ m de raio no topo e $6$ m de altura e está cheio
de água. Calcule o trabalho para bombear toda a água até $1$ m acima do topo.""",
resposta=r"""$441\,000\pi\approx1{,}39\times10^6$ J.""",
solucao=r"""**Coordenadas:** $y$ = altura medida a partir do vértice, $0\le y\le6$. Por semelhança de triângulos, o raio da superfície na altura $y$ é $r=\frac36y=\frac y2$.

**Fatia típica:** camada de espessura $\Delta y$ na altura $y$:
- volume $\pi r^2\Delta y=\frac\pi4y^2\Delta y$;
- peso $9800\cdot\frac\pi4y^2\Delta y$ N;
- distância a subir: até $y=7$, isto é, $7-y$.

**Trabalho:**
$$W=\int_0^6 9800\,\frac\pi4\,y^2(7-y)\,dy=2450\pi\Big[\frac{7y^3}3-\frac{y^4}4\Big]_0^6=2450\pi(504-324)=441\,000\pi\approx1{,}385\times10^6\ \text{J}.$$

**Intuição.** A maior parte da água está perto do topo (onde o cone é largo) e por isso sobe pouco. O mesmo volume num cilindro de mesma altura e mesmo volume exigiria mais trabalho.

**Animação.** O nível da água desce; o contador mostra o trabalho acumulado a cada camada retirada.""",
),
dict(id='comporta', origem='inspirado no Exemplo 6.6', titulo='Força numa comporta triangular',
enunciado=r"""Uma comporta vertical tem a forma de um triângulo com base de $4$ m na superfície da água e vértice
$3$ m abaixo. Calcule a força hidrostática sobre ela.""",
resposta=r"""$58\,800$ N.""",
solucao=r"""**Largura na profundidade $h$:** a largura cai linearmente de $4$ (em $h=0$) a $0$ (em $h=3$): $w(h)=\frac43(3-h)$.

**Força numa faixa:** pressão $9800h$ vezes área $w(h)\Delta h$.
$$F=\int_0^3 9800\,h\cdot\frac43(3-h)\,dh=\frac{39\,200}3\Big[\frac{3h^2}2-\frac{h^3}3\Big]_0^3=\frac{39\,200}3\cdot4{,}5=58\,800\ \text{N}.$$

**Conferência ($F=\rho g\bar hA$):** a área é $6$ m² e o centroide do triângulo fica a $\frac13$ da altura a partir da base, $\bar h=1$ m: $9800\cdot1\cdot6=58\,800$ N. ✓

**Observação.** Se o triângulo estivesse invertido (vértice para cima, na superfície), o centroide ficaria a $2$ m e a força dobraria: a parte larga estaria onde a pressão é maior.

**Animação.** Faixas horizontais são somadas de cima para baixo, com setas proporcionais à pressão, e a força total vai se acumulando.""",
),
dict(id='superficie', origem='inspirado no Exemplo 6.5', titulo='O teorema de Arquimedes da faixa esférica',
enunciado=r"""Mostre que a área da faixa de uma esfera de raio $R$ entre dois planos paralelos a distância $h$
(ambos cortando a esfera) é $2\pi Rh$, qualquer que seja a posição dos planos. Que fração da superfície da
Terra fica acima da latitude $60^\circ$?""",
resposta=r"""$S=2\pi Rh$; cerca de $6{,}7\%$.""",
solucao=r"""**Superfície de revolução:** gire $f(x)=\sqrt{R^2-x^2}$ em torno do eixo $x$, entre $x=a$ e $x=a+h$.

$f'(x)=-\frac x{\sqrt{R^2-x^2}}$, e
$$f\sqrt{1+f'^2}=\sqrt{R^2-x^2}\cdot\sqrt{\frac{R^2-x^2+x^2}{R^2-x^2}}=R .$$
O integrando é **constante**:
$$S=2\pi\int_a^{a+h}R\,dx=2\pi Rh .$$

**Esfera inteira:** $h=2R$ dá $4\pi R^2$.

**Interpretação (Arquimedes).** A área é a mesma do cilindro circunscrito na mesma faixa. Perto do ``equador'' a faixa é larga mas pouco inclinada; perto dos polos é estreita mas muito inclinada, e os dois efeitos se compensam exatamente.

**Terra acima de $60^\circ$:** a calota começa à altura $R\sen60^\circ$ e termina em $R$: $h=R(1-\tfrac{\sqrt3}2)\approx0{,}134R$. Fração $=\frac{2\pi Rh}{4\pi R^2}=\frac{1-\sqrt3/2}2\approx0{,}067$, ou seja, $6{,}7\%$.

**Animação.** Uma faixa de largura fixa $h$ desliza do polo ao equador; o valor da área permanece $2\pi Rh$.""",
),
dict(id='catenaria', origem='inspirado na seção 6.9', titulo='O cabo suspenso',
enunciado=r"""Um cabo pende entre dois postes de mesma altura, separados por $40$ m, na forma $y=a\cosh\frac xa$
com $a=20$ m ($-20\le x\le20$). Mostre que o comprimento é $L=2a\senh\frac{20}a$ e calcule $L$ e a flecha
(desnível entre os apoios e o ponto mais baixo).""",
resposta=r"""$L=40\senh1\approx47{,}0$ m; flecha $20(\cosh1-1)\approx10{,}9$ m.""",
solucao=r"""**Comprimento:** $y'=\senh\frac xa$ e $1+\senh^2u=\cosh^2u$, logo
$$L=\int_{-20}^{20}\cosh\frac xa\,dx=a\Big[\senh\frac xa\Big]_{-20}^{20}=2a\senh\frac{20}a .$$
Com $a=20$: $L=40\senh1=20(e-e^{-1})\approx47{,}01$ m.

**Flecha:** o ponto mais baixo é $y(0)=a=20$; nos apoios, $y(20)=20\cosh1\approx30{,}86$. Flecha $=20(\cosh1-1)\approx10{,}86$ m.

**O parâmetro $a$.** $a$ grande deixa o cabo esticado (flecha pequena, $L$ pouco maior que $40$); $a$ pequeno deixa-o frouxo. Por exemplo, $a=50$ dá $L\approx41{,}1$ m e flecha $\approx4{,}0$ m.

**Por que não uma parábola?** Perto do vértice, $\cosh u\approx1+\frac{u^2}2$, então a catenária parece uma parábola quando a flecha é pequena; mas a forma exata do cabo sob o próprio peso é o cosseno hiperbólico.

**Animação.** O parâmetro $a$ diminui e o cabo afrouxa; o título mostra $L$ e a flecha.""",
),
dict(id='toro', origem='inspirado no Exemplo 6.7', titulo='Volume do toro: Pappus × cascas',
enunciado=r"""Gire o disco $(x-3)^2+y^2\le1$ em torno do eixo $y$. Calcule o volume do toro por Pappus e
confira pelo método das cascas.""",
resposta=r"""$6\pi^2\approx59{,}22$.""",
solucao=r"""**Pappus:** área $\pi\cdot1^2=\pi$; centroide no centro $(3,0)$, a distância $d=3$ do eixo:
$V=2\pi\cdot3\cdot\pi=6\pi^2\approx59{,}22$.

**Cascas:** em $x\in[2,4]$, a faixa vertical tem altura $2\sqrt{1-(x-3)^2}$ e raio $x$:
$$V=2\pi\int_2^4x\cdot2\sqrt{1-(x-3)^2}\,dx .$$
Com $u=x-3$:
$$V=4\pi\int_{-1}^1(u+3)\sqrt{1-u^2}\,du=4\pi\Big[\underbrace{\int_{-1}^1u\sqrt{1-u^2}\,du}_{0\ (\text{ímpar})}+3\underbrace{\int_{-1}^1\sqrt{1-u^2}\,du}_{\pi/2\ (\text{semidisco})}\Big]=4\pi\cdot\frac{3\pi}2=6\pi^2 .\ ✓$$

**Generalização:** raio do tubo $r$, distância do centro ao eixo $R$: $V=2\pi^2Rr^2$, que é o volume de um cilindro de base $\pi r^2$ e comprimento $2\pi R$ (o toro ``desenrolado'').

**Animação.** O disco gira em torno do eixo $y$ e o toro vai se fechando.""",
),
]
