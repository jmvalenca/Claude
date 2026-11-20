# Análise: Capítulo 2a (Programação Cónica)

**Data:** 2026-11-20.
**Documento:** *Capítulo 2a: Programação Cónica* (Paper, `/Paper docs/`, revisão 48232, última edição a 2026-11-19).
**Ponto de partida:** `Validacao-Cap2-e-Cap2a-2026-11-19.md`. Os identificadores `C2a-n` referem-se a esse relatório.

**Método:**
- Histórico do Paper desde 2026-11-18 (uma sessão de edição, só do autor).
- Texto e LaTeX extraídos da página no Chrome. A secção RPP foi verificada por captura de ecrã.
- Código Clarabel do 2.º problema do portfolio, tal como está hoje, executado e comparado com o CVXPY (clarabel 0.11, cvxpy 1.9, `n = 200`).
- Teste do vetor triangular do cone PSD do Clarabel (`PSDTriangleConeT`).

**Legenda:** ✅ corrigido · 🔴 erro de conteúdo · 🟠 inconsistência / imprecisão · 🟡 forma · 🆕 ponto novo (não estava no relatório de 19/11)

---

## 1. Resumo

- A edição de 19/11 corrigiu o erro mais grave: o código Clarabel do 2.º problema do portfolio dava `PrimalInfeasible`. Agora dá `Solved`, com o mesmo ótimo que o CVXPY (diferença no objetivo ≈ 5e−10).
- Os outros cinco erros de conteúdo do relatório anterior (C2a-2 a C2a-6) continuam por corrigir. O mesmo vale para quase todas as imprecisões e gralhas.
- A correção do código deixou o **texto** à volta desatualizado: a ordem das variáveis slack e o vetor `b` por blocos já não batem com a matriz `A` (ver 3.1).
- Pontos novos: a dualidade forte é apresentada sem a condição de Slater; o cone PSD é definido mas não tem exemplo; e a vetorização `⌈S⌉` do texto não é a que o Clarabel usa.

## 2. Corrigido desde 19/11 ✅

- **C2a-1 (código do 2.º problema):** linhas de `A` reordenadas para `r | s | t | z`, `zero_` a zeros, `−G` em vez de `G`. A matriz `A` por blocos no texto também foi corrigida (`−Id_n`, ordem certa).
  - **Verificado:** `Solved`, objetivo −0,741738263 (Clarabel) vs −0,741738263 (CVXPY).
- **`settings.verbose = False`** em vez de `clarabel.verbose`.
- **"slack$"** (cifrão a mais).

## 3. Por corrigir

### 3.1 Introduzido pela correção do código 🆕🟠
- **Ordem das slacks:** o texto diz `s′ ≡ (r, z, s, t)`, mas a matriz `A` e os cones estão agora na ordem `(r, s, t, z)`. Deve ser `s′ ≡ (r, s, t, z)`.
- **Vetor `b` por blocos:** aparece `(1, 0_n, 0_n, 0)`. Com a nova ordem deve ser `(1, 0_n, 0, 0_n)`. Como é tudo zero, o resultado numérico não muda, mas os tamanhos dos blocos ficam trocados.
- **Comentário no código:** a linha `# cones inalterados: ZeroConeT(1), …` foi copiada do relatório e repete a linha `cones = …` logo a seguir. Pode sair.

### 3.2 Erros de conteúdo 🔴 (todos do relatório anterior)
| Id | Onde | Problema | Correção |
| --- | --- | --- | --- |
| C2a-2 | Portfolio em KKT | `P ≡ ½Q` | `P = 2Q` para `xᵀQx`, ou `P = Q` para `½xᵀQx` (o código usa `P = Q`) |
| C2a-3 | RPP | `zᵢ ≡ xᵢ/(xᵀQx)` não dá `zᵢ(Qz)ᵢ = bᵢ` | `zᵢ ≡ xᵢ/√(xᵀQx)` (verificado em `cap2a_risk_parity.py`) |
| C2a-4 | Considerações sobre o uso da CO | Cones não simétricos "dão resoluções exponenciais" | Exponencial e potência resolvem-se em tempo polinomial; NP-difíceis são casos como o cone copositivo |
| C2a-5 | Cone produto | "produto de SOCs é de 2ª ordem" | O produto não é um cone de Lorentz; o *problema* continua a ser SOCP |
| C2a-6 | SOC | "SOCP ou QP" | Não são sinónimos; QP convexa ⊂ SOCP |

### 3.3 Imprecisões 🟠 ainda presentes
Confirmei no texto atual que continuam lá todas as imprecisões listadas a 19/11. Destaco as que mais afetam a leitura:
- **Homogeneidade:** "para todo o real `λ`" (deve ser `λ > 0`); `1/k` em vez de `1/κ` no teorema de Euler.
- **Complexidade:** "na classe NP" e "deixa de ser P para ser NP" (deve ser NP-difícil).
- **Cholesky:** `S ≡ Lᵀ L` com `L` triangular inferior; mais à frente "`G` triangular inferior". Falta avisar que `numpy.linalg.cholesky` falha para matrizes PSD singulares.
- **Prova com `Y`:** conclui "positiva definida"; `Id_m` em vez de `Id_n`; só prova um sentido.
- **RSOC:** `x₁ > 0, x₂ > 0` estritos; "`a > b ≥ 0`"; `\mathcal{R}^soc` em vez de `\mathcal{K}^soc`.
- **Portfolio:**
  - "`γ` é um parâmetro e não deve ser tratado como variável" (a restrição `(γ, Gx) ∈ SOC` é válida);
  - `(x, t, y)` em vez de `(x, t, z)`;
  - `u_i ≥ 0` em vez de `s_i`; `r ∈ 0_n` em vez de `0_1`;
  - cone do 1.º KKT indicado só como `ℝ₊ⁿ` (falta o cone zero da igualdade).
- 🆕 **Papel duplo de `t`:** "introduz-se uma nova variável de decisão `t` e variáveis slack `r, s, t, z`". A variável de decisão é `σ`, como diz o parágrafo anterior.
- **Dualidade:** "cone polar" (o polar é `−𝒦*`); "`(𝒦*)* = 𝒦` é imediato" (exige 𝒦 fechado e convexo); `y*` em vez de `z*` (duas vezes).
- **Problema combinado 𝒞:** com `cᵀx + bᵀz = 0` o objetivo `sᵀz` é identicamente zero; é um problema de viabilidade, não de otimização quadrática.
- **RPP:** a nota sobre ínfimos assume `f ≥ 0`, o que não se aplica a `½zᵀQz − Σ bᵢ log zᵢ`; `(zᵢ, 1, tᵢ) ∈ 𝒦^exp` dá `tᵢ ≤ log zᵢ`, com igualdade só no ótimo.
- **Power cone:** "com `p` um inteiro", mas os casos usam `0 < p < 1` e `p < 0`.
- **Código:** `call()` usa `try/except`, mas `solve()` não lança exceção quando o problema é inviável (**verificado:** devolve `status = PrimalInfeasible` sem exceção). Testar `solution.status`. O ciclo `while True … is_psd()` continua desnecessário.

### 3.4 Gralhas 🟡
Continuam todas as do relatório anterior (por exemplo, "programção", "semi-definitivo", "caracterítico", "variávieis", "reescreva-se", "presupõem", "afim de", "RRP", "volatilbilidade", "controlara", "infímo", "ignorar-lo", "matrix", "com foi apresentado"). A lista completa está em `Validacao-Cap2-e-Cap2a-2026-11-19.md`.

## 4. Pontos novos 🆕

**N1. Dualidade forte sem condição de Slater** 🟠 (secção "2º resultado: teorema da dualidade forte").
- Tal como está, o "teorema" (`d* = p*` sse `(s*)ᵀz* = 0`) é só uma consequência da identidade `zᵀs = p* − d*` provada logo abaixo, e assume que os ótimos são atingidos.
- O resultado que interessa ao leitor é outro: em CO, ao contrário da LP, pode haver *duality gap* positivo ou ótimo não atingido. Basta, por exemplo, que o primal seja **estritamente** viável (existe `x` com `b − Ax ∈ int 𝒦`) e limitado para ter `d* = p*` com ótimo dual atingido.
- Sugestão: enunciar a condição de Slater e dar um exemplo curto de *gap* ou de não-atingimento, por exemplo com um SOC ou um SDP 2×2.

**N2. Vetorização das matrizes simétricas vs Clarabel** 🟠 (Notação e Terminologia).
- O texto define `⌈S⌉` como o triângulo superior lido por linhas, sem escala. O `PSDTriangleConeT` do Clarabel usa o triângulo superior **por colunas**, com os elementos fora da diagonal multiplicados por `√2` (para que `⌈X⌉ᵀ⌈Y⌉ = tr(XY)`).
- **Verificado:** com `s = (1, b, 1) ∈ PSDTriangleConeT(2)`, o máximo de `b` é `√2 ≈ 1,41421`, não 1.
- Sugestão: uma frase a avisar, sobretudo se houver exercícios SDP em Clarabel.

**N3. Cone PSD sem exemplo** 🟠. É definido e usado para mostrar que SDP ⊇ SOCP, mas não há nenhum problema SDP nem código. Um exemplo curto (por exemplo, a matriz de correlação mais próxima, ou o valor próprio máximo como SDP) completaria a hierarquia LP ⊂ SOCP ⊂ SDP.

**N4. Dimensão do SOC** 🟡. "`t ≥ ‖x‖`, que caracteriza um SOC de dimensão `n`": com `x ∈ ℝⁿ`, o cone `(t, x)` tem dimensão `n + 1` (como, aliás, a matriz de ordem `n + 1` logo a seguir).

**N5. Três formulações do portfolio com notação diferente** 🟠.
- Problemas 1 e 2: risco = desvio padrão `√(xᵀQx)`.
- Formulação de Markowitz e 1.º código: risco = variância `½xᵀQx`, peso `γ` no **retorno**.
- KKT com SOC e 2.º código: risco = desvio padrão, peso `λ` no **risco**, mas a variável do código chama-se `gamma`.
- Estratégia intermédia na secção anterior: `h = g − λf`, com `λ` no retorno.
- Sugestão: uma pequena tabela (problema · medida de risco · onde está o peso · nome do parâmetro) e usar o mesmo nome no código.

**N6. Aviso de depreciação no código** 🟡. `sp.triu(G)` com `G` um array NumPy dá `DeprecationWarning` no SciPy atual (vai passar a devolver *sparse array*). Usar `sp.triu(sp.csc_array(G))`, ou `np.triu` seguido de `sp.csc_matrix`.

**N7. Escala da LP** 🟡. "os melhores algoritmos de PL lidam facilmente com milhares de restrições e milhares de variáveis": hoje são rotina milhões. A afirmação está certa mas subestima.

**N8. Notação do fecho** 🟡. `Ω^ω` para o fecho de `Ω` não é habitual; `cl Ω` ou `Ω̄` evitam confusão com expoentes.

## 5. Estrutura e exposição

- **Duas apresentações do par primal/dual.** O par `(P, D)` é definido em "Dualidade em CO" e repetido em "Dualidade em `𝒦^pow` e `𝒦^exp`". Podia remeter para a primeira e só acrescentar os cones duais.
- **Forma "por defeito" vs KKT.** O texto introduz `inf {cᵀx | Ax ≤ b, x ∈ 𝒦}`, mas a dualidade e o código usam `Ax + s = b, s ∈ 𝒦`. Vale a pena mostrar explicitamente a passagem de uma forma para a outra (o cone passa das variáveis para as slacks), porque é aí que surgem os erros de ordem de linhas/cones como o de C2a-1.
- **Regra prática para o Clarabel.** O erro C2a-1 vinha de a ordem das linhas de `A` não coincidir com a ordem dos cones. Uma regra explícita no texto ("as linhas de `A` e `b` são consumidas pelos cones na ordem da lista `cones`") evitaria o mesmo erro nos exercícios dos alunos.
- **Secção "Considerações sobre o uso da CO".** Junta três coisas diferentes: complexidade (com o erro C2a-4), catálogo de cones (potência, exponencial) e uma aplicação (RPP). Separar "Outros cones" de "Aplicação: RPP" tornaria o índice mais claro.
- **Exercícios.** O capítulo não tem exercícios propostos. Os notebooks `cap2a_portfolio_clarabel.py` e `cap2a_risk_parity.py` já servem de base para alguns (variar `γ`, comparar variância vs desvio padrão, traçar a fronteira eficiente).

## 6. Prioridades sugeridas

1. C2a-2 (`P ≡ ½Q`) e C2a-3 (normalização do RPP): erros de fórmula que um aluno reproduz.
2. Acertar `s′` e `b` com a nova ordem do código (3.1).
3. C2a-4 e C2a-5: afirmações gerais erradas que contradizem o resto do capítulo.
4. N1 (Slater) e N2 (vetorização para o Clarabel).
5. Uniformizar a notação do portfolio (N5) e corrigir as gralhas.
