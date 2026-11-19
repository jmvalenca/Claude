# Validação: Capítulo 2 (Programação com Restrições) e Capítulo 2a (Programação Cónica)

**Data:** 2026-11-19.
**Documentos:**
- *Capítulo 2: Programação com Restrições* (Paper, `/Migrated Paper docs/Lógica Computacional/`, alterado a 2026-09-28).
- *Capítulo 2a: Programação Cónica* (Paper, `/Paper docs/`, alterado a 2026-10-13).

**Método:**
- Texto e LaTeX extraídos da página no Chrome, excluindo os editores internos do Paper.
- Figura do TSP verificada por captura de ecrã.
- Código Clarabel e CVXPY do Cap. 2a executado (clarabel 0.11.1, cvxpy 1.9.3, scipy 1.18.1) nos notebooks Marimo `cap2a_portfolio_clarabel.py` e `cap2a_risk_parity.py`.

**Legenda:** 🔴 erro de conteúdo · 🟠 inconsistência / imprecisão · 🟡 forma

Para localizar cada ponto no Paper indico a secção e uma frase próxima, porque a pesquisa do Paper não encontra texto dentro de fórmulas.

---

# Capítulo 2: Programação com Restrições

## Correto (verificado)
- Codificações LIA das *gates* (tabela em "Codificação da semântica dos operadores booleanos em LIA"): `neg`, `xor`, `or`, `nand`, `and`, `maj_k` estão todas certas, incluindo `or = maj_0`, `and = maj_{n−1}`.
- Formulações de incidência: *point/set packing*, *cover* e *partition*; problema de sensibilidade a erros (`x = e ⊕ z`, `Σe ≤ t`).
- Exemplo do TSP: na figura, os ramos são 0 a–b, 1 b–c, 2 c–f, 3 e–f, 4 a–e, 5 a–d, 6 b–d, 7 b–f.
  - `H = {1,…,6}` é o único ciclo hamiltoniano.
  - Os ramos 0 e 7 nunca entram num ciclo hamiltoniano, porque `c`, `d`, `e` têm grau 2.
  - `δ(a)`, `δ(b)` e `δ(A) = {1,4,7}` estão certos.
- Programação inteira disjuntiva: a construção com cópias `(x^(k), y^(k))` e `Σ y^(k) = 1` está correta. A convexidade fraca é exatamente o que força `x^(k) = 0` quando `y^(k) = 0`.
- Exemplo `2x₁ + x₂ ≤ 3` (suporte com 6 pontos) e a sua negação.
- k-centros: distância de Hamming `Σ xᵢ + yᵢ − 2xᵢyᵢ`; formulação da 2.ª abordagem (`Σ Aᵢ = k`, `Xᵢⱼ ≤ Aᵢ`, `Σ Xᵢⱼ Dᵢⱼ ≤ t`).

## 🔴 Erros de conteúdo

**C2-1. "PROP e LIA … ambas são decidíveis e finamente axiomatizáveis"** (Planeamento).
- A LIA (aritmética de Presburger) é decidível mas **não** é finitamente axiomatizável: precisa de um esquema de indução.
- Sugestão: "decidíveis e recursivamente axiomatizáveis", ou retirar "finitamente". ("finamente" é também gralha.)

**C2-2. "nos inteiros não é possível construir um circuito aritmético finito que … decida se [x, y] são ou não distintos"** (alldifferent).
- Na LIA, `x ≠ y ≡ (x < y) ∨ (x > y)`, que é trivialmente decidível.
- O problema real é outro: em **PI/PL** (só conjunções de inequações lineares) `x ≠ y` não é exprimível sem uma variável binária auxiliar e limites nos domínios (*big-M*): `x − y ≥ 1 − M·b`, `y − x ≥ 1 − M·(1−b)`.
- Isto também explica a frase seguinte ("é necessário incluir outro tipo de restrições nos domínios").

**C2-3. Convexidade de funções e restrições lineares** (Problemas de Alocação Linear; repetido em "propriedades de animação … relações côncavas" e no resumo do exemplo).
- "A função `φ_c` é positiva (ou convexa) se todos os `cᵢ` são positivos": **toda** a função linear é convexa (e côncava), seja qual for o sinal dos coeficientes. Coeficientes positivos dão uma função *monótona crescente*, não convexa.
- "Obrigação `φ_c(x) > c_n` … dizem-se côncavas porque o seu domínio é o complemento de uma região convexa": `{x | φ(x) ≥ c}` é um semiespaço, logo **convexo**; o complemento de um semiespaço é outro semiespaço.
- Toda a restrição linear define uma região convexa; a distinção limitação/obrigação é sobre o *sentido* da desigualdade (região que contém a origem ou não), não sobre convexidade.
- Em LP/PI usa-se `≥`, não `>`.
- Sugestão: trocar "convexa/côncava" por, por exemplo, "limitação (região limitada que contém a origem)" / "obrigação (região que exclui a origem)".

**C2-4. Programação inteira disjuntiva: "predicado convexo se todos os `cᵢ` forem não-negativos … suporte sempre finito e contém `0ⁿ`".**
- Com algum `cᵢ = 0` o suporte é infinito: por exemplo, `x₁ + 0·x₂ ≤ 3` deixa `x₂` livre.
- Com `c₀ < 0` o suporte é vazio, logo não contém `0ⁿ`.
- **Correção:** exigir `cᵢ > 0` (estritamente) e `c₀ ≥ 0`. É o que o exemplo e a condição "linha com todos os elementos positivos" usam.
- O mesmo se aplica a "um predicado côncavo tem sempre suporte infinito e não contém `0ⁿ`".

**C2-5. "O suporte de uma fórmula fracamente convexa é finito e, ou é vazio ou então contém `0ⁿ`."**
- Falso. Contra-exemplo: `(x₁ + x₂ ≤ 3) ∧ (x₁ + x₂ ≥ 1)`. É fracamente convexa, e o suporte é não-vazio, finito e não contém `(0,0)`.
- Só vale se **todos** os predicados forem convexos.
- A construção disjuntiva só usa a finitude e o facto de `C x ≤ 0` forçar `x = 0`, e isso continua certo.

**C2-6. Problema do "Corte máximo".**
- A restrição `Σᵢ A_{ij} Xᵢ < m` para todo `j` não diz que o caminho `j` fica intacto. Diz apenas que `X` não contém **todos** os ramos do caminho (e `m` é o número total de ramos, não o comprimento do caminho).
- Além disso, o enunciado pede que **exista** um caminho não cortado (disjunção), mas a fórmula impõe uma condição a **todos** os caminhos.
- A justificação "pelo menos para algum `i` se verifica `A_{ij}Xᵢ = 0`: isto é, o corte `X` não interfere no caminho `j`" é a confusão central: basta um ramo fora de `X` para a soma ser `< m`, mas o caminho pode estar cortado.
- **Formulação correta:** variáveis binárias `u_j` com `Σ_j u_j ≥ 1` e `Σᵢ A_{ij} Xᵢ ≤ |S_j|·(1 − u_j)` (o caminho `j` com `u_j = 1` não tem ramos em `X`).
- O ótimo é trivial: `X =` todos os ramos menos os de um caminho `s ⇝ t` mais curto. Vale a pena dizê-lo.
- "Corte máximo" (*max-cut*) é, na literatura, um problema diferente: partição dos nodos que maximiza os ramos que a atravessam. Convém mudar o nome ou avisar.

**C2-7. Restrição de eliminação de subciclos do TSP: "para todo o subgrafo próprio `A ⊂ 𝒢`".**
- Tal como está, inclui o subgrafo vazio: `δ(∅) = ∅`, logo `0 ≥ 2`, e o problema fica inviável.
- Inclui também o subgrafo com **todos** os nodos e todos os ramos menos um, `e`. Então `δ(A) = {e}` e a restrição obriga `e ∈ H`. Aplicado a cada ramo, obriga `H = 𝓔`, o que contradiz grau 2.
- **Correção:** quantificar sobre os subconjuntos de **nodos** `S`, com `∅ ≠ S ⊊ 𝒱`, e `δ(S)` = ramos com exatamente um extremo em `S`.
- O parágrafo seguinte já fala em "subconjuntos próprios dos nodos", e o exemplo usa um subgrafo induzido, onde a definição dá o resultado certo.

## 🟠 Inconsistências / imprecisões
- **CP indecidível** (Planeamento): "os problemas CP exigem extensões da LIA que não são decidíveis". Em domínios finitos, como no CP-SAT, os problemas CP são decidíveis (NP). A indecidibilidade só surge com aritmética não-linear sobre inteiros não limitados.
- **Classificação dos problemas:** "critério LIA … em caso contrário não-linear. Quando o problema é discreto designa-se por CP" contradiz o parágrafo anterior, onde um problema discreto linear é **PI**.
- **Domínios:** "Se alguma das variáveis tem domínio nos reais … só é resolúvel com MIP". Se **todas** são reais, é PL. MIP é quando há inteiras e reais.
- **`onlyIf` / `onlyIfNot`:** no OR-Tools (CP-SAT) o método é `OnlyEnforceIf(b)`. A negação faz-se com `OnlyEnforceIf(b.Not())` (ou `~b`); não existe `onlyIfNot`. Se os nomes forem notação própria, convém dizê-lo.
- **Set packing:** "não intersecta qualquer `ŵᵢ` em **não mais** de um `S_j`" diz o contrário do pretendido; deve ser "em mais do que um". A frase seguinte ("todo `wᵢ` está contido em quanto muito um `S_j ∈ Y`") está certa.
- **Gates com falhas:** "probabilidade de falha … para todas as gates **or**". As gates do modelo são `xor`, `and` e `maj`, logo deve ser `xor`. E "se ambos os argumentos são **positivos**" deve ser "se nenhum argumento é falha (≥ 0)".
- **Ordem topológica** `i₀ > i₁ > … > iₙ`: os inputs são um conjunto; basta `i₀ > i_k` para todo `k`.
- **k-centros:**
  - `X_{i,j} = 1` sse `aᵢ` é o centro **mais próximo**, mas as restrições só impõem que `e_j` está atribuído a um centro a distância `≤ t`. Para o problema não faz diferença, mas a interpretação "mais próximo" não é imposta.
  - "Infelizmente este tipo de problema [quadrático] não é suportado por nenhum dos solvers usados neste curso." O SCIP suporta restrições quadráticas (MINLP). Além disso, cada produto de binárias `X·A` lineariza-se exatamente (`w ≤ X`, `w ≤ A`, `w ≥ X + A − 1`), o que torna a 1.ª abordagem também PI linear.
  - Afirma-se que minimizar `K` "não permitiria formalizar este problema como programação inteira", mas na 2.ª abordagem faz-se isso mesmo (`Σ Aᵢ = k` com `k` variável). Convém explicar a diferença.
  - Notação: `n` (bits) vs `N` (número de centros potenciais) vs `M × N` na matriz `E`; `k` vs `K`.
- **Métrica:** "valor real positivo" deve ser "não-negativo" (`d(x,x) = 0`). Também "inteiros positivos ℕ", "`ℕ₊`" e "valores positivos" onde se quer `≥ 0`.
- **Fórmula de alldifferent:** `⋀_{x∈S} ⋀_{y<x} x ≠ y` mistura a ordem dos índices com a ordem dos valores. Escrever `⋀_{i<j} x_i ≠ x_j`.
- **"propriedades de animação":** o termo habitual em português é "vivacidade" (*liveness*).

## 🟡 Forma (gralhas)
- **Planeamento:**
  - "diz-se se linear", "Programmig", "cumprindo + restrições", "finamente axiomatisáveis".
  - "satisfabilidade", "estudamos" → "estudámos".
  - "alguma instâncias do problemas", "suporte distintos", "lineares.Tem".
  - "nivéis", "possoa", "satifazem", "planeamente".
  - "optimabilidade" (várias vezes; "otimalidade"), "optimabiliade".
- **alldifferent:** "algoritmo mais eficientes".
- **Alocação:**
  - fórmula vazia `\mathbf{}` antes de `t_j`;
  - "um operador só pode ser alocada", "no conjuntos de variáveis", "rendimentos diferente";
  - "objetivos" vs "compromissos"; "num salas".
- **Incidência:**
  - "empacotamente" (2×), "são também designado", "memo modo";
  - `{S ⊆ W) | w ∈ S}` com `)` a mais; "para todos `x ∈ W`" (deve ser `w`); "do vetores".
- **Circuitos:**
  - "modelas", "para os quais" → "as quais", "todas as restantes operadores … são binárias";
  - "conectivas boleadas", "ums restrição", "wire utput";
  - fórmula vazia `\mathbf{}` antes de `neg`.
- **Grafos:**
  - "eleticidade", "gaz", "cada um fica associada", "linke-as-edge";
  - legenda "Rede ferroviária" num exemplo de metropolitano;
  - "Um segundo exemplo de" (frase incompleta);
  - "o o", "i..e.", "conecção", "carcaterizar", "TSB", "satisfaza".
- **Programação inteira disjuntiva:** "models", "dos suporte", "um do", `x̄_(k)` (índice em baixo; deve ser `x̄^(k)`).
- **k-centros:**
  - "distânca", "satisfazíeis", "Com um problema" → "Como";
  - "e possível", "forcosamento", "dobre", "este quatro";
  - fórmula vazia `\mathcal{}`.

---

# Capítulo 2a: Programação Cónica

## Correto (verificado)
- **Forma LP:**
  - conversões (`≥`, `=`, max → min);
  - definição de cone convexo fechado;
  - representação de Gram e valores próprios.
- **Cones:**
  - SOC em ambas as formas (incluindo `√2 x₁ ≥ ‖x‖`, que é equivalente);
  - RSOC `2ab ≥ ‖z‖²`;
  - SDP ⊇ SOCP ⊇ LP;
  - power cone e o seu dual;
  - exponencial e o seu dual (coincidem com as definições do MOSEK).
- Equivalência `t ≥ ‖x‖ ⇔ [[t, xᵀ],[x, t·I]] ⪰ 0`; a fatorização `Y` com `t = 1` está certa.
- Reformulações com power cone (`p > 1`, `0 < p < 1`, `p < 0`).
- **Dualidade:**
  - par primal/dual (`−Aᵀz = c`, `z ∈ 𝒦*`);
  - dualidade fraca;
  - identidade `zᵀs = p* − d*`.
- **RPP:**
  - `f(z) = ½zᵀQz − Σ bᵢ log zᵢ` e a reformulação com o cone exponencial;
  - o código CVXPY: as contribuições de risco coincidem com `b` (erro ≈ 1e−5). Ver `cap2a_risk_parity.py`.
- **1.º problema do portfolio em Clarabel:** coincide com o CVXPY para `½xᵀQx − γμᵀx`. Ver `cap2a_portfolio_clarabel.py`.

## 🔴 Erros de conteúdo

**C2a-1. Código Clarabel do 2.º problema do portfolio (objetivo linear, restrições quadráticas): o problema construído é inviável.**
- As linhas de `A` estão na ordem `r | z (n) | s (n) | t`, mas os cones estão na ordem `Zero(1), Nonnegative(n), SOC(n+1)`. O Clarabel associa os cones às linhas pela ordem:
  - o cone não-negativo fica aplicado a `z = Gx` (em vez de `x`);
  - o SOC fica aplicado a `(s, t)` (em vez de `(t, z)`).
- Além disso, `zero_ = sp.csc_matrix([1.0]*n)` é um vetor de **uns**; deve ser de zeros.
- **Verificado** (`cap2a_portfolio_clarabel.py`): o código do texto dá `PrimalInfeasible`. O `call()` só apanha exceções, por isso não mostra nada.
- Com as linhas reordenadas (`r | s | t | z`), `zero_` a zeros e `−G` em vez de `G`, dá `Solved` com o mesmo ótimo que o CVXPY:
  ```python
  zero_ = sp.csc_matrix((1, n))
  A = sp.block_array([[[0], one_], [ZeroC(n), -id_], [[-1], zero_], [ZeroC(n), -G]]).tocsc()
  # cones inalterados: ZeroConeT(1), NonnegativeConeT(n), SecondOrderConeT(n+1)
  ```
- A matriz `A` por blocos no texto tem o mesmo problema de ordem, e ainda `+Id_n` onde deve ser `−Id_n` (a restrição é `−x + s = 0`).

**C2a-2. "`P ≡ ½Q`"** (portfolio em KKT, objetivo `xᵀQx − γμᵀx`). O objetivo KKT é `½xᵀPx`:
- para `xᵀQx` é preciso `P = 2Q`;
- para a formulação de Markowitz `½xᵀQx` é `P = Q`, que é o que o código faz (`P = QG(n)`).
- `½Q` não serve em nenhum dos casos.

**C2a-3. RPP: "normalizando as variáveis ao risco global `φ(x)²` … `zᵢ ≡ xᵢ/(xᵀQx)`".**
- Com esta normalização obtém-se `zᵢ(Qz)ᵢ = bᵢ/(xᵀQx)`, não `bᵢ`.
- A correta é `zᵢ ≡ xᵢ/φ(x) = xᵢ/√(xᵀQx)`.
- **Verificado** (`cap2a_risk_parity.py`): erro ≈ 0,1 com a versão do texto e ≈ 1e−5 com a correta.
- O resto do argumento (recuperar `x = z/Σz`) não muda.

**C2a-4. "os CCC's simétricos originam resoluções polinomiais enquanto que os não-simétricos dão origem a resoluções exponenciais ou sub-exponenciais"** (Considerações sobre o uso da CO).
- Os cones exponencial e de potência não são simétricos, mas são resolvidos em tempo polinomial por métodos de pontos interiores (MOSEK, Clarabel).
- O que é verdade: *existem* cones convexos fechados (por exemplo, o copositivo) para os quais a otimização é NP-difícil.
- A frase contradiz a secção seguinte, que recomenda esses cones.

**C2a-5. "Quando todos os cones são de 2ª ordem, o cone produto também é de 2ª ordem"** (e o mesmo para o semidefinido).
- Um produto de cones de Lorentz não é um cone de Lorentz.
- O que se mantém é a **classe** do problema: um produto de SOCs dá ainda um SOCP; um produto de cones PSD corresponde a uma matriz PSD diagonal por blocos.

**C2a-6. "SOCP (…) ou QP (quadratic programming)".**
- Não são sinónimos. A QP convexa (e a QCQP convexa) reduz-se a SOCP, mas a SOCP é mais geral.
- No Cap. 2, QP é "restrições lineares, objetivo quadrático".

## 🟠 Inconsistências / imprecisões
- **Siglas:** "programação cónica (CP)" choca com CP = *Constraint Programming* do Cap. 2. No texto aparecem ainda CO, PL/LP e SDP/SDPP.
- **Cone zero:** não tem dimensão completa, logo não satisfaz a condição (iv) dos CCC. Falta também a condição habitual de cone *pontiagudo* (*pointed*) na definição de cone próprio.
- **Homogeneidade:** "para todo o real `λ`" deve ser `λ > 0`. Para `λ < 0` e `κ` não inteiro, `λ^κ` nem está definido, e a norma não satisfaz a propriedade. No teorema de Euler aparece `k` em vez de `κ`.
- **Complexidade:** "existem cones … na classe NP" deve ser NP-**difícil**. Também "deixa de ser 𝒫 para ser 𝒩𝒫" (IP): NP não exclui P; dizer NP-difícil.
- **"R₊ⁿ é um produto de n cones de 2ª ordem de dimensão 0 casos"** deve ser "dimensão 1".
- **RSOC sem variáveis especiais:**
  - `x₁ > 0, x₂ > 0` estritos tornam o conjunto não fechado e diferente da definição com `ℝ₊²`; usar `≥`;
  - na equivalência SOC ↔ RSOC, a condição "`a > b ≥ 0`" deve ser "`a, b ≥ 0`" (`a > b` equivale a `x₂ > 0`, que não é exigido);
  - aparece `\mathcal{R}^soc` em vez de `\mathcal{K}^soc`.
- **Cholesky:**
  - a definição de sdp diz `S = Lᵀ L` com `L` triangular inferior; a fatorização de Cholesky é `L Lᵀ` (ou `Gᵀ G` com `G` superior, como mais à frente). Mais à frente aparece ainda "`G` triangular inferior";
  - `numpy.linalg.cholesky` exige matriz **definida** positiva e falha para matrizes PSD singulares (covariâncias com dependências). Convém referir a alternativa: decomposição espectral, LDLᵀ, ou somar `εI`.
- **Prova com `Y`:**
  - conclui que `X` é "positiva definida", mas só se prova semidefinida;
  - só se prova o sentido `‖x‖ ≤ 1 ⇒ X ⪰ 0`;
  - aparece `Id_m` em vez de `Id_n`.
- **"modelo KKT":** KKT designa as *condições de otimalidade*. A forma `min ½xᵀPx + qᵀx s.t. Ax + s = b, s ∈ 𝒦` é a forma-padrão do Clarabel/SCS.
- **MOSEK:** "Mosek e Clarabel resolvem problemas exclusivamente no modelo KKT" não se aplica ao MOSEK, cuja forma nativa é diferente (`x ∈ 𝒦` sobre variáveis, ou restrições cónicas afins) e cujo interface cónico não recebe `P`.
- **Portfolio:**
  - "esta descrição não está correta porque `γ` é um parâmetro": `γ ≥ ‖Gx‖` com `γ` constante é uma restrição cónica válida, `(γ, Gx) ∈ SOC`. A variável `t` é cómoda, mas não é obrigatória;
  - o 2.º problema minimiza `xᵀQx` (variância) mas é reformulado como `min t` com `t ≥ ‖Gx‖` (desvio padrão). O ótimo `x` é o mesmo, mas o valor ótimo não; o mesmo vale para a substituição de `xᵀQx` por `t ≥ √(xᵀQx)` na secção de técnicas;
  - em `(x, t, y) ∈ 𝒦 × 𝒦^soc` deve ser `(x, t, z)`;
  - `h(x) = g − λf` põe `λ` no retorno; em KKT põe-se `λ` (ou `γ`) no risco. Uniformizar.
- **KKT do portfolio:**
  - o cone indicado é só `ℝ₊ⁿ`, mas a igualdade `1ᵀx = 1` precisa do cone zero (o código usa `ZeroConeT(1)` corretamente);
  - "`uᵢ ≥ 0`" deve ser `sᵢ`;
  - "`r ∈ 𝟎_n`" deve ser `𝟎₁`;
  - "duas variáveis slack `t, s` e `z`" (são três), e depois "`υ, y`" e "`r, z, s, t`": nomes inconsistentes.
- **Dualidade:**
  - "cone dual … também designado por cone polar": o polar é `𝒦° = −𝒦*`;
  - "`(𝒦*)* = 𝒦`, pela definição é imediato": exige 𝒦 fechado e convexo (teorema bipolar);
  - "`(d*, y*)`" e "certificado `y*`" devem ser `z*`.
- **Problema combinado 𝒞:** com a restrição `cᵀx + bᵀz = 0`, a identidade `zᵀs = p* − d*` dá `sᵀz = 0` em todo o conjunto viável. O objetivo é constante, por isso o problema é de viabilidade, não de otimização quadrática.
- **RPP:**
  - "`Σ xᵢ φ'ᵢ(x) = 1` para qualquer função de risco" só vale para `ℛ` homogénea de grau 2 (Euler); deve dizê-lo;
  - nota sobre ínfimos: "se `f` é … não-negativa, os zeros de `f` são os ínfimos" não se aplica, porque esta `f` não é não-negativa. O argumento certo é: `f` é convexa em `z > 0`, logo o mínimo é o ponto onde o gradiente se anula, `zᵢ(Qz)ᵢ = bᵢ`;
  - a restrição `(zᵢ, 1, tᵢ) ∈ 𝒦^exp` dá `tᵢ ≤ log zᵢ`, não `=`; a igualdade obtém-se no ótimo porque `b > 0`. Vale a pena dizê-lo.
- **Power cone:** "com `p` um inteiro" mas os casos seguintes usam `0 < p < 1` e `p < 0`. Com `0 < p < 1`, `(x,1,z) ∈ 𝒦^pow_p` dá `|z| ≤ x^p`, mais forte que `z ≤ x^p` (só é equivalente se `z ≥ 0`).
- **Código:**
  - `clarabel.verbose = False` não tem efeito; deve ser `settings.verbose = False`;
  - `solver.solve()` não lança exceção quando o problema é inviável; deve testar-se `solution.status`;
  - o ciclo `while True: … psd_wrap(Q.T @ Q); if Q.is_psd(): break` é desnecessário, porque `QᵀQ` é sempre PSD e `psd_wrap` não verifica nada;
  - no RPP, o comentário de `t` ("sensibilidade relativa do investimento ao risco") está errado: `t = log z`.

## 🟡 Forma (gralhas)
- **Introdução:** "programção", "variáveis inteira".
- **Cones:**
  - "semi-definitiva/semi-definitivo positivo" deve ser "semidefinida/semidefinido" (várias vezes);
  - "construido", "caracterítico", "variávieis", "cones de ocorrem";
  - fórmulas vazias `\mathbb{}` e `\mathcal{}`;
  - "norma euclidiana em `ℝⁿ`" (é `ℝⁿ⁻¹`).
- **KKT:** "reescreva-se" (várias vezes; "reescreve-se"), "deriva" → "derivam", "que designam por", ".No" e ".Infelizmente" sem espaço, "distintas" → "distintos".
- **Portfolio:** "com foi apresentado", "valores reais positivos" (`≥ 0`), "ignorar-lo", "slack$" (cifrão a mais), "matrix".
- **Dualidade:** "Os cone", "presupõem", "afim de" → "a fim de", "é representado" → "representada".
- **RPP:** "juntando em power cone", "volatilbilidade", "volatibilidade", "media" → "medida", "RRP" → "RPP", "as as variáveis", "controlara", "infímo".

---

## Notebooks Marimo
- `cap2a_portfolio_clarabel.py`: 1.º e 2.º problemas do portfolio em Clarabel (código do texto, versão corrigida e referência CVXPY), com `n`, `γ` e semente ajustáveis.
- `cap2a_risk_parity.py`: exemplo RPP do texto e verificação da normalização `z`.

Dependências: `marimo`, `numpy`, `scipy`, `clarabel`, `cvxpy`.
