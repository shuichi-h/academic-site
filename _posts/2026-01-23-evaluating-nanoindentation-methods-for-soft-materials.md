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

## Abstract
This page is intended to support the design of nanoindentation experiments that can be carried out smoothly and interpreted without regret after measurement.
For soft and thin films in particular, the extracted mechanical properties can vary significantly depending on measurement conditions and analysis methods.
This sensitivity makes careful experimental design essential when comparing results across different materials or with values reported in the literature.
The aim of this note is to **provide practical guidance that helps avoid common mistakes and preserves interpretability in nanoindentation measurements**.

## 1. Nanoindentation

Nanoindentation is a technique for evaluating mechanical properties by pressing a small probe into a material surface and analyzing the resulting **force–displacement response**.  
Two aspects are particularly important in the context of this note. First, the probe physically penetrates into the material, probing a finite deformation volume rather than an idealized surface. Second, the contact area can be quantitatively defined and calibrated based on the indenter geometry.

Mechanical characterization at the nano- to microscale is also commonly performed using atomic force microscopy (AFM), however, Nanoindentation can probe an averaged mechanical response over the micrometer scale and contact area is defined through indenter geometry, allowing closer access to absolute mechanical values. Nanoindentation can be consider as a method for **quasi-bulk mechanical property evaluation at the microscale**.

![image]({{site.baseurl}}/images/images_pages_posts/img_2026-01-27-15-26-15.png)

**Figure**: Nanomechanical Test System Hysitron TI Premier


## 2. The Oliver–Pharr Method and Its Limitations for Soft Materials

The **Oliver–Pharr (OP) method** is widely regarded as the standard approach for extracting elastic modulus and hardness from nanoindentation experiments.  
The elastic response is determined from the initial slope of the unloading segment of the load–displacement curve, based on the assumptions that elastic recovery dominates the unloading response and time-dependent deformation (creep) can be neglected.

![image]({{site.baseurl}}/images/images_pages_posts/img_2026-01-27-15-51-06.png)

**Figure**: Schematic illustration of the determination of unloading stiffness in the Oliver–Pharr method.

For stiff materials such as metals and ceramics, which exhibit high elastic moduli and minimal time-dependent deformation, these assumptions are generally well satisfied.  
**However for soft and viscoelastic materials such as polymers and gels, the validity of these assumptions becomes increasingly limited, because of:**

- creep deformation during the load-hold segment,  
- time-dependent evolution of the contact area, and  
- depth-dependent changes in mechanical constraint imposed by the indenter geometry.

Taken together, such that the elastic modulus derived from OP analysis does not necessarily represent a uniquely defined material property.

An example is provided by the study of Paleti et al. (*S. H. K. Paleti et al., “Benchmarking the Elastic Modulus of Conjugated Polymers with Nanoindentation,” Macromolecules, 2025*), in which elastic moduli of conjugated polymers, including polythiophene derivatives, were evaluated using the Oliver–Pharr method.  
By compiling nanoindentation-derived moduli reported in the literature and comparing them with values obtained from bulk techniques such as dynamic mechanical analysis (DMA), the authors showed that OP-based moduli exhibit both systematic deviations from DMA values and substantial scatter across different studies.

![image]({{site.baseurl}}/images/images_pages_posts/img_2026-02-02-13-08-49.png)

**Figure**: Elastic modulus *E* of regioregular P3HT measured using various experimental techniques, including DMA, AFM-based methods, and nanoindentation (Oliver–Pharr and creep analysis), reproduced from Paleti et al.


## 3. Creep-Based Nanoindentation Measurements

**For soft and viscoelastic materials**, nanoindentation analyses often focus on the **creep response during the load-hold segment**, rather than on unloading-based methods.  

In the previous paper (*Macromolecules*, 2025), they performed creep nanoindentation using a diamond Berkovich indenter on a Hysitron TI Premier system and characterized **Time-dependent increase in compliance** and determined **shear creep compliance *J*(t)** using the following equation, and converted it to **shear modulus *Ge***.

<math display="block" indentalign="left"><mrow><mrow><mstyle indentshift="3em" indentshiftlast="3em"><mi>J</mi><mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mstyle></mrow></mrow><mrow><mo linebreak="nobreak">=</mo><mstyle indentshift="3em" indentshiftlast="3em"><mfrac><mrow><mn>4</mn><msup><mi>h</mi><mn>2</mn></msup><mo stretchy="false">(</mo><mi>t</mi><mo stretchy="false">)</mo></mrow><mrow><mi>π</mi><mo stretchy="false">(</mo><mn>1</mn><mo>−</mo><msub><mi>ν</mi><mi mathvariant="normal">f</mi></msub><mo stretchy="false">)</mo><mo lspace="0.03em" rspace="0.03em">·</mo><msub><mi>P</mi><mi mathvariant="normal">hold</mi></msub><mo lspace="0.03em" rspace="0.03em">·</mo><mi>tan</mi><mspace width="0.25em"></mspace><mi>α</mi></mrow></mfrac></mstyle></mrow></math>

<br>

<math display="block" indentalign="left"><mrow><mrow><mstyle indentshift="3em" indentshiftlast="3em"><mi>E</mi></mstyle></mrow></mrow><mrow><mo linebreak="nobreak">=</mo><mstyle indentshift="3em" indentshiftlast="3em"><mn>2</mn><mo lspace="0.03em" rspace="0.03em">·</mo><msub><mi>G</mi><mi mathvariant="normal">e</mi></msub><mo lspace="0.03em" rspace="0.03em">·</mo><mo stretchy="false">(</mo><mn>1</mn><mo>+</mo><msub><mi>ν</mi><mi mathvariant="normal">f</mi></msub><mo stretchy="false">)</mo></mstyle></mrow></math>

![image]({{site.baseurl}}/images/images_pages_posts/img_2026-02-02-13-29-09.png)

The resulting moduli were found to be consistent in order of magnitude with independently measured bulk dynamic mechanical analysis (DMA) values for the same material, supporting the physical plausibility of the creep-based approach.

This paper was fine because this only discussing the same type of materials in the same method, **but the obtained compliance and modulus values must be interpreted with care. Because the compliance reflects both *intrinsic material response* and the *mechanical constraint imposed by the indenter geometry***.

Constraint refers to the apparent increase in stiffness arising from the restriction of deformation freedom—particularly lateral flow—imposed by the indenter geometry and contact conditions.
For a Berkovich indenter, increasing indentation depth reduces the relative lateral constraint imposed on the material compared to the rapidly increasing contact area, which can lead to an apparent decrease in stiffness or elastic modulus even for the same material.


For this reason, to compare values between with materials or literature values, absolute modulus values alone is not ideal. The shape of the time-dependent response, as captured by normalized compliance or scaling exponents can also provides a more reliable basis.

![image]({{site.baseurl}}/images/images_pages_posts/img_2026-02-03-17-31-00.png)

Creep-based nanoindentation can provides complementary information as follows :

- **Initial compliance**, reflecting effective stiffness under the imposed mechanical constraint  
- **Time-dependent increase in compliance**, indicating viscoelastic relaxation  
- **Scaling behavior**, commonly expressed as a power-law dependence

In many soft materials, the creep compliance follows a scaling relation of the form

$$
J(t) \propto t^{m}
$$

where the exponent *m* reflects the shape of the underlying relaxation spectrum.  
For example, even when the absolute compliance values vary depends on theindentation depths or applied loads, **if the *m* remains same**, this suggests that the **dominant deformation mechanism is unchanged**.  

And here are the typical creep exponent value and their corresponding material behavior.

| Creep exponent *m* | Dominant mechanical behavior | Typical material examples |
|--------------------|------------------------------|---------------------------|
| *m* ≈ 0 | Nearly elastic response | Glassy polymers well below *Tg*, stiff crosslinked networks |
| 0.05 ≤ *m* < 0.15 | Very slow relaxation | High-*Tg* polymers, semicrystalline polymers with strong lamellar constraints |
| 0.15 ≤ *m* < 0.30 | Pronounced viscoelastic relaxation | Amorphous polymers, conjugated polymers (e.g., P3HT), lightly crosslinked networks |
| 0.30 ≤ *m* < 0.50 | Strong viscoelasticity | Rubbery polymers, swollen polymer networks, soft elastomers |
| *m* ≥ 0.50 | Flow-dominated response | Weakly crosslinked gels, highly swollen hydrogels, viscoplastic soft matter |






---

## 4. Toward Comparable Nanoindentation of Soft Materials  
### How Should Soft Materials Be Measured?

According to the discussion points from above, a practical baseline protocol for soft materials can be summarized as follows.

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

#### Option 1 Role of nanoDMA: Complement, Not Replacement

When quantitative comparison across materials is required, **nanoDMA** provides an important complementary tool.

In contrast to creep analysis, nanoDMA:

- probes the response in the frequency domain,
- yields storage modulus and loss-related quantities directly, and
- facilitates comparison using representations such as Ashby-type plots.

However, nanoDMA does not eliminate the depth-dependence problem.  
Because the oscillatory measurement is performed under a static preload, the actual indentation depth still depends on material stiffness.

For this reason, nanoDMA measurements should be conducted **at multiple loads or depths**, mirroring the creep protocol, rather than at a single nominal condition.

---

#### Option 2; Alternative Indenter Geometries
Indenter geometry plays a central role in determining mechanical constraint.

While the Berkovich indenter offers excellent reproducibility and well-established analysis frameworks, its self-similar geometry leads to a continuously evolving constraint with increasing depth.

Spherical or flat punch indenters can be useful in this context, primarily as **validation tools**:

- Spherical indenters provide a well-defined initial contact radius and a more gradual evolution of constraint.
- Flat punch indenters impose a nearly constant contact area once full contact is established.

Used selectively, these geometries can help distinguish between:

- genuine depth-dependent material behavior, and  
- apparent softening arising from changing constraint conditions.

At the same time, such indenters are highly sensitive to surface roughness and contact instability, particularly for very soft materials, and are therefore best employed in a supporting rather than primary role.




## 5. Checklist for Nanoindentation of Soft Materials

This checklist summarizes a **reusable experimental design** for nanoindentation of soft and viscoelastic materials to **prevent irreversible loss of information** and to ensure that data remain interpretable during post-analysis and inter-material comparison.

---

### 5.1 Experimental Design

| Item | Recommendation | Rationale |
|----|----|----|
| Primary indenter | **Berkovich** | High reproducibility; well-established contact mechanics |
| Validation indenter | **Spherical or flat punch (optional)** | Distinguish intrinsic material response from constraint effects |
| Number of peak loads | **≥ 3–5 distinct loads** | Ensure multiple indentation depths are sampled |
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

This page introduced the basics of nanoindentation, its concepts, and important points to note and solutions when evaluating soft materials. In conclusion, although it has been confirmed that the creep method provides more accurate results than Oliver Pharr, it is important to always evaluate at multiple indentation depths, especially when comparing multiple types of samples, and to evaluate the dependence of the scaling factor m on the thickness direction. I have provided all the relevant formulas, so I hope you will refer to them whenever necessary.
