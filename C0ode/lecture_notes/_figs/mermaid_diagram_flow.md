
## Solution by Substitution

### ① Homogeneous Equation:
Given:
\[
M(x, y)dx + N(x, y)dy = 0
\]

It is homogeneous if:
\[
M(tx, ty) = t^k M(x, y) \quad \text{and} \quad N(tx, ty) = t^k N(x, y)
\]

So, substitutions:
- \( y = ux \)
- \( x = vy \)

---

### ② Bernoulli's Equation:
\[
\frac{dy}{dx} + P(x)y = F(x)y^n
\]

If \( n \ne 1 \) or \( n \ne 0 \), use:
- Substitution: \( u = y^{1-n} \)
- Then use **Integrating Factor Method**

If \( n = 0, 1 \): Apply integrating factor method directly.

---

### ③ Reduction to Separation of Variables:
Given:
\[
\frac{dy}{dx} = F(Ax + By + C)
\]
If \( B \ne 0 \),

So, substitution:
- \( u = Ax + By + C \)

---

## General Strategy:
Given:
\[
M(x, y)dx + N(x, y)dy = 0
\]

1. Check if it's homogeneous:
   - If yes → Substitute \( y = ux \) or \( x = vy \)
2. Else, check if it's exact:
   - If yes → Solve as exact
   - If not → Try to make exact using integrating factor

Note: Homogeneous is a special case of exact.

---

## Special Integrating Factor Cases:

### If \( \mu \) only depends on \( x \):
\[
\mu_y = 0
\quad \Rightarrow \quad \mu = e^{\int \frac{N_x - M_y}{M} dx}
\]
\( \mu \) must be function of \( x \) only.

### If \( \mu \) only depends on \( y \):
\[
\mu_x = 0
\quad \Rightarrow \quad \mu = e^{\int \frac{M_y - N_x}{N} dy}
\]
\( \mu \) must be function of \( y \) only.

### In general:
\[
\mu = \frac{1}{M_x + N_y}
\]

### If you can factor \( x \) and \( y \) separately:
\[
\mu = \frac{1}{M_y - N_x}
\]

---

*(See diagram of strategy and flow in the Mermaid chart included below)*
