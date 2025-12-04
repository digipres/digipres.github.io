---
title: Community-owned Workflows
redirect_from: /workflow-webinars/
---

<img src="../assets/img/cow-logo.png" class="img-fluid mx-auto d-block" alt="Community-Owned Workflows logo">

Digital preservation needs great tools and systems, but nothing gets done without the support of the people and processes that knit those components into the day-to-day workflows that meet your goals. Great workflows with clear goals also help us cope over the long term, even as the tools and systems we rely on come and go.  That's why it's important to share workflows and learn from each other.

## Workflows

You can add details of your own workflows to the [Community-Owned Workflows](https://coptr.digipres.org/index.php/Workflow:Community_Owned_Workflows) part of the [COPTR wiki](https://coptr.digipres.org/).

## Workflow Webinars

The [Digital Preservation Coalition](https://dpconline.org/) has been running a series of "Workflow Webinars" for many years. These events are open to all, not just DPC members, and have become a popular forum for sharing the practical details involved in implementing digital preservation processes.  If you'd like to share your workflows look out for the call for contributions from the DPC, or get in touch with them directly via [the contact details on their web site](https://www.dpconline.org/about/contact-us).

The webinars from previous years are available 
on the DPC Website...

- 2025: [Digital Preservation Workflow Webinars 2025 - Digital Preservation Coalition](https://www.dpconline.org/events/eventdetail/434/-/digital-preservation-workflow-webinars-2025)
- 2024: [Digital Preservation Workflow Webinars 2024 - Digital Preservation Coalition](https://www.dpconline.org/events/eventdetail/254/-/digital-preservation-workflow-webinars-2024)
- 2023: [Digital Preservation Workflow Webinars 2023 - Digital Preservation Coalition](https://www.dpconline.org/events/eventdetail/114/-/digital-preservation-workflow-webinars-2023)
    - See also [Workflow:Abrdn Digital Preservation Workflow - COPTR Staging](https://coptr.openpreservation.org/index.php/Workflow:Abrdn_Digital_Preservation_Workflow)
- 2022: [Digital Preservation Workflow Webinars and COW-a-thon - Digital Preservation Coalition](https://www.dpconline.org/events/past-events/webinars/dp-workflows-cowathon-2022)
- 2021: [Digital Preservation Workflows Webinar Series and COW-a-thon event - Digital Preservation Coalition](https://www.dpconline.org/events/past-events/webinars/workflow-webinars-and-cow)

## Workflows & Webinars as Structured Data

<div class="alert alert-warning" role="alert">
  This is an experimental addition to the site, and feedback is very welcome. You can read <a href="https://github.com/orgs/digipres/discussions/63" class="alert-link">this GitHub discussion</a> to find out more about the status of this experiment.
</div>

As part of the [Registries of Good Practice project](https://www.dpconline.org/digipres/collaborative-projects/registries-of-good-practice), we are also experimenting with a different ways of documenting workflows. Here are the example(s) we've added or copied over from the COPTR wiki:

{% assign wfs = site.pages | where_exp: "item", "item.path contains 'workflows/'" %}

<ul>
{% for item in wfs %}
{% if item.path != 'workflows/index.md' %}
<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endif %}
{% endfor %}
</ul>

We are also experimenting with re-hosting the workflow webinars as more structured data:

{% assign wfs = site.pages | where_exp: "item", "item.path contains 'workflow-webinars/'" %}

<ul>
{% for item in wfs %}
{% if item.path != 'workflow-webinars/index.md' %}
<li><a href="{{ item.url }}">{{ item.title }} ({{item.start | date: '%-d %b' }} - {{item.end | date: '%-d %b %Y' }})</a></li>
{% endif %}
{% endfor %}
</ul>

_Please note there are no plans to change the Community-owned Workflows part COPTR wiki._ This is just a proof of concept implementation, to explore what might be done in the future. Please see the GitHub discussion linked above for more details.