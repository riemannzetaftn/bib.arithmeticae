# Section 3. Natural Transformations and Equivalence of Categories

So far, we defined categories, which consists of objects and their morphisms, and functors, which are morphisms of categories. We now introduce natural transformations, which are morphisms between functors (don't be afraid; this is the last step, and we will not consider morphisms of natural transformations). Natural transformations would help us to understand functors and categories better.

!!! definition "Natural Transformation"

    Let \(\caF,\caG:\sfC\to\sfD\) be functors. A *natural transformation* \(\eta\) from \(\caF\) to \(\caG\), denoted by \(\eta:\caF\to\caG\), is an indexed family \(\eta = (\eta_A)_{A\in\Ob(\sfC)}\) of morphisms \(\eta_A:\caF(A)\to\caG(A)\) in \(\sfD\), such that for all morphisms \(\phi:A\to B\) in \(\sfC\), \(\caG(\phi)\circ\eta_A = \eta_B\circ\caF(\phi)\). In other words, the following diagram commutes for all \(\phi:A\to B\) in \(\sfC\).

    ```tikzcd
        \begin{tikzcd}
            \caF(A) \arrow[rr,"\eta_A"{description}]\arrow[dd,"\caF(\phi)"{description}] & &\caG(A) \arrow[dd,"\caG(\phi)"{description}]\\
            \\
            \caF(B) \arrow[rr,"\eta_B"{description}] & &\caG(B)
        \end{tikzcd}
    ```

    For each functor \(\caF:\sfC\to\sfD\), there is *identity (natural) transformation* \(\id_\caF:\caF\to\caF\), consisting of identity morphisms \(\id_{\caF(A)}\). Given natural transformations \(\eta:\caF\to\caG\) and \(\varepsilon:\caG\to\caH\) of functors \(\sfC\to\sfD\), their *(vertical) composition* \(\varepsilon\circ\eta:\caF\to\caH\) consists of compositions \(\varepsilon_{A}\circ\eta_A\). A natural transformation \(\eta:\caF\to\caG\) with inverse (i.e. a natural transformation \(\varepsilon:\caG\to\caF\) such that \(\varepsilon\circ\eta = \id_\caF\) and \(\eta\circ\varepsilon = \id_\caG\)) is called a *natural isomorphism* of functors. If there is a natural isomorphism between \(\caF\) and \(\caG\), we say that two functors are *naturally isomorphic* and write \(\caF\cong\caG\). The set of natural transformations from \(\caF\) to \(\caG\) is denoted by \(\Nat(\caF,\caG)\).

<!-- This is sometimes compared with homotopy of continuous maps in topology; in fact, a natural transformation can be thought of a bifunctor \(\eta:\sfC\times\mathsf{2}\to\sfD\), where \(\mathsf{2}\) is the category \(\{0\to1\}\), with \(\eta(\bline,0) = \caF\) and \(\eta(\bline,1) = \caG\), whereas a homotopy of continuous maps \(f,g:X\to Y\) is a continuous map \(H:X\times[0,1]\to Y\) such that \(H(x,0) = f(x)\) and \(H(x,1) = g(x)\). -->

Here comes the examples.

!!! example "Natural Transformations"

    1. Recall from [](Section 2.md#ex-functors) that \(\GL_n\) and \((\bline)^\times\) define functors \(\cRing\to\Grp\). Then the determinant defines a natural transformation from \(\GL_n\to(\bline)^\times\); for each commutative ring \(R\), \(\det_R:\GL_n(R)\to R^\times\) is a group homomorphism, and given a ring homomorphism \(f:R\to S\) we have \(f^\times\circ\det_R = \det_S\circ\GL_n(f)\). The naturality implies that the determinant is defined in a uniform way, regardless of structure of each ring.
    2. The inversion maps \(g\mapsto g^{-1}\) define a natural isomorphism from the identity functor to the opposite functor on \(\Grp\): it is a group isomorphism from a group \(G\) to its opposite group \(G^\op\), and for any group homomorphism \(f:G\to H\), we have \(f(g)^{-1}=f^\op(g^{-1})\), proving naturality.