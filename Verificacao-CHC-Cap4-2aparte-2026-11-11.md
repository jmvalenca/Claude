# Verificação — secção "Verificação da correção usando CHC's" (Cap. 4, 2ª parte)

Documento: Dropbox Paper, `Capítulo 4_ Verificação de Modelos baseada em SAT (2ª parte).paper`, revisão 44626 (igual ao texto anexado a 2026-11-11). Li o texto com as fórmulas LaTeX.
Notebook de acompanhamento: `chc_multiplicacao.py` (marimo + z3/Spacer), na mesma pasta.
Data: 2026-11-11.

Legenda: 🔴 erro de conteúdo · 🟠 inconsistência / imprecisão · 🟡 gralha / forma · ✅ corrigido

---

## Resumo

- A parte **genérica** da secção CHC está correta. Agora também está bem explicada: a pós-condição de `stop` é `φ`, e o texto diz que existir modelo equivale a o CFA ser parcialmente correto e seguro.
- O **exemplo novo** da multiplicação tem **um erro de conteúdo**: a guarda de `(do,odd)`.
- O exemplo tem também uma conclusão em falta: com a definição de `overflow` dada, o sistema **não tem modelo**.
- Ambas as coisas foram confirmadas com z3 no notebook.

## 1. Notação e Havoc (alterações desde a revisão 42926)

✅ A Notação passou a aceitar `∀`/`∃` como quantificadores da meta-lógica "se não existir ambiguidade". Isto resolve a observação 1.1 da reavaliação anterior.
✅ O Havoc trata agora o caso **parcial** (`𝖷 = ⟨X,Y⟩`): `T ≡ (Y'=Y) ∧ ∃a·X'=a`, `wp(Q) ≡ ∀a·Q[X/a]`, `sp(P) ≡ ∃a·P[X/a]`. As fórmulas só são fechadas quando `Y = ∅`. Está correto (era a observação 2.1).

🟠 **1.1** "Essencialmente é equivalente a **`∀a·X ← a`**". Uma atribuição não-determinística é uma **escolha** entre todas as atribuições, ou seja, uma disjunção: `⋁a·X ← a` (era assim na versão anterior), ou `∃a`. O `∀` sugere todas as atribuições ao mesmo tempo.
🟡 **1.2** A mesma letra designa o vetor completo (`𝖷`, sans-serif) e uma das suas partes (`X`, itálico). Sugiro outro nome para a parte, por exemplo `U`.
🟡 A segunda fórmula fechada usa `P[𝖷/a]`; deve ser `P[X/a]`, como na primeira.

## 2. Secção CHC — parte genérica

✅ A pós-condição de `stop` passou a ser `φ`, e a de `error` passou a ser `False`. Os juízos `Q_error → False`, `Q_stop → φ`, `P_error → Q_error` e `P_stop → Q_stop` estão corretos (era a observação 6.1).
✅ O texto diz agora que a existência de modelo equivale a o CFA ser parcialmente correto e seguro (era a observação 6.3).
✅ As gralhas assinaladas foram corrigidas: "definida", "incógnitas", "pós-condições", "usam-se", "Os juízos".

🟠 **2.1 (por resolver).** Os nomes "orientada às pré-/pós-condições" designam o contrário do que designavam na secção dos transformadores de predicados (lá, a versão "pré" usa os `Q_a`; aqui usa os `P_a`).
🟡 Há várias formas de escrita a rever:
- "Esta é uma relação do tipo 2. :" → "do tipo 2:";
- "Temos dois juízos que caracterizam estas caracterizações" → "Estas convenções são expressas pelos juízos";
- "pré e pós condições nestes dois locais têm" → "tem";
- "aqui verifica-se os juízos" → "verificam-se".

## 3. Exemplo: correção parcial da "Multiplicação de inteiros com erros"

Verificação do conteúdo:
- **Transições:** `T_system` (havoc de `a,b`), `T_do = T_stop = T_error = id`, `T_even` e `T_odd` estão corretas. Ambas preservam `z + x·y = a·b`.
- **Guardas:** `sw_{system,do}`, `sw_{do,even}`, `sw_{*,do} = ¬overflow`, `sw_{*,error} = overflow` e `sw_{do,stop}` estão corretas.
- **Arestas:** a lista de 8 arestas está correta.
- **Pós-condição:** `φ ≡ z = a·b` está correta.

🔴 **3.1 Guarda de `(do,odd)`.** O texto define `sw_{do,odd} ≡ (X_y ≠ 0) ∧ even(X_y)`, igual a `sw_{do,even}`. Deve ser **`odd(X_y)`**. Assim como está:
- os dois ramos saem de `do` com a mesma guarda, e o ramo `odd` nunca é usado;
- com `y` ímpar, o controlo fica **bloqueado** em `do`.

O sistema CHC continua a ter modelo quando se restringem as entradas, mas apenas por vacuidade: as execuções com `y` ímpar nunca chegam a `stop`. No notebook, a opção "guarda tal como no texto" dá `sat`. Ou seja, o erro não é detetado pela verificação.

🟠 **3.2 Não existe modelo para o sistema tal como está.** Com `overflow ≡ (x > L) ∨ (z > L)` e o `havoc(a,b)` sem restrições, o local `error` é alcançável. O z3 devolve **unsat** nas duas abordagens, com o contra-exemplo `system → do → even → error`: com `L = 15`, `a = 8`, `b = 2`, obtém-se `x = 16 > L`. A conclusão do exemplo é então que o programa **não** é parcialmente correto e seguro, e convém o texto dizê-lo. Para obter um modelo é preciso uma pré-condição na guarda inicial, por exemplo `a ≥ 0 ∧ b ≥ 0 ∧ a·b ≤ L`. Com essa pré-condição, o z3 devolve **sat** nas duas abordagens, e o modelo de `do` implica o invariante `z + x·y = a·b`.

🟠 **3.3 `overflow` e valores negativos.** Se o `havoc` puder gerar valores negativos (a guarda `a ≥ 0 ∧ b ≥ 0` proposta no "2º problema" não está em `sw_{system,do}`), o `overflow` também deve testar `x < −L` e `z < −L`. Além disso, `a` e `b` têm de ser representáveis: `|a|, |b| ≤ L`.

🟠 **3.4 `T_{ℓ,ℓ'}` nas CHC's.** As CHC's do exemplo usam `T_{ℓ,ℓ'}` (indexado pelo **ramo**), que não está definido. As relações de transição estão definidas por **local**. Pelas regras gerais:
- **pré-condições:** `T_ℓ(X,X') ∧ sw_{ℓ,ℓ'}(X') ∧ P_ℓ(X) → P_{ℓ'}(X')`, com `T` do local de **origem**;
- **pós-condições:** `T_ℓ(X,X') ∧ sw_{ℓ',ℓ}(X) ∧ Q_{ℓ'}(X) → Q_ℓ(X')`, com `T` do local de **destino**.

🟠 **3.5** Na abordagem das pós-condições, a CHC `T_system → Q_system(X)` deve ser **`Q_system(X')`**. Faltam também os argumentos em `sw_{ℓ',ℓ}(X)` e em `¬φ(X)`.

🟡 Gralhas e forma:
- "Multiplicaçãop" → "Multiplicação";
- "pré-condidos"/"pós-condidos" → "pré-condições"/"pós-condições";
- "o sistemas de CHCs" → "o sistema de CHC's";
- "introduz-se as CHCs" → "introduzem-se";
- `φ ≡ (X_z = X_a*X_b$)`: o parêntese está fora da fórmula;
- "Para cada variável `𝖷` designamos por `𝖷_a, …`" → "Para o vetor de variáveis `𝖷` …";
- "predicado constante com a variável livre `𝖷`": "constante" está a mais;
- os locais aparecem como `𝓛` neste exemplo e como `𝒩` na secção anterior.

## 4. Codificação em z3 (resumo do notebook)

| guarda de `(do,odd)` | entradas | pré-condições | pós-condições | interpretação |
|---|---|---|---|---|
| corrigida: `odd(y)` | só `a,b ≤ L` | **unsat** (0,01 s) | **unsat** (0,02 s) | o overflow é alcançável (`a=8, b=2`) |
| corrigida: `odd(y)` | `a·b ≤ L` | **sat** (≈4 s) | **sat** (≈4 s) | correto e seguro; o modelo implica `z + x·y = a·b` |
| do texto: `even(y)` | `a·b ≤ L` | **sat** (0,3 s) | **sat** (0,4 s) | enganador: só é correto por vacuidade |

Estes valores são para `k = 4`, isto é, `L = 15`. Os inteiros são codificados como bit-vectors sem sinal de largura `k+3`, que chega para que nenhuma operação "dê a volta" antes de o teste de overflow a detetar. Com inteiros matemáticos (`Int`), o Spacer devolve `unknown`, por causa da não-linearidade de `a·b`. Com a restrição `a·b ≤ L`, o tempo é ≈ 20 s para `k = 5`, e o Spacer dá `unknown` (timeout) para `k = 6`.
