---
title: DigiPres Commons
subtitle: Community-owned digital preservation resources
layout: base
items:
 - title: The DigiPres Awesome List
   image: icons/dpo-signpost.png
   link: https://github.com/digipres/awesome-digital-preservation#readme
   description: This carefully curated list of digital preservation tools and resources is the main thing that the community maintains. Please take a look! 
 - description: 'The goal of this gateway website to help the members of the international digital preservation community to find each other, to grow, and to find ways to support each other. Crucially, we want to help pool our knowledge and resources so we can do more and better preservation, and try to avoid anyone re-inventing the wheel. Of course, this ethos also extends to this site, so please <a href="https://github.com/digipres/digipres.github.io/issues">raise any issues (e.g. what have we missed?)</a>, <a href="https://github.com/digipres/digipres.github.io">contribute to this web site</a>, or <a href="https://github.com/orgs/digipres/discussions">discuss your ideas with us</a>.'
 - title: Find Formats
   image: icons/dpo-formats.png
   link: /formats/
   description: "Search across multiple format registries at once, to help you understand the contents of your digital collections."
 - title: Find Publications
   image: icons/dpo-publications.png
   link: /publications/
   description: "Find publications on digital preservation issues via this dedicated search service and database."
 - title: Review Policies
   image: icons/dpo-policies.png
   link: /policies/
   description: "Learn from others via this list of digital preservation policies from across the world."
 - description: "With thanks to the <a href='https://openpreservation.org/'>Open Preservation Foundation</a> and <a href='https://www.dpconline.org/'>Digital Preservation Coalition</a> for hosting and supporting many of these resources."
 - title: Explore Workflows
   image: icons/dpo-workflows.png
   link: https://coptr.digipres.org/index.php/Workflow:Community_Owned_Workflows
   description: "Share your digital workflows, and explore how other peoples systems solve our shared challenges."
 - title: Experiment with the Workbench
   image: icons/dpo-workbench.png
   link: /workbench/
   description: "Try out the experimental DigiPres Workbench. Explore your formats. Compare your collections. Play with DigiPres tools, without installing a thing!"
 - description: 'The images used on this website were derived from the <a href="https://wiki.dpconline.org/index.php?title=SPRUCE_Digital_Preservation_Illustrations">SPRUCE Digital Preservation Illustrations</a>, created by <a href="http://www.tomwoolley.com/">Tom Woolley</a> and released under a <a href="https://creativecommons.org/licenses/by-nc/3.0/deed.en">CC-BY-NC</a> license thanks to funding from <a href="http://jisc.ac.uk/">Jisc</a>.'
---

<nav class="navbar navbar-expand-lg navbar-light bg-white">
  <div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarToggler" aria-controls="navbarToggler" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarToggler">
      <a class="navbar-brand fw-bolder" href="/">{{page.title}}</a>
      <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
      </ul>
    </div>
  </div>
</nav>


<main class="container-fluid">
  <div class="row" data-masonry='{"percentPosition": true }'>
{% for item in page.items %}
    <div class="col-6 col-sm-4 col-md-3 col-xl-2 p-1">
      <div class="card">
        {% if item.image %}<img src="{{ item.image }}" class="card-img" alt="...">{% endif %}
        <div class="card-body">
          {% if item.title %}<h5 class="card-title">{{ item.title }}</h5>{% endif %}
          {% if item.description %}<p class="card-text">{{ item.description }}</p>{% endif %}
          {% if item.link %}<a href="{{ item.link }}" target="_new" class="btn btn-primary float-end stretched-link">Go</a>{% endif %}
          {% if item.subtext %}<p class="card-text"><small class="text-muted">{{ item.subtext }}</small></p>{% endif %}
        </div>
      </div>
    </div>
{% endfor %}
  </div>

</main>

<script sync src="https://cdn.jsdelivr.net/npm/masonry-layout@4.2.2/dist/masonry.pkgd.min.js" integrity="sha384-GNFwBvfVxBkLMJpYMOABq3c+d3KnQxudP/mGPkzpZSTYykLBNsZEnG2D9G/X/+7D" crossorigin="anonymous"></script>
