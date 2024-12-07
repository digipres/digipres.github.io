---
title: DigiPres Commons
subtitle: Community-owned digital preservation resources
layout: base
items:
 - title: "Welcome!"
   description: "Welcome to digipres.org, a gateway to all of the wonderful community-owned and community-oriented resources dedicated to digital preservation!"
 - title: Use The DigiPres Awesome List
   image: icons/dpo-signpost.png
   link: https://github.com/digipres/awesome-digital-preservation#readme
   description: This carefully curated list of digital preservation tools and resources is the main thing that the community maintains. Please take a look!
   action: "Be Awesome"
 - title: Get Started
   image: icons/dpo-floppy-plain.png
   link: https://github.com/digipres/awesome-digital-preservation?tab=readme-ov-file#get-started
   description: "Find out how to start preserving your digital stuff."
   action: "Start Here"
 - title: Something Wrong?
   description: 'Broken or missing link? Website problems? Feature requests? Please raise them here.'
   link: https://github.com/digipres/digipres.github.io/issue
   action: "Raise an Issue"
 - title: Talk It Through
   image: icons/dpo-digipres-club.png
   link: https://github.com/digipres/awesome-digital-preservation?tab=readme-ov-file#become-part-of-the-digital-preservation-community
   description: "Find like-minded souls on digipres.club, mailings lists, forums and conferences."
   action: "Let's Talk"
 - title: Find Formats
   image: icons/dpo-formats.png
   link: /formats/
   description: "Search across multiple format registries at once, to help you understand the contents of your digital collections."
 - title: Track Down Tools
   image: icons/dpo-workbench.png
   link: https://coptr.digipres.org/
   description: "Use the COPTR wiki to find tools to help you do digital preservation."
 - title: Find Publications
   image: icons/dpo-publications.png
   link: /publications/
   description: "Find publications on digital preservation issues via this dedicated search service and database."
 - title: Review Policies
   image: icons/dpo-policies.png
   link: /policies/
   description: "Learn from others via this list of digital preservation policies from across the world."
 - title: Explore Workflows
   image: icons/dpo-workflows.png
   link: https://coptr.digipres.org/index.php/Workflow:Community_Owned_Workflows
   description: "Share your digital workflows, and explore how other peoples systems solve our shared challenges."
 - title: Download Test Files
   image: icons/dpo-workbench.png
   link: https://github.com/digipres/awesome-digital-preservation?tab=readme-ov-file#find-test-files
   description: "Explore all the sets of openly-available files you download and use to test tools, tactics and workflows."
 - title: Experiment with the Workbench
   image: icons/dpo-workbench.png
   link: /workbench/
   description: "Try out the experimental DigiPres Workbench. Explore your formats. Compare your collections. Play with DigiPres tools, without installing a thing!"
   action: "For Science!"
 - title: Want to talk about digipres.org?
   description: "Please use our discussion forum if you want to talk to us about digipres.org."
   link: https://github.com/orgs/digipres/discussions
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
          <a class="nav-link" href="https://github.com/digipres/digipres.github.io">GitHub</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://github.com/digipres/digipres.github.io/issues">Issues</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://github.com/orgs/digipres/discussions">Discussion</a>
        </li>
      </ul>
    </div>
  </div>
</nav>


<main class="container-fluid masonry">
  <div class="row" data-masonry='{"percentPosition": true }'>
{% for item in page.items %}
    <div class="col-6 col-sm-4 col-md-4 col-lg-3 col-xl-2 p-1">
      <div class="card{% if item.image == nil %} text-bg-light{% endif %}">
        {% if item.image %}<img src="{{ item.image }}" class="card-img" alt="{{ item.title | default: 'a decorative image' }}">{% endif %}
        <div class="card-body">
          {% if item.title %}<h5 class="card-title">{{ item.title }}</h5>{% endif %}
          {% if item.description %}<p class="card-text">{{ item.description }}</p>{% endif %}
          {% if item.subtext %}<p class="card-text"><small class="text-muted">{{ item.subtext }}</small></p>{% endif %}
          {% if item.link %}<a href="{{ item.link }}" target="_new" class="btn btn-primary float-end stretched-link">{{ item.action | default: 'Go' }}</a>{% endif %}
        </div>
      </div>
    </div>
{% endfor %}
  </div>

</main>

<script sync src="https://unpkg.com/imagesloaded@5/imagesloaded.pkgd.min.js"></script>
<script sync src="https://cdn.jsdelivr.net/npm/masonry-layout@4.2.2/dist/masonry.pkgd.min.js" integrity="sha384-GNFwBvfVxBkLMJpYMOABq3c+d3KnQxudP/mGPkzpZSTYykLBNsZEnG2D9G/X/+7D" crossorigin="anonymous"></script>

<script>
  window.addEventListener('load', function () {
    // Wait for images to load before using the masonry layout, as per https://masonry.desandro.com/layout#imagesloaded
    var cards = document.getElementsByClassName("masonry").imagesLoaded( function() {
      // init Masonry after all images have loaded
      cards.masonry();
    });
  });
</script>
