---
title: 'Evaluating Modern Literature Exploration Tools'
subtitle: "A Hands-on Log Using Epoxy Vitrimer as a Case Study"
date: 2026-01-13
tags:
  - literature-mapping
  - bibliometrics
  - methodology
  - epoxy-vitrimer
author_profile: true
---

## 1. Motivation

<!-- 近年、科学文献の量は指数関数的に増えており、個々の研究者が手動で読むだけで追跡できる範囲を超えています。しかし同時に、研究分野の発見、マッピング、理解をより効率的にサポートすると主張する幅広い**文献探索ツール**が登場しています。

今回、近年新しく出てきている**現代の文献探索ツールが、研究背景の把握や文献調査においてどの程度有用なのか、*エポキシビトリマー*を具体的な現実的なケーススタディとして使用して、評価を行った。

中心的な質問は：

> *新規分野における研究把握において、現在のツールがどの程度役に立つかいかです。* -->

In recent years, the volume of scientific literature has grown exponentially, exceeding what individual researchers can reasonably track through manual reading alone. At the same time, a wide range of **literature exploration tools** has emerged, claiming to support more efficient discovery, mapping, and understanding of research fields.

This note evaluates **how effective recently emerging modern literature exploration tools are in grasping research backgrounds and conducting literature surveys**, using *epoxy vitrimers* as a concrete and realistic case study.

The central question is:

> *How effective are current tools in helping researchers grasp new fields?*


---

## 2. Scope and Tools Evaluated

<!-- 以下のツールが実践的に評価されました：

- [Google Scholar](https://scholar.google.com/)
- [Semantic Scholar](https://www.semanticscholar.org/)
- [OpenAlex](https://openalex.org/)
- [Connected Papers](https://www.connectedpapers.com/)
- [ResearchRabbit](https://www.researchrabbit.ai/)
- [The Lens](https://www.lens.org/)
- [VOSviewer](https://www.vosviewer.com/)

これらのツールは、**文献計量学**、**科学計量学**、**科学の科学**、および**情報検索**を含む、重複するが異なる研究コミュニティから来てい流ということです。各ツールにはリンクから行けます。 -->

The following tools were evaluated hands-on:

- [Google Scholar](https://scholar.google.com/)
- [Semantic Scholar](https://www.semanticscholar.org/)
- [OpenAlex](https://openalex.org/)
- [Connected Papers](https://www.connectedpapers.com/)
- [ResearchRabbit](https://www.researchrabbit.ai/)
- [The Lens](https://www.lens.org/)
- [VOSviewer](https://www.vosviewer.com/)

These tools originate from overlapping but distinct research communities, including **bibliometrics**, **scientometrics**, **science-of-science**, and **information retrieval**. Each tool is accessible via the provided links.

---

## 3. Google Scholar

<!-- ### 概要
まず最初は、最も広く使われているGoogle Scholarから試しました。Goolge Scholarは最も広く使用されている学術検索エンジンであり、その強みはカバレッジとアクセシビリティにあると思われます。

### 今回行った手順
- `"epoxy vitrimer review"`というキーワードで検索を行った

### 結果
- 数5000件の結果が取得された
- Reviewとキーワードに入れて検索を行ったが、実際にはreview以外の論文も多く含まれているようであった。
- 左のタブにreviewのみを選択するツールがあるのでそれを適用すると約1000件まで結果が減少
- しかしまだ一部Review以外も含まれているように見え、また検索のたびにヒット件数が変化して安定性が疑われた
- また検索結果から重要Reviewを見つけるために、例えばCitationでソートなどをしたかったが、そのような機能は見つからなかった

### 観察
- **エントリーポイント**として優れていると思われる
- しかし体系的なマッピングや再現性には不向きであり
- 検索結果が時折不安定なのが気になった -->

### Overview
First, I tried Google Scholar, the most widely used tool. Google Scholar is the most widely used academic search engine, and its strengths appear to lie in coverage and accessibility.

### Procedure
- Searched with the keyword `"epoxy vitrimer review"`

### Results
- Approximately 5000 results were retrieved.
- Although "review" was included in the keyword, many non-review papers seemed to be included.
- There is a tool in the left tab to select only reviews, which reduced the results to about 1000.
- However, some non-reviews still appeared to be included, and the number of hits varied with each search, raising doubts about stability.
- Additionally, to find important reviews from the results, I wanted to sort by citation, for example, but no such function was found.

### Observations
- Appears excellent as an **entry point**.
- However, unsuitable for systematic mapping or reproducibility.

---

## 4. Semantic Scholar
<!-- ### 概要
Semantic Scholarは、引用分析、関連性ランキング、論文要約にAIベースの方法を適用します。

### 手順
- Google Scholarと同じキーワード検索
- 引用カウントと影響力のある論文によるソート

### 結果
- Google Scholarよりも構造化されたメタデータ
- このトピックでは信頼できる「レビューのみ」フィルターなし
- 引用ベースのランキングは役立つが不透明

### 観察
- **論文レベルの検査**に有用
- フィールドレベルの概要にはあまり適さない -->
### Overview
Semantic Scholar applies AI-based methods to citation analysis, relevance ranking, and paper summarization.

### Procedure
- Same keyword search as Google Scholar
- Sorting by citation count and influential papers

### Results
- More structured metadata than Google Scholar
- No reliable “Review-only” filter for this topic
- Citation-based ranking helpful but opaque

### Observations
- Useful for **paper-level inspection**
- Less suitable for field-level overview

---

## 5. OpenAlex

<!-- ### 概要
OpenAlexは、独自の書誌データベースの代替として設計されたオープンな学術知識グラフです。

### 手順
- 検索クエリ: `"epoxy vitrimer"`
- 最初はレビュー記事に制限
- 後ですべての記事タイプに拡張

### 結果
- エポキシビトリマーで~800件の記事が取得
- リッチなメタデータ: 概念、機関、年
- データエクスポートとAPIアクセスが可能

### 観察
- **透明なデータバックボーン**として理想的
- 可視化にはダウンストリームツールが必要 -->

### Overview
OpenAlex is an open scholarly knowledge graph designed as a replacement for proprietary bibliographic databases.

### Procedure
- Search query: `"epoxy vitrimer"`
- Initial restriction to review articles
- Later expanded to all article types

### Results
- ~800 articles retrieved for epoxy vitrimers
- Rich metadata: concepts, institutions, years
- Data export and API access available

### Observations
- Ideal as a **transparent data backbone**
- Requires downstream tools for visualization

---

## 6. Connected Papers

<!-- ### 概要
Connected Papersは、単一のシード論文周辺の**ローカル引用近傍**を可視化します。

### 手順
- 代表的なレビュー記事をシードとして使用
- 先行および派生作品を探索

### 結果
- 引用関係の明確な可視化
- 密集だがローカライズされたクラスター
- 一度に一つのシード論文に制限

### 観察
- **既知の論文を文脈化する**のに優れている
- グローバルフィールドマッピングには適さない -->

### Overview
Connected Papers visualizes a **local citation neighborhood** around a single seed paper.

### Procedure
- Seeded with representative review articles
- Explored prior and derivative works

### Results
- Clear visualization of citation relationships
- Dense but localized clusters
- Limited to one seed paper at a time

### Observations
- Excellent for **contextualizing a known paper**
- Not suitable for global field mapping

---

## 7. ResearchRabbit

<!-- ### 概要
ResearchRabbitは、反復的な探索を通じて**類似および関連論文**の発見に焦点を当てます。

### 手順
- 複数のレビュー記事をシードとして追加
- 類似性ベースの拡張を探索

### 結果
- 大規模な結果セット（数千の論文）
- グラフ構造は類似性を反映し、トピックを反映しない
- ページネーションがグローバル構造を不明瞭にする

### 観察
- **文献の発見**に強い
- 明示的なフィールドセグメンテーションには弱い -->

### Overview
ResearchRabbit focuses on discovering **similar and related papers** through iterative exploration.

### Procedure
- Multiple review articles added as seeds
- Similarity-based expansion explored

### Results
- Large result sets (thousands of papers)
- Graph structure reflects similarity, not topics
- Pagination limits obscure global structure

### Observations
- Strong for **literature discovery**
- Weak for explicit field segmentation

---

## 8. The Lens

<!-- ### 概要
The Lensは、**学術文献と特許**を単一のプラットフォームに統合します。

### 手順
- 特許検索: `(epoxy AND vitrimer)`
- 熱関連キーワードで拡張
- 学術と特許のトレンドの比較

### 結果
- 数百の関連特許が特定
- 明確な産業アクターと時間的トレンド

### 観察
- **科学–技術のリンク**における独自の強み
- アプリケーション指向の分析に不可欠 -->

### Overview
The Lens integrates **academic literature and patents** into a single platform.

### Procedure
- Patent search: `(epoxy AND vitrimer)`
- Extended with thermal-related keywords
- Comparison between academic and patent trends

### Results
- Hundreds of relevant patents identified
- Clear industrial actors and temporal trends


### Observations
- Unique strength in **science–technology linkage**
- Essential for application-oriented analysis

---

## 9. VOSviewer

<!-- ### 概要
VOSviewerは、**共起とネットワーク構造**に焦点を当てた文献計量可視化ツールです。

### 手順
- エポキシビトリマー文献のキーワード共起マップを生成
- バイナリカウントを適用
- ~140キーワードを選択

### 結果
- クラスターは以下に対応:
  - 化学と交換反応
  - 機械的特性と修復
  - 複合材と強化
  - 持続可能性とバイオベース材料
- 熱関連用語が定量的にランク付け

### 例の洞察
熱関連用語は**トップ10–20キーワード以内**に現れ、エポキシビトリマー文献内で熱性能が**重要だが支配的ではない**ことを示す。

### 観察
- **フィールドレベルの構造**に最適なツール
- パラメータの慎重な解釈が必要 -->

### Overview
VOSviewer is a bibliometric visualization tool focusing on **co-occurrence and network structure**.

### Procedure
- Keyword co-occurrence map generated for epoxy vitrimer literature
- Binary counting applied
- ~140 keywords selected

### Results
- Clusters corresponding to:
  - Chemistry and exchange reactions
  - Mechanical properties and healing
  - Composites and reinforcement
  - Sustainability and bio-based materials
- Thermal-related terms ranked quantitatively

### Example Insight
Thermal-related terms appeared **within the top 10–20 keywords**, indicating that thermal performance is **important but not dominant** within the epoxy vitrimer literature.

### Observations
- Best tool for **field-level structure**
- Requires careful interpretation of parameters

---

## 10. Cross-Tool Comparison

<!-- | ツール | 主な強み | 制限 |
|----|----|----|
| Google Scholar | カバレッジ | 低い再現性 |
| Semantic Scholar | 論文レベルの洞察 | 限定的なフィールド概要 |
| OpenAlex | 透明なデータ | 外部ツールが必要 |
| Connected Papers | ローカルコンテキスト | 単一シード制限 |
| ResearchRabbit | 発見 | 弱いグローバル構造 |
| The Lens | 特許 + 論文 | クエリ感度 |
| VOSviewer | 構造マッピング | パラメータ依存 | -->

| Tool | Primary Strength | Limitation |
|----|----|----|
| Google Scholar | Coverage | Low reproducibility |
| Semantic Scholar | Paper-level insight | Limited field overview |
| OpenAlex | Transparent data | Needs external tools |
| Connected Papers | Local context | Single-seed limitation |
| ResearchRabbit | Discovery | Weak global structure |
| The Lens | Patents + papers | Query sensitivity |
| VOSviewer | Structural mapping | Parameter dependence |

---

## 11. Reflections

<!-- 結論、今の所VOS Viewer内でのAPIを使ったOpenAlexによる検索と、VOSviewerによる可視化が最も効果的に全体像を把握するのには適していると感じた。またLensも特許のステータスや出願国、年代まで一発でまとめてくれてとても有用であると感じた。 -->

In conclusion, so far, I feel that searching using OpenAlex via API within VOS Viewer and visualization with VOS Viewer are most effective for grasping the overall picture. I also felt that Lens is very useful as it summarizes patent status, filing countries, and eras all at once.



