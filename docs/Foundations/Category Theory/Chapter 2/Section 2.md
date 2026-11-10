# Section 2. Limits and Colimits

In this section, we discuss details on limits and colimits, starting from common types (the shapes of diagrams) of them.

!!! example "Types of Limits and Colimits"

    1. If the index category \(\sfI\) is the discrete category with underlying set \(I\), then a diagram \(\caF:\sfI\to\sfC\) is equivalent to an indexed family \((A_i)_{i\in I}\) of objects of \(\sfC\), where \(A_i = \caF(i)\); since there are only identity maps, the functoriality is trivial. Also, a cone (resp. co-cone) over \(\caF\) is nothing but a family of morphisms \((\psi_i:A\to A_i)_{i\in I}\) (resp. \((\psi_i:A_i\to A)_{i\in I}\)) for some \(A\in\Ob(\sfC)\), as there is no non-trivial commutativity condition.

        Then the limit of \(\caF\) is called the *product* of the family of objects \((A_i)_{i\in I}\), and is denoted by \(\prod_{i\in I}A_i\). For each \(j\in I\), the natural morphism \(\pi_j:\prod_{i\in I}A_i\to A_j\) is called the *natural projection to \(j\)-th component*. Then the universal property is rephrased as follows: for every family of morphisms \((f_i:A\to A_i)_{i\in I}\), there is a unique morphism \(f:A\to\prod_{i\in I}A_i\) such that \(f_j = \pi_j\circ f\) for all \(j\in I\). We may describe this by the following commutative diagram.

        ```tikzcd
            \begin{tikzcd}
                A \arrow[ddrr, "\forall f_j"{description}]\arrow[dd, dashed, "\exists!f"{description}]\\
                \\
                \prod_{i\in I}A_i \arrow[rr, "\pi_j"{description}] & &A_j
            \end{tikzcd}
        ```

        Dually, the colimit of \(\caF\) is said to be the *coproduct* of the family of objects \((A_i)_{i\in I}\), and is denoted by \(\coprod_{i\in I}A_i\). For each \(j\in I\), the natural morphism \(\iota_j:A_j\to\coprod_{i\in I}A_i\) is called the *natural inclusion from \(j\)-th component*. The universal property says that for every family of morphisms \((f_i:A_i\to A)_{i\in I}\), there is a unique morphism \(f:\coprod_{i\in i}A_i\to A\) s.t \(f_j = f\circ\iota_j\) for all \(j\in I\). In commutative diagrams:
        
        ```tikzcd
            \begin{tikzcd}
                A_j \arrow[rr, "\iota_j"{description}]\arrow[ddrr, "\forall f_j"{description}] & &\coprod_{i\in I}A_i\arrow[dd,"\exists!f"{description},dashed]\\
                \\
                & &A
            \end{tikzcd}
        ```
    2. Let \(\sfI\) be the category where all non-identity morphisms are drawn as in the following diagram.
        
        ```tikzcd
            \begin{tikzcd}
                i \arrow[rr, shift left, "\phi_1"]\arrow[rr, shift right, swap, "\phi_2"] & &j
            \end{tikzcd}
        ```
        
        Then an \(\sfI\)-shaped diagram \(\caF\) in \(\sfC\) is equivalent to two morphisms \(f, g:A\to B\) (where \(f = \caF(\phi_1), g = \caF(\phi_2), A = \caF(i)\) and \(B = \caF(j)\)). A cone (resp. co-cone) over \(\caF\) is just a morphism \(h:C\to A\) with \(f\circ h = g\circ h\) (resp. \(h:B\to C\) with \(h\circ f = h\circ g\)), as the morphism from \(C\) to \(B\) (resp. from \(A\) to \(C\)) is then determined by commutativity.

        In this case, the limit of \(\caF\) is called the *equalizer* of \(f\) and \(g\), and denoted by \(\eq(f,g)\). Letting \(\iota:\eq(f,g)\to A\) be the natural morphism, we have the following universal property; for every morphism \(h:C\to A\) such that \(f\circ h = g\circ h\) (i.e. \(h\) 'equalizes' \(f\) and \(g\)), there is a unique morphism \(\tilde{h}:C\to\eq(f,g)\) s.t \(h = \iota\circ\tilde{h}\). Thus the following diagram commutes.

        ```tikzcd
            \begin{tikzcd}
                C \arrow[drr,"\forall h"{description}]\arrow[dd, "\exists!\tilde{h}"{description},dashed]\\
                & &A \arrow[rr, shift left, "f"]\arrow[rr, shift right, swap, "g"] & &B\\
                \eq(f,g) \arrow[urr, "\iota"{description}]
            \end{tikzcd}
        ```

        Dually, the colimit of \(\caF\) is called the *coequalizer* of \(f\) and \(g\), denoted by \(\coeq(f,g)\). Letting \(\pi:B\to\coeq(f,g)\) be the natural morphism, we have the following universal property; for every morphism \(h:B\to C\) such that \(h\circ f = h\circ g\) (i.e. \(h\) 'coequalizes' \(f\) and \(g\)), there is a unique morphism \(\tilde{h}:\coeq(f,g)\to C\) s.t \(h = \tilde{h}\circ\pi\). In other words, we have the following commutative diagram.

        ```tikzcd
            \begin{tikzcd}
                & & & &\coeq(f,g) \arrow[dd, "\exists!\tilde{h}"{description}, dashed]\\
                A \arrow[rr, shift left, "f"]\arrow[rr, shift right, swap, "g"] & &B \arrow[urr, "\pi"{description}]\arrow[drr, "\forall h"{description}]\\
                & & & &C
            \end{tikzcd}
        ```
    3. Let \(\sfI\) be the category whose all non-identity morphisms are drawn as in the following diagram.

        ```tikzcd
            \begin{tikzcd}
                i_1 \arrow[rr, "\phi_1"{description}] & &i_3 & &i_2 \arrow[ll, "\phi_2"{description}]
            \end{tikzcd}
        ```
        
        Then an \(\sfI\)-shaped diagram \(\caF\) in \(\sfC\) is equivalent to two morphisms \(f:A\to C, g:B\to C\) (where \(A = \caF(i_1), B = \caF(i_2), C = \caF(i_3), f = \caF(\phi_1), g = \caF(\phi_2)\)). A cone over such \(\caF\) is a pair of morphisms \(\phi:D\to A, \psi:D\to B\) such that \(f\circ\phi = g\circ\psi\), as the morphism \(D\to C\) is then determined by commutativity.

        Then the limit of \(\caF\) is called the *pullback* of \(\caF\) or \(f, g\), or the *fibered product* of \(A, B\) over \(C\), often denoted by \(A\times_C B\). Letting \(\pi_1:A\times_C B\to A\) and \(\pi_2:A\times_C B\to B\) be the natural morphisms, we have the following universal property. For every pair of morphisms \(\phi:D\to A, \psi:D\to B\) with \(f\circ\phi = g\circ\psi\), there is a unique morphism \(\varphi:D\to A\times_C B\) such that \(\phi = \pi_1\circ\varphi\) and \(\psi = \pi_2\circ\varphi\). In other words, we have the following commutative diagram.

        ```tikzcd
            \begin{tikzcd}
                D \arrow[drrr, "\phi"{description}, bend left = 15]\arrow[dddr, "\psi"{description}, bend right = 15]\arrow[dr, "\exists!\varphi"{description}, dashed]\\
                &A\times_C B \arrow[rr, "\pi_1"{description}]\arrow[dd, "\pi_2"{description}] & &A\arrow[dd, "f"{description}]\\
                \\
                &B \arrow[rr, "g"{description}] & &C
            \end{tikzcd}
        ```
        
        Note that equivalently, \(A\times_C B\) is the product of \(f, g\) in the over category \(\sfC/C\). This explains the name of fibered product.
    4. Let \(\sfI\) be the opposite category of the category introduced right before. Alternatively, we have

        ```tikzcd
            \begin{tikzcd}
                i_2 & &i_1 \arrow[ll, "\phi_1"{description}]\arrow[rr, "\phi_2"{description}] & &i_3
            \end{tikzcd}
        ```
        
        Then an \(\sfI\)-shaped diagram \(\caF\) in \(\sfC\) is equivalently two morphisms \(f:A\to B, g:A\to C\) (where \(A = \caF(i_1), B = \caF(i_2), C = \caF(i_3), f = \caF(\phi_1), g = \caF(\phi_2)\)). A co-cone over such \(\caF\) is a pair of morphisms \(\phi:B\to D, \psi:C\to D\) such that \(\phi\circ f = \psi\circ g\), as the morphism \(A\to D\) is then determined by commutativity.

        The colimit of such \(\caF\) is called the *pushout* of \(\caF\) or \(f, g\), or *fibered coproduct* of \(B, C\) under \(A\), often denoted by \(B\coprod_A C\). Letting \(\iota_1:B\to B\coprod_A C\) and \(\iota_2:C\to B\coprod_A C\) be the natural morphisms, we have the following universal property. For every pair of morphisms \(\phi:B\to D\), \(\psi:C\to D\) with \(\phi\circ f = \psi\circ g\), there is a unique morphism \(\varphi:B\coprod_A C\to D\) s.t \(\phi = \varphi\circ\iota_1\) and \(\psi = \varphi\circ\iota_2\). In other words, we have the following diagram.

        ```tikzcd
            \begin{tikzcd}
                A \arrow[rr, "f"{description}]\arrow[dd, "g"{description}] & &B \arrow[dd, "\iota_1"{description}]\arrow[dddr, "\phi"{description}, bend left = 15]\\
                \\
                C \arrow[rr, "\iota_2"{description}]\arrow[drrr, "\psi"{description}, bend right = 15] & &B\coprod_A C \arrow[dr, "\exists!\varphi"{description}, dashed]\\
                & & &D
            \end{tikzcd}
        ```
        
        Note that this corresponds to coproduct of \(f, g\) in the under category \(A/\sfC\).
    5. Let \(\sfI\) be a poset category, whose underlying poset \((I,\le)\) is a directed set; i.e. a nonempty poset such that for all \(i, j\in I\), there is \(k\in I\) with \(i, j\le k\). Then the \(\sfI\)-shaped diagrams \(\caF\) in \(\sfC\) are equivalent to a *directed system* in \(\sfC\), directed by \((I,\le)\). This consists of the following data: the collection of objects \((A_i)_{i\in I}\), the collection of morphisms \((f_{ij}:A_i\to A_j)_{i,j\in I, i\le j}\) such that \(f_{ii} = \id_{A_i}\) and \(f_{ik} = f_{jk}\circ f_{ij}\) whenever \(i\le j\le k\). Under the identification \(A_i = \caF(i), f_{ij} = \caF(i\to j)\), the latter conditions correspond to the functoriality. Then a co-cone over such \(\caF\) corresponds to a collection of morphisms \((\psi_i:A_i\to A)_{i\in I}\), such that \(\psi_i = \psi_j\circ f_{ij}\) whenever \(i, j\in I\), \(i\le j\).

        Then the colimit of \(\caF\) is called the *direct limit* or the *injective limit* of the directed system \(((A_i)_{i\in I},(f_{ij})_{i\le j})\), and is denoted by \((\varinjlim A_i,(\iota_i)_{i\in I})\). The universal property is as follows: for every family of morphisms \((\psi_i:A_i\to A)_{i\in i}\) such that \(\psi_i = \psi_j\circ f_{ij}\) whenever \(i, j\in I\), \(i\le j\), there exists a unique morphism \(\varphi:\varinjlim A_i\to A\) s.t \(\psi_i = \varphi\circ\iota_i\). The corresponding diagram is not much different from that of general colimit.
        
        Poset categories with underlying directed sets are special cases of *filtered categories*, which are categories in which every pair of objects (or equivalently, a functor from discrete category with two objects) and every pair of morphisms with same domain and codomain (or equivalently, a functor from the index category introduced in 2) admits a co-cone. Explicitly, a category \(\sfC\) is said to be *filtered* if the following hold.
            
        - For all \(A, B\in\Ob(\sfC)\), there is \(C\in\Ob(\sfC)\) and morphisms \(\varphi:A\to C, \psi:B\to C\).
        - For all morphisms \(\varphi,\psi:A\to B\), there is a morphism \(\phi:B\to C\) s.t \(\phi\circ\varphi = \phi\circ\psi\).

        In case of directed sets, the first condition is true, and the second condition follows since there are at most one morphism between two objects. A colimit of functor from a filtered category is called a *filtered colimit*.
    6. Let \(\sfI\) be as above. Then the \(\sfI^\op\)-shaped diagrams \(\caF\) in \(\sfC\) (in other words, a contravariant functor \(\caF:\sfI\to\sfC\)) are equivalent to the *inverse systems* in \(\sfC\), which consists of the following data; a collection of objects \((A_i)_{i\in I}\), a collection of morphisms \((f_{ij}:A_j\to A_i)_{i,j\in I,i\le j}\) such that \(f_{ii} = \id_{A_i}\) and \(f_{ik} = f_{ij}\circ f_{jk}\) whenever \(i\le j\le k\). Under the identification \(A_i = \caF(i), f_{ij} = \caF(i\to j)\), the latter conditions correspond to the functoriality. Then a cone over such \(\caF\) corresponds to a collection of morphisms \((\psi_i:A\to A_i)_{i\in I}\) such that \(\psi_i = f_{ij}\circ\psi_j\) whenever \(i\le j, i, j\in I\).

        Then the limit of \(\caF\) is called the *inverse limit* or the *projective limit* of the inverse system \(((A_i)_{i\in I}, (f_{ij})_{i\le j})\), and is denoted by \((\varprojlim A_i,(\pi_i)_{i\in I})\). The universal property is as follows. For every family of morphisms \((\psi_i:A\to A_i)_{i\in I}\) s.t \(\psi_i = f_{ij}\circ\psi_j\) whenever \(i\le j, i, j\in I\), there exists a unique morphism \(\varphi:A\to\varprojlim A_i\) s.t \(\psi_i = \pi_i\circ\varphi\) for all \(i\in I\). The diagram is not much different from general diagram for limits.

        The categories \(\sfI^\op\) are special cases of *cofiltered categories*, which are categories in which every pair of objects (or equivalently, a functor from discrete category with two objects) and every pair of morphisms with same domain and codomain (or equivalently, a functor from the index category introduced in 2) admits a cone. Explicitly, a category \(\sfC\) is said to be *cofiltered* if the following hold.
            
        - For all \(A, B\in\Ob(\sfC)\), there is \(C\in\Ob(\sfC)\) and morphisms \(\varphi:C\to A, \psi:C\to B\).
        - For all morphisms \(\varphi,\psi:A\to B\), there is a morphism \(\phi:C\to A\) s.t \(\varphi\circ\phi = \psi\circ\phi\).

        In case of opposite of directed sets, the first condition is true, and the second condition follows since there are at most one morphism between two objects. A limit of functor from a cofiltered category is called a *cofiltered limit*.
    7. A category \(\sfI\) is called *finite* if both \(\Ob(\sfI)\) and \(\Hom(\sfI)\) are finite, and a diagram \(\caF:\sfI\to\sfC\) is called *finite* if the index category is finite. The limits and colimits of a finite diagrams are called the *finite (co)limits*. For instance, (co)product of finitely many objects, (co)equalizers, pullback and pushour are finite (co)limits.

We have seen that universal object (and hence (co)limits) might not exist, depending on the category. Thus we are primarily concerned with their existence. If they exist, then we wish to compute them; i.e. their formula in terms of data of the diagram. There are many ways to do this, and here we present the most basic principle.

!!! theorem

    Let \(\caF:\sfI\to\sfC\) be a diagram.

    - Suppose that the products \(\prod_{i\in\Ob(\sfI)}\caF(i)\) and \(\prod_{\phi\in\Hom(\sfI)}\caF(\cod(\phi))\) exist. Then there are two natural morphisms from the former to the latter, and if their equalizer exists, it forms the limit of \(\caF\).
    - Suppose that the coproducts \(\coprod_{i\in\Ob(\sfI)}\caF(i)\) and \(\coprod_{\phi\in\Hom(\sfI)}\caF(\dom(\phi))\) exist. Then there are two natural morphisms from the latter to the former, and if their coequalizer exists, it forms the colimit of \(\caF\).

!!! proof

    We first consider the limits. Given a morphism \(\phi\) of \(\sfI\), there is a family of morphisms \(\pi_{\cod(\phi)}:\prod_{i\in\Ob(\sfI)}\caF(i)\to\caF(\cod(\phi))\) in \(\sfC\). This family induces a unique morphism \(\phi_1:\prod_{i\in\Ob(\sfI)}\caF(i)\to\prod_{\phi\in\Hom(\sfI)}\caF(\cod(\phi))\). Similarly, the family of morphisms \(\caF(\phi)\circ\pi_{\dom(\phi)}:\prod_{i\in\Ob(\sfI)}\caF(i)\to\caF(\cod(\phi))\) induces a unique morphism \(\phi_2:\prod_{i\in\Ob(\sfI)}\caF(i)\to\prod_{\phi\in\Hom(\sfI)}\caF(\cod(\phi))\).

    We denote their equalizer by \(\epsilon:L\to\prod_{i\in\Ob(\sfI)}\caF(i)\). Then there are morphisms \(\lambda_i:=\pi_i\circ\epsilon:L\to\caF(i)\), and we claim that \((L,\lambda = (\lambda_i)_{i\in\Ob(\sfI)})\) is the limit of \(\caF\).

    - First, we show that it is a cone. For each morphism \(\phi:i\to j\) in \(\sfI\), 

        \begin{align*}
            \caF(\phi)\circ\lambda_i &= \caF(\phi)\circ\pi_i\circ\epsilon &\text{by definition of }\lambda_i\\
            &= \caF(\phi)\circ\pi_{\dom(\phi)}\circ\epsilon &\text{by definition of }\phi\\
            &= \pi_{\phi}\circ\phi_2\circ\epsilon &\text{by definition of }\phi_2\\
            &= \pi_{\phi}\circ\phi_1\circ\epsilon &\text{by definition of }e\\
            &= \pi_{\cod(\phi)}\circ\epsilon &\text{by definition of }\phi_1\\
            &= \pi_j\circ\epsilon &\text{by definition of }\phi\\
            &= \lambda_j &\text{by definition of }\lambda_j.
        \end{align*}
    
    - Second, we show that this cone is universal. Suppose that \((N,\psi)\) is another cone over \(\caF\). Then the morphisms \(\psi_i\) induce a unique morphism \(\varepsilon:N\to\prod_{i\in\Ob(\sfI)}\caF(i)\). We claim that this map equalizes \(\phi_1\) and \(\phi_2\); i.e. \(\phi_1\circ\varepsilon = \phi_2\circ\varepsilon\). For each morphism \(\phi:i\to j\) in \(\sfI\), we have

        \begin{align*}
            \pi_\phi\circ\phi_2\circ\varepsilon &= \caF(\phi)\circ\pi_{\dom(\phi)}\circ\varepsilon &\text{by definition of }\phi_2\\
            &= \caF(\phi)\circ\psi_{\dom(\phi)} &\text{by definition of }\varepsilon\\
            &= \psi_{\cod(\phi)} &\text{since }(N,\psi)\text{ is a cone over }\caF\\
            &= \pi_{\cod(\phi)}\circ\varepsilon &\text{by definition of }\varepsilon\\
            &= \pi_{\phi}\circ\phi_2\circ\varepsilon &\text{by definition of }\phi_2.
        \end{align*}

        That is, two morphisms \(\phi_1\circ\varepsilon\) and \(\phi_2\circ\varepsilon\) are induced by the same family of morphisms, by the universal property of the product \(\prod_{\phi\in\Hom(\sfI)}\caF(\cod(\phi))\), and they must be the same, as claimed.

        Then by the universal property of the equalizer \(\epsilon\), there exists a unique morphism \(\varphi:N\to L\) such that \(\varepsilon = \epsilon\circ\varphi\). We claim that this is in fact a morphism of cones \(\varphi:(N,\psi)\to(L,\lambda)\). Indeed, for every object \(i\) of \(\sfI\), we have

        \begin{align*}
            \lambda_i \circ \varphi &= \pi_i\circ\epsilon\circ\varphi &\text{by definition of }\lambda_i\\
            &= \pi_i\circ\varepsilon &\text{by definition of }\varphi\\
            &= \psi_i &\text{by definition of }\varepsilon.
        \end{align*}