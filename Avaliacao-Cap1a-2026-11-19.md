# Avaliação: Capítulo 1a (Terminologia, Decidibilidade e Satisfabilidade)

**Data:** 2026-11-19.
**Documento:** *Capítulo 1a: Terminologia, Decidibilidade e Satisfabilidade* (Dropbox Paper).
**Ficheiros associados:**
- `Capitulo_1a_corrigido.md`: versão corrigida do capítulo; as marcas <sup>[Cn]</sup> remetem para os pontos abaixo.
- `cap1a_verificacoes.py`: notebook Marimo com as verificações (força bruta e `scipy.optimize.linprog`).

**Método:**
- Texto extraído da página no Chrome. As figuras não vieram na extração; a árvore de decisão e a BDD foram reconstruídas a partir da fórmula do texto e conferem com as contagens do original (9 → 5 nodos, 8 → 6 referências).
- Afirmações computáveis verificadas no notebook (scipy 1.18.1).

**Legenda:** 🔴 erro de conteúdo · 🟠 inconsistência / imprecisão · 🟡 rigor e forma

Para localizar cada ponto no Paper indico a secção e uma frase próxima.

---

## Correto (verificado)

- Codificação CNF → LIA do exemplo $F\equiv(x\vee\neg y\vee\neg z)\wedge(\neg x\vee z\vee w)$, incluindo a forma simplificada $(-x+y+z\le 1)\wedge(x-z-w\le 0)$ (força bruta em $\{0,1\}^4$).
- Negação em PI: $(c_0,\dots,c_n)\mapsto(-c_0-1,-c_1,\dots,-c_n)$. Só vale em domínios inteiros; em $\mathbb{Q}^+$ falha (a negação de $\le$ é $<$).
- Simplificação em PIB por $\sigma_{\max}=\sum_{c_i>0}c_i$ e $\sigma_{\min}=\sum_{c_i<0}c_i$, com as duas regras ($c_0\ge\sigma_{\max}$ ⇒ sempre verdadeiro; $c_0<\sigma_{\min}$ ⇒ sempre falso).
- Relação PIB/PI: consistente em PIB ⇒ consistente em PI, mas não o inverso.
- Exemplo da árvore de decisão e da BDD: com $x_0$ lido como $x_2$, a fórmula é $f=(x_1\wedge\neg x_2\wedge x_3)\vee(\neg x_1\wedge x_3)$; a árvore tem 9 nodos e 8 referências, a BDD 5 nodos e 6 referências.
- Interpretação de $\to$ em $\mathbb{F}_2$: $I=\{(a,b)\mid a=a\cdot b\}$.
- Terminação do *split-and-bound* (o número de variáveis livres desce a cada *split*).
- O segundo axioma intuicionista, $(A\to B)\to((A\to(B\to C))\to(A\to C))$, é o da axiomatização de Kleene e, com o primeiro e *Modus Ponens*, gera o fragmento implicacional.

---

## 🔴 Erros de conteúdo

**C1. Equivalência com negação** (Terminologia: "Se a linguagem contiver negação então a o juízo…").
- "se $\{A_1..A_k\}$ é válida então $\{B_1..B_n\}$ é válida" equivale a "**para todo** $i$, $\{A_1..A_k,\neg B_i\}$ é inconsistente", e não "para algum $i$": a conjunção $\{B_1..B_n\}$ é válida quando **todos** os $B_i$ o são.
- A equivalência só vale em lógica clássica: em lógica intuicionista, da inconsistência de $\{A,\neg B\}$ só se obtém $A\vdash\neg\neg B$.

**C2. Argumento sobre a axiomatização finita** (Decidibilidade: "isto porque $N^N$ não é contável…").
- Uma quantidade contável de axiomas ou esquemas, cada um com uma quantidade contável de instâncias, dá uma quantidade **contável** de instâncias: a cardinalidade é a de $\mathbb{N}\times\mathbb{N}$, não a de $\mathbb{N}^\mathbb{N}$.
- A conclusão "o número de axiomas e regras tem de ser finito" é falsa: a AP de 1.ª ordem tem um esquema infinito de indução e é uma lógica formal (o próprio capítulo o diz mais adiante).
- O que importa computacionalmente é a axiomatização **recursiva** (conjunto de axiomas decidível), que dá teoremas semi-decidíveis. A axiomatização finita não é necessária (Presburger) nem suficiente (FOL pura) para a decidibilidade.

**C3. Aritmética de Presburger** (Aritmética Linear Inteira: "não existe nenhum algoritmo finito que implemente a relação de inferência").
- Contradiz a frase anterior ("correta, completa e decidível"): decidível quer dizer que esse algoritmo existe (eliminação de quantificadores; algoritmo de Cooper, 1972).
- Não ser finitamente axiomatizável não impede a decidibilidade.
- Vale a pena acrescentar o custo (limite inferior duplamente exponencial, Fischer–Rabin 1974) e que os SMTs usam apenas o fragmento sem quantificadores (NP-completo).

**C4. Algoritmo do plano de corte** (último passo: "Constrói-se $\phi'_j$ substituindo a constante inteira $c_0$ por $c'_0\equiv\lfloor c^*\rfloor$").
- O corte não é válido. A justificação do texto ("para elas a quantidade $c^*$ é um inteiro") não chega: as soluções inteiras dão um valor inteiro a $\sum_i c_i x_i$, mas esse valor pode estar entre $\lfloor c^*\rfloor$ e $c_0$.
- Contra-exemplo (no notebook): $\varphi\equiv(2x_1+2x_2\le 3)\wedge(x_1-x_2\le 1)\wedge(-x_1\le -1)$ tem a solução única $(1,0)$; a relaxação dá $x^*=(1,\tfrac12)$; a regra troca $x_1-x_2\le 1$ por $x_1-x_2\le 0$; o LP fica inviável e o algoritmo responde `unsat` **erradamente**.
- Com coeficientes inteiros, arredondar um único predicado não produz nada. Os cortes de Chvátal–Gomory vêm de combinações racionais dos predicados (de uma linha do quadro do Simplex, no caso de Gomory) e são **acrescentados**, não postos no lugar de um predicado existente.
- Falta acrescentar $0\le x_i\le 1$ na inicialização: sem isso, a afirmação $x^*\in[0,1]^n$ não se justifica.
- "Pode não terminar": o método de Gomory, com regras adequadas (lexicográficas), termina; na prática combina-se com *split-and-bound* (*branch-and-cut*).

**C5. Programação Linear e Simplex** ("a sua complexidade é, no pior caso, polinomial com grau menor do que 3").
- O Simplex tem complexidade exponencial no pior caso (Klee–Minty, 1972).
- A polinomialidade da PL vem do elipsoide (Khachiyan, 1979) e dos pontos interiores (Karmarkar, 1984). O "grau menor do que 3" só se defende com resultados muito recentes e não se pode associar ao Simplex.
- Para inequações, o método análogo à eliminação gaussiana é Fourier–Motzkin.

**C6. Negação em BDDs** ("Calcular o diagrama de $\neg f$ … é bastante mais difícil").
- É o contrário: num ROBDD, a negação é linear (troca das folhas $0$ e $1$) e, com *complement edges* (o "bit extra" do texto), custa $O(1)$.
- O *apply* para $\wedge$ e $\vee$ custa $O(|f|\cdot|g|)$.
- Verificado no notebook: $\neg f$ por troca de folhas tem o mesmo tamanho, $f\wedge\neg f=0$ e $f\vee\neg f=1$.

---

## 🟠 Inconsistências e imprecisões

**C7. Monotonia** (Terminologia: "Se a lógica for monótona e $\{B_1..B_n\}$ é uma conjunção válida…").
- A regra enunciada (juntar uma asserção válida a uma conjunção válida) é trivial e não exprime monotonia.
- Monotonia: se $\Gamma\vdash B$ então $\Gamma\cup\{A\}\vdash B$, para **qualquer** $A$. Na linguagem de juízos do texto: se "Γ válida ⇒ Δ válida", então "Γ∪{A} válida ⇒ Δ válida".

**C8. Abreviaturas e lógica intuicionista** (Exemplo: "$A\vee B\equiv\neg A\to B$, $A\wedge B\equiv\neg(A\to\neg B)$").
- Só são adequadas em lógica clássica. Em lógica intuicionista (e mínima), $\wedge$ e $\vee$ não se definem a partir de $\to$ e $\bot$.
- A Lógica Intuicionista apresentada só com $\{\to,\bot\}$ e três axiomas é o fragmento $\{\to,\bot\}$; convém dizê-lo.

**C9. "As Lógicas Proposicionais… qualquer teoria é decidível e finitamente axiomatizável"**.
- Falso: há uma quantidade não contável de teorias (por exemplo, a gerada por $\{p_i: i\in S\}$ com $S$ não recursivo) e só uma quantidade contável de algoritmos.
- O que é decidível é a lógica (a relação de consequência); as teorias **finitamente axiomatizadas** são decidíveis.

**C10. Algoritmo de inferência** ("No caso de uma teoria $T\subseteq L$ ser decidível e a lógica $L$ ser finitamente axiomatisável…").
- Decidir $B\in T$ não decide $A_1..A_k\vdash B$: $B$ pode pertencer a $T$ sem ser consequência daquelas assunções. Exigir $B\in T$ à partida tira o sentido à pergunta.
- O que se pretende é a decidibilidade da relação de consequência (pelo teorema da dedução, decidir se $A_1\wedge\dots\wedge A_k\to B$ é teorema).

**C11. "Ferramentas do tipo model checker ou solver só funcionam corretamente em teorias decidíveis e finitamente axiomatisáveis"**.
- A condição "finitamente axiomatizáveis" contradiz o próprio texto: a LIA vem de Presburger, que não é finitamente axiomatizável.
- Os solvers SMT tratam também fragmentos indecidíveis (aritmética não linear, quantificadores), de forma incompleta (`unknown` ou não terminação). Sugestão: "só são procedimentos de decisão completos em teorias decidíveis".

**C12. Gödel e a indecidibilidade** ("Godel provou, nos anos 30, a indecidibilidade da Aritmética").
- Gödel provou a **incompletude** (1931). A indecidibilidade do *Entscheidungsproblem* deve-se a Church e Turing (1936). Escreve-se "Gödel".

**C13. Aritmética de Peano** ("Por isso a AP é uma linguagem de 2ª ordem sobre um domínio infinito (os inteiros)…").
- A AP habitual é de 1.ª ordem, com a indução como esquema. A versão de 2.ª ordem é categórica.
- A incompletude não decorre de ser de 2.ª ordem: a AP de 1.ª ordem já é incompleta (Gödel). Na versão de 2.ª ordem, o que falta é um cálculo completo para a lógica.
- "É o princípio da indução que permite definir funções recursivas sem as quais não seria possível definir… somas e multiplicações": na AP, $+$ e $\times$ são primitivos com axiomas recursivos; a indução serve para **provar** propriedades.
- O domínio são os naturais, não os inteiros.

**C14. Davis–Putnam** ("O algorimo SAT, conhecido por algoritmo de Davis-Putman…").
- O nome é Putnam. O DP original (1960) usa eliminação de variáveis por resolução; a estratégia de *splitting* descrita é a do DPLL (1962).
- "Split-and-bound" não é o termo usual (é *splitting*/*branching*, ou *branch-and-bound* em otimização). Mantive o termo do curso, com uma nota.

**C15. Conversão para CNF e transformação de Tseitin** ("o algoritmo de conversão de uma proposição genérica numa forma normal tem… complexidade equivalente à do próprio algoritmo SAT").
- Para efeitos de SAT basta uma CNF **equisatisfazível**, que a transformação de Tseitin produz em tempo linear. A dificuldade da abordagem por formas normais está no SAT, não na conversão.
- Isto torna a comparação final (formas normais vs. BDDs) menos desfavorável às formas normais do que o texto sugere.

**C16. Canonicidade e tamanho das BDDs** (Teorema; "BDD's manipulam eficientemente fórmulas com centenas de milhar de variáveis").
- A unicidade da RBDT vale **para uma ordem fixa das variáveis**; o Corolário 1 também só vale para a mesma ordem.
- O tamanho depende muito da ordem. No notebook, $(a_1\wedge b_1)\vee(a_2\wedge b_2)\vee(a_3\wedge b_3)$ tem 8 nodos com $a_1<b_1<a_2<\dots$ e 16 com $a_1<a_2<a_3<b_1<\dots$ (em geral, $2n+2$ contra $2^{n+1}$).
- Há funções (multiplicação) com BDDs exponenciais para qualquer ordem. "Centenas de milhar de variáveis" é otimista.

**C17. Sentido do algoritmo de redução** ("percorre-se a árvore do topo para as folhas reduzindo as sub-árvores e, depois de reduzidas, verificando…").
- O procedimento descrito (reduzir primeiro as subárvores) é ascendente, em pós-ordem: das folhas para a raiz.

**C18. NP-completude e complexidade exponencial** ("tanto PI como PIB têm, no pior caso, complexidade exponencial. De fato ambos os problemas são NP completos").
- Ser NP-completo não prova complexidade exponencial (questão P vs NP). Sugestão: "não se conhece algoritmo polinomial; os algoritmos conhecidos são exponenciais no pior caso".

---

## 🟡 Rigor e forma

**C20. Mundos na semântica geral** ("Sendo $n$ o número de variáveis usadas numa determinada lógica $L$…").
- Uma lógica tem infinitas variáveis. Deve fixar-se uma lista finita $x_1..x_n$ que contenha as variáveis livres das fórmulas em consideração; só assim a interseção $\pi_\Gamma$ faz sentido.

**C21. Exemplo em $\mathbb{F}_2$** ("se $a\models A$ e $b\models B$ então $(a,b)\models A\to B$…").
- Mistura valores de verdade ($a,b\in\mathbb{F}_2$) com mundos. Proposta: $w\models A\to B$ sse $([\![A]\!](w),[\![B]\!](w))\in I$.

**C22. "Tanto provas como modelos são, em princípio, objectos de domínios enumeráveis"**.
- As provas, sim. Os modelos de FOL podem ser infinitos e não enumeráveis.

**C23. Domínios e LIA sobre racionais.**
- "Inteiros positivos $N$" → não negativos (o próprio texto usa $w_i=0$). O mesmo para $\mathbb{Q}^+$.
- Falta o caso $c=0$ na multiplicação escalar.
- Com variáveis racionais trata-se de LRA; a observação "$r\equiv a/b$" deve explicar que se multiplica pelos denominadores.

**C24. "Visão deontológica dos juízos"** ("$P$ é evidência que assegura $C$").
- É uma leitura epistémica ou probatória; deôntico refere-se a obrigação e permissão.

**C25. Axiomas.**
- O 2.º axioma depende da associatividade de $\to$ à direita, que não está explicitada; acrescentei os parênteses.
- $(\neg A\to A)\to A$ chama-se habitualmente *consequentia mirabilis* (lei de Clavius); *reductio ad absurdum* costuma designar $\neg\neg A\to A$ ou a regra correspondente. Com *Ex Falso*, as duas são equivalentes.

**C26. Notação inconsistente.**
- $\kappa$ e $k$ para o mesmo índice; $w$ e $\omega$ para mundos.
- "diagramas de decisão binária **orientados** e reduzidos" → ordenados.
- "RBDT" não é usual; o termo habitual é ROBDD (mantive RBDT para a árvore e acrescentei ROBDD para o diagrama).
- "$C\equiv\{\ell_1\vee\ell_2\vee\dots\}$" mistura notação de conjunto com disjunção.

**C27. Definição de teoria repetida** (no Contexto Sintático e em Decidibilidade). Mantive a primeira e remeti para ela.

**C28. Fórmula da árvore de decisão**: "$(x_1\wedge x_0\wedge 0)$" deve ser $(x_1\wedge x_2\wedge 0)$.

**C29. Gralhas:**
- "a o juízo", "existem uma relações", "é determinado por provas" (validade… determinada)
- "forma formal" → forma normal
- "clásulas" (várias vezes), "algorimo", "preposicionais", "Davis-Putman", "Godel"
- "conconcluir", "insatisfazívíel", "aì", "domínito", "definito", "passoa", "variveis", "algortimo", "importência", "ligaçãoà"
- "axiomatisável" / "axiomatizável" (as duas grafias); "fato" / "facto"

**C30. Validade e inconsistência sintáticas.**
- "Uma fórmula é válida se e só se é um axioma ou então é a conclusão de uma prova cujas assunções são válidas" é circular; basta "conclusão de uma prova sem assunções".
- A definição de inconsistência ("prova todas as fórmulas") coincide com $\Gamma\vdash\bot$ só em presença de *Ex Falso*; na Lógica Mínima, apresentada logo a seguir, as duas noções separam-se.

---

## Prioridades

1. **C2, C3, C4**: estão errados e contradizem outras partes do capítulo.
2. **C1, C5, C6**: afirmações técnicas falsas, fáceis de corrigir.
3. **C9–C13, C15, C16**: imprecisões que os alunos podem levar para os capítulos seguintes (SMT, model checking).
