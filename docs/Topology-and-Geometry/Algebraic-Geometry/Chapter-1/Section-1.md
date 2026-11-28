# Section 1. Affine Schemes

In this section, we introduce affine schemes, which are local models of schemes, just as Euclidean spaces are local models of manifolds in topology and differential geometry. Throughout this section, let \(R\) be a (commutative) ring.

!!! definition "Spectrum of a Ring"

    The spectrum \(\Spec(R)\) of a ring \(R\), is defined by the set 

    \[\{\frp\subset R:\frp\text{ is a prime ideal of }R\}.\]

    We also define the followings.

    - Given a subset \(A\) of \(R\), its *vanishing locus* \(\V(A)\) is defined by the subset

        \[\{\frp\in\Spec(R):\frp\supset A\}.\]

    - Given an element \(r\) of \(R\), the associated *principal open subset* \(\D(r)\) is defined by the subset 

        \[\Spec(R) - \V(\{r\}) = \{\frp\in\Spec(R):\frp\not\ni r\}.\]