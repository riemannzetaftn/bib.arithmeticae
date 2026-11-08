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
    5. In \(\Top\), \(\CHaus\), \(\Mfd\), \(\sMfd\) and \(\cMfd\), the empty space and singleton spaces are initial and final. In \(\hTop\), the empty space is still initial, and contractible spaces (which are homotopy equivalent to singleton spaces) are final. In \(\hTop_\ast\), the contractible spaces are both initial and final.
    6. In discrete categories with more than one object, there is no initial or final object. In one-object categories (identified with a monoid) has no initial or final object, unless the monoid is trivial so that the unique object is both initial and final.
    7. In a poset category, an element is an initial object if and only if it is the minimum, and is a final object if and only if it is the maximum.
    8. In the category of [](<../Chapter 1/Section 1.md#ex-elementary-categories>) 5, there is no initial or final object, as there are two distinct morphisms between two objects.
    9. In \(\Cat\), the empty category \(\mathsf{0}\) is initial and the category \(\mathsf{1}\) is final.

You might notice that the above initial and final objects of usual categories are rather trivial and boring. More important and interesting examples comes from more complex, built-up categories.

!!! definition "Universal Morphism"

    Let \(\caF:\sfC\to\sfD\) be a functor and \(B\in\Ob(\sfD)\). A *universal morphism* from \(\caF\) to \(B\) is the final object in the category \(\caF/B\), and a *universal morphism* from \(\caF\) to \(B\) is the initial object in the category \(B/\caF\).