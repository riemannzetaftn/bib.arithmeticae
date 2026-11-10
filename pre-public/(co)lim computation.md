# Limit/colimit 계산법 정리

colimit 쪽으로 쓰고, limit은 끝에서 쌍대로 정리합니다. 아래 공식은 모두 Set에서 원소로 확인한 뒤 representable 논증으로 옮기는 방식이라, 해당 (co)limit이 존재하는 임의의 category에서 성립합니다.

## 0. 세팅

- Diagram $D: J \to \mathcal{C}$와 subcategory $I \subseteq J$를 잡습니다. $I$가 full일 필요는 없습니다.
- 핵심 조건은 **모든 $j\in J$에 대해 comma category $j\downarrow I$가 nonempty**라는 것입니다. 즉 모든 $j$에서 $I$의 어떤 object로 가는 화살표가 있어야 하고, 이를 "$I$가 weakly terminal"이라고 부르겠습니다.

## 1. 마스터 공식

$I$가 weakly terminal이면
$$
\operatorname{colim}_J D \;\cong\; \mathrm{Coeq}\Big( \coprod_{j} \coprod_{c \in \pi_0(j\downarrow I)\setminus\{c_0\}} D(j) \;\rightrightarrows\; \operatorname{colim}_I D|_I \Big)
$$
입니다.

- 각 $j$마다 $\pi_0(j\downarrow I)$의 성분별 대표 $(s_c, f_c: j\to s_c)$를 고르고, 기준 성분 $c_0$를 하나 정합니다.
- 두 화살표는 각각 $D(f_{c_0})$와 $D(f_c)$를 거쳐 $\operatorname{colim}_I$로 갑니다.
- **보정항은 $j\downarrow I$의 disconnectedness를 잰 것**입니다. $j \in I$이면 $(j,\mathrm{id})$가 terminal이라 기여가 없습니다.

## 2. $I$의 선택에 따른 특수한 경우

| $I$의 선택 | $\operatorname{colim}_I$ | 보정항 | 결과 |
|---|---|---|---|
| 모든 object, discrete | $\coprod_j D(j)$ | 모든 non-identity 화살표 | 표준 공식 $\mathrm{Coeq}\big(\coprod_{f:j\to s} D(j) \rightrightarrows \coprod_j D(j)\big)$ |
| weakly terminal set $S$ | $S$ 위의 colimit | 연결되지 않은 comma에서만 | pushout형: "끝 object들의 coproduct의 quotient" |
| final ($j\downarrow I$ 모두 connected) | $\operatorname{colim}_I D\vert_I$ | 없음 | final functor 정리 $\operatorname{colim}_J D \cong \operatorname{colim}_I D\vert_I$ |

예를 들어 pushout $B \leftarrow A \to C$에서는 $I=\{B,C\}$로 잡습니다. $\pi_0(A\downarrow I)$가 두 원소이므로 보정은 $A$ 하나이고, 결과는 $\mathrm{Coeq}(A \rightrightarrows B\sqcup C)$입니다.

## 3. Filtered colimit

$J$가 filtered이면 두 가지 단순화가 동시에 일어납니다.

**(a) 연결성이 공짜로 따라옵니다.** Full subcategory $I$에 대해 $j\downarrow I$가 nonempty이기만 하면 자동으로 connected입니다. 따라서 weakly terminal과 final이 같은 조건이 되고, 보정항이 사라집니다.
$$\operatorname{colim}_J D \cong \operatorname{colim}_I D|_I \quad (\text{모든 } j \text{가 } I\text{로 가는 화살표를 가지면})$$
이때 $I$도 filtered입니다. Directed set의 cofinal subset이 대표적인 예입니다.

**(b) 동치관계를 생성할 필요가 없습니다.** Set에서 일반 colimit은 zigzag로 *생성된* 동치관계로 나누지만, filtered에서는 zigzag가 cospan 하나로 압축됩니다.
$$\operatorname{colim} D = \coprod_j D(j)\big/\!\sim, \qquad x_i \sim x_j \iff \exists\, i\xrightarrow{u}k\xleftarrow{v}j,\ D(u)x_i = D(v)x_j$$

두 단순화를 합치면, weakly terminal object $t$가 있는 경우(유한 weakly terminal set이 있으면 상계를 잡아 항상 이렇게 됩니다)
$$\operatorname{colim} D \cong D(t)\big/(x\sim y \iff \exists\, e\in \mathrm{End}(t),\ D(e)x = D(e)y)$$
입니다. 최대원이 있는 directed poset이라면 그냥 $D(t)$입니다.

## 4. Limit 쪽 (쌍대)

$I$가 weakly initial이면(모든 $j$로 $I$에서 화살표가 들어오면)
$$
\lim_J D \;\cong\; \mathrm{Eq}\Big( \lim_I D|_I \;\rightrightarrows\; \prod_j \prod_{c\in\pi_0(I\downarrow j)\setminus\{c_0\}} D(j) \Big)
$$
입니다.

- **Discrete $I$**: 표준 공식 $\mathrm{Eq}\big(\prod_j D(j) \rightrightarrows \prod_{f: s\to j} D(j)\big)$가 나옵니다.
- **Pullback** $A\to C\leftarrow B$: $I=\{A,B\}$로 잡으면 $\mathrm{Eq}(A\times B\rightrightarrows C)$가 나옵니다.
- **Cofiltered limit**: (a)의 쌍대가 성립합니다. Coinitial subcategory로 줄이면 되고, 예를 들어 $\mathbb{Z}_p = \lim \mathbb{Z}/p^n$처럼 cofinal sequence만 쓰면 됩니다.

여기에는 **비대칭**이 하나 있습니다. Set에서 limit은 원래 "product의 부분집합에 등식 조건"이라 생성 과정이 없습니다. 그래서 (b)에 해당하는 이득이 limit 쪽에는 없고, cofiltered limit에서 실질적으로 쓰는 것은 (a)의 reduction뿐입니다.

## 5. 구체적 묘사가 통하는 범위

- **Set**: 위 공식들이 그대로 "disjoint union의 quotient"와 "product의 subset"이 됩니다.
- **Top**: 같은 집합에 colimit은 quotient topology, limit은 subspace topology를 줍니다.
- **Algebraic category (Grp, Ring, $R$-Mod 등)**: limit과 filtered colimit은 forgetful functor가 보존하므로 Set에서처럼 계산됩니다. 반면 pushout 같은 일반 colimit은 공식 자체는 성립하지만, coproduct가 free product 등이 되므로 underlying set이 disjoint union의 quotient는 아닙니다.

## 6. 실전 순서

1. **Filtered/cofiltered인가?** 그렇다면 cofinal(coinitial) subcategory로 줄이고, 3(b)의 명시적 관계를 씁니다.
2. **아니라면 작은 weakly terminal(initial) $I$가 있는가?** 있다면 $\operatorname{colim}_I$를 구하고, comma category가 disconnected인 곳에서만 보정 (co)equalizer를 붙입니다.
3. **그것도 아니라면** discrete $I$, 즉 표준 공식을 씁니다.

한 줄로 말하면, **$I$를 고르고, $\operatorname{colim}_I$를 구한 다음, $\pi_0(j\downarrow I)$만큼 보정합니다.** Filtered는 이 보정이 저절로 0이 되는 경우입니다.
