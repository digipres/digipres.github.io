---
title: Community-Owned Workflows
---

This is an experiment to see if there are benefits to having a dedicated home for [Community-Owned Workflows](https://coptr.digipres.org/index.php/Workflow:Community_Owned_Workflows).

{% assign wfs = site.pages | where_exp: "item", "item.path contains 'workflows/'" %}

<ul>
{% for item in wfs %}
{% if item.path != 'workflows/index.md' %}
<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endif %}
{% endfor %}
</ul>