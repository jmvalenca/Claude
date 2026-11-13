# Revisão — Capítulo 4: "Verificação de Modelos baseada em SAT" (3ª Parte)
 
Revisão do documento Dropbox Paper, feita em 26/10/2026. As fórmulas foram lidas a partir do LaTeX (KaTeX) do documento.
 
**Sobre o código:** não foi possível executá-lo, porque o z3-solver não estava disponível no ambiente. O invariante que o texto apresenta como resultado do primeiro exemplo foi verificado à mão e está correto (ver A4).
 
---
 
## A. Erros importantes
 
### 1. Forma genérica de uma CHC: a cabeça não tem de ser um dos pᵢ, e faltam os factos
O texto diz: "q coincide com um dos pᵢ ou então é a constante absurdo ⊥". Isto está errado. A cabeça pode ser **qualquer** variável de predicado, quer ocorra no corpo quer não.
 
Exemplo: a própria CHC de inicialização do exemplo, `init(x) ⇒ Inv(x)`, tem n = 0 (nenhum predicado no corpo) e cabeça Inv. Nem sequer cabe na forma genérica do texto, que pressupõe n ≥ 1. É preciso também admitir **n = 0** (os "factos").
 
Sobre a expressão "n variáveis **distintas**": o mesmo predicado pode aparecer várias vezes no corpo, por exemplo `p[x] ∧ p[y] ⇒ p[x+y]`. O que conta é o número de aplicações de predicados.
 
**Correção:** `∀υ · φ(υ) ∧ p₁[t₁(υ)] ∧ ⋯ ∧ pₙ[tₙ(υ)] ⇒ H`, com n ≥ 0 e H igual a `q[t₀(υ)]` (q é uma variável de predicado qualquer) ou a ⊥.
 
### 2. CHC linear: definição demasiado restrita
"quando n = 1 … a CHC diz-se linear", com a forma `φ ∧ p[t₁] ⇒ p[t₀]`. Uma CHC é linear quando o corpo tem **no máximo uma** aplicação de predicado (n ≤ 1). A cabeça pode ser um predicado **diferente** do do corpo. As formas lineares são, portanto:
 
- `φ ⇒ q[t₀]` (facto, n = 0);
- `φ ∧ p[t₁] ⇒ q[t₀]`;
- `φ ∧ p[t₁] ⇒ ⊥`.
Com a definição do texto, o próprio exemplo (chc0) não seria linear. Também não seriam lineares os sistemas com vários predicados, um por ponto do programa, que são precisamente o caso habitual na verificação de programas com vários ciclos.
 
### 3. Problema SAT em CHC's: as variáveis de ordem zero não recebem valores
O texto diz: "existe uma atribuição de predicados às variáveis de 1ª ordem **e uma atribuição de valores da teoria base às variáveis de ordem zero** que faz com que … todas as fórmulas sejam válidas".
 
As variáveis de ordem zero estão **quantificadas universalmente** em cada cláusula, por isso não lhes é atribuído nenhum valor. O problema é: existe uma interpretação das variáveis de predicado tal que todas as cláusulas (fórmulas fechadas, com ∀) são **válidas** em 𝒯?
 
Convém também distinguir as duas noções de solução:
 
- **semântica:** os predicados são conjuntos arbitrários;
- **sintática:** os predicados são definidos por fórmulas de 𝒯, que é o que o solver devolve.
### 4. Exemplo Spacer: a propriedade verificada não é a anunciada
O texto diz que se vai "verificar que, dentro do ciclo while, a variável x é sempre não-nula". Isto é **falso** neste programa: x chega a 0 com `on` verdadeiro, imediatamente antes da transição t1.
 
O que o código verifica é `error ≡ (x ≠ 0) ∧ ¬on`, ou seja, **quando o ciclo termina, x = 0**. O invariante devolvido, `x ≥ 0 ∧ (on ∨ x ≤ 0)`, confirma-o: implica x = 0 quando ¬on. (Verificado à mão: implicado por init, preservado por t0 e t1, e inconsistente com error.)
 
**Correção:** "verificar que, à saída do ciclo, x = 0".
 
Outros pontos do exemplo:
 
- **assume vs assert:** o pseudo-código começa com `assert x > 0`, mas isto é uma pré-condição. Deve ser `assume x > 0`, coerente com o esquema `assume φ ; while … ; assert ϕ` da secção seguinte.
- **Guarda do ciclo:** o pseudo-código tem `while x != 0`, mas t0 usa a guarda `x > 0`. Com a pré-condição x > 0 dá o mesmo resultado. No entanto, para x < 0 o modelo fica bloqueado (nem t0 nem t1 se aplicam), enquanto o programa não terminaria. Para ser fiel ao programa, t0 deve ter `x != 0`.
- **Nome `vars`:** sobrepõe-se à função `vars` do Python. Sugere-se `xs`/`xs_`.
- **Representação do resultado:** a forma impressa do invariante pode variar com a versão do Z3. Convém dizê-lo, ou dar o invariante numa forma legível (`x ≥ 0 ∧ (on ∨ x = 0)`).
### 5. Invariantes de ciclos: as condições (1) e (2) estão erradas
Para `assume φ ; while b do S od ; assert ϕ`, as condições do texto são:
 
1. `φ ∧ b ⇒ ϑ`
2. `ϑ ⇒ wp_S(ϑ)` (ou `ϑ ∧ T_S ⇒ ϑ'`)
3. `ϑ ∧ ¬b ∧ ¬ϕ ⇒ ⊥`
**(1) torna o método incorreto.** Deve ser `φ ⇒ ϑ`. Contra-exemplo: φ = True, b = False, ϕ = False. O programa `assume True; while False do skip od; assert False` é incorreto, mas ϑ = False satisfaz (1), (2) e (3). O caso φ ∧ ¬b (o ciclo não executa) fica sem cobertura.
 
**(2) é demasiado forte.** Deve ser `ϑ ∧ b ⇒ wp_S(ϑ)`, ou `ϑ ∧ b ∧ T_S ⇒ ϑ'`, porque o corpo só executa quando a guarda é verdadeira. Sem b, muitos programas corretos ficam sem invariante. Por exemplo, num `while x > 0 do x := x − 1` com ϑ = (x ≥ 0), o passo x = 0 → x = −1 viola a condição.
 
As mesmas correções aplicam-se ao sistema de CHC's:
 
- `∀x · φ(x) ⇒ ϑ(x)`
- `∀x,x' · ϑ(x) ∧ b(x) ∧ T_S(x,x') ⇒ ϑ(x')`
- `∀x · ϑ(x) ∧ ¬b(x) ∧ ¬ϕ(x) ⇒ ⊥`
Na 3ª fórmula, a quantificação em x' é desnecessária.
 
No exemplo Spacer acima isto não é problema, porque `trans` já inclui as guardas (t0 tem `x > 0`, t1 tem `x == 0`).
 
### 6. Promessa não cumprida: a extensão do PDR
O texto diz: "Usando exclusivamente CHC's lineares é possível, **como veremos nesta secção**, estender o algoritmo PDR … para espaços de estado não-finitos." A secção não apresenta essa extensão. Só usa o Spacer como caixa negra.
 
O documento também parece terminar abruptamente: acaba no código de `interpolate`, sem exemplo de uso nem conclusão. Sugestões:
 
- esboçar o Spacer: frames como fórmulas de 𝒯, bloqueio de *obrigações de prova* com generalização por interpolação e MBP (*model-based projection*);
- ou retirar o "como veremos nesta secção";
- acrescentar um exemplo de chamada a `interpolate`, p.ex. `interpolate(And(x < a, a < y), And(y < b, b < x))`, com o resultado esperado (algo equivalente a x < y).
---
 
## B. Observações menores
 
- **Título:** "Cláusulas de Horn **Restritas**" é uma tradução ambígua de *Constrained Horn Clauses*. Parece dizer que as cláusulas são restringidas, quando o que acontece é que têm restrições φ na teoria. Sugestão: "Cláusulas de Horn **com Restrições**".
- **"variáveis que tomam valores sobre predicados e funções":** nas CHC's as incógnitas são só **predicados**, não funções.
- **"predicados representando conjuntos de termos t(υ)":** representam conjuntos de **valores** (tuplos de 𝒯), não de termos.
- **"CHC's são uma extensão de SMT's da Lógica de 1ª Ordem":** convém dizer que, ao quantificar sobre predicados, se sai da 1ª ordem. É um fragmento da lógica de 2ª ordem, embora se resolva com técnicas de 1ª ordem.
- **Decidibilidade:** o problema SAT em CHC's é **indecidível** em geral (já para LIA). O Spacer pode devolver `unknown` ou não terminar. O código só trata o caso `sat`. Convém tratar `unsat` (existe contra-exemplo; `s.proof()` / resposta de erro) e `unknown`.
- **"Um dos primeiros é o algoritmo Spacer":** o Spacer (Komuravelli, Gurfinkel, Chaki, 2014) não é dos primeiros. Antes dele houve o GPDR (Hoder & Bjørner, 2012), o HSF, o Eldarica e o μZ. Sugestão: "um dos mais usados".
- **"interpolador" / "interpeladores":** na 1ª parte o termo é **interpolante**. Uniformizar ("interpolante de Craig") e corrigir "interpeladores".
- **Ligação com a 1ª parte:** a redução a CHC é precisamente a forma atual de obter interpolantes em Z3, já que a API de interpolação foi removida na versão 4.8 (ver a revisão da 1ª parte, A7). Vale a pena dizê-lo.
- **`free_vars`:**
  - recolhe todas as aplicações com `Z3_OP_UNINTERPRETED`, incluindo aplicações de funções não interpretadas com argumentos (f(x)). Estas não podem ser quantificadas em `ForAll`. Convém filtrar por `f.num_args() == 0`;
  - se A ou B não tiverem variáveis livres, ou se não houver variáveis partilhadas, `ForAll([])`/`Function('Itp', BoolSort())` falha ou degenera. Pode valer a pena um comentário;
  - os comentários do código estão em inglês e português misturados ("#Returns…", "# as regras definidoras…").
- **"um term Z3"** → "um termo Z3".
- **Ortografia:** "correcto" (pré-AO) ao lado de "respetivamente", "vetor", "diretamente" (AO).
---
 
## C. Gralhas e português
 
- "variáveis que tomam valores tomam valores sobre predicados" → "variáveis que tomam valores sobre predicados"
- "(inteiros, booleanos, vetores de bits, etc…)" → "etc.)"
- "Bool , Int , BitVec , Arrays …) ," → espaços antes das vírgulas
- "para espaços de estado não-finitos" → "infinitos" (ou "não finitos")
- "contém a verificação das propriedades" → "inclui a verificação de propriedades"
- "em outros autómatos" → "noutros autómatos"
- "existe um grande esforço para construção" → "para a construção"
- "este programa é correcto se existe um predicado $\,$ ϑ" → há um espaço LaTeX (`$\,$`) solto antes de ϑ
- "na procura dos interpeladores" → "interpolantes"
