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