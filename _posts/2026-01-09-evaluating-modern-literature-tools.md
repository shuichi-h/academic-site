---
title: 'Evaluating Modern Literature Exploration Tools'
subtitle: "A Hands-on Log Using Epoxy Vitrimer as a Case Study"
date: 2026-01-0
categories:
  - research-notes
tags:
  - literature-mapping
  - bibliometrics
  - methodology
  - epoxy-vitrimer
author_profile: true
---

#1. Purpose and Background

In recent years, the explosive growth of academic publications has made deciding what to read a research problem in itself.

The aim of this note is not to review a specific scientific topic, but to address the following question:

How can researchers more effectively explore and grasp the structure of a research field using modern literature exploration tools?

This study evaluates what recent tools can and cannot do when applied to the same research question, using epoxy vitrimer as a concrete case study.

The focus is not on vitrimer chemistry itself, but on the capabilities, limitations, and underlying assumptions of the tools.


#2. Evaluated Tools and Disciplinary Background

The following tools were evaluated in this study:

Google Scholar

Semantic Scholar

OpenAlex

Connected Papers

ResearchRabbit

The Lens

VOSviewer

Most of these tools are built upon concepts from:

Bibliometrics and Scientometrics

Science Mapping

Information Retrieval

Network Science

A key premise of this evaluation is that each tool operationalizes a different notion of “distance” or “importance” in the literature, which fundamentally shapes what can be observed.


#3. Hands-on Evaluation Log

The tools are discussed below in the order they were actually tested, following a log-style structure: overview, procedure, result, and reflection.

3.1 Google Scholar
Overview

Google Scholar is the most widely used academic search engine, with its primary strength being its sheer coverage.

Procedure

Searches were performed using keywords such as:

epoxy vitrimer
epoxy vitrimer review

Results

Several thousand results were returned.

Review articles were included, but could not be reliably filtered.

Sorting by citation count was unstable, and results varied between sessions.

Reflection

Google Scholar functions well as an entry point for exploration, but:

It provides little reproducibility.

It offers no insight into field structure or conceptual organization.

It is a search tool, not a mapping tool.

3.2 Semantic Scholar
Overview

Semantic Scholar emphasizes AI-based relevance ranking and citation analysis.

Procedure

The same keywords were used, and results were sorted by influence and relevance.

Results

Approximately 4,400 results were retrieved.

Review articles were not explicitly categorized.

Influence scores were useful but opaque in definition.

Reflection

Semantic Scholar is effective for initial identification of potentially important papers, but:

It is difficult to justify why certain papers are prioritized.

It does not provide a structural overview of the field.

3.3 OpenAlex
Overview

OpenAlex is an open scholarly metadata platform and successor to Microsoft Academic Graph.

Procedure

Searches for “epoxy vitrimer” were conducted to define the document corpus.

Results

Approximately 800 relevant papers were identified.

Metadata and filters were explicit, though visualization capabilities were limited.

Reflection

OpenAlex is best understood as infrastructure rather than an analysis tool.
Its primary value lies in defining transparent and reproducible corpora for downstream analysis.

3.4 Connected Papers
Overview

Connected Papers visualizes citation-based relationships, such as co-citation and bibliographic coupling.

Procedure

Representative review articles were used as seeds to generate citation graphs.
Multiple maps were generated using different starting papers.

Results

The resulting graphs formed largely single, cohesive clusters.

Foundational papers appeared at the periphery.

Application-oriented concepts (e.g., thermal performance) were not visible.

Reflection

Connected Papers captures historical and genealogical proximity, not conceptual or application-level prominence.

It is well suited for tracing research lineages, but not for assessing field structure or thematic emphasis.

3.5 ResearchRabbit
Overview

ResearchRabbit is a recommendation-oriented discovery tool designed to surface related literature.

Procedure

Collections were created using multiple review papers, and “Similar Works” and timeline views were examined.

Results

Approximately 2,000 related papers were suggested.

Results were paginated and grouped loosely by similarity.

Some degree of topic dispersion was observable.

Reflection

ResearchRabbit is valuable for discovering additional relevant papers and reducing omission, but:

The notion of similarity is not transparent.

Quantitative comparison and structural positioning are not supported.

It functions best as a complementary exploration tool.

3.6 VOSviewer
Overview

VOSviewer enables bibliometric mapping based on keyword co-occurrence, citation, or authorship networks.

Procedure

A keyword co-occurrence analysis was performed using “epoxy vitrimer” as the search term.

Binary counting and a minimum occurrence threshold of five were applied.

The top 140 keywords were extracted and exported as JSON.

The JSON file was further analyzed using Python to generate complete rankings.

Results

All keywords were ranked by occurrence frequency.

Thermal-related terms such as:

high temperature

thermal property

high glass transition temperature
appeared in the 10th–17th range.

Reflection

Thermal performance is:

Not a peripheral concept,

Yet not a core organizing principle of the field.

Instead, it functions as a recurring evaluation axis within a broader design-oriented discourse.

3.7 The Lens
Overview

The Lens integrates scholarly literature and patents, enabling analysis of application-oriented framing.

Procedure

Patent searches were conducted using:

(epoxy AND vitrimer)


followed by performance-oriented constraints:

("thermal stability" OR "heat resistance" OR "heat resistant")

Results

523 patents were identified in the baseline corpus.

162 patents (~30%) explicitly emphasized thermal performance.

Reflection

Unlike academic literature, patents foreground application requirements and performance claims.

The contrast reveals a clear divergence between academic conceptual structure and technological framing.

4. Cross-Tool Comparison
Tool	What it Measures	Role in This Study
Google Scholar	Textual matching	Entry point
Semantic Scholar	AI-ranked relevance	Initial filtering
OpenAlex	Scholarly metadata	Corpus definition
Connected Papers	Citation genealogy	Context tracing
ResearchRabbit	Similarity (opaque)	Discovery support
VOSviewer	Conceptual co-occurrence	Structural analysis
The Lens	Application framing	Academic–patent contrast
