---
title: GOTO
layout: simple_page
---

This is a folder for managing short alias links to other resources. This is so reasonably simple links can be shared without locking down the final resource and repository names, etc. Apply sparingly.

## List of redirects

{% assign items = site.pages | where_exp: "item", "item.redirect_to != nil" %}

<ul>
{% for item in items %}
<li><a href="{{ item.url }}">{{ item.title }}</a><br><i>{{ item.url }} --> {{ item.redirect_to }}</i></li>
{% endfor %}
</ul>