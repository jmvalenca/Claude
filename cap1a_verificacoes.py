import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import itertools
    import numpy as np
    from scipy.optimize import linprog
    return itertools, linprog, mo, np


@app.cell
def _(mo):
    mo.md(r"""
    # Cap. 1a · verificações

    Este notebook verifica por força bruta, ou com `scipy.optimize.linprog`, as
    afirmações do Cap. 1a que a avaliação (`Avaliacao-Cap1a-2026-11-19.md`) confirma ou corrige:

    1. a codificação CNF → LIA do exemplo (correta);
    2. a negação de predicados em PI (correta);
    3. a simplificação de predicados em PIB por $\sigma_{\min}$ e $\sigma_{\max}$ (correta);
    4. a regra de corte do texto ($c_0 \mapsto \lfloor c^*\rfloor$), que **não é válida**:
       um contra-exemplo em que o algoritmo responde `unsat` a uma fórmula satisfazível;
    5. o corte de Chvátal–Gomory, que resolve o mesmo exemplo;
    6. a árvore de decisão e a BDD do exemplo (9 → 5 nodos, 8 → 6 referências),
       a canonicidade, a negação linear e a dependência da ordem das variáveis.
    """)
    return


@app.cell
def _(itertools):
    # 1. CNF -> LIA:  F = (x ∨ ¬y ∨ ¬z) ∧ (¬x ∨ z ∨ w)
    #    φ = (−x + y + z ≤ 1) ∧ (x − z − w ≤ 0)
    def F(x, y, z, w):
        return (x or not y or not z) and (not x or z or w)

    def phi(x, y, z, w):
        return (-x + y + z <= 1) and (x - z - w <= 0)

    cnf_lia_ok = all(
        bool(F(*v)) == phi(*v) for v in itertools.product((0, 1), repeat=4)
    )
    print("1. CNF -> LIA equivalente em {0,1}^4:", cnf_lia_ok)
    return


@app.cell
def _(itertools, np):
    # 2. Em PI: ¬(c·x ≤ c0)  ≡  (−c)·x ≤ −c0 − 1   para x inteiro
    rng = np.random.default_rng(1)
    neg_ok = True
    for _ in range(300):
        n = int(rng.integers(1, 4))
        c = rng.integers(-5, 6, size=n)
        c0 = int(rng.integers(-8, 9))
        for x in itertools.product(range(0, 5), repeat=n):
            x = np.array(x)
            if (not (c @ x <= c0)) != ((-c) @ x <= -c0 - 1):
                neg_ok = False
    print("2. negação em PI correta:", neg_ok)

    # ... mas não em Q+ (a negação de ≤ é <, não ≤ c0−1): x = 0.5, c = (1), c0 = 0
    print("   em Q+ falha: ¬(0.5 ≤ 0) =", not (0.5 <= 0), " mas −0.5 ≤ −1 =", -0.5 <= -1)
    return


@app.cell
def _(itertools, np):
    # 3. PIB: c0 ≥ σmax ⇒ sempre verdadeiro; c0 < σmin ⇒ sempre falso
    rng3 = np.random.default_rng(2)
    sigma_ok = True
    for _ in range(500):
        n = int(rng3.integers(1, 6))
        c = rng3.integers(-6, 7, size=n)
        smax, smin = c[c > 0].sum(), c[c < 0].sum()
        vals = [c @ np.array(w) for w in itertools.product((0, 1), repeat=n)]
        sigma_ok &= (max(vals) == smax) and (min(vals) == smin)
    print("3. σmax e σmin corretos:", bool(sigma_ok))
    return


@app.cell
def _(mo):
    mo.md(r"""
    ## 4–5. Plano de corte

    Fórmula PIB (solução única $x = (1,0)$):

    $$\varphi \;\equiv\; (2x_1 + 2x_2 \le 3)\;\wedge\;(x_1 - x_2 \le 1)\;\wedge\;(-x_1 \le -1)$$

    A relaxação LP (com $0 \le x_i \le 1$ e objetivo $\max x_2$) dá $x^* = (1, \tfrac12)$.
    O único predicado com $c^* = \sum_i c_i x^*_i$ não inteiro é $x_1 - x_2 \le 1$ ($c^* = \tfrac12$).
    A regra do texto troca-o por $x_1 - x_2 \le 0$, e o LP passa a ser **inviável**:
    o algoritmo responderia `unsat`, embora $(1,0)$ seja solução.

    O corte de Chvátal–Gomory com multiplicador $\lambda = \tfrac12$ no 1.º predicado,
    $x_1 + x_2 \le \lfloor 3/2 \rfloor = 1$, é **acrescentado** e o LP devolve $(1,0)$.
    """)
    return


@app.cell
def _(itertools, linprog, np):
    A = np.array([[2, 2], [1, -1], [-1, 0]], dtype=float)
    b = np.array([3, 1, -1], dtype=float)
    obj = np.array([0, -1.0])  # max x2
    bounds = [(0, 1), (0, 1)]

    pib = [w for w in itertools.product((0, 1), repeat=2) if np.all(A @ w <= b)]
    print("soluções PIB:", pib)

    r = linprog(obj, A_ub=A, b_ub=b, bounds=bounds)
    xs = r.x
    cstar = A @ xs
    print("LP:", r.status, "x* =", xs.round(6), " c* =", cstar.round(6))

    # regra do texto: substituir c0 por floor(c*) no predicado com c* não inteiro
    j = next(i for i, v in enumerate(cstar) if abs(v - round(v)) > 1e-9)
    b_txt = b.copy()
    b_txt[j] = np.floor(cstar[j])
    r_txt = linprog(obj, A_ub=A, b_ub=b_txt, bounds=bounds)
    print(f"regra do texto: predicado {j}, c0 {b[j]:g} -> {b_txt[j]:g};",
          "LP inviável (unsat ERRADO)" if r_txt.status == 2 else f"status {r_txt.status}")

    # corte de Chvátal–Gomory: λ = 1/2 no 1.º predicado -> x1 + x2 <= 1
    lam = np.array([0.5, 0, 0])
    a_cg, b_cg = np.floor(lam @ A), np.floor(lam @ b)
    valido = all(a_cg @ w <= b_cg for w in pib)
    r_cg = linprog(obj, A_ub=np.vstack([A, a_cg]), b_ub=np.append(b, b_cg), bounds=bounds)
    print("corte CG:", a_cg, "<=", b_cg, "| válido para todas as soluções PIB:", valido,
          "| novo x* =", r_cg.x.round(6) + 0.0)
    return


@app.cell
def _():
    # 6. ROBDD mínima com tabela única (dicionário), como descrito no texto
    class BDD:
        def __init__(self, nvars):
            self.n = nvars
            self.T = {0: None, 1: None}          # id -> (var, high, low)
            self.U = {}                          # (var, high, low) -> id

        def mk(self, v, hi, lo):
            if hi == lo:                         # regra de redução
                return hi
            k = (v, hi, lo)
            if k not in self.U:
                self.U[k] = len(self.T)
                self.T[self.U[k]] = k
            return self.U[k]

        def var(self, v):
            return self.mk(v, 1, 0)

        def apply(self, op, u1, u2, memo=None):
            memo = {} if memo is None else memo
            if (u1, u2) in memo:
                return memo[(u1, u2)]
            if u1 in (0, 1) and u2 in (0, 1):
                r = int(op(u1, u2))
            else:
                v1 = self.T[u1][0] if u1 > 1 else self.n + 1
                v2 = self.T[u2][0] if u2 > 1 else self.n + 1
                v = min(v1, v2)
                h1, l1 = (self.T[u1][1], self.T[u1][2]) if v1 == v else (u1, u1)
                h2, l2 = (self.T[u2][1], self.T[u2][2]) if v2 == v else (u2, u2)
                r = self.mk(v, self.apply(op, h1, h2, memo), self.apply(op, l1, l2, memo))
            memo[(u1, u2)] = r
            return r

        def neg(self, u, memo=None):             # troca das folhas: linear
            memo = {} if memo is None else memo
            if u in (0, 1):
                return 1 - u
            if u not in memo:
                v, h, l = self.T[u]
                memo[u] = self.mk(v, self.neg(h, memo), self.neg(l, memo))
            return memo[u]

        def size(self, u):                       # nodos (com folhas) e referências
            seen, stack, edges = set(), [u], 0
            while stack:
                w = stack.pop()
                if w in seen:
                    continue
                seen.add(w)
                if w > 1:
                    edges += 2
                    stack += [self.T[w][1], self.T[w][2]]
            return len(seen), edges

    AND = lambda a, b: a and b
    OR = lambda a, b: a or b
    return AND, BDD, OR


@app.cell
def _(AND, BDD, OR):
    B = BDD(3)
    x1, x2, x3 = B.var(1), B.var(2), B.var(3)
    nx1, nx2 = B.neg(x1), B.neg(x2)
    # f = (x1 ∧ ¬x2 ∧ x3) ∨ (¬x1 ∧ x3)   (fórmula da árvore do texto, com x0 -> x2)
    f = B.apply(OR, B.apply(AND, B.apply(AND, x1, nx2), x3), B.apply(AND, nx1, x3))
    # forma equivalente: x3 ∧ ¬(x1 ∧ x2)
    g = B.apply(AND, x3, B.neg(B.apply(AND, x1, x2)))
    print("6. BDD de f: (nodos, referências) =", B.size(f), "  [texto: 5 nodos, 6 referências]")
    print("   árvore de decisão reduzida: 4 nodos internos + 5 folhas = 9 nodos, 8 referências")
    print("   canonicidade: f e x3 ∧ ¬(x1∧x2) dão o mesmo nodo:", f == g)
    nf = B.neg(f)
    print("   ¬f por troca de folhas: tamanho", B.size(nf), "| f ∧ ¬f = 0:",
          B.apply(AND, f, nf) == 0, "| f ∨ ¬f = 1:", B.apply(OR, f, nf) == 1)
    return


@app.cell
def _(AND, BDD, OR):
    # dependência da ordem: (a1∧b1) ∨ (a2∧b2) ∨ (a3∧b3)
    def pares(ordem):
        Bo = BDD(6)
        pos = {name: i + 1 for i, name in enumerate(ordem)}
        r = 0
        for k in (1, 2, 3):
            r = Bo.apply(OR, r, Bo.apply(AND, Bo.var(pos[f"a{k}"]), Bo.var(pos[f"b{k}"])))
        return Bo.size(r)[0]

    print("   ordem a1<b1<a2<b2<a3<b3:", pares(["a1", "b1", "a2", "b2", "a3", "b3"]), "nodos")
    print("   ordem a1<a2<a3<b1<b2<b3:", pares(["a1", "a2", "a3", "b1", "b2", "b3"]), "nodos")
    return


if __name__ == "__main__":
    app.run()
