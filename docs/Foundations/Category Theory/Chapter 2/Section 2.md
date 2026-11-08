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

        In this case, the limit of \(\caF\) is called the *equalizer* of \(f\) and \(g\), and denoted by \(\eq(f,g)\). Letting \(\iota:\eq(f,g)\to A\) be the natural morphism, we have the following universal property; for every morphism \(h:C\to A\) such that \(f\circ h = g\circ h\) (i.e. \(h\) 'equalizes' \(f\) and \(g\)), there is a unique morphism \(\Tilde{h}:C\to\eq(f,g)\) s.t \(h = \iota\circ\Tilde{h}\). Thus the following diagram commutes.

        ```tikzcd
            \begin{tikzcd}
                C \arrow[drr,"\forall h"{description}]\arrow[dd, "\exists!\Tilde{h}"{description},dashed]\\
                & &A \arrow[rr, shift left, "f"]\arrow[rr, shift right, swap, "g"] & &B\\
                \eq(f,g) \arrow[urr, "\iota"{description}]
            \end{tikzcd}
        ```

        Dually, the colimit of \(\caF\) is called the *coequalizer* of \(f\) and \(g\), denoted by \(\coeq(f,g)\). Letting \(\pi:B\to\coeq(f,g)\) be the natural morphism, we have the following universal property; for every morphism \(h:B\to C\) such that \(h\circ f = h\circ g\) (i.e. \(h\) 'coequalizes' \(f\) and \(g\)), there is a unique morphism \(\Tilde{h}:\coeq(f,g)\to C\) s.t \(h = \Tilde{h}\circ\pi\). In other words, we have the following commutative diagram.

        ```tikzcd
            \begin{tikzcd}
                & & & &\coeq(f,g) \arrow[dd, "\exists!\Tilde{h}"{description}, dashed]\\
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
    4. Let \(\sfI\) be the opposite category of the category introduced in (3) above. Alternatively, we have

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
    5. 