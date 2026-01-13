---
layout: archive
title: "Research Notes"
permalink: /categories/research-notes/
author_profile: true
---

{% assign posts = site.posts | where_exp: "post", "post.categories contains 'research-notes'" %}

{% for post in posts %}
- <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
  <span style="color: #666;">({{ post.date | date: "%Y-%m-%d" }})</span>
{% endfor %}
