---
title: 'Evaluating Nanoindentation Methods for Soft Materials'
date: 2026-01-23
tags:
  - Nanoindentation
  - Oliver–Pharr
  - Creep
  - trimer
author_profile: true
---

<!--このページはNanoindentaionの測定をスムーズに、かつ測定後に後悔のないように実験を設計することをサポートするためのページです。特に柔らかく薄い薄膜の場合は測定条件や計算の仕方によって値が大きく変わるので、他材料や論文の値と比較などをするときは特に重要です。このノートが参考になるといいと思っています。-->
## 0. Executive Summary
This page is intended to support the design of nanoindentation experiments that can be carried out smoothly and interpreted without regret after measurement.
For soft and thin films in particular, the extracted mechanical properties can vary significantly depending on measurement conditions and analysis methods.
This sensitivity makes careful experimental design essential when comparing results across different materials or with values reported in the literature.
The aim of **this note is to provide practical guidance that helps avoid common mistakes and preserves interpretability in nanoindentation measurements**.

## 1. Nanoindentation

<!-- 1. Nanoindentation とは
Nanoindentation は、微小なプローブを材料表面に押し込み、力–変位応答から機械物性を評価する手法である。特徴的なのは、実際に材料内部へプローブを侵入させる点と、プローブ形状に基づく接触面積のキャリブレーションが可能である点である。
同様にナノ・ミクロスケールの力学評価として AFM を用いた手法があるが、位置づけがことなる。
* AFM
    * 極表面（nm スケール）の局在物性
    * 接触条件・有効面積の不確定性が大きい
* Nanoindentation
    * µm スケールの平均応答
    * 接触面積が定義でき、比較的「絶対値」に近い評価が可能
nanoindentation は 表面評価とバルク評価の中間、より正確には「準バルク物性評価」と言える。

図nanoindentatiornの模式図
-->

Nanoindentation is a technique for evaluating mechanical properties by pressing a small probe into a material surface and analyzing the resulting **force–displacement response**.  
Two aspects are particularly important in the context of this note. First, the probe physically penetrates into the material, probing a finite deformation volume rather than an idealized surface. Second, the contact area can be quantitatively defined and calibrated based on the indenter geometry.

Mechanical characterization at the nano- to microscale is also commonly performed using atomic force microscopy (AFM), however, Nanoindentation can probe an averaged mechanical response over the micrometer scale and contact area is defined through indenter geometry, allowing closer access to absolute mechanical values. Nanoindentation can be consider as a method for **quasi-bulk mechanical property evaluation at the microscale**.

![image]({{site.baseurl}}/images/images_pages_posts/img_2026-01-27-15-26-15.png)

**Figure**: Nanomechanical Test System Hysitron TI Premier


## 2. The Oliver–Pharr Method and Its Limitations for Soft Materials


<!--1. 2. Oliver–Pharr 法と軟材料における限界
Nanoindentation における弾性率・硬さ評価といえば、Oliver–Pharr（OP）法が事実上の標準である。OP 法は、除荷曲線の初期勾配から弾性応答を抽出する解析手法であり、
* 弾性回復が支配的
* 時間依存変形（creep）が無視できる
という前提のもとで成立している。

図OP法の接線の取り方の模式図

金属やセラミックなど、弾性率が高く時間依存性の小さい材料では、この前提は概ね満たされる。しかし高分子やゲルなどの軟材料では、
* 荷重保持中の creep
* 接触面積の時間変化
* 押し込み深さ依存の拘束条件変化
が避けられず、OP 法の前提が崩れる。

例えば、論文XXXにおいては、半導体性高分子の一種であるポリチオフェン誘導体の弾性率をOP法にて評価した近年の論文の報告値をまとめており、その値がDMAなどから得られる値と比較してやや乖離し、かつ報告値も大きく振れているのがわかる。

テーブル、XXXサポーティングInfo

この他にも、これらの論文において同様のOP法の限界が示唆されている。-->

The **Oliver–Pharr (OP) method** is widely regarded as the standard approach for extracting elastic modulus and hardness from nanoindentation experiments.  
The elastic response is determined from the initial slope of the unloading segment of the load–displacement curve, based on the assumptions that elastic recovery dominates the unloading response and time-dependent deformation (creep) can be neglected.

![image]({{site.baseurl}}/images/images_pages_posts/img_2026-01-27-15-51-06.png)

**Figure**: Schematic illustration of the determination of unloading stiffness in the Oliver–Pharr method.

For stiff materials such as metals and ceramics, which exhibit high elastic moduli and minimal time-dependent deformation, these assumptions are generally well satisfied.  
For soft and viscoelastic materials such as polymers and gels, however, the validity of these assumptions becomes increasingly limited.
In such materials, several effects tend to interfere with the physical interpretation of the unloading stiffness:

- **creep deformation during the load-hold segment**,  
- **time-dependent evolution of the contact area**, and  
- **depth-dependent changes in mechanical constraint imposed by the indenter geometry**.

Taken together, such that the elastic modulus derived from OP analysis does not necessarily represent a uniquely defined material property.

An example is provided by the study of Paleti et al.  
(*S. H. K. Paleti et al., “Benchmarking the Elastic Modulus of Conjugated Polymers with Nanoindentation,” Macromolecules, 2025*), in which elastic moduli of conjugated polymers, including polythiophene derivatives, were evaluated using the Oliver–Pharr method.  
By compiling nanoindentation-derived moduli reported in the literature and comparing them with values obtained from bulk techniques such as dynamic mechanical analysis (DMA), the authors showed that OP-based moduli exhibit both systematic deviations from DMA values and substantial scatter across different studies.

![image]({{site.baseurl}}/images/images_pages_posts/img_2026-01-27-15-39-31.png)

**Figure**: Elastic modulus *E* of regioregular P3HT measured using various experimental techniques, including DMA, AFM-based methods, and nanoindentation (Oliver–Pharr and creep analysis), reproduced from Paleti et al.



<!--3. Creep 測定とは
軟材料評価では、除荷解析に代わり 荷重保持中の creep 応答に注目する測定がしばしば行われる。
典型的な creep 測定では、一定荷重下での押し込み深さh(t) の時間変化を測定し、これを応力–ひずみ応答として解釈する。
概念的には、
￼

で定義される creep compliance が評価対象となる。

nanoindentation においては、
* 応力：有効接触応力
* ひずみ：押し込み深さ（あるいは規格化深さ）
を用いた 有効 compliance として解釈される。

Creep 応答から得られる情報
Creep 法からは、主に以下の情報が得られる。
* 初期 compliance
    * 有効剛性（拘束条件の影響を含む）
* 時間依存の増加挙動
    * 粘弾性緩和の存在
* スケーリング挙動
    * 例：J(t)∝tm
    * ここでの指数 m は、材料内部の緩和スペクトルの形を反映する指標と解釈できる
特に、異なる条件間で m が不変である場合、時間応答の本質的なメカニズムが共通であることを示唆する。


論文XXXにおいては、


一方で、この論文においては、同じ材料の力学物性を同じ条件に置いて評価しているので問題ないが、今後これを複数材料間での比較などをしたいと思った場合は、議論が少し難しくなる。
例えばチップ形状である。
本論文では Berkovich チップを用いているが、これは
* 接触面積が押し込み深さの二乗で急激に増加する
* 押し込みが進むにつれて拘束条件が連続的に変化するという特徴を持つ。
すなわち、仮に厚さ方向に均一な力学物性を持つ薄膜であった場合においても、Berkovich チップを用いて、Creep試験においてCreep Cpmlianceを求めると、深い場所における評価の方がチップの接触面積に比べて材料の拘束が小さくなり材料がチップから逃げやすくなってしまう。結果として深い場所の方が一見すると柔らかいような挙動を示す。
この一見柔らかい様子が、真に材料に起因するのか、拘束条件に由来するのかは、緩和スペクトル、mの議論によって行うことは可能であるが、注意を要する。
また異なる材料の比較の場合、一方が真に柔らかく、同じ試験力で評価しても結果としてチップが深くまで押し込んでしまったとする。その場合別のサンプルでは表層のみの評価しかしていなかった場合、それらの結果の単純比較は注意しなければならない。

この議論を助けるための手法として球状チップもしくはフラットチップの使用がある。
もし 球状チップ を用いた場合には、
* 初期接触半径が明確
* 拘束条件の深さ依存性がより緩やかとなるため、* 深さ依存性と材料固有の時間応答をより分離しやすい 可能性がある。
一方で球状チップやフラットチップは
表面粗さに極端に弱い
初期接触の決定が難しい
非常に柔らかい材料では
座屈
周辺破壊
接触不安定
が起きやすい、ことから別の注意も必要である。
-->

## 3. Creep-Based Nanoindentation Measurements

For soft and viscoelastic materials, nanoindentation analyses often focus on the **creep response during the load-hold segment**, rather than on unloading-based methods.  
In a typical creep experiment, the time-dependent evolution of the indentation depth during a constant applied load is recorded and interpreted as a mechanical response of the material.

Conceptually, the quantity of interest is the **creep compliance**, which relates time-dependent strain to applied stress.  
In nanoindentation, this compliance is necessarily interpreted as an **effective quantity**, where the applied stress is approximated by an effective contact stress and the strain is represented by the indentation depth (or a normalized depth).

![image]({{site.baseurl}}/images/images_pages_posts/img_2026-01-27-15-57-08.png)

---

### Information Extracted from Creep Measurements

Creep-based nanoindentation provides access to complementary information that is not available from unloading-based analysis alone:

- **Initial compliance**, reflecting effective stiffness under the imposed mechanical constraint  
- **Time-dependent increase in compliance**, indicating viscoelastic relaxation  
- **Scaling behavior**, commonly expressed as a power-law dependence

In many soft materials, the creep compliance follows a scaling relation of the form

$$
J(t) \propto t^{m}
$$

where the exponent *m* reflects the shape of the underlying relaxation spectrum.  
If *m* remains invariant across different indentation depths or applied loads, this suggests that the **dominant deformation mechanism is unchanged**, even when absolute compliance values vary.

---

### Experimental Implementation in a Representative Study

A representative implementation of creep-based nanoindentation is provided by Paleti et al. (*Macromolecules*, 2025), who investigated the mechanical properties of regioregular poly(3-hexylthiophene) (P3HT) thin films.

In their experiments, nanoindentation was performed using a diamond Berkovich indenter on a Hysitron TI Premier system.  
Each measurement consisted of a loading segment up to a prescribed holding load, followed by a constant-load hold segment and subsequent unloading.

Rather than analyzing the unloading stiffness, the authors evaluated the creep response under constant holding load.  
This approach avoids numerical instability associated with differentiating noisy load–displacement data during loading and circumvents the assumption of purely elastic unloading inherent to the Oliver–Pharr method.

Under these conditions, the time-dependent creep compliance was calculated directly from the evolution of indentation depth during the hold segment, based on contact-mechanics relations for a self-similar pyramidal indenter.

In a typical experiment, the indentation depth increased gradually during the hold segment and approached a steady value at long times.  
The long-time limit of the creep compliance was interpreted as an equilibrium compliance, from which an effective elastic modulus was obtained.

The resulting moduli were found to be consistent in order of magnitude with independently measured bulk dynamic mechanical analysis (DMA) values for the same material, supporting the physical plausibility of the creep-based approach.

---

### Interpretation and Limitations

Creep-based nanoindentation avoids several limitations of unloading-based analysis for soft materials by directly probing time-dependent deformation.  
At the same time, the obtained compliance and modulus values must be interpreted with care.

Because the compliance reflects both intrinsic material response and the mechanical constraint imposed by the indenter geometry, it should be regarded as an **effective quantity rather than a unique material constant**.

This distinction becomes particularly important when creep measurements are compared across different indentation depths or between different materials.  
Changes in absolute compliance may arise from evolving constraint conditions, even when the underlying relaxation mechanism remains unchanged.

For this reason, **the shape of the time-dependent response**, as captured by normalized compliance or scaling exponents, often provides a more reliable basis for comparison than absolute modulus values alone.



## 4. Toward Robust and Comparable Nanoindentation of Soft Materials  
### How Should Soft Materials Be Measured?

The discussion so far leads to a central conclusion:  
**for soft and viscoelastic materials, nanoindentation results obtained under a single experimental condition rarely constitute a reliable basis for comparison.**

In such systems,

- the indentation depth is not a controlled parameter but an outcome of the applied load,
- the probed deformation volume varies strongly with depth and indenter geometry, and
- time-dependent deformation is inseparably coupled to evolving mechanical constraint.

As a result, elastic moduli or compliance values extracted from a single load, a single depth, or a single analysis method are inherently fragile.  
This section therefore shifts the focus from *data interpretation* to *experimental design*, with the aim of answering a practical question:

> **How should nanoindentation experiments be designed so that the resulting data remain interpretable, even in hindsight?**

---

### 4.1 Core Principle: Indentation Depth Must Be Treated as a Variable

A key insight is that **indentation depth cannot be fixed a priori when comparing different soft materials**.  
For materials with markedly different stiffness, the same applied load can probe fundamentally different deformation volumes.

Consequently, attempts to “match” experiments by prescribing a single indentation depth are often impractical or misleading.  
A more robust strategy is to **treat indentation depth itself as an experimental variable** and to design measurements such that a range of depths is sampled systematically.

In practice, this is most reliably achieved by performing nanoindentation at **multiple applied loads**, rather than attempting to target a single depth.

---

### 4.2 Recommended Routine: Multi-Load Berkovich Indentation with Creep Analysis

A practical baseline protocol for soft materials can be summarized as follows.

#### Step 1: Multiple Peak Loads

- Perform Berkovich nanoindentation at **three to five distinct peak loads**.
- Allow the resulting indentation depths to emerge naturally from the material response.
- Categorize data *post hoc* by actual indentation depth (or normalized depth, e.g., *h/d* for thin films).

This ensures that both shallow and deeper deformation regimes are sampled without prior assumptions about material stiffness.

---

#### Step 2: Creep Analysis at Each Condition

For each indentation condition, extract:

- the time-dependent indentation depth during the load-hold segment,
- the corresponding creep compliance,
- normalized creep compliance (e.g., relative to an initial reference time), and
- the scaling exponent describing the time dependence.

This enables two complementary perspectives:

- **absolute compliance**, which is sensitive to constraint and geometry, and  
- **time-response shape**, which reflects intrinsic relaxation behavior.

If the scaling exponent remains invariant across loads or depths, this indicates that the underlying viscoelastic mechanism is unchanged, even if the apparent stiffness varies.

---

### 4.3 Role of nanoDMA: Complement, Not Replacement

When quantitative comparison across materials is required, **nanoDMA** provides an important complementary tool.

In contrast to creep analysis, nanoDMA:

- probes the response in the frequency domain,
- yields storage modulus and loss-related quantities directly, and
- facilitates comparison using representations such as Ashby-type plots.

However, nanoDMA does not eliminate the depth-dependence problem.  
Because the oscillatory measurement is performed under a static preload, the actual indentation depth still depends on material stiffness.

For this reason, nanoDMA measurements should be conducted **at multiple loads or depths**, mirroring the creep protocol, rather than at a single nominal condition.

---

### 4.4 Alternative Indenter Geometries as Validation Tools

Indenter geometry plays a central role in determining mechanical constraint.

While the Berkovich indenter offers excellent reproducibility and well-established analysis frameworks, its self-similar geometry leads to a continuously evolving constraint with increasing depth.

Spherical or flat punch indenters can be useful in this context, primarily as **validation tools**:

- Spherical indenters provide a well-defined initial contact radius and a more gradual evolution of constraint.
- Flat punch indenters impose a nearly constant contact area once full contact is established.

Used selectively, these geometries can help distinguish between:

- genuine depth-dependent material behavior, and  
- apparent softening arising from changing constraint conditions.

At the same time, such indenters are highly sensitive to surface roughness and contact instability, particularly for very soft materials, and are therefore best employed in a supporting rather than primary role.

---

### 4.5 What This Strategy Prevents

Designing experiments around multiple loads and complementary analyses prevents several common pitfalls:

- interpreting deeper indentation as intrinsically softer material,
- comparing materials probed at fundamentally different deformation volumes, and
- collapsing time-dependent behavior into a single modulus value that obscures underlying mechanisms.

Most importantly, it ensures that **no essential information is irreversibly lost at the experimental stage**, even if the final interpretation evolves later.

---

### 4.6 Key Takeaway

The central message of this section can be stated succinctly:

> **For soft materials, the critical question is not which nanoindentation method to use, but how to design measurements that remain interpretable across depths, loads, and materials.**

By embracing controlled redundancy—multiple loads, explicit depth dependence, and complementary analyses—nanoindentation can be transformed from a fragile point measurement into a robust comparative tool for soft and viscoelastic systems.


## 5. Practical Checklist for Nanoindentation of Soft Materials

This checklist summarizes a **reusable experimental design** for nanoindentation of soft and viscoelastic materials to **prevent irreversible loss of information** and to ensure that data remain interpretable during post-analysis and inter-material comparison.

---

### 5.1 Experimental Design

| Item | Recommendation | Rationale |
|----|----|----|
| Primary indenter | **Berkovich** | High reproducibility; well-established contact mechanics |
| Validation indenter | **Spherical or flat punch (optional)** | Distinguish intrinsic material response from constraint effects |
| Number of peak loads | **≥ 3–5 distinct loads** | Ensure multiple indentation depths are sampled |
| Depth targeting | **Do not prescribe depth a priori** | Depth emerges from material stiffness |
| Depth range | **Shallow to deep (e.g., h/d ≈ 0.1–0.8)** | Probe different deformation volumes |

---

### 5.2 Creep Measurement Protocol

| Item | Recommendation | Purpose |
|----|----|----|
| Hold segment | **Constant load hold** | Stable extraction of time-dependent response |
| Recorded signal | **Indentation depth vs time during hold** | Basis for creep compliance analysis |
| Hold duration | **Sufficient to reach near-steady behavior** | Identify long-time response |
| Loading rate | **Consistent across measurements** | Avoid rate-induced artifacts |

---

### 5.3 Creep Analysis: Minimal Equation Set (Quick Reference)

The table below summarizes the **minimum equations required for creep-based nanoindentation analysis**.  
Only quantities that are typically available from standard nanoindentation output are included.

| Purpose | Quantity | Expression | Notes / When to Use |
|------|--------|-----------|---------------------|
| Creep response | Creep compliance | J(t) = 4·h²(t) / [π·(1 − ν_f)·P_hold·tanα] | Constant-load hold segment (Berkovich) |
| Time normalization | Normalized compliance | J(t) / J(t₀) | Compare time-response shapes across depths/materials |
| Scaling behavior | Creep exponent | J(t) ∝ t^m | Extract *m* from log–log plot |
| Long-time stiffness | Equilibrium shear modulus | G_e = 1 / J(t) (t ≫ 0) | Only if clear plateau is observed |
| Elastic modulus | Tensile modulus | E = 2·G_e·(1 + ν_f) | Effective modulus under indentation constraint |

---

#### Parameter Definitions

| Symbol | Meaning | Typical Value / Comment |
|-----|--------|------------------------|
| h(t) | Indentation depth during hold | Measured directly |
| P_hold | Constant holding load | Experimental parameter |
| ν_f | Poisson’s ratio of film | Often 0.3–0.5 for polymers |
| α | Half-angle of Berkovich tip | 65.27° |

---

#### Practical Notes

- Absolute values depend on **indentation depth and constraint**
- Normalized compliance and exponent *m* are more robust for comparison
- Always record **actual indentation depth**, not only applied load

---

### 5.4 nanoDMA (Optional but Recommended)

| Item | Recommendation | Purpose |
|----|----|----|
| Measurement mode | **Depth-fixed nanoDMA** | Frequency-domain characterization |
| Preload strategy | **Multiple loads or depths** | Avoid depth bias |
| Oscillation amplitude | **Linear viscoelastic regime** | Ensure meaningful moduli |
| Extracted quantities | **Storage modulus, loss factor** | Enable Ashby-type representations |

---

### 5.5 Reproducibility and Statistics

| Item | Recommendation | Rationale |
|----|----|----|
| Repeats per condition | **Multiple indents per load** | Statistical robustness |
| Spatial distribution | **Avoid clustering** | Reduce local heterogeneity bias |
| Drift control | **Monitor and correct** | Ensure temporal stability |

---

### 5.6 Reporting and Documentation

| Item | Must Be Reported | Why It Matters |
|----|----|----|
| Indenter geometry | Tip type, nominal angles | Defines constraint |
| Applied load(s) | Absolute values | Enables comparison |
| Resulting depths | Actual indentation depths | Critical for interpretation |
| Hold duration | Time scale of measurement | Relates to viscoelastic response |
| Analysis method | OP / creep / nanoDMA | Clarifies assumptions |

---

### Final Note

The hope is that this note can serve as a reference point—helping experimentalists make informed choices and avoid losing essential information before analysis even begins.
