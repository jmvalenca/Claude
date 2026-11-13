import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import z3
    import time

    return mo, time, z3


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # CHC's para a "Multiplicação de inteiros com erros" (z3 / Spacer)

    Este notebook codifica em **z3** os dois sistemas de CHC's do Capítulo 4 (2ª parte),
    secção *"Verificação da correção parcial do programa Multiplicação de Inteiros com Erros"*:

    * **orientado às pré-condições** — incógnitas $P_\ell$, uma CHC por ramo $(\ell,\ell')$:
      $\;\models\;\mathsf{T}_\ell(\mathsf{X},\mathsf{X}')\land \mathsf{sw}_{\ell,\ell'}(\mathsf{X}')\land P_\ell(\mathsf{X}) \to P_{\ell'}(\mathsf{X}')$
    * **orientado às pós-condições** — incógnitas $Q_\ell$, uma CHC por ramo $(\ell',\ell)$:
      $\;\models\;\mathsf{T}_\ell(\mathsf{X},\mathsf{X}')\land \mathsf{sw}_{\ell',\ell}(\mathsf{X})\land Q_{\ell'}(\mathsf{X}) \to Q_{\ell}(\mathsf{X}')$

    mais as CHC's de `system`, `stop` ($\neg\varphi\land\cdot\to\mathtt{False}$) e `error` ($\cdot\to\mathtt{False}$).
    O solver de CHC's do z3 (**Spacer**) procura um **modelo** (uma interpretação das variáveis de predicado).
    Pelo texto, *existe modelo* $\iff$ o CFA é **parcialmente correto e seguro**.

    **Codificação.** Os inteiros são representados por *bit-vectors* sem sinal de largura $W=k+3$ com
    $L = 2^k-1$. A largura é suficiente para que nenhuma operação "dê a volta" antes de o teste de
    `overflow` ($x>L \lor z>L$) a detetar ($2L < 2^W$); $\varphi$ é calculada com o dobro da largura.
    Com inteiros matemáticos (`Int`) o Spacer devolve `unknown`, por causa da não-linearidade de
    $a*b$ em $\varphi$ e do invariante necessário $z + x*y = a*b$.
    """)
    return


@app.cell
def _(mo):
    k_ui = mo.ui.slider(3, 5, value=4, label="k (L = 2^k − 1)", show_value=True)
    texto_ui = mo.ui.checkbox(value=False, label="guarda de (do,odd) tal como no texto: (y≠0) ∧ even(y)")
    restr_ui = mo.ui.checkbox(value=False, label="restringir as entradas: a·b ≤ L")
    run_ui = mo.ui.run_button(label="Resolver os dois sistemas")
    mo.vstack([
        mo.md("### Parâmetros"),
        k_ui, texto_ui, restr_ui, run_ui,
        mo.md("_Com `a·b ≤ L` e k = 5 cada sistema demora cerca de 20 s._"),
    ])
    return k_ui, restr_ui, run_ui, texto_ui


@app.cell
def _(z3):
    NAMES = ["a", "b", "x", "y", "z"]
    LOCS = ["system", "do", "even", "odd", "stop", "error"]
    EDGES = [("system", "do"), ("do", "even"), ("do", "odd"),
             ("even", "do"), ("odd", "do"),
             ("do", "stop"), ("even", "error"), ("odd", "error")]

    def cfa(k, guarda_do_texto=False, restringir=False):
        """CFA da multiplicação: variáveis, T_ℓ, sw_{ℓ,ℓ'} e φ."""
        L = 2**k - 1
        W = k + 3
        X = {n: z3.BitVec(n, W) for n in NAMES}
        Xp = {n: z3.BitVec(n + "'", W) for n in NAMES}

        def same(*vs):
            return z3.And([Xp[v] == X[v] for v in vs])

        # relações de transição dos locais
        T = {
            "system": same("x", "y", "z"),          # havoc(a,b)
            "do": same(*NAMES),
            "stop": same(*NAMES),
            "error": same(*NAMES),
            "even": z3.And(Xp["x"] == 2 * X["x"], Xp["y"] == z3.UDiv(X["y"], 2),
                           same("z", "a", "b")),
            "odd": z3.And(Xp["x"] == X["x"], Xp["y"] == X["y"] - 1,
                          Xp["z"] == X["x"] + X["z"], same("a", "b")),
        }

        def ext(v):  # dupla largura para a*b
            return z3.ZeroExt(W, v)

        def sw(e, S):
            """guarda do ramo e, avaliada no vetor de variáveis S"""
            even = z3.URem(S["y"], 2) == 0
            overflow = z3.Or(z3.UGT(S["x"], L), z3.UGT(S["z"], L))
            init = [S["x"] == S["a"], S["y"] == S["b"], S["z"] == 0,
                    z3.ULE(S["a"], L), z3.ULE(S["b"], L)]  # a, b representáveis
            if restringir:
                init.append(z3.ULE(ext(S["a"]) * ext(S["b"]), L))
            g = {
                ("system", "do"): z3.And(init),
                ("do", "even"): z3.And(S["y"] != 0, even),
                ("do", "odd"): z3.And(S["y"] != 0, even if guarda_do_texto else z3.Not(even)),
                ("even", "do"): z3.Not(overflow),
                ("odd", "do"): z3.Not(overflow),
                ("even", "error"): overflow,
                ("odd", "error"): overflow,
                ("do", "stop"): S["y"] == 0,
            }
            return g[e]

        def phi(S):
            return ext(S["z"]) == ext(S["a"]) * ext(S["b"])

        return dict(L=L, W=W, X=X, Xp=Xp, T=T, sw=sw, phi=phi, ext=ext)

    return EDGES, LOCS, NAMES, cfa


@app.cell
def _(EDGES, LOCS, NAMES, z3):
    def chc_system(M, abordagem):
        """Lista de CHC's (sem quantificadores; variáveis X, X' universais)."""
        X, Xp, T, sw, phi = M["X"], M["Xp"], M["T"], M["sw"], M["phi"]
        V = [X[n] for n in NAMES]
        Vp = [Xp[n] for n in NAMES]
        S = z3.BitVecSort(M["W"])
        pre = abordagem == "pre"
        R = {l: z3.Function(("P_" if pre else "Q_") + l, *[S] * 5, z3.BoolSort()) for l in LOCS}
        clauses = []
        for (l, m) in EDGES:
            if pre:   # T_ℓ(X,X') ∧ sw_{ℓ,ℓ'}(X') ∧ P_ℓ(X) → P_ℓ'(X')
                clauses.append(z3.Implies(z3.And(T[l], sw((l, m), Xp), R[l](*V)), R[m](*Vp)))
            else:     # T_ℓ(X,X') ∧ sw_{ℓ',ℓ}(X) ∧ Q_ℓ'(X) → Q_ℓ(X')   (ℓ' = l, ℓ = m)
                clauses.append(z3.Implies(z3.And(T[m], sw((l, m), X), R[l](*V)), R[m](*Vp)))
        if pre:
            clauses.append(R["system"](*V))                                  # True → P_system(X)
        else:
            clauses.append(z3.Implies(T["system"], R["system"](*Vp)))        # T_system → Q_system(X')
        clauses.append(z3.Implies(z3.And(z3.Not(phi(X)), R["stop"](*V)), False))
        clauses.append(z3.Implies(R["error"](*V), False))
        return R, clauses, V + Vp

    return (chc_system,)


@app.cell
def _(NAMES, chc_system, time, z3):
    def resolve(M, abordagem, timeout_ms=120_000):
        R, clauses, allv = chc_system(M, abordagem)
        s = z3.SolverFor("HORN")
        s.set("timeout", timeout_ms)
        for c in clauses:
            s.add(z3.ForAll(allv, c))
        t0 = time.time()
        r = s.check()
        return dict(res=r, model=s.model() if r == z3.sat else None, R=R,
                    clauses=clauses, tempo=time.time() - t0, smt2=s.sexpr())

    def contraexemplo(M, abordagem, timeout_ms=120_000):
        """Spacer (Fixedpoint) dá o caminho no CFA até à violação;
        z3.Solver dá valores concretos ao longo desse caminho."""
        R, clauses, allv = chc_system(M, abordagem)
        fp = z3.Fixedpoint()
        fp.set(engine="spacer", timeout=timeout_ms)
        fp.set("xform.inline_linear", False, "xform.inline_eager", False, "xform.slice", False,
               "xform.coi", False, "xform.compress_unbound", False)
        Bad = z3.Function("Bad", z3.BoolSort())
        for f in R.values():
            fp.register_relation(f)
        fp.register_relation(Bad)
        fp.declare_var(*allv)
        for c in clauses:
            if not z3.is_implies(c):
                fp.add_rule(c)
                continue
            body, head = c.arg(0), c.arg(1)
            fp.add_rule(Bad() if z3.is_false(head) else head, body)
        if fp.query(Bad()) != z3.sat:
            return None
        nomes = []
        for r in fp.get_rules_along_trace():
            b = r.body() if z3.is_quantifier(r) else r
            h = b.arg(1) if z3.is_implies(b) else b
            n = h.decl().name()
            if n[:2] in ("P_", "Q_"):
                nomes.append(n[2:])
        path = list(reversed(nomes))
        if path[0] != "system":
            path = ["system"] + path
        # estado i = valores das variáveis à entrada do local path[i]
        W = M["W"]
        St = [{n: z3.BitVec(f"{n}_{i}", W) for n in NAMES} for i in range(len(path))]

        def sub(f, A, B):
            return z3.substitute(f, *[(M["X"][n], A[n]) for n in NAMES],
                                 *[(M["Xp"][n], B[n]) for n in NAMES])

        s = z3.Solver()
        for i, (l, m) in enumerate(zip(path, path[1:])):
            s.add(sub(M["T"][l], St[i], St[i + 1]))
            s.add(sub(M["sw"]((l, m), M["Xp"]), St[i], St[i + 1]))
        if path[-1] == "stop":
            s.add(z3.Not(sub(M["phi"](M["X"]), St[-1], St[-1])))
        if s.check() != z3.sat:
            return dict(path=path, estados=None)
        mdl = s.model()
        estados = [{"local": path[i], **{n: mdl.eval(St[i][n], model_completion=True).as_long()
                                         for n in NAMES}} for i in range(len(path))]
        return dict(path=path, estados=estados)

    return contraexemplo, resolve


@app.cell
def _(cfa, k_ui, restr_ui, texto_ui):
    M = cfa(k_ui.value, guarda_do_texto=texto_ui.value, restringir=restr_ui.value)
    return (M,)


@app.cell(hide_code=True)
def _(M, chc_system, mo):
    def _show(ab):
        _, _cl, _ = chc_system(M, ab)
        return mo.md("```\n" + "\n\n".join(str(c) for c in _cl) + "\n```")

    mo.accordion({
        "CHC's — abordagem orientada às pré-condições (P_ℓ)": _show("pre"),
        "CHC's — abordagem orientada às pós-condições (Q_ℓ)": _show("post"),
    })
    return


@app.cell
def _(M, contraexemplo, mo, resolve, run_ui):
    mo.stop(not run_ui.value, mo.md("_Carregue em **Resolver os dois sistemas**._"))
    resultados = {}
    for _ab in ("pre", "post"):
        _r = resolve(M, _ab)
        if str(_r["res"]) == "unsat":
            _r["cex"] = contraexemplo(M, _ab)
        resultados[_ab] = _r
    return (resultados,)


@app.cell(hide_code=True)
def _(M, NAMES, mo, resultados, z3):
    def _invariante_classico(r):
        """O modelo de P_do / Q_do implica z + x*y = a*b ?"""
        X, ext = M["X"], M["ext"]
        f = r["model"].eval(r["R"]["do"](*[X[n] for n in NAMES]), model_completion=True)
        s = z3.Solver()
        s.add(f, ext(X["z"]) + ext(X["x"]) * ext(X["y"]) != ext(X["a"]) * ext(X["b"]))
        return s.check() == z3.unsat, f

    _blocos = []
    for _ab, _nome in (("pre", "pré-condições (P_ℓ)"), ("post", "pós-condições (Q_ℓ)")):
        _r = resultados[_ab]
        _res = str(_r["res"])
        _txt = [f"### Abordagem orientada às {_nome}",
                f"Resultado do Spacer: **{_res}** ({_r['tempo']:.1f} s), com L = {M['L']}."]
        if _res == "sat":
            _ok, _f = _invariante_classico(_r)
            _txt.append("Existe modelo, logo o CFA é **parcialmente correto e seguro**.")
            _txt.append(f"O modelo de `do` implica o invariante clássico `z + x·y = a·b`: **{_ok}**.")
            _s = str(_f)
            _txt.append("Interpretação de `" + ("P" if _ab == "pre" else "Q") + "_do` (excerto):\n```\n"
                        + (_s[:1200] + (" …" if len(_s) > 1200 else "")) + "\n```")
            _blocos.append(mo.md("\n\n".join(_txt)))
        elif _res == "unsat":
            _txt.append("Não existe modelo, logo o CFA **não** é parcialmente correto e seguro.")
            _c = _r.get("cex")
            if _c and _c["estados"]:
                _txt.append("Caminho até à violação: `" + " → ".join(_c["path"]) + "`")
                _txt.append("_Cada linha dá os valores à entrada do local; a 1ª linha é o estado "
                            "antes do `havoc(a,b)`._")
                _blocos.append(mo.vstack([mo.md("\n\n".join(_txt)),
                                          mo.ui.table(_c["estados"], selection=None)]))
            else:
                _blocos.append(mo.md("\n\n".join(_txt)))
        else:
            _txt.append("O Spacer não conseguiu decidir dentro do tempo limite.")
            _blocos.append(mo.md("\n\n".join(_txt)))
    mo.vstack(_blocos)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Resultados de referência (k = 4, L = 15)

    | guarda de `(do,odd)` | entradas | pré-condições | pós-condições | interpretação |
    |---|---|---|---|---|
    | corrigida: `odd(y)` | só `a,b ≤ L` | **unsat** | **unsat** | o `overflow` é alcançável, por ex. `a=8, b=2`: `x = 16 > L` |
    | corrigida: `odd(y)` | `a·b ≤ L` | **sat** | **sat** | correção parcial e segurança; o modelo implica `z + x·y = a·b` |
    | do texto: `even(y)` | `a·b ≤ L` | **sat** | **sat** | **enganador**: com `y` ímpar o controlo fica bloqueado em `do`; a correção parcial vale por vacuidade |

    ## Observações sobre o texto

    1. 🔴 Na guarda `sw_{do,odd}` está `even(X_y)`; deve ser `odd(X_y)`. Com o texto tal como está,
       os dois ramos saem de `do` com a mesma guarda e o ramo `odd` nunca é usado. O sistema continua
       a ter modelo (última linha da tabela), mas só porque as execuções com `y` ímpar ficam bloqueadas.
    2. 🟠 Com `overflow ≡ (x > L) ∨ (z > L)` e o `havoc(a,b)` sem restrições, **não existe modelo**:
       o erro é alcançável. Para obter "parcialmente correto e seguro" é preciso uma pré-condição,
       como `a·b ≤ L` (com `a, b ≥ 0`). Além disso, se `a, b` puderem ser negativos, o `overflow`
       deve também testar `< −L`. (Aqui os *bit-vectors* sem sinal tornam `a, b ≥ 0` implícito.)
    3. 🟠 Nas CHC's do exemplo aparece `T_{ℓ,ℓ'}`, indexado pelo ramo. Pelas regras gerais deve ser
       `T_ℓ` (o local de **origem**) na abordagem das pré-condições, e `T_ℓ` (o local de **destino**)
       na abordagem das pós-condições. É isso que este notebook usa.
    4. 🟠 Na abordagem das pós-condições, `T_system → Q_system(X)` deve ser `→ Q_system(X')`.
    """)
    return


if __name__ == "__main__":
    app.run()
