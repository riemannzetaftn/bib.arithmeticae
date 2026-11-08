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
    2. 