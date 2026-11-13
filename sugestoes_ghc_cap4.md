Li o capítulo. As CHC's (Constrained Horn Clauses) aparecem nele só uma vez, numa caixa que as adia para a 3ª parte. Há também uma secção marcada "A completar", em "CFA's e Transformadores de Predicados", que é o sítio natural para elas entrarem. Estes são os pontos onde me parece que as CHC's completam o material, do mais importante para o menos importante.

## 1. Preencher o "A completar": um CFA é um sistema de CHC's

As "equações" P_a ≡ ⋁ sw_{b,a} ∧ sp_b(P_b) passam a cláusulas quando se troca ≡ por →. Cada ramo b → a dá uma cláusula, onde T_b(X,X') é a transição do local b:

- P_b(X) ∧ T_b(X,X') ∧ sw_{b,a}(X') → P_a(X')
- true → P_system(X)
- P_stop(X) ∧ ¬φ(X) → false
- P_error(X) → false

Há três observações que vale a pena pôr no texto:

- **Desaparece o problema dos quantificadores.** Sem quantificadores, sp_b não se consegue calcular em geral, e o texto já o diz. Na cláusula, o ∃Z de sp fica implícito: as variáveis do corpo que não aparecem na cabeça estão quantificadas universalmente na cláusula, o que equivale a um ∃ no corpo.
- **As formulações wp e sp dão a mesma CHC.** Pela conexão de Galois, Q_a ∧ sw → wp_b(Q_b) equivale a sp_b(Q_a ∧ sw) → Q_b. Isto dá exatamente a cláusula acima. A orientação sp corresponde à **menor** solução, a orientação wp à **maior**, e qualquer solução entre as duas é um certificado de correção. É uma forma muito limpa de unificar as duas "representações" da secção.
- **"Calcular uma solução como ponto fixo" passa a ser "encontrar um modelo da CHC".** Já não é preciso iterar até chegar ao ponto fixo exato.

## 2. Uma tabela de tradução dos t.p. para CHC's

A secção "Alguns exemplos de transformadores de predicados" fica fechada com esta tabela:

| Construção | Em CHC |
|---|---|
| Atribuição X ← e(X) | P(X) → Q(e(X)) |
| Havoc(X) | P(X) → Q(Z), com Z uma variável nova |
| Guarda G ∧ S | G(X) passa a ser uma restrição no corpo |
| Escolha T₀ ‖ T₁ | duas cláusulas com a mesma cabeça (por isso sp = sp₀ ∨ sp₁) |
| Composição T₀ ; T₁ | o estado intermédio é uma variável do corpo, sem ∃ explícito (ou um predicado intermédio) |
| Invariante indutivo | I → Inv, Inv ∧ T → Inv', Inv ∧ E → false |

## 3. Segurança como satisfazibilidade de CHC's

Na secção "Acessibilidade e Segurança", o ponto 5 já é, na prática, uma CHC. Com estas cláusulas:

- I → R
- R ∧ T → R'
- R ∧ E → false

Σ é seguro se e só se o sistema tem solução, e a menor solução é sp*(I). A versão dual, com E → U, T ∧ U' → U e I ∧ U → false, dá pre*(E). Isto também é Horn, porque cada cláusula tem uma única cabeça. A observação final do texto, de que basta que R ou U seja indutivo, fica mais clara assim: escolhe-se resolver o sistema para a frente ou para trás.

## 4. Reescrever o exemplo da multiplicação

Escrito como CHC's sobre (a,b,x,y,z), o exemplo resolve os dois problemas que o texto aponta.

**Primeiro problema (iterar do_n até ao ponto fixo, ou limitar como no BMC).** Um solver de CHC's, como o Spacer do Z3 (`SolverFor('HORN')`), procura diretamente um invariante. Se não houver, devolve um contra-exemplo.

**Segundo problema (o havoc e a guarda b ≥ 0).** Passa a ser só uma restrição na cláusula de entrada: a ≥ 0 ∧ b ≥ 0 ∧ x=a ∧ y=b ∧ z=0 → Do(a,b,x,y,z). Convém notar que as CHC's tratam correção **parcial** e segurança. A terminação continua a precisar de uma função de variante, o que pode ser um comentário útil.

O exemplo também mostra uma coisa interessante aos alunos. Com error ≡ False, o solver responde **unsafe**, porque para a e b grandes o overflow acontece mesmo. A especificação precisa de a·b ≤ MAX como pré-condição.

Um aviso prático: o invariante natural, z + x·y = a·b, é não-linear, e o Spacer pode ter dificuldade com NIA. Talvez valha a pena uma versão com a ou b limitados, ou a prova separada de "ausência de overflow".

## 5. Ligar o PDR ao Spacer

O PDR está restrito a variáveis booleanas. O Spacer é o PDR generalizado a CHC's sobre uma teoria 𝒯, e cada noção tem correspondente:

- as frames F_k passam a ser aproximações de cada predicado desconhecido;
- o bloqueio de cubos passa a ser o bloqueio de obrigações de prova;
- a expansão de cubos passa a ser generalização por interpolação e MBP (model-based projection, que substitui a eliminação de quantificadores em sp);
- um CFA com vários locais passa a ser vários predicados, isto é, um "PDR por local".

Um exercício natural é reescrever o `counter(4)` do pysmt como CHC e comparar a resposta do Spacer com a do PDR simplificado.

A revisão da 3ª parte já guardada no projeto diz que essa parte promete esta extensão do PDR mas não a apresenta. Este ponto pode servir de ponte entre as duas partes.

## 6. TCFA e SyncCFA (opcional)

No TCFA, o tempo é só mais uma variável, com restrições t' ≥ t nas cláusulas. No SyncCFA, o produto sincronizado dá predicados sobre pares de locais. Também se pode antecipar que chamadas de procedimentos dão CHC's **não-lineares**, com vários predicados no corpo.

Para não repetir o que a 3ª parte vai definir, sugiro manter na 2ª parte só a tradução (pontos 1 a 3, mais o exemplo do ponto 4 escrito como cláusulas) e deixar o solver e o Spacer para a 3ª parte. Posso redigir o texto da secção "A completar" no estilo do capítulo, com o exemplo da multiplicação em código z3 testado. Antes disso preciso de confirmar o algoritmo exato do diagrama: o texto não o descreve e eu não abri a imagem.

Fontes: Capítulo_4_2a_parte.md, na pasta LC; revisão da 3ª parte no projeto (claude/revisao-capitulo-4-SAT-MC-3a-parte.md)
