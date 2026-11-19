# Capítulo 1: Breve Revisão da Lógica

> Versão revista do texto original no Dropbox Paper. Todas as fórmulas estão em LaTeX entre pares `$$ … $$`. As alterações de conteúdo estão resumidas na secção final, *Notas de revisão*.

# Domínios e Computações

$$\,\mathbb{N}\,$$ denota o domínio dos números naturais e $$\,\mathbb{B}\equiv\{0,1\}\,$$ (ou $$\,2\,$$) denota o domínio dos bits. O domínio $$\,\mathbb{B}^\ast\equiv\{0,1\}^\ast\,$$ denota o domínio das strings de bits finitas. Os domínios $$\,\mathbb{N}\,$$ e $$\,\mathbb{B}^\ast\,$$ são isomórficos; na maioria dos problemas é indiferente usar um ou o outro.

Neste contexto $$\,|x|\,$$ denota o comprimento da sequência de bits $$\,x\in\{0,1\}^\ast\,$$. Para um inteiro $$\,n\,$$, o seu tamanho é o comprimento da string $$\,\tilde{n}\,$$ que codifica $$\,n\,$$; com a bijeção apresentada em seguida tem-se

$$|n| \;\equiv\; |\tilde{n}| \;=\; \lfloor \log_2 (n+1) \rfloor$$

Uma função que estabelece o isomorfismo $$\,\{0,1\}^\ast\to\mathbb{N}\,$$ é, usualmente,

$$x \;\mapsto\; 2^{|x|}-1+\sum_{i=0}^{|x|-1} x_i\,2^i$$

em que $$\,x = x_{|x|-1}\cdots x_1\,x_0\,$$, isto é, $$\,x_0\,$$ é o bit mais à direita. Outras bijeções podem ser utilizadas.

Esta função é conhecida por **enumeração canónica** (ou *shortlex*: primeiro por comprimento, depois lexicograficamente) das strings, uma vez que as enumera como se indica em seguida

$$\varepsilon,\,0,\,1,\,00,\,01,\,10,\,11,\,000,\,001,\,010,\,011,\,100,\,101,\,110,\,111,\,\cdots$$

**Nota**

Em muitas situações o isomorfismo entre $$\,\mathbb{N}\,$$ e $$\,\{0,1\}^\ast\,$$ está sempre presente e, por isso, qualquer definição que envolva um destes domínios gera uma definição análoga envolvendo o outro domínio.

Por isso, no que se segue, usamos $$\,2\,$$ como abreviatura de qualquer domínio isomórfico com $$\,\{0,1\}\,$$ e usamos $$\,\omega\,$$ para representar qualquer domínio contável infinito, isto é, isomórfico com $$\,\mathbb{N}\,$$ (ou com $$\,\{0,1\}^\ast\,$$). O símbolo $$\,\omega\,$$ é também o primeiro ordinal infinito.

A cardinalidade de domínios cujos elementos são sequências de bits ou números naturais permite uma classificação desses domínios. Por exemplo:

- **domínios finitos** têm como exemplo paradigmático o domínio $$\,\mathbb{B}^n\equiv\{0,1\}^n\,$$ das palavras (“words”) ou vetores (“bit-vectors”) com exatamente $$\,n\,$$ componentes. São também exemplos de domínios finitos os domínios da forma
$$[t]\;\equiv\;\{\,i\in\mathbb{N}\mid i<t\,\}$$

- **domínios contáveis** são domínios isomórficos com um subconjunto dos números naturais; i.e. domínios $$\,D\,$$ para os quais existe uma função injetiva $$\,\mathsf{inx}:D\to\mathbb{N}\,$$.

- **domínios de Cantor** são domínios cujos elementos são subconjuntos de um domínio contável infinito (equivalentemente, funções $$\,\omega\to 2\,$$).

Na terminologia da computabilidade,

- *objetos* são elementos de domínios contáveis,
- *conjuntos* identificam-se com coleções de números naturais e são elementos dos domínios de Cantor,
- *classes* são coleções de conjuntos ou coleções de classes.

O paradigma de um domínio de Cantor é a classe $$\,\{0,1\}^\infty\,$$ (ou $$\,2^\infty\,$$) de todas as sequências infinitas de bits (também designadas por *streams*)

$$\{w_n\}_{n\in\mathbb{N}}$$

As streams $$\,w\in\{0,1\}^\infty\,$$ podem identificar-se ainda com

- **funções** $$\,w:\omega\to 2\,$$. O espaço de tais funções representa-se por $$\,2^{\mathbb{N}}\,$$ ou $$\,2^{\omega}\,$$ (é um espaço de funções; a sua cardinalidade é $$\,2^{\aleph_0}\,$$).

- **conjuntos** $$\,\overline{w}\equiv\{\,n\in\mathbb{N}\mid w_n=1\,\}\,$$. Genericamente tem-se conjuntos $$\,\overline{w}\equiv\{\,x\in\omega\mid w_{\mathsf{inx}(x)}=1\,\}\,$$.

- **séries infinitas**
$$0\cdot w \;\equiv\; \sum_{n\in\overline{w}} 2^{-n-1}$$
isto é, **números reais** em $$\,[0,1]\,$$ vistos como limites das somas parciais (sequências crescentes e limitadas de racionais diádicos). Note-se que esta correspondência não é injetiva: por exemplo $$\,0\cdot 0111\cdots = 0\cdot 1000\cdots = 1/2\,$$.

## Computações

No modelo de computação que se segue considera-se que $$\,\mathbb{N}\,$$ (ou $$\,\{0,1\}^\ast\,$$) tem a ordem dos inteiros e está equipado com um conjunto de operações primitivas:

- as constantes $$\,0,1\,$$;
- relações binárias $$\,<,\,\neq,\,\cdots\,$$;
- os operadores binários soma $$\,+\,$$ e concatenação de strings $$\,xy\,$$;
- o par $$\,(x,y)\,$$, codificado pela concatenação $$\,0^{|x|}\,1\,x\,y\,$$ (codificação auto-delimitada);
- o operador ternário $$\,\mathsf{ite}\,$$ (if-then-else).

A concatenação $$\,xy\,$$ pode também ser representada com um operador específico: $$\,x\parallel y\,$$.

# Funções Booleanas

A título de exemplo vamos considerar os problemas paradigmáticos das funções booleanas representadas como **polinómios booleanos** ou **polinómios de Zhegalkin** (também chamada *forma normal algébrica*, ANF).
Estes problemas têm variantes que ocorrem também noutras estruturas: nomeadamente nas fórmulas proposicionais e nas relações lineares inteiras.

Uma função booleana total $$\,f:\{0,1\}^n\to\{0,1\}\,$$ é completamente determinada por um polinómio booleano em $$\,n\,$$ variáveis e de grau menor ou igual a $$\,n\,$$.

Todo o polinómio é definido por operações de soma e multiplicação numa estrutura algébrica apropriada (um anel; neste caso, um corpo).
Neste caso a soma $$\,+\,$$ é a operação *xor* de bits e a multiplicação é o *and* de bits. O corpo assim definido representa-se por $$\,\mathbb{F}_2\,$$ (corpo finito com 2 elementos).

Como as variáveis tomam valores em $$\,\mathbb{F}_2\,$$, tem-se $$\,x_i^2=x_i\,$$ para todo $$\,i\,$$. Por isso os polinómios booleanos são os elementos do anel quociente

$$\mathbb{F}_2[x_0,\cdots,x_{n-1}]\,/\,(x_0^2-x_0,\;\cdots,\;x_{n-1}^2-x_{n-1})$$

e neste anel todo o polinómio $$\,f\,$$ verifica $$\,f^2=f\,$$ (diz-se *idempotente* ou *booleano*) e $$\,f+f=0\,$$ (diz-se *binário*).

## Exemplo 1

Exemplos de polinómios com 4 variáveis serão

$$1+x_0x_2+x_1x_3\,,\qquad x_0x_1+x_2+x_1x_2x_3\,,\qquad x_0+x_1+x_2+x_3$$

Um polinómio diferente de zero que usa apenas multiplicações designa-se por **monómio**.
Cada monómio escreve-se como

$$x_0^{e_0}\times x_1^{e_1}\times\cdots\times x_{n-1}^{e_{n-1}}$$

e, por isso, é completamente determinado pelo vetor dos seus expoentes

$$(e_0,e_1,\cdots,e_{n-1})$$

Nos polinómios booleanos os expoentes são sempre $$\,0\,$$ ou $$\,1\,$$, uma vez que $$\,x_i^2=x_i\,$$ para todo $$\,i\,$$.
Por isso cada monómio é completamente determinado por um vetor de $$\,n\,$$ bits. Escreve-se $$\,x^e\,$$ para o monómio com vetor de expoentes $$\,e\in\{0,1\}^n\,$$.

## Exemplo 2

Nos monómios com $$\,4\,$$ variáveis tem-se

- $$\,x_0x_2x_3 = x_0^1x_1^0x_2^1x_3^1\,$$ é representado pela palavra $$\,1011\,$$;
- $$\,x_1x_2 = x_0^0x_1^1x_2^1x_3^0\,$$ é representado pela palavra $$\,0110\,$$;
- $$\,1 = x_0^0x_1^0x_2^0x_3^0\,$$ é representado pela palavra $$\,0000\,$$.

(Aqui, ao contrário da bijeção com $$\,\mathbb{N}\,$$, o bit $$\,e_0\,$$ é o mais à esquerda.)

Um polinómio $$\,f(x_0,\cdots,x_{n-1})\,$$ é uma soma de monómios e é completamente determinado pelo conjunto dos vetores de expoentes. Por isso um polinómio booleano em $$\,n\,$$ variáveis é completamente descrito por um conjunto de palavras de bits de tamanho $$\,n\,$$ (i.e. um subconjunto de $$\,\mathbb{B}^n\,$$) que se designa como o **espectro de expoentes** de $$\,f\,$$, representado por $$\,\Sigma_f\,$$.

## Exemplo 3

Os três polinómios do Exemplo 1 são descritos pelos seguintes conjuntos de strings

$$\{0000,\,1010,\,0101\}\,,\qquad \{1100,\,0010,\,0111\}\,,\qquad \{1000,\,0100,\,0010,\,0001\}$$

Note-se que com a soma *xor* verifica-se $$\,x+x=0\,$$ para todo $$\,x\,$$; por isso, na construção do polinómio, dois monómios iguais anulam-se mutuamente.

Em alternativa, um polinómio booleano $$\,f(x_0,\cdots,x_{n-1})\,$$ pode ser descrito pelo conjunto de pontos $$\,z\in\mathbb{B}^n\,$$ onde toma o valor $$\,1\,$$; isto define um conjunto

$$S_f \;\equiv\; \{\,z\in\mathbb{B}^n\mid f(z)=1\,\}$$

designado como **suporte** do polinómio $$\,f\,$$.

Se fixarmos um qualquer subconjunto $$\,S\subseteq\mathbb{B}^n\,$$ pode-se definir uma função booleana $$\,f_S\,$$ como

$$f_S(x_0,\cdots,x_{n-1}) \;\equiv\; \begin{cases} 1 & \text{se } (x_0,\cdots,x_{n-1})\in S\\ 0 & \text{em caso contrário}\end{cases}$$

Por definição, o suporte de $$\,f_S\,$$ é precisamente $$\,S\,$$; e, como toda a função booleana é descrita por um polinómio booleano, $$\,f_S\,$$ tem também um espectro $$\,\Sigma_{f_S}\,$$.

No que se segue, dada uma linguagem (conjunto de strings) $$\,L\subseteq\{0,1\}^n\,$$ como descrição de um polinómio booleano $$\,f\,$$ com $$\,n\,$$ variáveis, quer como suporte quer como espectro, representamos por $$\,|L|\,$$ a cardinalidade desse conjunto. Se $$\,L\,$$ for o espectro de $$\,f\,$$, essa cardinalidade é designada por **tamanho** de $$\,f\,$$ e representa-se por $$\,|f|\,$$.

## A transformada de Möbius

Dado que o mesmo polinómio booleano $$\,f\,$$ pode ser igualmente representado por dois subconjuntos distintos de $$\,\{0,1\}^n\,$$, o espectro $$\,\Sigma_f\,$$ e o suporte $$\,S_f\,$$, deve existir um algoritmo que converta uma representação na outra.

Para $$\,u,e\in\{0,1\}^n\,$$ escreve-se $$\,e\preceq u\,$$ quando $$\,e_i\le u_i\,$$ para todo $$\,i\,$$. Como $$\,x^e(u)=1\,$$ se e só se $$\,e\preceq u\,$$, tem-se

$$u\in S_f \;\iff\; |\{\,e\in\Sigma_f\mid e\preceq u\,\}| \text{ é ímpar}$$

A conversão $$\,\mathsf{M}\,$$ assim definida é a **transformada de Möbius** (ou transformada de Reed–Muller) sobre $$\,\mathbb{F}_2\,$$. É uma função invertível que mapeia subconjuntos de $$\,\mathbb{B}^n\,$$ em subconjuntos de $$\,\mathbb{B}^n\,$$ tal que, para todo $$\,f\,$$,

$$\mathsf{M}(\Sigma_f)\equiv S_f \qquad\text{e}\qquad \mathsf{M}^{-1}(S_f)\equiv\Sigma_f$$

Uma propriedade de $$\,\mathsf{M}\,$$, específica dos polinómios booleanos, é o facto de coincidir com a sua própria inversa: $$\,\mathsf{M}\circ\mathsf{M}=\mathrm{id}\,$$ (é *involutiva*).

Por esse motivo faz sentido definir a noção de função dual de uma função booleana $$\,f\,$$ do seguinte modo:

**Definição:** o **dual** de $$\,f\,$$ é a função $$\,\bar{f}\,$$ cujo espectro de expoentes coincide com o suporte de $$\,f\,$$ e, equivalentemente, cujo suporte coincide com o espectro de $$\,f\,$$:

$$\Sigma_{\bar f}=S_f\,,\qquad S_{\bar f}=\Sigma_f$$

## Exemplo 4

É interessante comparar a cardinalidade do espectro e do suporte em alguns casos de funções em $$\,n\,$$ variáveis:

- A função booleana constante $$\,f=1\,$$ tem um único monómio: $$\,\Sigma_f\equiv\{0^n\}\,$$. Todo $$\,x\in\{0,1\}^n\,$$ satisfaz $$\,f(x)=1\,$$; por isso o suporte é $$\,S_f\equiv\{0,1\}^n\,$$.
Neste caso temos uma função cujo espectro é um conjunto singular, enquanto o seu suporte é a linguagem máxima de ordem $$\,n\,$$.

- A **função de Kronecker** define-se por $$\,\delta(x)=1\,$$ sse $$\,x=0^n\,$$. O seu suporte é o conjunto singular $$\,S_\delta\equiv\{0^n\}\,$$.
Esta função pode escrever-se também como
$$\delta(x_0,\cdots,x_{n-1}) = (1+x_0)(1+x_1)\cdots(1+x_{n-1})$$
que, por indução em $$\,n\,$$, se verifica conter todos os $$\,2^n\,$$ monómios em $$\,n\,$$ variáveis.
Portanto o espectro de $$\,\delta\,$$ é a linguagem máxima de ordem $$\,n\,$$: $$\,\Sigma_\delta=\{0,1\}^n\,$$.

Pode-se afirmar, portanto, que a função de Kronecker é dual da função constante $$\,f(x_0,\cdots,x_{n-1})=1\,$$.

## Valoração (EVAL) e satisfação (SAT)

Associados a uma função booleana $$\,f\,$$ determinada por um espectro $$\,\Sigma_f\,$$ existem dois problemas fundamentais:

- **valoração** ($$\,\mathsf{EVAL}\,$$): dado um vetor $$\,x\in\{0,1\}^n\,$$, calcular o valor de $$\,f(x)\,$$; equivalente a decidir $$\,x\in S_f\,$$;
- **satisfação** ($$\,\mathsf{SAT}\,$$): determinar se existe algum vetor $$\,z\in\{0,1\}^n\,$$ que “valide” $$\,f\,$$; equivalente a decidir $$\,S_f\neq\emptyset\,$$, i.e.
$$\exists\,z\in\{0,1\}^n\cdot f(z)=1$$
Na versão de *procura*, $$\,\mathsf{SAT}\,$$ deve ainda produzir uma tal testemunha $$\,z\,$$.

### Valoração

O algoritmo de valoração percorre as $$\,n\,$$ componentes de $$\,x\,$$ e, para cada uma, percorre todos os elementos de $$\,L=\Sigma_f\,$$. É um exemplo paradigmático de algoritmo determinístico.

$$\mathsf{EVAL}(n,L,x)\;\equiv$$

1. Testa o tipo dos argumentos: $$\,n>0\,\land\,|x|=n\,\land\,L\subseteq\{0,1\}^n\,$$. Se falhar, devolve $$\,\bot\,$$ (erro).
2. Para $$\,i=0,1,\cdots,n-1\,$$: se $$\,x_i=0\,$$, remove de $$\,L\,$$ todos os expoentes $$\,e\in L\,$$ tais que $$\,e_i=1\,$$.
3. Se no final $$\,|L|\,$$ é par, o resultado é $$\,0\,$$; se $$\,|L|\,$$ é ímpar, o resultado é $$\,1\,$$.

Os monómios da função booleana que têm o valor $$\,0\,$$ após as suas variáveis serem substituídas pelos valores $$\,x_i\,$$ são aqueles onde pelo menos um desses $$\,x_i\,$$ é zero.
No final do passo 2 foram eliminados de $$\,L\,$$ todos os monómios onde uma das suas variáveis tem o valor $$\,0\,$$. Restam só os monómios que têm a valoração $$\,1\,$$ (os $$\,e\preceq x\,$$); a soma final de todos estes $$\,1\,$$’s será $$\,0\,$$ se o número desses monómios for par e $$\,1\,$$ se for ímpar.

O algoritmo limita-se a comparar vetores de bits e a verificar o valor de componentes individuais de vetores; não executa qualquer operação de soma ou multiplicação.

A sua complexidade é $$\,O(n\cdot|f|)\,$$ e depende crucialmente do número de monómios em $$\,f\,$$, isto é, da cardinalidade de $$\,L\,$$. No pior caso o número de monómios é exponencial em $$\,n\,$$: $$\,|f|=O(2^n)\,$$, e a complexidade será exponencial em $$\,n\,$$.
Porém, muitas vezes o número de monómios é polinomialmente limitado na dimensão $$\,n\,$$; nesse caso a complexidade deste algoritmo é polinomial.

### Satisfação na representação por polinómios

Na representação por polinómios, $$\,\mathsf{SAT}\,$$ é um problema **fácil**. Como a forma de Zhegalkin é canónica (cada função tem um único espectro), tem-se

$$S_f\neq\emptyset \iff f\neq 0 \iff \Sigma_f\neq\emptyset$$

Também a procura de uma testemunha é polinomial: escolhe-se $$\,e\in\Sigma_f\,$$ com o menor número de bits $$\,1\,$$ e toma-se $$\,z\equiv e\,$$. Os monómios $$\,e'\in\Sigma_f\,$$ com $$\,e'\preceq z\,$$ são apenas o próprio $$\,e\,$$ (pela minimalidade), pelo que $$\,f(z)=1\,$$. O custo é $$\,O(n\cdot|f|)\,$$.

A dificuldade do $$\,\mathsf{SAT}\,$$ não é intrínseca à função, mas sim à **representação**: quando $$\,f\,$$ é dada por uma fórmula em forma normal conjuntiva (CNF) ou por um circuito, o problema é NP-completo e os melhores algoritmos conhecidos têm complexidade exponencial no pior caso — o que não impede que existam algoritmos eficientes no caso médio. Converter uma CNF ou um circuito para a forma de Zhegalkin pode produzir um número exponencial de monómios. Nos polinómios, o problema difícil é o cálculo do suporte completo ($$\,\mathsf{SAT}^\ast\,$$, abaixo) ou a sua contagem ($$\,\#\mathsf{SAT}\,$$).

### A decomposição de Shannon e o algoritmo SAT genérico

O algoritmo seguinte não depende da representação escolhida e é o esquema base dos algoritmos de $$\,\mathsf{SAT}\,$$ para CNF e circuitos (por exemplo, DPLL). Apresenta-se aqui para polinómios.

A computação $$\,\mathsf{SAT}(n,f)\,$$ produz $$\,\bot\,$$ se $$\,f\,$$ não é satisfazível e produz não-deterministicamente algum $$\,x\,$$ tal que $$\,f(x)=1\,$$ quando for satisfazível.

Um polinómio $$\,f\,$$ em $$\,n\,$$ variáveis pode ser decomposto numa soma

$$f = x_0\,g + h$$

em que $$\,x_0\,$$ é a primeira variável e $$\,g,h\,$$ são polinómios em $$\,n-1\,$$ variáveis que não contêm $$\,x_0\,$$.

Seja $$\,\upsilon\equiv(x_1,\cdots,x_{n-1})\,$$ o vetor das restantes variáveis.

Somando $$\,x_0h\,$$ duas vezes, a decomposição passa a ser

$$f = x_0\,(g+h) + (1+x_0)\,h$$

isto é

$$f(x_0\,\upsilon) = \begin{cases} (g+h)(\upsilon) & \text{se } x_0=1\\ h(\upsilon) & \text{se } x_0=0\end{cases}$$

Agora, se $$\,y\in\{0,1\}^{n-1}\,$$ é uma solução de $$\,\mathsf{SAT}\,$$ para $$\,(g+h)\,$$, então $$\,1y\,$$ é uma solução de $$\,\mathsf{SAT}\,$$ para $$\,f\,$$; se $$\,y\,$$ é uma solução de $$\,\mathsf{SAT}\,$$ para $$\,h\,$$, então $$\,0y\,$$ é uma solução de $$\,\mathsf{SAT}\,$$ para $$\,f\,$$.

Esta decomposição define recursivamente um algoritmo não-determinístico paradigmático:

$$\mathsf{SAT}(n,f)\;\equiv$$

1. Se $$\,n=0\,$$ e $$\,f=0\,$$, devolve $$\,\bot\,$$; se $$\,n=0\,$$ e $$\,f=1\,$$, devolve a string vazia $$\,\varepsilon\,$$.
2. Se $$\,n>0\,$$, obtém de $$\,f\,$$ os polinómios $$\,(g+h)\,$$ e $$\,h\,$$, em $$\,n-1\,$$ variáveis, como referido atrás.
3. Escolhe não-deterministicamente $$\,b\in\{0,1\}\,$$.
4. Se $$\,b=1\,$$, calcula $$\,y\leftarrow\mathsf{SAT}(n-1,\,g+h)\,$$; se $$\,b=0\,$$, calcula $$\,y\leftarrow\mathsf{SAT}(n-1,\,h)\,$$.
5. Se $$\,y=\bot\,$$, devolve $$\,\bot\,$$; caso contrário devolve $$\,b\,y\,$$.

$$\,f\,$$ é satisfazível se e só se alguma execução de $$\,\mathsf{SAT}(n,f)\,$$ devolve um resultado diferente de $$\,\bot\,$$. Cada execução tem $$\,n\,$$ níveis de recursividade (um por variável) e faz uma única chamada por nível.

**Nota**

Se $$\,f\,$$ é descrito por um conjunto de palavras de $$\,n\,$$ bits, então, dividindo $$\,f\,$$ em palavras cujo $$\,0\,$$-ésimo bit é $$\,1\,$$ ou $$\,0\,$$, constrói-se

$$g=\{\,\upsilon\mid 1\upsilon\in\Sigma_f\,\}\qquad\text{e}\qquad h=\{\,\upsilon\mid 0\upsilon\in\Sigma_f\,\}$$

Para calcular a descrição de $$\,(g+h)\,$$ faz-se a diferença simétrica

$$g\,\triangle\,h \;=\; (g\setminus h)\cup(h\setminus g)$$

isto é, faz-se a união de $$\,g\,$$ e $$\,h\,$$ como multiconjuntos e removem-se os pares de elementos iguais.

A computação $$\,\mathsf{SAT}(n,f)\,$$ é não-determinística mas tem **não-determinismo finito**: em cada nível de recursividade há $$\,\le 2\,$$ escolhas (passo 3), pelo que o número de execuções, e de resultados possíveis, está limitado a $$\,2^n\,$$.

Como qualquer algoritmo com não-determinismo finito, é sempre possível construir um algoritmo determinístico $$\,\mathsf{SAT}^\ast\,$$ tal que $$\,\mathsf{SAT}^\ast(n,f)\,$$ devolve, como resultado, o conjunto de todos os resultados possíveis de $$\,\mathsf{SAT}(n,f)\,$$ diferentes de $$\,\bot\,$$, isto é, o suporte $$\,S_f\,$$.

$$\mathsf{SAT}^\ast(n,f)\;\equiv$$

1. Se $$\,n=0\,$$ e $$\,f=0\,$$, devolve o conjunto vazio $$\,\{\,\}\,$$; se $$\,n=0\,$$ e $$\,f=1\,$$, devolve $$\,\{\varepsilon\}\,$$.
2. Se $$\,n>0\,$$, decompõe $$\,f\,$$ e obtém os polinómios $$\,(g+h)\,$$ e $$\,h\,$$, em $$\,n-1\,$$ variáveis, como referido anteriormente.
3. Calcula $$\,Y\leftarrow\mathsf{SAT}^\ast(n-1,\,g+h)\,$$ e $$\,Z\leftarrow\mathsf{SAT}^\ast(n-1,\,h)\,$$.
4. Calcula $$\,Y'\leftarrow\{\,1a\mid a\in Y\,\}\,$$ e $$\,Z'\leftarrow\{\,0b\mid b\in Z\,\}\,$$.
5. Devolve $$\,Y'\cup Z'\,$$.

Aqui a recursividade é dupla e há $$\,n\,$$ níveis, pelo que a complexidade no pior caso é $$\,O(2^n)\,$$ chamadas. Este limite não pode ser melhorado em geral, porque o próprio resultado $$\,S_f\,$$ pode ter $$\,2^n\,$$ elementos (por exemplo para $$\,f=1\,$$). Note-se que $$\,\mathsf{SAT}^\ast\,$$ calcula precisamente a transformada de Möbius: $$\,\mathsf{SAT}^\ast(n,f)=\mathsf{M}(\Sigma_f)=S_f\,$$.

# Circuitos Booleanos e Aritméticos

Circuitos são um modelo importante para os problemas que vamos encontrar ao longo deste curso.

A função principal de um circuito é a descrição de uma computação funcionalmente complexa através de operações elementares numa determinada álgebra. Por isso, uma parte essencial da descrição do circuito é a escolha do domínio onde se vai realizar a computação e dos operadores básicos desse domínio.

Outra componente do circuito é a definição da sua topologia; isto é, a forma como as operações básicas se combinam para construir a computação principal.

É possível descrever a topologia de várias formas, mas a mais simples é através de diagramas de operações (“gates”) e conexões (“wires”).

## Diagramas e Grafos

Genericamente, um diagrama é um grafo bipartido orientado e acíclico.

Um **grafo bipartido orientado** é um grafo onde os nodos estão agrupados em dois conjuntos disjuntos $$\,W,V\,$$ e onde cada ramo tem origem num nodo de um dos conjuntos e destino num nodo do outro conjunto.

Num diagrama, os nodos que não são destino de qualquer ramo designam-se por **sources** e os nodos que não são origem de qualquer ramo designam-se por **sinks**. Uma **raiz** do diagrama $$\,D\,$$ é um sink $$\,r\,$$ tal que, para qualquer source $$\,s\,$$, existe um caminho com origem em $$\,s\,$$ e destino em $$\,r\,$$. (Um diagrama com vários sinks não tem, em geral, raízes: no exemplo abaixo, nenhum dos dois outputs é alcançável a partir de todos os inputs.)

Num circuito, a topologia está organizada num diagrama onde os nodos estão agrupados em dois conjuntos, *gates* e *wires*, e onde todos os sinks são wires. Os sinks do circuito designam-se por **outputs** e os wires que são sources do circuito designam-se por **inputs**. Gates sem inputs (constantes) são também sources.

> **[Figura: Um circuito $$\,4\times 2\,$$ — ver diagrama no documento original.]**

O diagrama representa um circuito com 6 gates (três somas, duas multiplicações e uma constante) e 10 wires:
quatro são inputs do circuito ($$\,x_0,x_1,x_2,x_3\,$$), dois são outputs do circuito ($$\,y_0,y_1\,$$) e quatro são conexões intermédias ($$\,w_0,w_1,w_2,w_3\,$$) que ligam o output de uma gate aos inputs de outras.
Nestes diagramas não existem ciclos: a informação flui sempre dos inputs para os outputs.

Genericamente, um diagrama representa apenas a topologia do circuito; isto é, o arranjo das gates e dos wires a que estão ligadas. Para completar a definição do circuito é necessária também uma descrição algébrica, como veremos em seguida.

Cada gate tem zero ou mais wires de onde flui informação (os seus inputs) e um só wire para onde flui informação (o seu output). A informação flui, sempre, na forma de elementos do domínio algébrico do circuito.

Em cada wire, a informação pode fluir de uma só origem: o exterior do circuito ou uma só gate.
Analogamente, cada wire envia informação para o exterior do circuito ou então para uma ou mais gates.

> **[Figura: grafo bipartido do circuito anterior, com gates e wires representados por símbolos distintos — ver documento original.]**

## Descrição algébrica

A descrição algébrica do circuito parte de uma álgebra (um domínio e um conjunto de operadores) e associa a cada wire uma variável que toma valores no domínio do circuito e a cada gate um operador da álgebra. A descrição é formada por um conjunto de equações, uma por gate, da forma

$$\mathit{output} = \mathit{operador}(\mathit{input}_1,\cdots,\mathit{input}_\ell)$$

em que $$\,\mathit{operador}\,$$ é o operador da gate e $$\,\mathit{output}\,$$ e os $$\,\mathit{input}_i\,$$ denotam as variáveis associadas, respetivamente, ao output e aos inputs da gate.

No exemplo anterior associámos multiplicações às gates $$\,g_0\,$$ e $$\,g_1\,$$, somas às gates $$\,g_2,g_3\,$$ e $$\,g_4\,$$ e uma constante $$\,c\,$$ à gate $$\,g_5\,$$. As relações algébricas definidas são, neste caso,

$$y_0=w_0\times w_1\,,\quad y_1=w_1\times w_2\,,\quad w_0=x_0+x_1\,,\quad w_1=x_1+x_2\,,\quad w_2=x_3+w_3\,,\quad w_3=c$$

Como no diagrama e no grafo bipartido não existem ciclos, e a informação flui sempre dos inputs para os outputs, é sempre possível manipular as relações eliminando todas as variáveis intermédias.
Neste exemplo teríamos

$$y_0=(x_0+x_1)\times(x_1+x_2)\,,\qquad y_1=(x_1+x_2)\times(x_3+c)$$

Após simplificação, a descrição tem uma equação por cada variável de output, no lado esquerdo da equação, e no lado direito tem uma expressão exclusivamente formada por operadores das gates e variáveis de input. Note-se que esta eliminação pode duplicar subexpressões partilhadas (aqui, $$\,x_1+x_2\,$$); em geral a expressão resultante pode ser exponencialmente maior do que o circuito.

Num circuito genérico de dimensão $$\,n\times m\,$$, em que as variáveis de input são $$\,x_0,\cdots,x_{n-1}\,$$ e as variáveis de output são $$\,y_0,\cdots,y_{m-1}\,$$, a descrição é definida por um sistema de equações

$$y_i=f_i(x_0,\cdots,x_{n-1})\qquad\text{para } i=0,\cdots,m-1$$

sendo $$\,f_i\,$$ expressões compostas pelos operadores das gates e pelas variáveis de input.

## Tipos de Circuitos

Essencialmente descrevemos um processo que, a partir da topologia de um circuito $$\,n\times m\,$$ sobre o domínio $$\,X\,$$ e dos operadores elementares associados, permite construir uma função computável $$\,f:X^n\to X^m\,$$.

O processo inverso designa-se por **síntese** do circuito: partindo de uma função computável $$\,f:X^n\to X^m\,$$, pretende-se construir a descrição topológica e a descrição algébrica que permitem definir essa função.

Obviamente podem existir vários circuitos $$\,C\,$$ que constroem a mesma função. Há um compromisso entre a riqueza da álgebra e a complexidade da topologia: com operadores mais poderosos são, em geral, necessárias menos gates, e vice-versa. Por isso a síntese está associada a alguma forma de otimização: por exemplo, minimizar o número de gates.

Existem algumas formas frequentes de circuitos:

- **circuitos booleanos**
O domínio é formado pelos valores lógicos $$\,X\equiv\{0,1\}\,$$, que também determinam as constantes. Os operadores binários elementares são as conectivas *and*, *or* e *xor*, representadas por $$\,\land,\,\lor,\,\oplus\,$$.
Quando o número de outputs é $$\,1\,$$, o circuito booleano é completamente determinado por uma única fórmula proposicional (possivelmente muito maior do que o circuito).

- **circuitos booleanos vetoriais**
A informação está organizada em vetores de bits de um tamanho $$\,\ell\,$$ fixo. Assim o domínio é $$\,X\equiv\{0,1\}^\ell\,$$ e cada elemento desse domínio define uma constante. Os operadores binários são $$\,\land,\,\lor\,$$ e $$\,\oplus\,$$, executados posição a posição. Cada posição $$\,0\le i<\ell\,$$ define um operador unário que seleciona, em cada $$\,x\in X\,$$, a sua componente $$\,x_i\,$$ (devolvendo, por exemplo, o vetor $$\,x_i^\ell\,$$ com essa componente replicada, para que o resultado esteja em $$\,X\,$$).

- **circuitos aritméticos**
A informação está organizada em inteiros não negativos representáveis com $$\,\ell\,$$ bits. Formalmente o domínio é
$$\mathbb{Z}_N\equiv\{\,k\in\mathbb{Z}\mid 0\le k<N\,\}\,,\qquad N\equiv 2^\ell$$
Neste domínio define-se a estrutura algébrica de um anel com soma e multiplicação modulares: $$\,x+y\bmod N\,$$ e $$\,x\times y\bmod N\,$$.
Associando os inteiros à sua representação binária, estão ainda disponíveis todas as operações elementares dos circuitos booleanos vetoriais: $$\,\land,\,\lor,\,\oplus\,$$ e seleção de componente.

## Descrição de circuitos e suas complexidades

O **tamanho** de um circuito $$\,C\,$$, representado por $$\,|C|\,$$, é o seu número de gates. Nesta secção vamos analisar alguns dos principais problemas definíveis através de circuitos, analisar a sua complexidade computacional e relacioná-la com o tamanho do circuito.

A maioria destes problemas pode ser estudada no contexto simplificado dos circuitos booleanos com um único output. Nesse caso a dimensão do circuito coincide com o número dos seus input wires.

Em primeiro lugar, um circuito é uma entidade finita, composta por um número finito de conexões e gates. Por isso pode ser descrito, numa linguagem apropriada, por uma string de bits.

A descrição algébrica de um circuito permite definir recursivamente uma função que calcula os valores dos outputs do circuito através de uma ordenação das gates designada por **ordenação topológica**.

Considere-se um circuito com $$\,n\,$$ inputs e $$\,k\,$$ gates. Numeram-se os wires de modo que:

- os wires de input são $$\,w_0,\cdots,w_{n-1}\,$$, e calcula-se
$$w_i\leftarrow x_i\qquad\text{para todo } 0\le i<n$$
- as gates são $$\,g_i\,$$, com $$\,n\le i<n+k\,$$, e o wire de output de $$\,g_i\,$$ é $$\,w_i\,$$, identificado pelo mesmo índice $$\,i\,$$;
- todos os wires que são inputs de $$\,g_i\,$$ têm índices inferiores a $$\,i\,$$.

Cada gate é um tuplo

$$g_i=\langle\,\mathit{op}_i,\,\mathit{args}_i\,\rangle$$

em que $$\,\mathit{op}_i\,$$ é o identificador do operador que interpreta algebricamente essa gate e $$\,\mathit{args}_i=(a_1,\cdots,a_\ell)\,$$ é a **sequência** (ordenada, possivelmente com repetições) dos índices dos wires que são inputs dessa gate.
Portanto o circuito introduz uma computação singular por gate, dada por

$$w_i\leftarrow f_{\mathit{op}_i}(w_{a_1},\cdots,w_{a_\ell})\qquad\text{para } i=n,\cdots,n+k-1$$

Assim o circuito é completamente descrito pela sua ordenação topológica

$$C=\{\,\langle\mathit{op}_i,\mathit{args}_i\rangle\,\}_{n\le i<n+k}$$

O algoritmo $$\,\mathsf{EVAL}(C,x)\,$$ calcula o output $$\,w_{n+k-1}\,$$ percorrendo todas as gates do circuito de forma ordenada:

$$\mathbf{for}\;\; 0\le i<n:\qquad w_i\leftarrow x_i$$

$$\mathbf{for}\;\; n\le i<n+k:\qquad w_i\leftarrow f_{\mathit{op}_i}(w_{a_1},\cdots,w_{a_\ell})\quad\text{com }(a_1,\cdots,a_\ell)=\mathit{args}_i$$

A sua complexidade é linear no tamanho da descrição do circuito.

Por outro lado, um circuito identifica outras entidades também descritas por uma string finita. Nomeadamente:

- **Linguagem de suporte**
O circuito $$\,C\,$$ determina um conjunto de strings
$$L_C\equiv\{\,x\mid\mathsf{EVAL}(C,x)=1\,\}$$
Os elementos de $$\,L_C\,$$ dizem-se *aceites* pelo circuito $$\,C\,$$ e $$\,L_C\,$$ designa-se por **linguagem de suporte** de $$\,C\,$$.
A linguagem $$\,L_C\,$$ é de ordem $$\,n\,$$; isto é, todos os seus elementos têm comprimento $$\,n\,$$. É também uma entidade finita e, por isso, também pode ser descrita por uma string de bits.

- **Função booleana**
Como vimos anteriormente, um circuito booleano $$\,C\,$$ de dimensão $$\,n\,$$ com um só output implementa uma função booleana
$$f_C(x_0,\cdots,x_{n-1})$$
com exatamente $$\,n\,$$ variáveis.
Recorde-se que $$\,f_C\,$$, como toda a função booleana, é descrita pelo espectro de expoentes: i.e. pelo conjunto dos vetores $$\,e\in\{0,1\}^n\,$$ tais que $$\,x^e\,$$ é um monómio dessa função.
Assim, $$\,f_C\,$$ identifica-se com um subconjunto de $$\,\{0,1\}^n\,$$; isto é, $$\,\Sigma_{f_C}\,$$ é também uma linguagem de ordem $$\,n\,$$ e, portanto, pode ser descrita por uma string finita.

É importante frisar que o circuito, a função que ele implementa e a linguagem de suporte são entidades distintas. A mesma função pode ser implementada por circuitos diferentes e, igualmente, uma linguagem de ordem $$\,n\,$$ é suporte de circuitos distintos.

No entanto, para cada função booleana $$\,f\,$$ em $$\,n\,$$ variáveis existe uma única linguagem $$\,S_f\,$$ formada por todos os $$\,x\in\{0,1\}^n\,$$ que satisfazem $$\,f\,$$; em particular $$\,L_C=S_{f_C}\,$$. Essa linguagem é determinada, a partir do espectro de $$\,f\,$$, pelo algoritmo $$\,\mathsf{SAT}^\ast\,$$ descrito anteriormente.

---

# Notas de revisão

Principais alterações de conteúdo relativamente ao texto original:

1. **SAT em polinómios.** O original afirmava que, mesmo com um número polinomial de monómios, os melhores algoritmos de SAT são exponenciais. Na forma de Zhegalkin, SAT é trivial ($$\,f\neq 0\,$$) e a testemunha obtém-se em tempo polinomial (monómio de grau mínimo). Foi acrescentada a explicação de que a dificuldade está na representação (CNF, circuitos) e em $$\,\mathsf{SAT}^\ast\,$$ / $$\,\#\mathsf{SAT}\,$$.
2. **Nome da conversão espectro → suporte.** Passou a chamar-se transformada de Möbius $$\,\mathsf{M}\,$$, reservando $$\,\mathsf{SAT}\,$$ para o problema de satisfação. Foi explicitada a caracterização $$\,u\in S_f\iff|\{e\in\Sigma_f\mid e\preceq u\}|\,$$ ímpar.
3. **Algoritmo SAT não-determinístico.** Passou a escolher um ramo e a seguir só esse (uma chamada por nível), em vez de calcular ambos e escolher no fim.
4. **Raiz e outputs.** No exemplo $$\,4\times2\,$$ nenhum output é raiz segundo a definição dada; os outputs passaram a ser definidos como os sinks.
5. **Ordenação topológica.** Indexação uniformizada ($$\,n\,$$ inputs, $$\,k\,$$ gates, output $$\,w_{n+k-1}\,$$), sem reutilizar $$\,m\,$$; os inputs são wires (não gates); $$\,\mathit{args}_i\,$$ passou a ser uma sequência, não um conjunto.
6. **Tamanho de um inteiro.** $$\,\lceil\log_2 n\rceil\,$$ foi substituído por $$\,\lfloor\log_2(n+1)\rfloor\,$$, coerente com a bijeção; explicitou-se que $$\,x_0\,$$ é o bit mais à direita e que a ordem é *shortlex*.
7. **Domínios.** $$\,\varpi\,$$ foi uniformizado para $$\,\omega\,$$ (domínio contável infinito, isomórfico com $$\,\mathbb{N}\,$$, e não com $$\,\{0,1\}\,$$); $$\,2^{\mathbb{N}}\,$$ passou a ser descrito como espaço de funções e não como ordinal; os domínios de Cantor passaram a ser definidos como conjuntos de subconjuntos; foi notada a não injetividade da correspondência streams → reais.
8. **Booleano/binário.** Passou a ser enquadrado no anel quociente $$\,\mathbb{F}_2[x]/(x_i^2-x_i)\,$$.
9. **Pormenores.** «grau $$\,n-1\,$$» → «em $$\,n-1\,$$ variáveis»; posição $$\,0\le i<\ell\,$$ (e não $$\,<n\,$$) nos circuitos vetoriais; inteiros «não negativos»; gates constantes sem inputs; EVAL devolve $$\,\bot\,$$ em erro de tipos; numeração $$\,x_0,\cdots,x_{n-1}\,$$ uniformizada; nota sobre a explosão exponencial ao eliminar variáveis intermédias.
10. **Gralhas e ortografia** corrigidas (Acordo Ortográfico uniformizado; «ordenação tipológica» → «topológica», etc.).

As figuras do original (diagrama e grafo bipartido do circuito $$\,4\times2\,$$) não foram reproduzidas e estão assinaladas no texto.
