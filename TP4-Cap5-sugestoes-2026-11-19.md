# TP4 — Autómatos híbridos e sincronismo (Capítulo 5)

Duas propostas de problema para o TP4, com resolução de referência em notebooks Marimo (pySMT 0.9.6, Z3 5.4.1, Marimo 0.25.2). Os temas dos anos anteriores (ABS, controlo de tráfego) foram evitados.

| Exercício | Tema | Enunciado (Dropbox) | Resolução (este repositório) |
|---|---|---|---|
| TP4.1 | Pâncreas artificial: um só autómato híbrido | `Enunciados dos Trabalho Práticos/TP4.1/pancreas_artificial_enunciado.py` | `tp4_p1_pancreas.py` (≈ 20 s) |
| TP4.2 | Sincronização de relógios: Mestre ∥ Canal ∥ Sensor₁ ∥ Sensor₂ | `Enunciados dos Trabalho Práticos/TP4.2/sincronizacao_relogios_enunciado.py` | `tp4_p2_relogios.py` (≈ 3,5 min) |

Os enunciados seguem o formato do TP3: Contexto, O sistema, Pretende-se, Requisitos obrigatórios, Notas técnicas, Como testar/validar, Critério do aluno, Extensões opcionais.

## TP4.1 — Pâncreas artificial

**Modelo.** Variáveis G (glicose), I (insulina ativa), t (relógio do modo); entrada não determinista r ∈ [0, r_max]. Fluxos por Euler com Δ = 10 min:

    G' = G + Δ (r − a I)      I' = I + Δ (u − b I)      t' = t + Δ

Modos BASAL (u_b), BOLUS (u_B), SUSP (0) e ALARME (absorvente). O controlador usa a **glicose prevista** Gp = G − (a/b) I. Transições discretas urgentes:

| De | Para | Guarda | Reset |
|---|---|---|---|
| BASAL | SUSP | Gp < L_s | t := 0 |
| BASAL | BOLUS | G > 180 ∧ Gp ≥ L_s | t := 0 |
| BOLUS | SUSP | Gp < L_s | t := 0 |
| BOLUS | BASAL | t ≥ T_B ∨ G ≤ 140 | — |
| SUSP | BASAL | G > 100 ∧ t ≥ T_S | — |
| qualquer | ALARME | G < 50 ∨ G > 300 | — |

Parâmetros: Δ = 10, a = 0,02, b = 0,05, u_b = 1, u_B = 3, r_max = 1,2, L_s = 90, T_B = T_S = 30. Inicial: BASAL, t = 0, G ∈ [100, 180], I ∈ [0, 20].

**Resultados esperados (resolução de referência).**

| Alínea | Resultado |
|---|---|
| 3 | BMC sem violações de G ≥ 70 nem de ALARME até 20 transições. Com 30 transições já demora vários minutos. |
| 4 | k-indução simples falha para k ≤ 4. Invariante 1-indutivo: modo ∈ {BASAL, BOLUS, SUSP} ∧ 0 ≤ I ≤ 60 ∧ t ≥ 0 ∧ 78 ≤ Gp ≤ 188 ∧ (SUSP → Gp ≤ L_s + r_max·t ∧ Gp ≤ 138). A chave é Gp' = Gp + Δ (r − (a/b) u). |
| 5 | A partir de BOLUS, G = 210, I = 0, r ≤ 0,5: o traço mais longo com G > 180 tem 11 transições, 7 temporizadas (≈ 70 min). |
| 6 | Com L_s = 72 há violação em 10 transições (G desce a 69,98 em SUSP). Segurança exige L_s − Δ (a/b) u ≥ 70 nos modos com infusão. |

## TP4.2 — Sincronização de relógios numa rede de sensores

**Modelo.** Mestre (relógio x ≤ P, emite `envia` em x = P), Canal (LIVRE/TRÂNSITO, temporizador y ≤ d_max, `entrega` com y ≥ d_min), Sensor_i (SINC/DESSINC, relógio c_i com ċ_i ∈ [1−ρ, 1+ρ], contador de perdas f_i; DESSINC quando f_i = K). Sincronização por rótulos: `envia` (Mestre, Canal), `entrega` (Canal, Sensores), `tempo(τ)` (todos). Na resolução usa-se o desvio e_i = c_i − T, com receção e_i := d_min − y.

Parâmetros: P = 10, ρ = 0,01, d_min = 0,1, d_max = 0,5, K = 3. Propriedade φ_δ: ambos em SINC → |c₁ − c₂| ≤ δ.

**Resultados esperados (resolução de referência).**

| Alínea | Resultado |
|---|---|
| 3 | δ = 0,5 falha em 4 transições (um sensor recebe com atraso máximo, o outro perde). δ = 1 sem violações até 16 transições. |
| 4 | Maior desvio observado ≈ 0,91. Majorante analítico (d_max − d_min) + 2ρ (K P + d_max) = 1,01. |
| 5 | Com A_i = f_i P + x + (P se TRÂNSITO), o invariante d_min − d_max − ρ A_i ≤ e_i ≤ ρ A_i (mais 0 ≤ x ≤ P, TRÂNSITO → y = x ≤ d_max, d_i ↔ f_i ≥ K) é 1-indutivo e prova φ com δ = 1,01. Observação-chave: x e y são postos a zero no mesmo `envia`. |
| 6 | Com relógio auxiliar w: B = P falha em 3 transições; B = P + d_max é provado pelo invariante w + (tempo restante até à entrega) ≤ B. |
| 7 | P = 12 com δ = 1: violação em 11 transições (sensores derivam em sentidos opostos durante dois períodos com perdas). |

## Notas de implementação

- Usar constantes racionais exatas, `Real(Fraction(str(x)))`. Com `Real(0.02)` o Z3 recebe a expansão binária do float: o BMC ficou ≈ 5× mais lento e a prova indutiva do TP4.1 falhou por arredondamento.
- No TP4.2, τ é variável e pode ser arbitrariamente pequeno, pelo que a vivacidade tem de ser medida em tempo (relógio w) e não em número de passos.
- A versão editável das propostas, com as notas para o docente, está em [TP4 — Autómatos híbridos e sincronismo](https://claude.ai/artifact/HyEjR1JBRzPW1FnvMCLnFh).
