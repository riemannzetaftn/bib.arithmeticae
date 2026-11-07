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

    For each functor \(\caF:\sfC\to\sfD\), there is *identity (natural) transformation* \(\id_\caF:\caF\to\caF\), consisting of identity morphisms \(\id_{\caF(A)}\). Given natural transformations \(\eta:\caF\to\caG\) and \(\varepsilon:\caG\to\caH\) of functors \(\sfC\to\sfD\), their *(vertical) composition* \(\varepsilon\circ\eta:\caF\to\caH\) consists of compositions \(\varepsilon_{A}\circ\eta_A\) (the naturality is established by pasting two commutative rectangles together). A natural transformation \(\eta:\caF\to\caG\) with inverse (i.e. a natural transformation \(\varepsilon:\caG\to\caF\) such that \(\varepsilon\circ\eta = \id_\caF\) and \(\eta\circ\varepsilon = \id_\caG\)) is called a *natural isomorphism* of functors. If there is a natural isomorphism between \(\caF\) and \(\caG\), we say that two functors are *naturally isomorphic* and write \(\caF\simeq\caG\). The set of natural transformations from \(\caF\) to \(\caG\) is denoted by \(\Nat(\caF,\caG)\).

We observe the following.

- A natural transformation \(\eta:\caF\to\caG\) is a natural isomorphism if and only if each component \(\eta_A\) is an isomorphism in \(\sfD\). If \(\eta\) is a natural isomorphism with inverse \(\varepsilon:\caG\to\caF\), then for each object \(A\) of \(\sfC\) we have \(\varepsilon_A\circ\eta_A = (\varepsilon\circ\eta)_A = (\id_\caF)_A = \id_{\caF(A)}\) and similarly \(\eta_A\circ\varepsilon_A = \id_{\caG(A)}\), so that \(\eta_A:\caF(A)\to\caG(A)\) is an isomorphism with inverse \(\varepsilon_A\). Conversely, if each \(\eta_A\) is an isomorphism, let us denote the inverse by \(\varepsilon_A\). Then they form a natural transformation \(\varepsilon = (\varepsilon_A)\), since from \(\caG(\phi)\circ\eta_A = \eta_B\circ\caF(\phi)\) we obtain \(\varepsilon_B\circ\caG(\phi) = \caF(\phi)\circ\varepsilon_A\).
- The identity and composition of natural transformations satisfy the identity and composition assumption, hence for given categories \(\sfC\) and \(\sfD\), we have a *functor category* \([\sfC,\sfD]\) (or \(\sfD^\sfC\)), whose objects are functors \(\sfC\to\sfD\) and morphisms are natural transformations.
- The natural isomorphisms are sometimes compared with homotopy of continuous maps in topology; in fact, a natural isomorphism corresponds to a bifunctor \(\eta:\sfC\times\sfI\to\sfD\), where \(\sfI\) consists of two objects \(0,1\), which are isomorphic via unique isomorphism (hence there are four morphisms, two identities, an isomorphism and its inverse), with \(\eta(\bline,0) = \caF\) and \(\eta(\bline,1) = \caG\), whereas a homotopy of continuous maps \(f,g:X\to Y\) is a continuous map \(H:X\times[0,1]\to Y\) such that \(H(x,0) = f(x)\) and \(H(x,1) = g(x)\). More generally, natural transformations correspond to bifunctors \(\sfC\times\mathsf{2}\to\sfD\).

Here comes the examples.

!!! example "Natural Transformations"

    1. Recall from [](Section 2.md#ex-functor) that \(\GL_n\) and \((\bline)^\times\) (the unit groups) define functors \(\cRing\to\Grp\). Then the determinant defines a natural transformation \(\GL_n\to(\bline)^\times\); for each commutative ring \(R\), \(\det_R:\GL_n(R)\to R^\times\) is a group homomorphism, and given a ring homomorphism \(f:R\to S\) we have \(f^\times\circ\det_R = \det_S\circ\GL_n(f)\). The naturality implies that the determinant is defined in a uniform way, regardless of structure of each ring.
    2. The inversion maps \(g\mapsto g^{-1}\) define a natural isomorphism from the identity functor to the opposite functor on \(\Grp\): it is a group isomorphism from a group \(G\) to its opposite group \(G^\op\), and for any group homomorphism \(f:G\to H\), we have \(f(g)^{-1}=f^\op(g^{-1})\), proving naturality.
    3. We have a natural transformation from the identity functor on \(\Vec_k\) to the double dual functor, given as follows: for each vector space \(V\), the morphism \(\eta_V:V\to V^{\vee\vee}\) send a vector \(v\) to the linear functional \(\tilde{v}:V^\vee\to k\), \(\tilde{v}(f) = f(v)\). This is \(k\)-linear, and the naturality is proved as follows: if \(\phi:V\to W\) is a linear map, then \(\phi^{\vee\vee}(\tilde{v}) = \widetilde{\phi(v)}\). Indeed, for every \(f\in W^\vee\), \(\phi^{\vee\vee}(\tilde{v})(f) = (\tilde{v}\circ\phi^\vee)(f) = \tilde{v}(\phi^\vee(f)) = \tilde{v}(f\circ\phi) = f(\phi(v)) = \widetilde{\phi(v)}(f)\). One can see that the maps \(\eta_V\) are injective.

        When restricted to the subcategory \(\fdVec_k\), since the space and its dual (hence the double dual) has the same finite dimension, the maps \(\eta_V\) form a natural isomorphism.
    4. Given a pair of forgetful and free functors, there are natural transformations associated. We shall later see their general theory, and for now just enjoy the examples of natural transformations.

        - The forgetful functor \(\Ab\to\Grp\) and the free functor (the abelianization) form a pair. The abelianization composed with the forgetful functor gives rise to a functor \(\caF:\Grp\to\Grp\), \(G\mapsto G/[G,G]\). Then the quotient maps \(G\to G/[G,G]\) form a natural transformation from \(\id_\Grp\) to \(\caF\). The naturality is in fact a part of definition of abelianization of morphisms.
        - The forgetful functor \(\cAlg_R\to\Set\) and the free functor \(S\mapsto R[S]\) form a pair. The free functor composed with the forgetful functor gives rise to a functor \(R[\bline]:\Set\to\Set\), and there is a natural transformation consisting of inclusion functions \(S\to R[S]\), sending \(s\in S\) to the variable \(s\in R[S]\).
    5. A \(G\)-equivariant map between two \(G\)-sets \(A\) and \(B\) (more generally, morphisms of sets with monoid actions), viewed as functors \(\sfG\to\Set\), is exactly the natural transformations between those functors. Indeed, since there is only one object of \(\sfG\), a natural transformation is a single map \(f:A\to B\), such that for all \(g\in G\), the following diagram commutes.

        ```tikzcd
            \begin{tikzcd}
                A \arrow[rr,"f"{description}]\arrow[dd,"g\cdot"{description}] & &B \arrow[dd,"g\cdot"{description}]\\
                \\
                A \arrow[rr,"f"{description}] & &B
            \end{tikzcd}
        ```

        That is, we have \(g\cdot f(a) = f(g\cdot a)\), or the map is \(G\)-equivariant. This applies to linear representations of groups and \(G\)-modules; that is, the category of \(G\)-sets is identified with the functor category \([\sfG,\Set]\), the category of \(k\)-linear representations of \(G\) is identified with \([\sfG,\Vec_k]\), and the category of \(G\)-module is identified with \([\sfG,\Ab]\). This is a first example of functor categories that arise in practice.
    6. A cone \((N,\psi)\) over a diagram \(\caF:\sfI\to\sfC\) is equivalent to a natural transformation from the constant functor \(\Delta_N\) to the functor \(\caF\), where \(\psi = (\psi_i)_{i\in\Ob(\sfI)}\) is the natural transformation. Indeed, the commutativity assumption is equivalent to the naturality. Dually, a co-cone \((N,\psi)\) of a functor \(\caF\) is equivalent to a natural transformation from \(\caF\) to the \(\Delta_N\). We further observe the following:

        - The product category \(\sfC^I\), where \(I\) is a set, is identified with functor category \([\sfI,\sfC]\), where \(\sfI\) is the discrete category with underlying set \(I\). If \(\caF\) is such a functor, then the collection \((\caF(i))_{i\in\Ob(\sfI)}\) is an object of \(\sfC^I\), and given an object \((A_i)_{i\in\Ob(\sfI)}\) of \(\sfC^I\), the association \(i\mapsto A_i\), \(\id_i\mapsto\id_{A_i}\) defines a functor \(\sfI\to\sfC\). This explains the general notation \(\sfD^\sfC\) of a functor category; it generalizes product categories.
        - There is a *diagonal functor* \(\Delta = \Delta_{\bline}:\sfC\to\sfC^\sfI\) for any categories \(\sfI\) and \(\sfC\), which sends an object \(A\) of \(\sfC\) to the constant functor \(\Delta_A\), and sends a morphism \(\phi:A\to B\) of \(\sfC\) to a natural transformation \(\Delta_\phi:\Delta_A\to\Delta_B\), which consists of the family \((\Delta_\phi)_i = \phi\), which natural as \(\phi\circ\id_A = \phi = \id_B\circ\phi\).
        - Then a cone over \(\caF\) is a natural transformation from some constant functor \(\Delta_N\) to \(\caF\), which is an object of the over category \(\Delta/\caF\); note that \(\caF\) is an object of the functor category \(\sfC^\sfI\). Moreover, a morphism of cones \((N,\psi)\to(N',\psi')\) corresponds to a morphism \(\varphi:N\to N'\) such that the induced natural transformation \(\Delta_\varphi:\Delta_N\to\Delta_{N'}\) satisfies \(\psi = \psi'\circ\Delta_\varphi\). Indeed, the equation reduces to \(\psi_i = \psi'_i\circ\varphi\), as desired.

        As a conclusion, the category \(\Cone(\caF)\) is identified with the category \(\Delta/\caF\). Dually, the category \(\coCone(\caF)\) corresponds to the category \(\caF/\Delta\).
<!-- unit, counit 소개하기... 귀찮음. -->

The natural transformations can also be composed horizontally.

!!! definition "Horizontal Composition"

    Let \(\caF_1,\caG_1:\sfC\to\sfD\) and \(\caF_2,\caG_2:\sfD\to\sfE\) be functors and \(\eta:\caF_1\to\caG_1\), \(\varepsilon:\caF_2\to\caG_2\) be natural transformations. Their *horizontal composition* \(\varepsilon\ast\eta:\caF_2\circ\caF_1\to\caG_2\circ\caG_1\) is defined by 
        
    \[(\varepsilon\ast\eta)_A = \varepsilon_{\caG_1(A)}\circ\caF_2(\eta_A) = \caG_2(\eta_A)\circ\varepsilon_{\caF_1(A)}.\]

We observe the following.

- First, the equality holds by the naturality of \(\varepsilon\): see the following commutative diagram.

    ```tikzcd
        \begin{tikzcd}
            \caF_2(\caF_1(A)) \arrow[dd,"\caF_2(\eta_A)"{description}]\arrow[rr,"\varepsilon_{\caF_1(A)}"{description}] & &\caG_2(\caF_1(A)) \arrow[dd,"\caG_2(\eta_A)"{description}]\\
            \\
            \caF_2(\caG_1(A)) \arrow[rr,"\varepsilon_{\caG_1(A)}"{description}] & &\caG_2(\caG_1(A))
        \end{tikzcd}
    ```
    
- Second, given a morphism \(\phi:A\to B\) in \(\sfC\), consider the following diagram.

    ```tikzcd
        \begin{tikzcd}
            \caF_2(\caF_1(A)) \arrow[dd,"\caF_2(\caF_1(\phi))"{description}]\arrow[rr,"\caF_2(\eta_A)"{description}] & &\caF_2(\caG_1(A)) \arrow[rr,"\varepsilon_{\caG_1(A)}"{description}]\arrow[dd,"\caF_2(\caG_1(\phi))"{description}] & &\caG_2(\caG_1(A)) \arrow[dd,"\caG_2(\caG_1(\phi))"{description}]\\
            \\
            \caF_2(\caF_1(B)) \arrow[rr,"\caF_2(\eta_B)"{description}] & &\caF_2(\caG_1(B)) \arrow[rr,"\varepsilon_{\caG_1(B)}"{description}] & &\caG_2(\caG_1(B))
        \end{tikzcd}
    ```

    The left rectangle is commutative by naturality of \(\eta\) and functoriality of \(\caF_2\) (it is a composition of a commutative diagram and \(\caF_2\)), and the right rectangle is commutative by naturality of \(\varepsilon\), applied to the morphism \(\caG_1(\phi):\caG_1(A)\to\caG_1(B)\). Thus the whole diagram commutes, and we see that the horizontal composition is indeed a natural transformation, and the horizontal composition is well-defined.

- As a special case, suppose that \(\eta = \id_{\caF}\) where \(\caF = \caF_1 = \caG_1\). Then the composition has components \(\varepsilon_{\caF(A)}\), which is a natural transformation \(\caF_2\circ\caF\to\caG_2\circ\caF\). We abbreviate this composition by \(\varepsilon\caF\) or \(\varepsilon_{\caF}\). Similarly, if \(\varepsilon = \id_{\caG}\) where \(\caG = \caF_2 = \caG_2\), then the composition has components \(\caG(\eta_A)\), which is a natural transformation \(\caG\circ\caF_1\to\caG\circ\caG_1\). We abbreviate this composition by \(\caG\eta\). The general horizontal compositions are then expressed by the vertical comopsition of these; the definition becomes \(\varepsilon\ast\eta = \varepsilon\caG_1\circ\caF_2\eta = \caG_2\eta\circ\varepsilon\caF_1\). Note that if \(\varepsilon\) is a natural isomorphism, then so are the compositions \(\varepsilon\caF\) and if \(\eta\) is a natural isomorphism, then so are the compositions \(\caG\eta\). <!--    An example is the case where \(\eta\) is the abelianization maps -->
- The name of vertical and horizontal compositions come from the following visualization.

    ```tikzcd
        \begin{tikzcd}[sep = large]
            \sfC \arrow[rr,bend left = 55,"\caF_1"{name = F1, description}]\arrow[rr,"\caG_1"{name = G1, description}]\arrow[rr,bend right = 55,"\caH_1"{name = H1, description}] & &\sfD \arrow[from = F1, to = G1, "\eta_1"{description}]\arrow[from = G1, to = H1, "\eta_2"{description}]\arrow[rr,bend left = 55,"\caF_2"{name = F2, description}]\arrow[rr,"\caG_2"{name = G2, description}]\arrow[rr,bend right = 55,"\caH_2"{name = H2, description}] & &\sfE \arrow[from = F2, to = G2, "\varepsilon_1"{description}]\arrow[from = G2, to = H2, "\varepsilon_2"{description}]
        \end{tikzcd}
    ```

    The vertical compositions give natural transformations \(\eta_2\circ\eta_1:\caF_1\to\caH_1\) and \(\varepsilon_2\circ\varepsilon_1:\caF_2\to\caH_2\), and horizontal compositions give \(\varepsilon_1\ast\eta_1:\caF_2\circ\caF_1\to\caG_2\circ\caG_1\) and similar ones.

We now introduce the equivalence of categories.

!!! definition "Equivalence of Categories"

    A functor \(\caF:\sfC\to\sfD\) is called an *equivalence of categories*, or simply an *equivalence* if there is a functor \(\caG:\sfD\to\sfC\) such that \(\caG\circ\caF\simeq\id_{\sfC}\) and \(\caF\circ\caG\simeq\id_{\sfD}\). In this case, \(\caG\) is called an *inverse equivalence* of \(\caF\), and \(\sfC\) is said to be *equivalent* to \(\sfD\).

We observe the following.

- This is a weaker notion than the isomorphism of categories, which might be too strong in view of category theory. For instance, consider the category \(\mathsf{1}\), which has unique object and morphism. Given any set \(S\neq\emptyset\), we have a category \(\sfC\) where \(\Ob(\sfC) = S\) and for each \(s_1, s_2\in S\), \(\Hom_{\sfC}(s_1,s_2)\) is a singleton. Then every pair of objects is isomorphic via unique isomorphism, and the category is equivalent to \(\mathsf{1}\); given \(s_0\in S\) we can choose a constant functor \(\mathsf{1}\to\sfC\) with value \(s_0\), and a constant functor \(\sfC\to\mathsf{1}\) to the unique object of \(\mathsf{1}\). Then their compositions become an identity on \(\mathsf{1}\) and a constant functor \(\sfC\to\sfC\) with value \(s_0\), which is naturally isomorphic to the identity functor on \(\sfC\), as the morphisms \(\eta_s:s\to s_0\) form a natural transformation. Indeed, every diagram in \(\sfC\) commutes, since morphisms between given objects are unique. However, if \(|S|>1\), then two categories are never isomorphic. In view of category theory, \(\sfC\) do not necessarily contain more data than \(\mathsf{1}\); every objects are isomorphic, and are not distinguished by the structure of category.
- If we keep the analogy between homotopy and natural isomorphism, this corresponds to homotopy equivalence in topology.
- The equivalence is an equivalence relation of categories. By definition the reflexivity and symmetry are immediate. For transitivity, suppose that \(\caF_1:\sfC\to\sfD\) has an inverse equivalence \(\caG_1\) and \(\caF_2:\sfD\to\sfE\) has an inverse equivalence \(\caG_2\). We claim that \(\caG_1\circ\caG_2:\sfE\to\sfC\) is an inverse equivalence of \(\caF_2\circ\caF_1\). Let \(\eta_1:\caG_1\circ\caF_1\to\id_\sfC\), \(\varepsilon_1:\caF_1\circ\caG_1\to\id_\sfD\), \(\eta_2:\caG_2\circ\caF_2\to\id_\sfD\) and \(\varepsilon_2:\caF_2\circ\caG_2\to\id_\sfE\) be the natural isomorphisms. Then we have 

    \begin{align*}
        \caG_1\circ\caG_2\circ\caF_2\circ\caF_1 &\simeq \caG_1\circ\id_\sfD\circ\caF_1 &\text{via }\caG_1\eta_2\caF_1\\
        &= \caG_1\circ\caF_1\\
        &\simeq \id_\sfC &\text{via }\eta_1
    \end{align*}

    and 

    \begin{align*}
        \caF_2\circ\caF_1\circ\caG_1\circ\caG_2 &\simeq \caF_2\circ\id_\sfD\circ\caG_2 &\text{via } \caF_2\varepsilon_1\caG_2\\
        &= \caF_2\circ\caG_2\\
        &\simeq \id_\sfE &\text{via }\varepsilon_2
    \end{align*}

    as desired.

- Being an inverse equivalence is invariant under natural isomorphism. If \(\caG\) is an inverse equivalence of \(\caF:\sfC\to\sfD\) and \(\caG\simeq\caG'\), then we have

    \begin{align*}
        &\caG'\circ\caF \simeq \caG\circ\caF \simeq \id_\sfC,
        &\caF\circ\caG' \simeq \caF\circ\caG \simeq \id_\sfD
    \end{align*}

    by the horizontal composition of natural isomorphisms with identity transformations.

- Conversely, if exists, inverse equivalence of a functor is unique up to natural isomorphism (i.e. any two inverse equivalence are naturally isomorphic). Suppose that \(\caF:\sfC\to\sfD\) and \(\caG,\caG':\sfD\to\sfC\) are functors with natural isomorphisms \(\eta:\caG\circ\caF\to\id_\sfC\) and \(\varepsilon':\id_\sfD\to\caF\circ\caG'\). Then we have 

    \begin{align*}
        \caG &= \caG\circ\id_\sfD\\
        &\simeq \caG\circ(\caF\circ\caG') &\text{via }\caG\varepsilon'\\
        &= (\caG\circ\caF)\circ\caG'\\
        &\simeq \id_\sfC\circ\caG' &\text{via }\eta\caG'\\
        &= \caG'
    \end{align*}

    as desired. Note that we only used one direction of equivalences, hence we have something more: given that \(\caF\) is an equivalence of categories, with \(\caG\) being its one-sided inverse equivalence (i.e. we only have one of two natural isomorphisms), then \(\caG\) is naturally isomorphic to any inverse equivalence of \(\caF\), and hence is itself an inverse equivalence of \(\caF\) by the previous observation.

!!! definition "Properties of Functors"

    A (covariant or contravariant) functor \(\caF:\sfC\to\sfD\) is said to be 

    - *faithful* (resp. *full*, *fully faithful*) if for each pair \((A,B)\) of objects of \(\sfC\), the map \(\caF:\Hom_\sfC(A,B)\to\Hom_\sfC(\caF(A),\caF(B))\) is injective (resp. surjective, bijective).
    - *essentially surjective*, if any object \(B\) of \(\sfD\) is isomorphic to \(\caF(A)\) for some object \(A\) of \(\sfC\).

We observe the following.

- The inclusion functors are faithful, and it is fully faithful iff the subcategory is full.
- If \(\caF:\sfC\to\sfD\) is fully faithful and \(\caF(\phi)\) is an isomorphism in \(\sfD\), then \(\phi:A\to B\) is an isomorphism in \(\sfC\) (the converse was true for all functors, so we have equivalence). Indeed, if \(\psi:\caF(B)\to\caF(A)\) is the inverse of \(\caF(\phi)\), then \(\psi = \caF(\varphi)\) for some \(\varphi:B\to A\) in \(\sfC\) by fullness, and we have

    \begin{align*}
        \caF(\varphi\circ\phi) &= \caF(\varphi)\circ\caF(\phi) = \psi\circ\caF(\phi) = \id_{\caF(A)} = \caF(\id_A),\\
        \caF(\phi\circ\varphi) &= \caF(\phi)\circ\caF(\varphi) = \caF(\phi)\circ\psi = \id_{\caF(B)} = \caF(\id_B).
    \end{align*}

    and the faithfulness implies that \(\varphi\circ\phi = \id_A, \phi\circ\varphi = \id_B\), so that \(\phi\) is an isomorphism with inverse \(\varphi\).

!!! proposition

    A functor is an equivalence of categories if and only if it is fully faithful and essentially surjective.

!!! proof

    Let \(\caF\) be an equivalence with inverse \(\caG\), and the natural isomorphism \(\eta:\id_{\sfC}\to\caG\circ\caF\). Consider the function
    
    \begin{align*}
        {\small\Hom_{\sfC}(A,B)\xrightarrow{\caF}\Hom_{\sfD}(\caF(A),\caF(B))\xrightarrow{\caG}\Hom_{\sfC}(\caG(\caF(A)),\caG(\caF(B)))\xrightarrow{\eta_B^{-1}\circ(\bline)\circ\eta_A}\Hom_{\sfC}(A,B)}
    \end{align*}
    
    of Hom-sets. This is the identity, since \(\caG(\caF(\phi))\circ\eta_A=\eta_B\circ\id_{\sfC}(\phi) = \eta_B\circ\phi\) by naturality of \(\eta\). This shows that \(\caF\) is injective on Hom-sets, and by symmetry of equivalence, \(\caG\) is also injective on Hom-sets. The rightmost map is a bijection, as the morphisms \(\eta_A,\eta_B^{-1}\) are isomorphisms. Since the composition of two rightmost maps (which are injective) is injective and is also a left inverse to the map \(\caF\), it is bijective. It follows that \(\caF\), being a right inverse to a bijection, is in fact bijective and a two-sided inverse to the composition. Thus \(\caF\) is fully faithful. For given \(B\in\Ob(\sfD)\), we see that \(\caF(\caG(B))\cong B\) by the natural isomorphism \(\caF\circ\caG\simeq\id_{\sfD}\), and \(\caF\) is also essentially surjective.

    Conversely, let \(\caF\) be a fully faithful and essentially surjective functor. Given \(A\in\Ob(\sfD)\), take some \(\caG(A)\in\Ob(\sfC)\) s.t there is an isomorphism \(\varepsilon_A:\caF(\caG(A))\to A\) (we are using the axiom of choice). Also, given \(\phi:A\to B\) in \(\sfD\), let \(\caG(\phi):\caG(A)\to\caG(B)\) be given by the unique morphism s.t \(\caF(\caG(\phi)) = \varepsilon_{B}^{-1}\circ\phi\circ\varepsilon_A\). Then by functoriality and faithfulness of \(\caF\) it follows that \(\caG:\sfD\to\sfC\) is a functor, and by construction \(\varepsilon:\caF\circ\caG\to\id_{\sfD}\) is a natural isomorphism. Thus for given \(A\in\Ob(\sfC)\), there is an isomorphism \(\varepsilon_{\caF(A)}:\caF(\caG(\caF(A)))\to\caF(A)\), and its preimage under \(\caF\) is a morphism \(\eta_A:\caG(\caF(A))\to A\), which is also an isomorphism by the above observation. We shall show that they are natural. Let \(\phi:A\to B\) in \(\sfC\) be given. If we take \(\caF\) to the desired diagram, we have 
    
    ```tikzcd
        \begin{tikzcd}
            \caF(\caG(\caF(A))) \arrow[rr,"\varepsilon_{\caF(A)}"{description}]\arrow[dd,"\caF(\caG(\caF(\phi)))"{description}] & &\caF(A)\arrow[dd, "\caF(\phi)"{description}]\\
            \\
            \caF(\caG(\caF(B))) \arrow[rr,"\varepsilon_{\caF(B)}"{description}] & &\caF(B)
        \end{tikzcd}
    ```
    
    which is commutative by naturality of \(\varepsilon\) applied to the morphism \(\caF(\phi):\caF(A)\to\caF(B)\). Thus by faithfulness, we see that the original diagram also commutes, and \(\eta\) is a natural isomorphism, and \(\caF\) is an equivalence with an inverse \(\caG\).

Next, we show that every category is equivalent to a skeletal one; that is, up to equivalence, isomorphic objects are identified.

!!! definition "Skeletal Category"

    A category \(\sfC\) is called *skeletal* if any two isomorphic objects are equal. A *skeleton* of a category \(\sfC\) is a full subcategory of \(\sfC\) containing exactly one object for each isomorphism class of \(\sfC\).

!!! corollary

    Every category \(\sfC\) is equivalent to any of its skeleton.

!!! proof

    The inclusion of a skeleton into \(\sfC\) is fully faithful and essentially surjective.