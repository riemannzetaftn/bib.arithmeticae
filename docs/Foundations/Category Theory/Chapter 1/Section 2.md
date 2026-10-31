# Section 2. Functors

A category is a structure where we relate objects by arrows between them. Why not we relate different categories?

!!! definition "Functor"

    1. A *(covariant) functor* \(\caF\) from a category \(\sfC\) to a category \(\sfD\), denoted by \(\caF:\sfC\to\sfD\), consists of the following data:
    { #def-functor }

        - A function \(\Ob(\sfC)\to\Ob(\sfD)\) of objects, also denoted by \(\caF\).
        - For each pair of objects \((A,B)\) of \(\sfC\), a function \(\Hom_{\sfC}(A,B)\to\Hom_\sfD(\caF(A),\caF(B))\) of morphisms, also denoted by \(\caF\).

        These data are subject to the following conditions (called *functorialities*).

        - For any object \(A\) of \(\sfC\), \(\caF(\id_A) = \id_{\caF(A)}\). In words, the functor preserves identities.
        - For any composable pair of morphisms \((\phi:B\to C,\psi:A\to B)\) in \(\sfC\), \(\caF(\phi\circ\psi) = \caF(\phi)\circ\caF(\psi)\). In words, the functor preserves compositions.

    2. A *contravariant functor* \(\caF:\sfC\to\sfD\) is a covariant functor \(\caF:\sfC^\op\to\sfD\). Equivalently, it consists of the following data: 

        - A function \(\caF:\Ob(\sfC)\to\Ob(\sfD)\).
        - For each pair of objects \((A,B)\) of \(\sfC\), a function \(\caF:\Hom_{\sfC}(A,B)\to\Hom_\sfD(\caF(B),\caF(A))\).

        These data are subject to the following conditions (also called functorialities).

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

    1. If \(\sfD\) is a subcategory of \(\sfC\), then the inclusions \(\Ob(\sfD)\hookrightarrow\Ob(\sfC)\) and \(\Hom_\sfD(A,B)\hookrightarrow\Hom_\sfC(A,B)\) form a functor \(\sfD\to\sfC\) since the identities and compositions were inherited, called an *inclusion functor*. The specific examples follow from [](<Section 1.md#ex-1st-const-categories>), 1.
    2. If \(\sim\) is a congruence on a category \(\sfC\), then the identity map on \(\Ob(\sfC)\) and the quotient maps \(\Hom_{\sfC}(A,B)\to\Hom_{\sfC/\sim}(A,B)\) form a functor \(\sfC\to\sfC/\sim\) since the identities and compositions were inherited, called a *quotient functor*.
    3. In [](<Section 1.md#ex-category>), we have seen many examples of concrete categories. If \(\sfC\) is a concrete category, then there is a natural functor \(\caU:\sfC\to\Set\), which sends objects to their underlying sets, and morphisms to their underlying functions. This can be seen as forgetting the additional structure assigned. More generally, if a category \(\sfD\) is obtained by assigning more structure to given category \(\sfC\), then there is a natural functor \(\sfD\to\sfC\) forgetting the structures, and these are **informally** called the *forgetful functors*.
        
        This is not a rigorous concept; depending on what we mean by 'structure', one may even consider every functor forgetful. Hence the following examples should be regarded as examples of functors whose functorialities are evident, and it's not important whether they are really forgetful or not. Many inclusion functors are considered to be forgetful functors, so we do not repeat most of them. Note that the composition of forgetful functors are usually considered to be forgetful again.

        - From every category in [](Section 1.md#ex-category) except for \(\hTop, \hTop_\ast\) to \(\Set\).
        - From \(\Alg_R\) to \(\Ring\) and \(\Mod_R\), and from these to \(\Ab\), where compositions are the same. \(\cAlg_R\to\cRing\to\Ab\). More generally, if \(S\) is a commutative \(R\)-algebra, we have forgetful functors \(\Mod_S\to\Mod_R\), \(\Alg_S\to\Alg_R\), \(\cAlg_S\to\cAlg_R\). \(\LieAlg_k\to\Vec_k\), and from the category of \(\ast\)-algebras over \(R\) to \(\Alg_R\).
        - The above forgetful functor \(\cAlg_R\to\cRing\) has the following generalization: we have forgetful functors \(\sfC/A, A/\sfC\to\sfC\), which forgets the morphism into / from the object \(A\).
        - If we forget addition, we have forgetful functors \(\Ring\to\Mnd\) and \(\cRing\to\cMnd\). As a slight variant, the unit group \(R^\times\) of a ring \(R\) define functors \(\Ring\to\Grp\) and \(\cRing\to\Ab\).
        - \(\hTop_\ast\to\hTop\), \(\cMfd\to\sMfd\to\Mfd\), from \(\Var_k, \LRS, \Sch\) to \(\Top\).
        - From every category in [](Section 1.md#ex-category), 6 to \(\Top\). Metric spaces with \(1\)-Lipschitz / Lipschitz / uniformly continuous functions to uniform spaces with uniformly continuous functions.
        - From measure-preserving systems with their homomorphisms to measure spaces with measure-preserving maps, to measurable spaces with measurable maps.
        - From the category Hilbert spaces with unitary / bounded linear maps to Banach spaces with unitary / bounded linear maps, to metric spaces with \(1\)-Lipschitz / Lipschitz functions.
        - From \(\tGrp\) to both \(\Top\) and \(\Grp\), \(\tRing,\tVec_k\to\tGrp\) by considering only additive structure, from \(\LieGrp\) to both \(\sMfd\) and \(\Grp\).
        - From the category of C\({}^\ast\)-algebras to the category of Banach \({}^\ast\)-algebras, to the category of Banach algebras to the category of Banach spaces and \(\Alg_\bbC\) (the last one only exists if we restrict to the category of unital Banach algebras, or extend \(\Alg_\bbC\) to possibly non-unital \(\bbC\)-algebras).
    4. Conversely, sometimes we may canonically upgrade an object of \(\sfC\) to an object of \(\sfD\), and this forms a functor, called a *free functor*. Again, this is not a rigorous term (but we will elaborate more on the relation of free and forgetful functors in later chapters).
        
        - Given a set \(S\), there is a free monoid \(F(S)\) generated by \(S\). If \(f:S\to T\) is a function, then it induces unique monoid homomorphism \(F(f):F(S)\to F(T)\), which sends the generators \(s\in S\) to the generators \(f(s)\in T\) of \(F(T)\). This association defines a free functor \(\Set\to\Mnd\). Similarly, we have free commutative monoid generated by \(S\), which can be described by the product monoid \(\bbZ_{\ge0}^S\), defining a free functor \(\Set\to\cMnd\). Similarly, there are free functors \(\Set\to\Grp,\Ab,\Ring,\cRing,\Alg_R,\cAlg_R\). For \(\Ab\) it has the form \(S\mapsto\bbZ^S\). For \(\cRing\) and \(\cAlg_R\), they consist of polynomial algebras \(S\mapsto \bbZ[S], R[S]\).
        - The free functor \(\Grp\to\Ab\) is abelianization \(G\mapsto G/[G,G]\), and the free functor \(\Ring\to\cRing\) is the quotient by commutator ideal generated by elements of the form \(ab-ba\). The second generalizes to \(\Alg_R\to\cAlg_R\).
        - The free functor \(\Dom\to\Field\) is the field of fraction \(\Frac\).
        - The free functors \(\Set\to\Mod_R, \Vec_k\) send a set \(S\) to the free module generated by \(S\) (which has the form \(R^{\oplus S}\)), and vector space with basis \(S\).
        - If \(S\) is an \(R\)-algebra, then the tensoring \(M\mapsto M\otimes_R S\) define free functors \(\Mod_R\to\Mod_S\), \(\Alg_R\to\Alg_S\) and \(\cAlg_R\to\cAlg_S\) (if \(S\) is commutative). If \(R = \bbZ\), this becomes \(\Ab\to\Mod_S\), \(\Ring\to\Alg_S\) and \(\cRing\to\cAlg_S\).
        - Given a set \(S\), we can assign discrete topology to form a discrete space with underlying set \(S\), this gives a free functor \(\Set\to\Top\).
    5. The fundamental groups in topology define a functor \(\pi_1:\Top_\ast\to\Grp\), which factors through the quotient functor \(\Top_\ast\to\hTop_\ast\), inducing a functor \(\overline{\pi_1}:\hTop_\ast\to\Grp\). Similarly, the homology groups define functors \(H_n:\Top\to\Ab\) and induced functors \(\hTop\to\Ab\).
    6. We have seen in [](Section 1.md#ex-elementary-categories) how structures of sets, monoids (in particular, groups), posets, graphs induce categories. In fact, the morphisms of those structures induce functors between induced categories. The following examples generalize last four items of [](Section 1.md#ex-first-const-categories) 1, where the functions are injective.

        - If \(f:S\to T\) is a function, then it induces a functor between discrete categories \(\sfS\to\sfT\), which is \(f\) on objects and send \(\id_s\) to \(\id_{f(s)}\); the functoriality is clear, since only composable pairs are identities of the same object.
        - If \(f:M\to N\) is a monoid homomorphism, then it induces a functor \(\sfM\to\sfN\), which send \(\ast\) to \(\ast\), and is \(f\) on morphisms \(\ast\to\ast\). In particular, a group homomorphism induces a functor between induced categories.
        - If \(f:P\to Q\) is an order-preserving map, then it induces a functor between poset categories \(\sfP\to\sfQ\), which is \(f\) on objects, and send the unique morphism \(i\to j\) (i.e. when \(i\le j\)) in \(\sfP\) to the unique morphism \(f(i)\to f(j)\) (as \(f(i)\le f(j)\)). Then the functoriality is clear, since the morphisms with given source and target is unique in poset categories.
        - If \(f:G\to H\) is a morphism of graphs, then it induces a functor between induced categories.
    7. Given a function \(f:A\to B\), its image and inverse image induce order-preserving maps \(f_\ast:\caP(A)\to\caP(B)\) and \(f^\ast:\caP(B)\to\caP(A)\), and the corresponding functors between the poset categories. Moreover, the association is functorial; i.e. assining \(f\) to its (inverse) image map between power sets preserve identity and composition, hence we have two functors \(\Set\to\poSet\) and \(\Set^\op\to\poSet\), which sends a set \(A\) to its power set \(\caP(A)\) and send a function to associated image / inverse image maps.
    8. The general linear groups define functors \(\GL_n:\cRing\to\Grp\), as a ring homomorphism \(\varphi:R\to S\) induces a group homomorphism \(\GL_n(R)\to\GL_n(S)\) obtained by applying \(\varphi\) to each entry. Similarly, the special linear groups define functors.
    9. An action of a monoid \(M\) to a set \(S\) corrensponds to a functor from the induced category \(\sfM\) to \(\Set\), whose image of the unique object \(\ast\) being the set \(S\). Indeed, the only map between morphisms is the map \(M = \End_\sfM(\ast)\to\End_\Set(S)\), and the functoriality is exactly the assumptions for the monoid action. In particular, if we take \(M\) to be a group \(G\), we recover group action, since invertible elements must map to an invertible element, so that the map corestricts to the map \(G\to\Aut_\Set(S)\), and the functoriality says that this is a group homomorphism. Similarly, a \(k\)-linear representation of a group \(G\) is equivalent to a functor \(\sfG\to\Vec_k\).