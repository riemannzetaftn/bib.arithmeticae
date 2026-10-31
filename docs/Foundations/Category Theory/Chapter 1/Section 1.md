# Section 1. Categories

In this section we define categories.

!!! definition "Category"

    A *category* $\sfC$ consists of the following data.
    { #def-category }

    - A class of its *objects*, denoted by \(\Ob(\sfC)\), and
    - For each pair \((A,B)\) of its objects, a set of the *morphisms* or *arrows* from $A$ to $B$, denoted by \(\Hom_{\sfC}(A,B)\) (these are called the *Hom-sets*). We denote \(\phi\in\Hom_\sfC(A,B)\) by \(\phi:A\to B\).
    - For each triple \((A,B,C)\) of its objects, a *composition function* \(\circ=\circ_{A,B,C}:\Hom_{\sfC}(B,C)\times\Hom_{\sfC}(A,B)\to\Hom_{\sfC}(A,C)\), \((\phi,\psi)\mapsto \phi\circ\psi\).

    These data are subject to the following conditions.

    - The classes \(\Hom_\sfC(A,B)\) are disjoint for distinct pairs \((A,B)\).
    - For each object \(A\), there exist a morphism \(\id_A:A\to A\), called the *identity* of \(A\), such that for every \(B\in\Ob(\sfC)\), \(\phi:A\to B\) and \(\psi:B\to A\), \(\phi = \phi\circ\id_A\) and \(\psi = \id_A\circ\psi\).
    - For each quadruple \((A,B,C,D)\) of objects, and each triple \((\phi:C\to D,\psi:B\to C,\varphi:A\to B)\) of morphisms, we have *associativity* \(\phi\circ(\psi\circ\varphi) = (\phi\circ\psi)\circ\varphi\).

    Given a category \(\sfC\), we define the followings.

    - Given a morphism \(\phi:A\to B\) in \(\sfC\), \(A\) is called a *domain* (or a *source*) of \(\phi\) and \(B\) is called a *codomain* (or a *target*) of \(\phi\).
    - A morphism \(\phi:A\to B\) in \(\sfC\) is called an *isomorphism* if there exist an *inverse* \(\psi:B\to A\), which satisfies \(\psi\circ\phi = \id_A\) and \(\phi\circ\psi = \id_B\).
    - Two objects \(A\) and \(B\) of \(\sfC\) are said to be *isomorphic* if there is an isomorphism \(\phi:A\to B\), and this is denoted by \(A\cong B\).
    - Given an object \(A\) of \(\sfC\), any morphism \(\phi:A\to A\) is called an *endomorphism* of \(A\), and an endomorphism which is an isomorphism is called an *automorphism* of \(A\). The set of endomorphisms and automorphisms of \(A\) are denoted by \(\End_\sfC(A)\) and \(\Aut_\sfC(A)\).

We observe the followings.

- From the first assumption, the domain and codomain of any morphism is uniquely determined, and there's no ambiguity in omitting subscript \(A,B,C\) from the composition symbol \(\circ\). Therefore, we speak of 'the' domain and 'the' codomain from now on. The pair \((\phi,\psi)\) of morphisms is said to be *composable* if the domain of \(\phi\) equals the codomain of \(\psi\), so that the composition \(\phi\circ\psi\) is defined.
- If a morphism \(\phi:A\to B\) in \(\sfC\) has inverses \(\psi,\varphi\), then we have
    
    \[\psi = \psi\circ\id_B = \psi\circ(\phi\circ\varphi) = (\psi\circ\phi)\circ\varphi = \id_A\circ\varphi = \varphi.\]
    
    That is, inverse of a morphism is unique provided that it exists, and we shall speak of 'the' inverse. The inverse of \(\phi\), if exists, is also denoted by \(\phi^{-1}\).
- The relation of being isomorphic is

    - Reflexive, since for any object \(A\), \(\id_A:A\to A\) satisfies \(\id_A\circ\id_A = \id_A\), so that it is the inverse of itself, and is an isomorphism.
    - Symmetric, since for an isomorphism \(\phi:A\to B\), its inverse \(\psi:B\to A\) is also an isomorphism as \(\phi\) is its inverse by definition.
    - Transitive, since for isomorphisms \(\phi:A\to B\) and \(\psi:B\to C\), \(\psi\circ\phi:A\to C\) is an isomorphism with the inverse \(\phi^{-1}\circ\psi^{-1}\):
        
        \begin{align*}
            (\phi^{-1}\circ\psi^{-1})\circ(\psi\circ\phi) &= \phi^{-1}\circ(\psi^{-1}\circ(\psi\circ\phi))\\
            &= \phi^{-1}\circ((\psi^{-1}\circ\psi)\circ\phi)\\
            &= \phi^{-1}\circ(\id_B\circ\phi)\\
            &= \phi^{-1}\circ\phi\\
            &= \id_A
        \end{align*}
        
        and similarly \((\psi\circ\phi)\circ(\phi^{-1}\circ\psi^{-1}) = \id_C\).
- The set \(\End_\sfC(A)\) is a monoid, with \(\id_A\) being the identity and composition being the multiplication. Then \(\Aut_\sfC(A)\) is its subset of invertible elements, hence form a group.
    
    Therefore, the relation of being isomorphic is an equivalence relation, and we sometimes identify those objects.

When the category \(\sfC\) is obvious from context, we may omit this in the notations. For instance, we may denote the set of morphisms, isomorphisms, endomorphisms and automorphisms by \(\Hom(A,B), \End(A)\) and \(\Aut(A)\).

We now introduce the most typical examples of categories, from various fields of mathematics. Note that in practice, we can always force the first assumption (disjointness of Hom-sets), as in the formal definition of functions in set theory (we include the domain and codomain in the definition of a function), so we don't bother about it.

!!! example "Category"

    1. The category \(\Set\) has sets as its objects, and functions between those sets as morphisms between the objects. The conditions are verified in set theory. A function is an isomorphism if and only if it is a bijection, and two sets are isomorphic if and only if they have the same cardinality. The automorphisms of a set \(A\) are also called the 'permutations' of \(A\), and \(\Aut_\Set(A)\) is often denoted by \(\Sym(A)\).
    { #ex-category }
    2. The category \(\Set_\ast\) consists of 'pointed sets' (i.e. a pair \((A,a)\) of a set \(A\) and its element \(a\)) and 'pointed maps' between them (i.e. a pointed map from \((A,a)\) to \((B,b)\) is a function \(f:A\to B\) with \(f(a) = b\)).
    3. Partially ordered sets and order-preserving maps between them form a category \(\poSet\), whose isomorphisms are order-isomorphisms (i.e. a bijective order-preserving maps).
    4. In algebra, we have bunch of algebraic structures, and each with structure-preserving functions form categories. In the below examples, isomorphisms are exactly the bijective morphisms (since inverse function is also a morphism).

        - \(\Mnd\): monoids and monoid homomorphisms.
        - \(\cMnd\): commutative monoids and monoid homomorphisms between them.
        - \(\Grp\): groups and group homomorphisms.
        - \(\Ab\): abelian groups and group homomorphisms between them.
        - \(\Ring\): (unital) rings and (unital) ring homomorphisms between them. (Throughout this blog, 'ring' and 'ring homomorphism' will always denote unital ones.)
        - \(\cRing\): commutative rings and ring homomorphisms between them.
        - \(\Dom\): integral domains and injective ring homomorphisms between them. (The choice of morphisms is on purpose: we shall shortly see its convenience while dealing with universal property of field of fractions.)
        - \(\Field\): fields and ring homomorphisms between them.
        - For each field \(k\), the category \(\Vec_k\) consists of \(k\)-vector spaces and \(k\)-linear maps between them. More generally, for each ring \(R\), the category \(R-\Mod\) (resp. \(\Mod-R\)) consists of left (resp. right) \(R\)-modules and \(R\)-linear maps between them. For these categories, we have another abbreviation for sets of morphisms: we denote them by \(\Hom_R(M,N)\), \(\End_R(M)\), and \(\Aut_R(M)\). If \(R\) is commutative, we simply denote the category by \(\Mod_R\).
        - For each commutative ring \(R\) (including the case of \(R = k\) being a field), the category \(\Alg_R\) consists of \(R\)-algebras (i.e. a ring \(S\) with a ring homomorphism \(\varphi:R\to S\) (or the homomorphism \(\varphi\) itself) whose image lie inside the center of \(S\)) and \(R\)-algebra homomorphisms (if \(\varphi:R\to S\) and \(\psi:R\to T\) represents two \(R\)-algebras, an \(R\)-algebra homomorphism from former to latter is a ring homomorphism \(\phi:S\to T\) with \(\phi\circ\varphi = \psi\)).
        - For each commutative ring \(R\), the category \(\cAlg_R\) consists of commutative \(R\)-algebras (i.e. a ring homomorphism \(\varphi:R\to S\) with \(S\) being a commutative ring) and \(R\)-algebra homomorphisms between them.
        - For each field \(k\), the category \(\LieAlg_k\) consists of Lie algebras over \(k\) with Lie algebra homomorphisms between them.
        - For each commutative \(\ast\)-ring \(R\), \(\ast\)-algebras over \(R\) (an \(R\)-algebra with an involution \(\ast\) satisfying some conditions) and \(\ast\)-algebra homomorphisms form a category.
    
    5. Similarly, in topology and geometry, there are bunch of geometric structures, and each with structure-preserving functions form categories.

        - \(\Top\): topological spaces and continuous functions.
        - \(\CHaus\): compact Hausdorff spaces and continuous functions (which are necessarily closed maps).
        - \(\Top_\ast\): pointed topological spaces (i.e. a pair \((X,x)\) of a topological space \(X\) and a point \(x\in X\)) and pointed continuous maps between them (i.e. a pointed continuous map from \((X,x)\) to \((Y,y)\) is a continuous map \(f:X\to Y\) with \(f(x) = y\)).
        - \(\hTop\): topological spaces and homotopy classes of continuous functions between them, where isomorphisms are homotopy equivalences.
        - \(\hTop_\ast\): pointed topological spaces and basepoint-preserving-homotopy classes of pointed continuous maps between them.
        - \(\Mfd\): topological manifolds and continuous functions.
        - \(\sMfd\): smooth manifolds and smooth maps.
        - \(\cMfd\): complex manifolds and holomorphic maps.
        - \(\Var_k\): abstract varieties over an algebraically closed field \(k\) and morphisms between them.
        - \(\LRS\): locally ringed spaces and their morphisms.
        - \(\Sch\): schemes and morphisms of schemes.
    
    6. We now look at examples in analysis / probability or ergodic theory.

        - Metric spaces with morphisms (continuous functions / uniformly continuous functions / Lipschitz functions / \(1\)-Lipschitz functions) form categories. Similarly, metrizable spaces with continuous functions form a category.
        - Uniform spaces and uniformly continuous functions.
        - Measurable spaces and measurable maps.
        - Measure spaces / probability spaces and measure-preserving maps.
        - Measure-preserving dynamical systems and their homomorphisms.
        - Banach spaces and bounded linear maps.
        - Hilbert spaces and bounded linear / unitary maps.
    
    7. There are structures where different structures are intertwined, and they form categories.

        - \(\tGrp\): topological groups and continuous group homomorphisms.
        - \(\tRing\): topological rings and continuous ring homomorphisms.
        - For each topological field \(k\), the category \(\tVec_k\) consists of topological vector spaces over \(k\) and continuous \(k\)-linear maps.
        - \(\LieGrp\): Lie groups (which are smooth manifolds and groups at the same time, with some conditions) and Lie group homomorphisms (smooth maps which are group homomorphisms).
        - Banach (resp. Banach \({}^\ast\)-, C\({}^\ast\)-) algebras with Banach (resp. B\({}^\ast\)-, C\({}^\ast\)-) algebra homomorphisms.
        - Locally compact abelian groups and continuous group homomorphisms.

Note that in the most of the above examples, the objects are sets with additional structures, and morphisms are functions between the underlying sets preserving some structures (such categories are informally referred to as *concrete categories*). But this need not be the case, as in the examples of \(\hTop\) and \(\hTop_\ast\); as long as we can define the compositions in a way that satisfies the assumptions, the objects and morphisms can be anything. Let us illustrate this with more examples.

!!! example "Elementary Categories"

    1. Sets and binary relations (which is a generalization of functions, and we can compose relations) between them form a category \(\Rel\).
    { #ex-elementary-categories }
    2. Any set \(S\) can be considered as a category (let us denote this temporarily by \(\sfS\)), whose only morphisms are identities: i.e. \(\Hom_\sfS(a,b)\) is empty if \(a\neq b\), and is a singleton \(\{\id_a\}\) if \(a = b\). This is called a *discrete category* with underlying set \(S\). The followings are the first examples of discrete categories.
        - When \(S = 0 = \emptyset\), we obtain the *empty category*, which we denote by \(\mathsf{0}\), is a category with no object or morphisms.
        - When \(S = 1 = \{0\}\) is a singleton, we obtain the category \(\mathsf{1}\) with unique object \(\ast\) and unique morphism \(\id_\ast\).
    3. A monoid \(M = (M,e,\cdot)\) is equivalent to a category with one object (let us denote this temporarily by \(\sfM\)). We let \(\ast\) denote the unique object, and let \(\Hom_\sfM(\ast,\ast) = M\), where \(e = \id_\ast\) and \(\cdot\) being the composition; the monoid axioms exactly says that the result is a category. Any category with unique object leads to a monoid, by the last observation after the defintion of categories. Under this correspondence, a group corresponds to a category with unique object, where all morphisms are isomorphisms. By a slight generalization, a groupoid can be thought of a category (possibly with many objects) where all morphisms are isomorphisms.
    4. Any poset \((P,\le)\) can be considered as a category (denoted by \(\sfP\) here), called the *poset categories*, where the relation \(\le\) serves as morphisms; i.e. \(\Hom_\sfP(a,b)\) is empty unless \(a\le b\), in which case it is a singleton. The axioms corresponds to the poset axiom (reflexivity and transitivity). The followings are special cases.
        - The category \(\mathsf{2}\) is induced from the poset \(2 = \{0,1\}\) with usual order.
        - For any set \(S\), the equality \(=\) is a partial order, and the induced poset category is the same as the discrete category with underlying set \(S\). Thus discrete categories are poset categories.
        - The posets \(\bbN, \bbZ_{\ge0}, \bbZ\) with usual order, their subsets such as intervals \(\{n,n+1,\cdots,n+k\}\), and \(\bbN\) with divisibility order form poset categories.
        - For any topological space \(X\), the topology (collection of open sets) form a poset under inclusion, and the induced poset category is denoted by \(\Op(X)\). In other words, this is a category with objects being open subsets of \(X\) and morphisms being inclusion of those open subsets.
    5. There is a category \(\Mat_R\), whose objects are natural numbers and morphisms \(n\to m\) are the \(n\times m\) matrices with coefficients in \(R\), and the composition is given by matrix multiplication. In this case, \(\End(n)\) is the set of \(n\times n\) square matrices, and \(\Aut(n)\) is the group \(\GL_n(R)\) of invertible \(n\times n\) square matrices.
    6. Any directed graph \(G\) induces a category, whose objects are vertices, morphisms between two vertices are finite paths between them, the composition is concatenation of the paths, and the identities are the empty paths.
        - The graph of two vertices and two distinct edges from a vertice to another induces a category, where all non-identity morphisms are drawn as in the following diagram.
            ```tikzcd
                \begin{tikzcd}
                    \bullet \arrow[rr, shift left = 5pt]\arrow[rr, shift right = 5pt] & &\bullet
                \end{tikzcd}
            ```
        - Other such graphs include the followings, whose induced categories are also poset categories.
            ```tikzcd
                \begin{tikzcd}
                    \bullet & &\bullet \arrow[ll]\arrow[rr] & &\bullet, &\bullet \arrow[rr] & &\bullet & &\bullet \arrow[ll]
                \end{tikzcd}
            ```

We now look at some elementary constructions on the categories.

!!! definition "First Constructions on Categories"

    1. A *subcategory* \(\sfD\) of a category \(\sfC\) is a category with \(\Ob(\sfD)\subset\Ob(\sfC)\) and \(\Hom_{\sfD}(A,B)\subset\Hom_{\sfC}(A,B)\) for each \(A, B\in\Ob(\sfD)\), where identities and compositions are inherited from that of \(\sfC\). It is called a *full subcategory* if for each \(A,B\in\Ob(\sfD)\), we have \(\Hom_{\sfD}(A,B) = \Hom_\sfC(A,B)\). We write \(\sfD\subset\sfC\) if \(\sfD\) is a subcategory of \(\sfC\). 
    { #def-1st-const-categories }
    2. A *congruence* on a category \(\sfC\) is a family of equivalence relations \(\sim = \sim_{A,B}\) on each \(\Hom_\sfC(A,B)\), such that given \(\phi_1,\phi_2\in\Hom_\sfC(A,B)\) with \(\phi_1\sim\phi_2\) and any morphisms \(\varphi:A'\to A\), \(\psi:B\to B'\), \(\phi_1\circ\varphi\sim\phi_2\circ\varphi\) and \(\psi\circ\phi_1\sim\psi\circ\phi_2\); i.e. the relations are preserved by compositions. If \(\sim\) is a congruence on \(\sfC\), the *quotient category of \(\sfC\) by \(\sim\)*, denoted by \(\sfC/\sim\), is the category whose objects are the same as \(\sfC\), and the morphisms are quotient sets \(\Hom_\sfC(A,B)/\sim_{A,B}\), where the identity and compositions are inherited (the definition of congruence ensures that the inherited compositions are well-defined). 
    3. The *product category* of two categories \(\sfC\) and \(\sfD\) is the category given by \(\Ob(\sfC\times\sfD) = \Ob(\sfC)\times\Ob(\sfD)\),

        \[\Hom_{\sfC\times\sfD}((A,C),(B,D)) = \Hom_{\sfC}(A,B)\times\Hom_{\sfD}(C,D),\]
        
        and the composition being defined componentwisely. Of course, one can extend this construction to arbitrary family of categories, as long as the product of object classes exists as a class.
    4. The *opposite category* of a category \(\sfC\), denoted by \(\sfC^\op\), is given by \(\Ob(\sfC^\op) = \Ob(\sfC)\) and \(\Hom_{\sfC^\op}(B,A) = \Hom_{\sfC}(A,B)\). To avoid confusion, the morphism \(\phi:A\to B\) in \(\sfC\), when considered as a morphism in \(\sfC^\op\), will be denoted by \(\phi^\op:B\to A\). The composition is defined as follows: given morphisms \(\phi^\op:B\to A\) and \(\psi^\op:C\to B\), \(\phi^\op\circ\psi^\op := (\psi\circ\phi)^\op:C\to A\). The identity is ketp the same.
    4. Let \(A\) be an object of a category \(\sfC\). The *overcategory* or *slice category* \(\sfC/A\) is defined as follows: an object is a morphism \(\varphi:B\to A\) in \(\sfC\) with target \(A\), and a morphism from \(\varphi:B\to A\) to \(\psi:C\to A\) is a morphism \(\phi:B\to C\) such that \(\varphi = \psi\circ\phi\). The objects are also called the *objects of \(\sfC\) over \(A\)*. Similarly, the *undercategory* or *coslice category* \(A/\sfC\) is defined as follows: an object is a morphism \(\varphi:A\to B\) in \(\sfC\) with source \(A\), and a morphism from \(\varphi:A\to B\) to \(\psi:A\to C\) is a morphism \(\phi:B\to C\) such that \(\psi = \phi\circ\varphi\). Its objects are also called the *objects of \(\sfC\) under \(A\)*.

!!! example "First Constructions on Categories"

    1. If \(\sfD\) consists of given subsets \(\Ob(\sfD)\subset\Ob(\sfC)\) and \(\Hom_\sfD(A,B)\subset\Hom_\sfC(A,B)\), then for \(\sfD\) to be a subcategory of \(\sfC\) under the inherited identity and composition, it is necessary and sufficient that each \(\Hom_\sfD(A,A)\) contain \(\id_A\) and that the morphisms are closed under composition. The followings are usual examples of subcategories.
    { #ex-1st-const-categories }

        - By the observation right after the definition of categories, for any category \(\sfC\), the collection of all objects of \(\sfC\) and the collection of all isomorphisms of \(\sfC\) form a subcategory of \(\sfC\), which is a groupoid.
        - \(\Set\) is a subcategory of \(\Rel\).
        - \(\Ab\subset\Grp\subset\Mnd\). Both inclusions define full subcategories. Also, one may replace \(\Grp\) by the category of commutative monoids without changing the conclusion.
        - \(\Field\subset\Dom\subset\cRing\subset\Ring\), and \(\cAlg_R\subset\Alg_R\) for \(R\in\Ob(\cRing)\). All inclusions except for the second one define full subcategories.
        - \(\CHaus,\Mfd\) are full subcategories of \(\Top\).
        - Metrizable topological spaces with continuous functions form a subcategory of \(\Top\).
        - Metric spaces with \(1\)-Lipschitz functions / Lipschitz functions / uniformly continuous functions / continuous functions form a chain of subcategories.
        - Locally compact groups with continuous maps form a subcategory of \(\TGrp\).
        - Given a category \(\sfC\), the discrete category with underlying set \(\Ob(\sfC)\) is a subcategory of \(\sfC\).
        - \(\Sch\) is a subcategory of \(\LRS\).
        - Given a category \(\sfC\) and its object \(A\), the monoid \(\End_\sfC(A)\) induces a category with one object, which is a subcategory of \(\sfC\).
        - If \(S'\) is a subset of \(S\), then the induced discrete categories form a full subcategory \(\sfS'\to\sfS\).
        - If \(M'\) is a submonoid of \(M\), then the induced categories form a subcategory \(\sfM'\subset\sfM\). It is a full subcategory if and only if \(M' = M\). In particular, this includes the concept of subgroups.
        - If \(Q\) is a subset of a partially ordered set \(P\), then \(Q\) is itself a partially ordered set under inherited order, and the induces poset categories form a full subcategory \(\sfQ\subset\sfP\). In particular, if \(U\) is an open subset of \(X\), then \(\Op(U)\) is a subcategory of \(\Op(X)\), and inclusion of subsets induce inclusion of full subcategory of associated discrete categories.
        - If \(H\) is a subgraph of a graph \(G\), then the induced categories form a subcategory.

        There are non-examples that one needs to be careful: giving more structures do not form subcategories in general. For instance, \(\Grp\) is not a subcategory of \(\Set\): a group \((G,\cdot)\) is more than the underlying set \(G\), and non-isomorphic groups can have same underlying set. Similarly, \(\Ring\) is not a subcategory of \(\Ab\), \(\Top\) is not a subcategory of \(\Set\), metric spaces with continuous functions or the uniform spaces with uniformly continuous functions do not form subcategories of \(\Top\), \(\cMfd\) is not a subcategory of \(\sMfd\), \(\sMfd\) is not a subcategory of \(\Mfd\), \(\LieGrp\) is not a subcategory of \(\tGrp\), and so on.
    2. The category \(\hTop\) is the quotient category of \(\Top\) where the congruence is given by homotopy. Similarly, \(\hTop_\ast\) is the quotient category of \(\Top_\ast\) where the congruence is given by basepoint-preserving homotopy. If we consider a category induced from a monoid \(M\), then the congruence corresponds to congruence relation of monoids, and the quotient category is just the category induced from the corresponding quotient monoid. If the given category is induced from a group, then the quotient category corresponds to quotient groups (one can show that the equivalence class \(N = [e]\) forms a normal subgroup, and the congruence relation is equal to the congruence modulo \(N\)).
    3. Product categories themselves do not give many interesting examples, so we introduce only elementary examples.

        - The discrete category with underlying set \(S_1\times S_2\) is the product category of two discrete categories with underlying sets \(S_1\), \(S_2\).
        - The category induced from product monoid \(M_1\times M_2\) is the product category of two categories induced from monoids \(M_1, M_2\).
    4. The under category is opposite of over category: precisely, we have \(A/\sfC = (\sfC^\op/A)^\op\).
    5. \(\cAlg_R\) is the coslice category \(R/\cRing\).

!!! remark "Grothendieck Universe"

    Note that in the above we define \(\Ob(\sfC)\) to be a class, and in the most of the above examples the objects form a proper class. Later, we shall give more constructions of categories and in the process, sometimes, the size explodes and we no longer have categories. One way is to assume existence of a 'Grothendieck universe', a set \(U\) with the following properties.
    { #rmk-Grothendieck.universe }

    - If \(y\in x\in U\), then \(y\in U\).
    - If \(x, y\in U\), then \(\{x, y\}, (x, y)\) and \(x\times y\in U\).
    - If \(x\in U\), then \(\caP(x)\in U\) and \(\cup x\in U\).
    - \(\bbN\in U\).
    - If \(f:a\to b\) is a surjective function and \(a\in U\), \(b\subset U\), then \(b\in U\).
    
    That is, this is a set where all classical mathematical operations can be done. Elements of a fixed universe are called the *small sets*.
    
    So we fix a universe \(U\), and we remedy the above examples to only include small objects; i.e. small sets, posets, groups, rings, and so on, which is enough for our practical purpose. Then the resulting classes \(\Ob(\sfC)\) are all sets (which might be not small itself). **Accordingly, from now on, we shall require that the class of objects of any category to be a set.** If \(\Ob(\sfC)\) is itself small, and each \(\Hom_\sfC(A,B)\) is small, then we say that \(\sfC\) is a *small category*. Then we can build categories over small categories with no foundational problem.

    However, checking if some built-up category is indeed consists of sets, or if it is small, is tedious. For this reason, in this blog, we shall deliberately ignore these foundational issues. We shall construct as we wish, on the belief that we can reduce the size if necessary.