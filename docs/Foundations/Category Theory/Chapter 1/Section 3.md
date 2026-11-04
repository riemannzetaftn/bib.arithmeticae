# Section 3. Natural Transformations and Equivalence of Categories

So far, we defined categories, which consists of objects and their morphisms, and functors, which are morphisms of categories. We now introduce natural transformations, which are morphisms between functors (don't be afraid; this is the last step, and we will not consider morphisms of natural transformations). Natural transformations would help us to understand functors and categories better.

!!! definition "Natural Transformation"

    Let \(\caF,\caG:\sfC\to\sfD\) be functors. A *natural transformation* \(\eta\) from \(\caF\) to \(\caG\), denoted by \(\eta:\caF\to\caG\), is an indexed family \(\eta = (\eta_A)_{A\in\Ob(\sfC)}\) of morphisms \(\eta_A:\caF(A)\to\caG(A)\) in \(\sfD\), which satisfies the *naturality* assumption, that for all morphisms \(\phi:A\to B\) in \(\sfC\), \(\caG(\phi)\circ\eta_A = \eta_B\circ\caF(\phi)\). In other words, the following diagram commutes for all \(\phi:A\to B\) in \(\sfC\).

    ```tikzcd
        \begin{tikzcd}
            \caF(A) \arrow[rr,"\eta_A"{description}]\arrow[dd,"\caF(\phi)"{description}] & &\caG(A) \arrow[dd,"\caG(\phi)"{description}]\\
            \\
            \caF(B) \arrow[rr,"\eta_B"{description}] & &\caG(B)
        \end{tikzcd}
    ```

    For each functor \(\caF:\sfC\to\sfD\), there is *identity (natural) transformation* \(\id_\caF:\caF\to\caF\), consisting of identity morphisms \(\id_{\caF(A)}\). Given natural transformations \(\eta:\caF\to\caG\) and \(\varepsilon:\caG\to\caH\) of functors \(\sfC\to\sfD\), their *(vertical) composition* \(\varepsilon\circ\eta:\caF\to\caH\) consists of compositions \(\varepsilon_{A}\circ\eta_A\) (the naturality is established by pasting two commutative rectangles together). A natural transformation \(\eta:\caF\to\caG\) with inverse (i.e. a natural transformation \(\varepsilon:\caG\to\caF\) such that \(\varepsilon\circ\eta = \id_\caF\) and \(\eta\circ\varepsilon = \id_\caG\)) is called a *natural isomorphism* of functors. If there is a natural isomorphism between \(\caF\) and \(\caG\), we say that two functors are *naturally isomorphic* and write \(\caF\cong\caG\). The set of natural transformations from \(\caF\) to \(\caG\) is denoted by \(\Nat(\caF,\caG)\).

We observe the followings.

- A natural transformation \(\eta:\caF\to\caG\) is a natural isomorphism if and only if each component \(\eta_A\) is an isomorphism in \(\sfD\). If \(\eta\) is a natural isomorphism with inverse \(\varepsilon:\caG\to\caF\), then for each object \(A\) of \(\sfC\) we have \(\varepsilon_A\circ\eta_A = (\varepsilon\circ\eta)_A = (\id_\caF)_A = \id_{\caF(A)}\) and similarly \(\eta_A\circ\varepsilon_A = \id_{\caG(A)}\), so that \(\eta_A:\caG(A)\to\caF(A)\) is an isomorphism with inverse \(\varepsilon_A\). Conversely, if each \(\eta_A\) is an isomorphism, let us denote the inverse by \(\varepsilon_A\). Then they form a natural transformation \(\varepsilon = (\varepsilon_A)\), since from \(\caG(\phi)\circ\eta_A = \eta_B\circ\caF(\phi)\) we obtain \(\varepsilon_B\circ\caG(\phi) = \caF(\phi)\circ\varepsilon_A\).
- The identity and composition of natural transformations satisfy the identity and composition assumption, hence for given categories \(\sfC\) and \(\sfD\), we have a *functor category* \([\sfC,\sfD]\), whose objects are functors \(\sfC\to\sfD\) and morphisms are natural transformations.
- The natural isomorphisms are sometimes compared with homotopy of continuous maps in topology; in fact, a natural isomorphism corresponds to a bifunctor \(\eta:\sfC\times\sfI\to\sfD\), where \(\sfI\) consists of two objects \(0,1\), which are isomorphic via unique isomorphism (hence there are four morphisms, two identities, an isomorphism and its inverse), with \(\eta(\bline,0) = \caF\) and \(\eta(\bline,1) = \caG\), whereas a homotopy of continuous maps \(f,g:X\to Y\) is a continuous map \(H:X\times[0,1]\to Y\) such that \(H(x,0) = f(x)\) and \(H(x,1) = g(x)\).

Here comes the examples.

!!! example "Natural Transformations"

    1. Recall from [](Section 2.md#ex-functor) that \(\GL_n\) and \((\bline)^\times\) (the unit groups) define functors \(\cRing\to\Grp\). Then the determinant defines a natural transformation from \(\GL_n\to(\bline)^\times\); for each commutative ring \(R\), \(\det_R:\GL_n(R)\to R^\times\) is a group homomorphism, and given a ring homomorphism \(f:R\to S\) we have \(f^\times\circ\det_R = \det_S\circ\GL_n(f)\). The naturality implies that the determinant is defined in a uniform way, regardless of structure of each ring.
    2. The inversion maps \(g\mapsto g^{-1}\) define a natural isomorphism from the identity functor to the opposite functor on \(\Grp\): it is a group isomorphism from a group \(G\) to its opposite group \(G^\op\), and for any group homomorphism \(f:G\to H\), we have \(f(g)^{-1}=f^\op(g^{-1})\), proving naturality.
    3. We have a natural transformation from the identity functor on \(\Vec_k\) to the double dual functor, given as follows: for each vector space \(V\), the morphism \(\eta_V:V\to V^{\vee\vee}\) send a vector \(v\) to the linear functional \(\Tilde{v}:V^\vee\to k\), \(\Tilde{v}(f) = f(v)\). This is \(k\)-linear, and the naturality is proved as follows: if \(\phi:V\to W\) is a linear map, then \(\phi^{\vee\vee}(\Tilde{v}) = \Tilde{\phi(v)}\). Indeed, for every \(f\in W^\vee\), \(\phi^{\vee\vee}(\Tilde{v})(f) = (\Tilde{v}\circ\phi^\vee)(f) = \Tilde{v}(\phi^\vee(f)) = \Tilde{v}(f\circ\phi) = f(\phi(v)) = \Tilde{\phi(v)}(f)\). One can see that the maps \(\eta_V\) are injective.

        When restricted to the subcategory \(\fdVec_k\), since the space and its dual (hence the double dual) has the same finite dimension, the maps \(\eta_V\) form a natural isomorphism.
    4. A \(G\)-equivariant map between two \(G\)-sets \(A\) and \(B\) (more generally, morphisms of sets with monoid actions), viewed as functors \(\sfG\to\Set\), is exactly the natural transformations between those functors. Indeed, since there is only one object of \(\sfG\), a natural transformation is a single map \(f:A\to B\), such that for all \(g\in G\), the following diagram commutes.

        ```tikzcd
            \begin{tikzcd}
                A \arrow[rr,"f"{description}]\arrow[dd,"g\cdot"{description}] & &B \arrow[dd,"g\cdot"{description}]\\
                \\
                A \arrow[rr,"f"{description}] & &B
            \end{tikzcd}
        ```

        That is, we have \(g\cdot f(a) = f(g\cdot a)\), or the map is \(G\)-equivariant. This applies to linear representations of groups and \(G\)-modules; that is, the category of \(G\)-sets is identified with functor category \([\sfG,\Set]\), the category of \(k\)-linear representations of \(G\) is identified with \([\sfG,\Vec_k]\), and the category of \(G\)-module is identified with \([\sfG,\Ab]\). This is a first example of functor categories that arise in practice.
    5. 
<!-- cone as a natural transform...? but is this used later? same as categories too? -->