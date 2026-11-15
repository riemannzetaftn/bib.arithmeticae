# Section 1. Finite and Algebraic Extensions

Note that any field extension \(K/F\) is an \(F\)-algebra and hence an \(F\)-vector space.

!!! definition "Degree"

    Let \(K/F\) be a field extension. The *degree* of this extension is the dimension \(\dim_F K\), and is denoted by \([K:F]\). If \([K:F]<\infty\), we say that the extension is *finite*.

Note that the degree is always positive, since \(F\) is a subspace of \(K\). We first observe that the degree is multiplicative.

!!! proposition

    Let \(L/K/F\) be extensions of fields. We have \([L:F] = [L:K][K:F]\), and in particular the extension \(L/F\) is finite if and only if both extensions \(L/K, K/F\) are finite.

!!! proof

    Let \((\alpha_i)_{i\in I}\) be an \(F\)-basis of \(K\) and \((\beta_j)_{j\in J}\) be a \(K\)-basis of \(L\). We claim that the set \((\alpha_i\beta_j)_{(i,j)\in I\times J}\) is an \(F\)-basis of \(L\).

    First, every element of \(L\) is a finitely supported sum \(\sum_{j}b_j\beta_j\) where \(b_j\in K\), and each \(b_j\) is a finitely supported sum \(\sum_{i}a_{ij}\alpha_i\) where \(a_{ij}\in F\). Thus every element of \(L\) is a finitely supported sum \(\sum_{i,j}a_{ij}\alpha_{i}\beta_j\). If a finitely supported sum \(\sum_{i,j}a_{ij}\alpha_i\beta_j\) is zero, then as \((\beta_j)_{j\in J}\) is \(K\)-linearly independent, we have \(\sum_ia_{ij}\alpha_i = 0\) for all \(j\in J\). Since \((\alpha_i)_{i\in I}\) is \(F\)-linearly independent we have \(a_{ij} = 0\) for all \(i,j\). Thus the claim is proved.

    Since the degree is always positive, the second claim follows.