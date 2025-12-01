---
title: Digital Preservation Workflows
redirect_from: /workflow-webinars/
---



## Workflow Webinars

{% assign wfs = site.pages | where_exp: "item", "item.path contains 'workflow-webinars/'" %}

<ul>
{% for item in wfs %}
{% if item.path != 'workflow-webinars/index.md' %}
<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endif %}
{% endfor %}
</ul>


Originally published at:

- Workflow Webinars
    - 2025: [Digital Preservation Workflow Webinars 2025 - Digital Preservation Coalition](https://www.dpconline.org/events/eventdetail/434/-/digital-preservation-workflow-webinars-2025)
    - 2024: [Digital Preservation Workflow Webinars 2024 - Digital Preservation Coalition](https://www.dpconline.org/events/eventdetail/254/-/digital-preservation-workflow-webinars-2024)
    - 2023: [Digital Preservation Workflow Webinars 2023 - Digital Preservation Coalition](https://www.dpconline.org/events/eventdetail/114/-/digital-preservation-workflow-webinars-2023)
        - [Workflow:Abrdn Digital Preservation Workflow - COPTR Staging](https://coptr.openpreservation.org/index.php/Workflow:Abrdn_Digital_Preservation_Workflow) ?
    - 2022: [Digital Preservation Workflow Webinars and COW-a-thon - Digital Preservation Coalition](https://www.dpconline.org/events/past-events/webinars/dp-workflows-cowathon-2022)
    - 2021: [Digital Preservation Workflows Webinar Series and COW-a-thon event - Digital Preservation Coalition](https://www.dpconline.org/events/past-events/webinars/workflow-webinars-and-cow)


## Workflows

This is an experiment to see if there are benefits to having a dedicated home for [Community-Owned Workflows](https://coptr.digipres.org/index.php/Workflow:Community_Owned_Workflows).

{% assign wfs = site.pages | where_exp: "item", "item.path contains 'workflows/'" %}

<ul>
{% for item in wfs %}
{% if item.path != 'workflows/index.md' %}
<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endif %}
{% endfor %}
</ul>