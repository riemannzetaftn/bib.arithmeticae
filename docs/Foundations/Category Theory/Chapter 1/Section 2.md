# Section 2. Functors

A category is a structure where we relate objects by arrows between them. Why not we relate different categories?

!!! definition "Functor"

    1. A *(covariant) functor* \(\caF\) from a category \(\sfC\) to a category \(\sfD\), denoted by \(\caF:\sfC\to\sfD\), consists of the following data:
    { #def-functor }

        - A function \(\Ob(\sfC)\to\Ob(\sfD)\) of objects, also denoted by \(\caF\).
        - For each pair of objects \((A,B)\) of \(\sfC\), a function \(\Hom_{\sfC}(A,B)\to\Hom_\sfD(\caF(A),\caF(B))\) of morphisms, also denoted by \(\caF\).

        These data are subject to the following conditions.

        - For any object \(A\) of \(\sfC\), \(\caF(\id_A) = \id_{\caF(A)}\). In words, the functor preserves identities.
        - For any composable pair of morphisms \((\phi:B\to C,\psi:A\to B)\) in \(\sfC\), \(\caF(\phi\circ\psi) = \caF(\phi)\circ\caF(\psi)\). In words, the functor preserves compositions.

    2. A *contravariant functor* \(\caF:\sfC\to\sfD\) is a covariant functor \(\caF:\sfC^\op\to\sfD\). Equivalently, it consists of the following data: 

        - A function \(\caF:\Ob(\sfC)\to\Ob(\sfD)\).
        - For each pair of objects \((A,B)\) of \(\sfC\), a function \(\caF:\Hom_{\sfC}(A,B)\to\Hom_\sfD(\caF(B),\caF(A))\).

        These data are subject to the following conditions.

        - For any object \(A\) of \(\sfC\), \(\caF(\id_A) = \id_{\caF(A)}\). In words, the functor preserves identities.
        - For any composable pair of morphisms \((\phi:B\to C,\psi:A\to B)\) in \(\sfC\), \(\caF(\phi\circ\psi) = \caF(\psi)\circ\caF(\phi)\). In words, the functor preserves compositions, but reverses the order.

    The set of functors from \(\sfC\) to \(\sfD\) is denoted by \(\Fun(\sfC,\sfD)\).
    
    For any category \(\sfC\), there is a covariant functor \(\id_\sfC\), called the *identity functor* of \(\sfC\), which consists of identity functions on the sets \(\Ob(\sfC)\), \(\Hom_\sfC(A,B)\).

    Given a pair of covariant functors \(\caG:\sfD\to\sfE\) and \(\caF:\sfC\to\sfD\), we define their *composition* by the covariant functor \(\caG\circ\caF:\sfC\to\sfE\), which consists of compositions 

    ```tikzcd
        \begin{tikzcd}
            \Ob(\sfC) \arrow[rr,"\caF"{description}] & &\Ob(\sfD) \arrow[rr,"\caG"{description}] & &\Ob(\sfE)\\
            \Hom_{\sfC}(A,B) \arrow[rr,"\caF"{description}] & &\Hom_\sfD(\caF(A),\caF(B)) \arrow[rr,"\caG"{description}] & &\Hom_\sfE(\caG(\caF(A)),\caG(\caF(B))).
        \end{tikzcd}
    ```

    Given functors \(\caF:\sfC\to\sfD\) and \(\caG:\sfD\to\sfC\), if \(\caG\circ\caF = \id_\sfC\) and \(\caF\circ\caG = \id_\sfD\), we say that \(\caG\) is the *inverse* of \(\caF\), and \(\caF\) is an *isomorphism of categories*.
    
<!-- A (covariant or contravariant) functor \(\caF:\sfC\to\sfD\) is said to be 

    - *faithful*, if it is injective on morphisms.
    - *full*, if it is surjective on morphisms.
    - *fully faithful*, if it is bijective on morphisms; i.e. it is both full and faithful.
    - *essentially surjective*, if any object \(B\) of \(\sfD\) is isomorphic to \(\caF(A)\) for some object \(A\) of \(\sfC\). -->

Throughout this blog, unless otherwise specified, a functor will denote a covariant one. 
<!-- We observe the followings. The composition of functors is associative, and the identity functors acts as identites of the composition (i.e. for all functors \(\caF:\sfC\to\sfD\), \(\caF\circ\id_\sfC = \caF\) and \(\id_\sfD\circ\caF = \caF\)). Thus the categories and functors form a category, and for the size matter we have a category \(\Cat\) consists of all small categories and functors between them. Of course, even for non-small categories, the observations in the previous section (uniqueness of inverse, \((\caG\circ\caF)^{-1} = \caF^{-1}\circ\caG^{-1}\), etc) hold true. -->

!!! example "Functor"

    1. If \(\sfD\) is a subcategory of \(\sfC\), then the inclusions \(\Ob(\sfD)\hookrightarrow\Ob(\sfC)\) and \(\Hom_\sfD(A,B)\hookrightarrow\Hom_\sfC(A,B)\) form a functor \(\sfD\to\sfC\) since the identities and compositions were inherited, called an *inclusion functor*. The specific examples follow from [](<Section 1.md#ex-1st-const-categories>) 1.
    2. If \(\sim\) is a congruence on a category \(\sfC\), then the identity map on \(\Ob(\sfC)\) and the quotient maps \(\Hom_{\sfC}(A,B)\to\Hom_{\sfC/\sim}(A,B)\) form a functor \(\sfC\to\sfC/\sim\) since the identities and compositions were inherited, called a *quotient functor*.
    3. Many kinds of functions 

<!-- 2. For every concrete category \(\sfC\) where objects are sets with structures, and morphisms are functions preserving the structure, there is a functor into \(\Set\), which sends each object into its underlying set and map each morphism into the underlying function (so that the identity and compositions are preserved). More generally, if a category \(\sfC\) is obtained by assigning more structure and (possibly) more assumption on the morphism, we have a functor \(\sfC\to\sfD\) that forgets the structure and the assumptions, informally called a *forgetful functor*. Hence it is clear that composition of forgetful functors is again a forgetful functor. Specifically, we have the following examples. (Warning: as the term is informal and varies among people, some may disagree with some of these functors. However, the next examples are only for giving plenty of examples of functors, so this is not really important.)

    - From every category in [](Section 1.md#ex-category) except for \(\hTop, \hTop_\ast\) to \(\Set\).
    - \(\Field\to\Dom\to\CRing\to\Ring\to\Ab\to\Grp\to\Mnd\) (where the last two functors are also inclusions), \(\CAlg_R\to\Alg_R\to\Ring\), \(\CAlg_R\to\CRing\), \(\Mod_R\to\Ab\). More generally, if \(S\) is a commutative \(R\)-algebra, we have forgetful functors \(\Mod_S\to\Mod_R\), \(\Alg_S\to\Alg_R\), \(\CAlg_S\to\CAlg_R\). \(\LieAlg_k\to\Alg_k\), and from the category of \(\ast\)-algebras over \(R\) to \(\Alg_R\).
    - \(\hTop_\ast\to\hTop\), \(\CMfd\to\SMfd\to\Mfd\to\Top\), from \(\Var_k, \Sch\) to \(\Top\).
    - From every category in [](Section 1.md#ex-category), 6 to \(\Top\). Metric spaces with \(1\)-Lipschitz functions to metric spaces with Lipschitz functions, to metric spaces with uniformly continuous functions, to metric spaces with continuous functions or to uniform spaces with uniformly continuous functions. From measure-preserving systems with their homomorphisms to measure spaces with measure-preserving maps, to measurable spaces with measurable maps. From the category of Hilbert spaces with unitary maps to Hilbert spaces with bounded linear maps, to Banach spaces with bounded linear maps, to metric spaces with Lipschitz functions.
    - From \(\TGrp\) to both \(\Top\) and \(\Grp\), \(\TRing,\TVec_k\to\TGrp\) by considering only additive structure, from \(\LieGrp\) to both \(\SMfd\) and \(\Grp\). From the category of C\({}^\ast\)-algebras to the category of Banach \({}^\ast\)-algebras, to the category of Banach algebras to the category of Banach spaces and \(\Alg_\bbC\) (the last one only exists if we restrict to the category of unital Banach algebras, or extend \(\Alg_\bbC\) to possibly non-unital \(\bbC\)-algebras).
    - From the category of locally compact abelian groups to \(\TGrp\).
    - From \(\Set\to\Rel\),  -->