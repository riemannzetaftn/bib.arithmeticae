# Section 2. Finite and Algebraic Extensions

Throughout this section, let \(K/F\) be a field extension. Since \(K/F\) is an \(F\)-algebra, it is an \(F\)-vector space.

!!! definition "Degree and Finite Extension"

    The *degree* of the extension \(K/F\) is the dimension \(\dim_F K\), and is denoted by \([K:F]\). If \([K:F]<\infty\), we say that the extension is *finite*.

Note that the degree is always positive, since \(F\) is a subspace of \(K\).

!!! proposition

    Let \(L/K/F\) be extensions of fields. We have \([L:F] = [L:K][K:F]\), and in particular the extension \(L/F\) is finite if and only if both extensions \(L/K, K/F\) are finite.

!!! proof

    Let \((\alpha_i)_{i\in I}\) be an \(F\)-basis of \(K\) and \((\beta_j)_{j\in J}\) be a \(K\)-basis of \(L\). We claim that the set \((\alpha_i\beta_j)_{(i,j)\in I\times J}\) is an \(F\)-basis of \(L\).

    First, every element of \(L\) is a finitely supported sum \(\sum_{j}b_j\beta_j\) where \(b_j\in K\), and each \(b_j\) is a finitely supported sum \(\sum_{i}a_{ij}\alpha_i\) where \(a_{ij}\in F\). Thus every element of \(L\) is a finitely supported sum \(\sum_{i,j}a_{ij}\alpha_{i}\beta_j\). If a finitely supported sum \(\sum_{i,j}a_{ij}\alpha_i\beta_j\) is zero, then as \((\beta_j)_{j\in J}\) is \(K\)-linearly independent, we have \(\sum_ia_{ij}\alpha_i = 0\) for all \(j\in J\). Since \((\alpha_i)_{i\in I}\) is \(F\)-linearly independent we have \(a_{ij} = 0\) for all \(i,j\). Thus the claim is proved.

    Since the degree is always positive, the second claim follows.

The finite extensions are closely related to algebraic extensions.

!!! definition "Zeros and Algebraic / Transcendental Extension"

    For any \(\alpha\in K\), there is unique morphism of \(F\)-algebras \(F[x]\to K\) sending \(x\) to \(\alpha\), and we denote this by \(f\mapsto f(\alpha)\). If \(f(\alpha) = 0\), we say that \(\alpha\) is a *zero* of \(f\). An element \(\alpha\) of \(K\) is called *algebraic over \(F\)* if there is a nonzero polynomial \(f\in F[x]\) having \(\alpha\) as its zero, and otherwise it is called *transcendental over \(F\)*. The extension \(K/F\) is called *algebraic*, or \(K\) is *algebraic over \(F\)*, if every element of \(K\) is algebraic over \(F\), and otherwise (i.e. if there exist a transcendental element) \(K/F\) called *transcendental* or \(K\) is *transcendental over \(F\)*. When \(\alpha\in K\) is algebraic over \(F\), there is unique monic polynomial in \(F[x]\) vanishing at \(\alpha\) with minimal degree, which is called the *minimal polynomial of \(\alpha\) over \(F\)*, and denoted by \(m_{\alpha,F}\). The degree of minimal polynomial is called the *degree* of \(\alpha\) over \(F\).

We shall talk about transcendental extensions later, and now focus on algebraic extensions. Let us observe the followings.

- An element \(\alpha\) is a zero of a polynomial \(f\) iff \(f\) lies in the kernel of the morphism \(F[x]\to K\). The kernel is a prime ideal of the Euclidean domain \(F[x]\), hence is of the form \((g)\) for some irreducible polynomial \(g\), or \((0)\). Thus \(\alpha\) is transcendental iff the kernel is \((0)\), and otherwise (i.e. it is algebraic) we have \(f(\alpha) = 0\) iff \(g\) divides \(f\). The generator \(g\) is determined up to a nonzero scalar multiple, hence it is unique if we force it to be monic. Moreover, it is the unique monic irreducible polynomial having \(\alpha\) as a zero, and by the division algorithm it is the unique monic polynomial with minimal degree among the ones having \(\alpha\) as a zero. This establishes well-definedness of minimal polynomial.
- If \(E/F\) is a subextension of \(K/F\) and \(\alpha\in E\), then the evaluation map into \(K\) factors through \(E\); we have decomposition \(F[x]\to E\to K\). Since the map \(E\to K\) is injective, the kernel is the same regardless of the codomain. Thus the minimal polynomial is the same for any subfield of \(K\) containing \(F(\alpha)\) (or a further extension of \(K\)), hence the notation \(m_{\alpha,F}\) is legitimate.
- The minimal polynomial may change if we change the base field: for instance, the minimal polynomial of \(\alpha\in K/F\) over \(F(\alpha)\) is simply the polynomial \(x-\alpha\), but if \(\alpha\notin F\) it is not the minimal polynomial over \(F\). In general, we only have divisibility: since \(m_{\alpha,F}\in F[x]\subset E[x]\) vanishes at \(\alpha\), \(\alpha\) is algebraic over the larger subfield \(E\), and \(m_{\alpha,E}\mid m_{\alpha,F}\).
    { #obs-minimal-poly-base-change }

The above definition reads to the following description of simple extensions.

!!! proposition "Simple Extension"

    Let \(\alpha\in K/F\) and consider the evaluation homomorphism \(F[x]\to K\), \(x\mapsto\alpha\).
    { #prop-simple-ext }

    1. If \(\alpha\) is transcendental over \(F\), then the homomorphism is injective and induces the isomorphism \(F(x)\cong F(\alpha)\).
    2. If \(\alpha\) is algebraic over \(F\) with \(d = \deg m_{\alpha,F}\), then the homomorphism induces an isomorphism of fields \(F[x]/(m_{\alpha,F})\cong F(\alpha)\). In particular \(F(\alpha) = F[\alpha]\) is finite over \(F\) with \(F\)-basis \(1,\alpha,\dots,\alpha^{d-1}\), so that \([F(\alpha):F] = d\); the degree of an algebraic element is the degree of the simple extension it generates.

!!! proof

    The first item is clear by definition and the universal property of field of fractions. This explains the coincidence of notations for the field of rational functions and the simple extensions in this special case. Indeed, the field of rational functions \(F(x)\) is a simple extension generated by \(x\) in \(F(x)\) itself.

    If \(\alpha\in K\) is algebraic, the kernel of the homomorphism \((m_{\alpha,F})\) is a nonzero prime ideal of the PID \(F[x]\), hence is a maximal ideal. Thus the induced injective homomorphism \(F[x]/(m_{\alpha,F})\to K\) is a morphism of fields. The image equals the simple extension \(F(\alpha)\): indeed, the image is a subfield of \(K\) containing \(F\) and \(\alpha\), and any such subfield must contain the image, as the image consists of polynomials with variable \(\alpha\). In particular, we have \(F(\alpha) = F[\alpha]\); the \(F\)-algebra generated by \(\alpha\) is in fact a subfield of \(K\). Moreover, the division algorithm shows that it is a finite extension of degree \(\deg(m_{\alpha,F})\), since \(1, x, \cdots, x^{d-1}\) is an \(F\)-basis.

!!! remark
    
    Finding inverse of a polynomial in \(\alpha\) in \(K\) can be done by Euclidean algorithm with the minimal polynomial \(m_{\alpha,F}\); if \(f\notin(m_{\alpha,F})\), then their gcd is \(1\), and finding \(g,h\in F[x]\) with \(fg + hm_{\alpha,F} = 1\) gives the inverse \(g\) of \(f\) modulo \(m_{\alpha,F}\).

!!! corollary

    If \((\alpha_i)_{i\in I}\) is a family of algebraic elements of \(K/F\), then \(F(\alpha_i:i\in I) = F[\alpha_i:i\in I]\).

!!! proof

    By induction with [](#prop-simple-ext) 2, using inductive formula of finitely generated extensions, we see that if \(\alpha_1, \alpha_2, \cdots, \alpha_n\) are algebraic elements of \(K/F\), then the subfield \(F(\alpha_1,\cdots,\alpha_n) = F[\alpha_1, \cdots, \alpha_n]\); note that \(\alpha_{i+1}\) is algebraic over \(F(\alpha_1,\cdots,\alpha_{i})\) by [the base change](#obs-minimal-poly-base-change). For general index sets, note that every element of a field extension \(F(\alpha_i:i\in I)\) consists of rational functions with variables in \(\alpha_i\), and every such element lies in a finitely generated subextension \(F(\alpha_1,\cdots,\alpha_n) = F[\alpha_1,\cdots,\alpha_n]\subset F[\alpha_i:i\in I]\).