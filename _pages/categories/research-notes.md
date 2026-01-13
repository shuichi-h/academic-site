---
layout: single
title: "Research Notes"
permalink: /categories/research-notes/
category: research-notes
author_profile: true
---

{% assign notes = site.posts | where_exp: "post", "post.categories contains 'research-notes'" %}

{% if notes.size > 0 %}
<ul>
  {% for post in notes %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <small>({{ post.date | date: "%Y-%m-%d" }})</small>
    </li>
  {% endfor %}
</ul>
{% else %}
<p>No Research Notes yet.</p>
{% endif %}
