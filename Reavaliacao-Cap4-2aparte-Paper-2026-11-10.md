# Reavaliação (3) — Capítulo 4: Verificação de Modelos baseada em SAT (2ª parte)

Documento analisado: Dropbox Paper `/Migrated Paper docs/Lógica Computacional/Capítulo 4_ Verificação de Modelos baseada em SAT (2ª parte).paper`, revisão 42926. Li o texto completo, com as 631 fórmulas LaTeX.
Reavaliação anterior: `Reavaliacao-Cap4-2aparte-Paper-2026-11-08.md`, revisão 39269.
Data: 2026-11-10.

Legenda: 🔴 erro de conteúdo · 🟠 inconsistência / imprecisão · 🟡 gralha / forma · ✅ corrigido

---

## Resumo

- O erro de conteúdo da versão anterior (a iteração que parava logo no início) **está corrigido**. A iteração parte agora de `do_0 ≡ True`, a sequência é decrescente e o algoritmo calcula o maior ponto fixo.
- Também foram corrigidos estes pontos: a referência "(a)" no PDR, a condição repetida, e o argumento em `sp_{havoc(a,b)}(I)`.
- **Conteúdo novo:** uma secção **Notação** e a secção **Verificação da correção usando CHC's**. Verifiquei as quatro codificações CHC (os juízos-base e as versões orientadas às pré-condições e às pós-condições) e estão **todas corretas**.
- Não há erros de conteúdo novos. Ficam algumas imprecisões de exposição na secção CHC (6.1 e 6.2) e na Notação (1.1 e 1.2).

---

## 1. Notação (secção nova)

A secção está correta. Fixa `⊨ A` para "A é tautologia", `¬A ⊨ ⊥` para "¬A é insatisfazível", e `⇒`, `⟺`/"sse", `&` e `not` para as conectivas dos juízos.

🟠 **1.1 Quantificadores da meta-lógica.** A Notação diz que a quantificação nos juízos se escreve com `⋀` e `⋁`, mas o texto continua a usar `∀`/`∃` ao nível meta. Por exemplo:
- `x ⊨ wp(Q) se e só se ∀z·(x,z)∈T ⇒ z∈Q`;
- `∀y·(x,y)∉T`;
- `∀ n≥0, m≥0 · SAT(…) = ∅`.

Ao mesmo tempo, o `⋁a·X←a` da secção Havoc está escrito com o símbolo da meta-lógica, mas está dentro de uma fórmula da lógica objeto. Ou se uniformiza o texto com a convenção, ou se diz que `∀`/`∃` também são aceites ao nível meta quando não há ambiguidade.

🟠 **1.2 Sobrecarga de `⊤` e de `⊨`.**
- `⊤` aparece em `⊤ ⊨ A` (verdade) e em `Σ^⊤` (sistema dual).
- `⊨` tem dois sentidos: "x é modelo de P" em `x ⊨ P` e "é tautologia" em `⊨ A`. Isto é habitual, mas convém uma frase a dizê-lo.

🟡 Gralhas e forma:
- "A representação do juízo … é representado por" (repete a ideia);
- "num SMT" → "numa SMT" (o resto do texto diz "a SMT");
- "a conjunção é representado" → "representada";
- "Quantificação é descrito" → "descrita".

## 2. Transformadores de Predicados

✅ As definições de `wp`/`sp` foram reescritas na forma compacta `⊨ P → wp(Q) ⟺ ⊨ ∀Z·P ∧ T[X'/Z] → Q[X/Z]`. Estão corretas.
✅ A propriedade 4 escreve agora `⊨ pre(Q) → P ⟺ ⊨ Q → post(P)`. Está correta.

🟠 **2.1 Havoc parcial (por resolver).** A secção Havoc continua a tratar apenas o caso em que o havoc atinge todas as variáveis, ao passo que o exemplo usa `havoc(a,b)`.
🟡 "O **FOTS** `Σ` cria dois transformadores" deve ler-se "SFOTS".

## 3. Control Flow Automata

🟠 **3.1 (por resolver).** O texto diz que "um ramo com vários eventos é equivalente a vários ramos com um evento cada". Isto é uma escolha de semântica, e convém dizer explicitamente que é uma opção.

## 4. Exemplo — Multiplicação de inteiros com erros

✅ **4.1 (era 🔴):** a iteração faz agora `do_0 ≡ True`, produz uma sequência decrescente e pára quando `⊨ do_n → do_{n+1}`. Isto calcula o **maior ponto fixo**, como o texto agora diz, e é coerente com a "correção parcial".
✅ 4.2: `sp_{havoc(a,b)}(I)` tem agora o argumento.
✅ O 2º problema diz agora corretamente que basta `b ≥ 0` para a terminação, e explica porque se inclui `a ≥ 0`.

🟡 "nececessária" → "necessária"; "parcialmente correcto que não é correcto" → "correto", como no resto do texto.
🟡 A condição de segurança e a equação de `system` ainda usam a guarda sem `a ≥ 0 ∧ b ≥ 0`. É coerente com o texto (a correção só é proposta no fim), mas pode valer a pena reescrever `system` com a guarda nova.

## 5. CFA's e Transformadores de Predicados

🟡 **5.1 (por resolver).** Na representação por pós-condições, o item 1 ainda diz "`a ∈ 𝒱`". Deve ler-se `a ∈ 𝒩`.
🟠 **5.2 (por resolver).** `𝒫` continua a designar o conjunto dos predicados unários (secção 2) e o vetor `{P_a}`. O CFA é descrito como "multigrafo" na secção CFA e como "grafo orientado" aqui.

## 6. Verificação da correção usando CHC's (secção nova)

Verificação do conteúdo:
- **Juízos 1–3** (`T_a ∧ P_a → Q_a'`, `Q_a ∧ sw_{a,b} → P_b`, `True → P_system`): corretos.
- **Orientada às pré-condições:** `⊨ T_a(X,X') ∧ sw_{a,b}(X') ∧ P_a(X) → P_b(X')` obtém-se de 1 e 2 eliminando `Q_a`. Está correta. Os juízos terminais `¬φ ∧ P_stop → False` e `P_error → False` também estão corretos.
- **Orientada às pós-condições:** `⊨ T_b(X,X') ∧ sw_{a,b}(X) ∧ Q_a(X) → Q_b(X')`, `⊨ T_system → Q_system'`, `¬φ ∧ Q_stop → False` e `Q_error → False`. Estão todas corretas. A guarda aparece em `X'` numa versão e em `X` na outra, e isso está certo.

🟠 **6.1 Pós-condição dos locais terminais.** O texto diz que em `stop` e `error` "não existe realmente pós-condição, o que é equivalente a afirmar que a pós-condição é `False`". Isto só é verdade para `error`. Para `stop`, a restrição é `Q_stop → φ`, e o próprio texto escreve logo a seguir `⊨ Q_stop → φ(X)`. O parágrafo seguinte diz que, em `stop`, "a transição para a pós-condição `False` só ocorre quando `φ` não é satisfeita", mas a fórmula que se segue é `P_stop → Q_stop`, que é igual à de `error`. A explicação e a fórmula não batem certo. Sugestão:
- dizer que `T_stop` e `T_error` são a identidade, o que dá `P → Q` (juízo do tipo 1);
- dizer que os juízos terminais são `Q_error → False` (o erro é inalcançável) e `Q_stop → φ` (a especificação vale à saída).

🟠 **6.2 Terminologia "pré-/pós-condições".** Na secção anterior, a representação "orientada às pré-condições mais fracas" usa os **`Q_a`** como incógnitas e a "orientada às pós-condições mais fortes" usa os **`P_a`**. Nesta secção, "orientada às pré-condições" usa os **`P_a`** e "orientada às pós-condições" usa os **`Q_a`**. Ou seja, os nomes trocam de papel entre as duas secções. Convém dizê-lo, ou escolher nomes que não colidam: por exemplo, "eliminação das pós-condições" e "eliminação das pré-condições".

🟠 **6.3 Ligação à correção parcial.** O texto diz que se procura "um modelo deste conjunto de CHC's". Vale a pena acrescentar que **existir** um modelo equivale a o CFA ser parcialmente correto e seguro. Também vale a pena acrescentar que o maior ponto fixo da secção do exemplo é um desses modelos.

🟡 Gralhas e forma:
- "A semântica do CFA é definido" → "definida";
- "incógitas" → "incógnitas";
- "pós-condiçoes" → "pós-condições";
- "usa-se apenas as pós-condições" → "usam-se";
- "O juízo que determinam" → "Os juízos que determinam";
- "pré e pós condições nestes dois locais têm" → "tem";
- "Esta é uma relação do tipo 2. considerando …" (pontuação; sugiro "Esta é uma relação do tipo 2: considerar a ausência de predecessores … é equivalente a …");
- `Q_stop`/`Q_error` aparecem às vezes sem `(X)`;
- o marcador "completar" continua no texto.

## 7. PDR

✅ **7.1:** as condições estão numeradas 1–4, a condição repetida foi removida e o texto refere-se agora à "propriedade (1.)".

🟠 **7.2 Resíduo de `R_k` (por resolver).** A query usa `R_{k-1}`, mas o texto à volta ainda fala de `R_k`:
- a definição em destaque continua com "para todo o estado acessível em `k` passos, `s ∈ R_k` … diz-se indutivo para `R_k`";
- o parágrafo seguinte diz "cubo `c` indutivo para `R_k` … bloqueado na frame `k`", embora use `s ∈ R_{k-1}`.

Deve ler-se `R_{k-1}` nos dois sítios.

🟠 **7.3 (por resolver):**
- o texto define `X = ⟨x_1,…,x_n⟩`, mas o exemplo usa `x_0,…,x_7`;
- `T` é descrita como uma "frame" (DNF), quando no PDR original é dada em CNF.

## 8. Código pysmt

O código não mudou em relação à versão testada a 2026-11-07, que deu **safe** para `r → bits = 0` e **bug no passo 15** para `bits ≠ 15`, com 212 bloqueios no total. As notas da avaliação anterior continuam por resolver:
- falta dizer que o código guarda `R_k` e o texto usa `F_k = ¬R_k`;
- o código não faz o teste `c ∧ I`;
- o código não volta a tentar `c` dentro de `recursive_block` (é o ciclo principal que o faz);
- `Or`, `Implies`, `is_sat` e `is_unsat` são importados e nunca usados;
- o link para o pysmt continua partido em três pedaços.

---

## Prioridades

1. 🟠 **6.1**: corrigir a explicação da pós-condição de `stop` na secção CHC.
2. 🟠 **7.2**: substituir `R_k` por `R_{k-1}` na definição em destaque e no parágrafo do bloqueio.
3. 🟠 **6.2**: harmonizar os nomes "orientada às pré-/pós-condições" entre a secção dos t.p. e a secção CHC.
4. 🟠 **1.1**: harmonizar o uso de `∀`/`∃` e de `⋀`/`⋁` com a nova secção de Notação.
