# Reavaliação — Capítulo 4: Verificação de Modelos baseada em SAT (2ª parte)

Documento analisado: Dropbox Paper `/Migrated Paper docs/Lógica Computacional/Capítulo 4_ Verificação de Modelos baseada em SAT (2ª parte).paper`, revisão 39269, modificada em 2026-11-08 21:02. Li o texto completo, com as 568 fórmulas LaTeX.
Validação anterior: `Capítulo_4_Verificação_de_Modelos_baseada_em_SAT.md`, versão de 2026-11-07.
Data da reavaliação: 2026-11-08.

Legenda: 🔴 erro de conteúdo · 🟠 inconsistência / imprecisão · 🟡 gralha / forma · ✅ corrigido

---

## Resumo

Os dois erros de conteúdo do PDR estão corrigidos:
- a query de bloqueio usa agora `R_{k-1}`;
- o teste de paragem é agora `k ≥ 1 ∧ F_{k-1} ↔ F_k`.

Também foram resolvidas várias das inconsistências:
- definição de invariante indutivo;
- forma de `system_n`;
- índices `succ`/`pred`;
- descrição de `Q_a`;
- guarda `a ≥ 0 ∧ b ≥ 0` na inicialização;
- notação `𝒩` para os nodos;
- a maior parte das gralhas.

A alteração ao critério de paragem da iteração no exemplo da multiplicação **introduziu um erro novo** (ver 3.1).

---

## 1. Transformadores de Predicados

✅ 1.1: a definição de invariante indutivo inclui agora `I → P`.
✅ As gralhas assinaladas foram corrigidas: "*inversa*", negrito em "em", "domínios finitos", itálicos e asteriscos soltos, e "determinística" em todo o texto.

🟠 **1.2 Havoc parcial (por resolver).** A secção Havoc continua a tratar apenas o caso em que o havoc atinge todas as variáveis, que é o único em que `wp`/`sp` dão fórmulas fechadas. O exemplo usa `havoc(a,b)`, que é parcial. Sugiro uma frase a cobrir esse caso: `wp(Q) ≡ ∀a,b·Q`, que continua a depender de `x, y, z`.

🟡 "O **FOTS** `Σ` cria dois transformadores" deve ler-se "SFOTS", como no resto da secção.

## 2. Control Flow Automata

🟠 **2.1 (por resolver).** O texto diz que "um ramo com vários eventos é equivalente a vários ramos com um evento cada". Isto é uma escolha de semântica (disjuntiva), não a única possível. Convém dizer explicitamente que se trata de uma opção.

## 3. Exemplo — Multiplicação de inteiros com erros

✅ 3.1 (anterior): `system_n` está agora na forma de implicação, `… → do_n`, coerente com `system`.
✅ 3.3: foi acrescentado o "2º problema" (o havoc gera inteiros negativos e então não há garantia de terminação), com a guarda corrigida `… ∧ a ≥ 0 ∧ b ≥ 0`.
✅ A notação `wp_even`/`wp_odd` está agora em minúsculas.

🔴 **3.1 Critério de paragem da iteração (erro novo).** A iteração parte de `do_0 ≡ False` e termina "se for possível construir `do_n` tal que `do_n → do_{n+1}` é tautologia". Como o operador é monótono e `do_0 ≡ False`, a sequência é crescente. Logo `do_n → do_{n+1}` é **sempre** tautologia: já com `n = 0` se tem `False → do_1`. O critério para à primeira iteração, com `do_0 ≡ False`, e o resultado não serve para nada. Há duas formas de corrigir:
- **(recomendada)** inicializar com `do_0 ≡ True`. A sequência passa a ser decrescente, `do_{n+1} → do_n` é automático e o critério `do_n → do_{n+1}` deteta o ponto fixo. Calcula-se assim o **maior** ponto fixo, que corresponde a **correção parcial**, exatamente o que o texto agora diz pretender ("se terminar, …");
- manter `do_0 ≡ False` e usar `do_{n+1} → do_n` como critério. Nesse caso calcula-se o **menor** ponto fixo, que corresponde a correção **total**, e as frases "parcialmente correto" e "se terminar" deixam de estar certas.

🟠 **3.2 `sp_{havoc(a,b)}` sem argumento.** A condição de segurança está escrita `sp_{havoc(a,b)} ∧ (x=a)∧(y=b)∧(z=0) → wp(do)`, mas falta o argumento: deve ser `sp_{havoc(a,b)}(I)`. O texto diz ainda que `sp(I)` "é determinado por este comando havoc seguido pela guarda", mas a fórmula `sp_{havoc(a,b)}(I) = True` inclui só o havoc. Convém alinhar as duas.

🟡 "parcialmente correcto que não é correcto": o resto do texto usa "correto".
🟡 Para a terminação basta `b ≥ 0`, porque é `y = b` que controla o ciclo. A condição `a ≥ 0` vem do enunciado ("inteiros positivos"). Não é um erro, mas pode valer a pena dizê-lo.

## 4. CFA's e Transformadores de Predicados

✅ 4.1: `Q_a` é agora descrito como "a pós-condição associada ao fluxo de informação do local `a`".
✅ 4.2: os índices passaram a `⋀_{b∈succ(a)}` e `⋁_{b∈pred(a)}`.
✅ 4.3 (em parte): os nodos passaram a `𝒩`, o que elimina a colisão com `𝒱` (variáveis).
✅ "(ou “switches”)", "Temos assim", "Uma abordagem" e "tal como no exemplo anterior" foram corrigidos.

🟡 **4.3a.** Na representação por pós-condições, o item 1 ainda diz "`a ∈ 𝒱`". Deve ler-se `a ∈ 𝒩`.
🟠 **4.3b (por resolver).** `𝒫` continua a designar o conjunto dos predicados unários (secção 1) e o vetor `{P_a}`. O CFA é descrito como "multigrafo" na secção CFA e como "grafo orientado" com ramos `(a,b)` nesta secção.
🟠 **4.4 (por resolver).** As condições `Q_stop ≡ φ` e `Q_error ≡ False` pressupõem que `wp_stop` e `wp_error` são a identidade. Se `error` fosse um estado de bloqueio, ter-se-ia `wp_error(·) ≡ True`.
🟡 O marcador "A completar" continua no texto.

## 5. PDR

✅ **5.1 (era 🔴):** a tautologia e a query de bloqueio usam agora `R_{k-1}`: `SAT{R_{k-1} ∧ T ∧ ¬c ∧ c'}`.
✅ **5.2 (era 🔴):** o passo 5 do pseudo-código testa agora `k ≥ 1` e `F_{k-1} ↔ F_k`.
✅ 5.6: a ordem `F_0 ⊇ F_1 ⊇ …` foi removida.
✅ "com um cubo que interseta `I`" e "`α ≡ {…}`" foram corrigidos.

🟠 **5.1a Resíduo de `R_k`.** A query está correta, mas o texto à volta ainda fala de `R_k`:
- a definição em destaque continua com "para todo o estado acessível em `k` passos, `s ∈ R_k` … diz-se indutivo para `R_k`";
- o parágrafo seguinte diz "o significado associado a um cubo `c` indutivo para `R_k` é o de estar bloqueado na frame `k`", embora depois use `s ∈ R_{k-1}`.

Para ficar coerente com a query, deve ler-se "indutivo para `R_{k-1}`" e "`s ∈ R_{k-1}`" nos dois sítios.

🟠 **5.3 Numeração e referência a "(a)".** As condições estão agora numeradas 1–5, mas o texto continua a referir "a propriedade **(a)**", que é agora a condição 2. Além disso, a condição 1 (`F_{k+1} → F_k`) repete parte da condição 4.

🟠 **5.4 (por resolver).** O texto define `X = ⟨x_1,…,x_n⟩`, mas o exemplo usa `x_0,…,x_7`.
🟠 **5.5 (por resolver).** O texto descreve `T` como uma "frame" (DNF). No PDR original `T` é dada em CNF.

## 6. Código pysmt

O código não mudou em relação à versão testada a 2026-11-07, que deu **safe** para `r → bits = 0` e **bug no passo 15** para `bits ≠ 15`, com 212 bloqueios no total.

🟠 6.1 (por resolver): continua por dizer que o código guarda `R_k` e o texto usa `F_k = ¬R_k`.
🟠 6.2 e 6.3 (por resolver):
- o código não faz o teste `c ∧ I` que o texto descreve;
- o código não volta a tentar `c` dentro de `recursive_block`; é o ciclo principal que o faz.

🟡 `Or`, `Implies`, `is_sat` e `is_unsat` são importados e nunca usados. O link "documentação do pysmt" continua partido em três pedaços.

---

## Prioridades

1. 🔴 **3.1**: mudar `do_0 ≡ False` para `do_0 ≡ True`, que é coerente com "parcialmente correto" e com o critério `do_n → do_{n+1}`.
2. 🟠 **5.1a**: substituir `R_k` por `R_{k-1}` na definição em destaque e no parágrafo do significado do bloqueio.
3. 🟠 **5.3**: substituir a referência "(a)" por "condição 2".
4. 🟠 **3.2**: escrever o argumento em `sp_{havoc(a,b)}(I)`.
