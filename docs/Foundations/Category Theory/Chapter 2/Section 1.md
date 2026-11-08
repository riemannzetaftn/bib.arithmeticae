# Section 1. Introduction

The concept of universal properties has many different realizations, and we begin with the most simple one.

!!! definition "Universal Object"

    Let \(\sfC\) be a category. An object \(A\) of \(\sfC\) is said to be
    
    - an *initial object* of \(\sfC\), or is *initial* in \(\sfC\), if for every object \(B\) of \(\sfC\) there is unique morphism \(A\to B\).
    - a *final object* of \(\sfC\), or is *final* in \(\sfC\), if for every object \(B\) of \(\sfC\) there is unique morphism \(B\to A\).
    - a *universal object* of \(\sfC\), or is *universal* in \(\sfC\), if it is an initial or a final object of \(\sfC\).

    The property of being universal in \(\sfC\) is called the *universal property* in \(\sfC\).

We first observe the followings.

- An object \(A\) of \(\sfC\) is initial (resp. final) in \(\sfC\) iff it is final (resp. initial) in \(\sfC^\op\). That is, two concepts are dual to each other.
- Universal properties determine an object uniquely, up to a unique isomorphism.

    - If \(A\) is initial, and \(\phi:A'\to A\) is an isomorphism, then \(A'\) is also initial, since the maps \(\Hom_\sfC(\phi,B)\) are bijections.
    - Conversely, if \(A\) and \(A'\) are both initial, then there are unique morphisms \(\phi:A\to A'\) and \(\phi':A'\to A\). Their compositions \(\phi'\circ\phi:A\to A\) and \(\phi\circ\phi':A'\to A'\) are the unique morphisms from \(A\) and \(A'\), hence must be the identities \(\id_A\) and \(\id_{A'}\). Thus the unique morphisms \(\phi, \phi'\) are isomorphisms which are inverses to each other.

    In this sense, we shall speak of 'the' initial (resp. final, universal) object.

Again, we start with examples.

!!! example "Universal Object"

    1. In \(\Set\), the empty set is initial, and the singletons are final. In \(\Set_\ast\), the singletons are both initial and final. In \(\poSet\), the empty poset is initial and singleton posets are final. In \(\Rel\), the empty set is both initial and final.
    2. In most categories arise in algebra such as \(\Mnd,\cMnd,\Grp,\Ab,\Vec_k,\fdVec_k,\Mod_R,\LieAlg_k\), there is a *zero object*, which are both initial and final. They consist of one element (usually called the identity or the zero element) and trivial operation between them.
    3. In \(\Ring\) and \(\cRing\), the ring \(\bbZ\) is initial and the zero ring is final. In \(\Alg_R\) and \(\cAlg_R\), the trivial algebra \(R\) is initial and zero algebra is final.
    4. In \(\Field\), there is no initial or final object. In fact, there is no morphism between fields of different characteristic. If we restrict to the full subcategory of fields of fixed characteristic, then \(\bbQ\) is initial in the characteristic \(0\), and \(\bbF_p\) are initial in characteristic \(p\). However, there is no final object. If \(F\) is a final object, then any field \(K\) with the given characteristic is uniquely embedded in \(F\), and in particular \(K\) has no non-trivial automorphisms which would induce different embeddings, but this is not the case for many fields (e.g. \(\bbC\), \(\bbF_{p^n}\)).
    5. The initial object of \(\biLin_R(M,N)\) is the tensor product \(M\otimes_R N\) equipped with natural bilinear map \(M\times N\to M\otimes_R N\), \((m,n)\mapsto m\otimes n\).
    6. In \(\Top\), \(\CHaus\), \(\Mfd\), \(\sMfd\) and \(\cMfd\), the empty space and singleton spaces are initial and final. In \(\hTop\), the empty space is still initial, and contractible spaces (which are homotopy equivalent to singleton spaces) are final. In \(\hTop_\ast\), the contractible spaces are both initial and final.
    7. In discrete categories with more than one object, there is no initial or final object. In one-object categories (identified with a monoid) has no initial or final object, unless the monoid is trivial so that the unique object is both initial and final.
    8. In a poset category, an element is an initial object if and only if it is the minimum, and is a final object if and only if it is the maximum.
    9. In the category of [](<../Chapter 1/Section 1.md#ex-elementary-categories>) 5, there is no initial or final object, as there are two distinct morphisms between two objects.
    10. In \(\Cat\), the empty category \(\mathsf{0}\) is initial and the category \(\mathsf{1}\) is final.

You might notice that the above initial and final objects of usual categories are rather trivial and boring. More important and interesting examples comes from more complex, built-up categories.

!!! definition "Universal Morphism"

    Let \(\caF:\sfC\to\sfD\) be a functor and \(B\in\Ob(\sfD)\). A *universal morphism* from \(\caF\) to \(B\) is the final object in the category \(\caF/B\), and a *universal morphism* from \(\caF\) to \(B\) is the initial object in the category \(B/\caF\).

We observe the followings.

- First, we expand the definition explicitly.
    
    - A universal morphism from \(\caF\) to \(B\) is an ordered pair \((A,\phi)\), where \(A\) is an object of \(\sfC\) and \(\phi:\caF(A)\to B\) is a morphism in \(\sfD\), such that for any other such pair \((A',\phi')\), there exists a unique morphism \(\psi:A'\to A\) in \(\sfC\) such that \(\phi' = \phi\circ\caF(\psi)\). This is described by the following diagram.

        ```tikzcd
            \begin{tikzcd}
                A' \arrow[dd, dashed, "\exists!\psi"{description}] & &\caF(A') \arrow[dd, "\caF(\psi)"{description}]\arrow[drr, "\forall\phi'"{description}]\\
                & & & &B\\
                A & &\caF(A) \arrow[urr, "\phi"{description}]
            \end{tikzcd}
        ```

        (From now on, we shall denote uniquely existing morphisms by dashed arrows.)

    - Dually, a universal morphism from \(B\) to \(\caF\) is an ordered pair \((A,\phi)\) where \(A\) is an object of \(\sfC\) and \(\phi:B\to\caF(A)\) is a morphism in \(\sfD\), such that for any other such pair \((A',\phi')\), there exists a unique morphism \(\psi:A\to A'\) in \(\sfC\) such that \(\phi' = \caF(\psi)\circ\phi\). This is described by the following diagram.

        ```tikzcd
            \begin{tikzcd}
                & &\caF(A) \arrow[dd,"\caF(\psi)"{description}] & &A \arrow[dd,dashed,"\exists!\psi"{description}]\\
                B \arrow[urr,"\phi"{description}]\arrow[drr,"\forall\phi'"{description}]\\
                & &\caF(A') & &A'
            \end{tikzcd}
        ```

        This equals the universal morphism from \(\caF^\op\) to \(B\).

- The universal morphisms are also unique up to unique isomorphism, but in the over / under category: i.e. even though \((A,\phi)\) and \((A',\phi')\) are two universal morphisms, mere isomorphisms \(\psi:A\to A'\) in \(\sfC\) might not be unique, and we need the commutativity assumption to have uniqueness. Thus when we say that a universal morphism is unique, you should keep in mind the exact sense in which this is unique. Having said this, we shall speak of 'the' universal morphism.

- Some authors say that universal properties are properties of being universal morphisms. These turns out to be equivalent in some sense.

    - By definition, universal morphisms are universal objects in the over/under categories.
    - Conversely, any universal object \(A\) of a category \(\sfC\) is in fact equivalent to a universal morphism: for the unique functor \(\Delta_\ast:\sfC\to\mathsf{1}\), we see that the category \(\Delta_\ast/\ast\) is identified (via isomorphism of categories) to \(\sfC\) as the commutativity in \(\mathsf{1}\) is trivial, so that the initial (resp. final) object of \(\sfC\) corresponds to a universal morphism from \(\Delta_\ast\) to \(\ast\) (resp. from \(\ast\) to \(\Delta_\ast\)).

The categories of cones and co-cones also induce interesting universal properties.

!!! definition "Limit and Colimit"

    Let \(\caF:\sfI\to\sfC\) be a diagram. A *limit* of \(\caF\), denoted by \(\lim\caF\), is the final object of the category \(\Cone(\caF)\), and a *colimit* of \(\caF\), denoted by \(\colim\caF\), is the initial object of the category \(\coCone(\caF)\).

We observe the followings.

- We expand the definition again.

    - A limit of \(\caF\) is a cone \((\lim\caF,\pi = (\pi_i)_{i\in\Ob(\sfI)})\) over \(\caF\) such that for any other cone \((N,\psi)\) over \(\caF\), there exists a unique morphism \(\varphi:N\to\lim\caF\) such that for all \(i\in\Ob(\sfI)\), \(\psi_i = \pi_i\circ\varphi\). The corresponding commutative diagram is the following, where \(\phi:i\to j\) is any morphism in \(\sfI\).
        
        ```tikzcd
            \begin{tikzcd}
                &N'\arrow[dd,dashed,"\exists!\varphi"{description}]\arrow[ddddl, bend right = 30, "\psi_i"{description}]\arrow[ddddr, bend left = 30, "\psi_j"{description}]\\
                \\
                &\lim\caF\arrow[ddl, swap, "\pi_i"{description}]\arrow[ddr, "\pi_j"{description}]\\
                \\
                \caF(i) \arrow[rr, "\caF(\phi)"{description}] & &\caF(j)
            \end{tikzcd}
        ```
        
        In this case, the morphism \(\varphi\) is said to be *induced* from the family of morphisms \((\psi_i)\), by the universal property of limit.
    
    - Dually, a colimit of \(\caF\) is a co-cone \((\colim\caF,\iota = (\iota_i)_{i\in\Ob(\sfI)})\) over \(\caF\) such that for any other co-cone \((N,\psi)\) over \(\caF\), there exists a unique morphism \(\varphi:\colim\caF\to N\) such that for all \(i\in\Ob(\sfI)\), \(\psi_i = \varphi\circ\iota_i\). The corresponding commutative diagram is the following, where \(\phi:i\to j\) is any morphism in \(\sfI\).

        ```tikzcd
            \begin{tikzcd}
                \caF(i) \arrow[rr, "\caF(\phi)"{description}]\arrow[ddddr, "\psi_i"{description}, bend right = 30]\arrow[ddr, "\iota_i"{description}] & &\caF(j) \arrow[ddl, "\iota_j"{description}]\arrow[ddddl, "\psi_j"{description}, bend left = 30]\\
                \\
                &\colim\caF \arrow[dd, dashed, "\exists!\varphi"{description}]\\
                \\
                &N
            \end{tikzcd}
        ```
        
        In this case, the morphism \(\varphi\) is said to be *induced* from the family of morphisms \((\psi_i)\), by the universal property of colimit.
    
    Here, we are abusing notations: the notation \(\lim\caF\) (resp. \(\colim\caF\)) will stand for both the limit (resp. colimit), which is an ordered pair, and its underlying object in \(\sfC\).

- The limits and colimits are also unique up to unique isomorphism, but one needs to make sure in which sense the morphism is unique. Having said this, we shall speak of 'the' limit and colimit.
- Being limits or colimits is again equivalent to being universal object or morphisms in a sense.

    - By definition, the limit and colimit of a functor are universal objects in the category of cones and co-cones over the functor. Also, since the category \(\Cone(\caF)\) is identified with the category \(\Delta/\caF\), the limit of \(\caF\) corresponds to the universal morphism from \(\Delta\) to \(\caF\), and since the category \(\coCone(\caF)\) is identified with the category \(\caF/\Delta\), the colimit of \(\caF\) corresponds to the universal morphism from \(\caF\) to \(\Delta\).
    - Conversely, the initial (resp. final) object of a category \(\sfC\) corresponds to the limit (resp. colimit) of empty diagram \(\caF:\mathsf{0}\to\sfC\), since a cone or co-cone over the diagram is nothing but an object of \(\sfC\) (and the categories \(\Cone(\caF),\coCone(\caF)\) are identified with \(\sfC\)).

The examples of universal morphisms and (co)limits will be given in the later sections.