---
title: DigiPres.org
subtitle: Digital preservation community portal
layout: base
items:
 - title: "Welcome!"
   description: "<p>Welcome to DigiPres.org, a gateway to all of the wonderful community-owned and community-oriented resources dedicated to digital preservation! </p><p>Any questions or comments? Please join our <a href='https://www.dpconline.org/digipres/pr-sig'>online meet-ups</a> (lurkers welcome!) or use <a href='https://github.com/orgs/digipres/discussions'>our forums</a>.</p><p>Something wrong? Broken or missing link? Please <a href='https://github.com/digipres/digipres.github.io/issues'>raise an issue</a>! Website or sevice down or broken? <a href='https://github.com/orgs/digipres/discussions/categories/incidents-outages'>Check for/report outages or incidents!</a></p>"
   link: https://github.com/digipres/digipres.github.io
   action: "Go"
   subtext: Hosted by GitHub
   button-class: btn-primary

 - title: Find Your Crowd
   image: icons/dpo-digipres-club.png
   link: /communities/
   description: "Find like-minded souls on digipres.club, mailings lists, forums and conferences."
   action: "Let's Talk"

 - title: Get Started
   image: icons/dpo-floppy-plain.png
   link: https://github.com/digipres/awesome-digital-preservation?tab=readme-ov-file#get-started
   description: "Find out how to start preserving your digital stuff."
   action: "Start Here"

 - title: Use The DigiPres Awesome List
   image: icons/dpo-signpost.png
   link: https://github.com/digipres/awesome-digital-preservation#readme
   description: This carefully curated list of digital preservation tools and resources is the main thing that the community maintains. Please take a look!
   subtext: "Be Awesome"

 - title: Find Formats
   image: icons/dpo-formats.png
   link: /formats/
   description: "Search across multiple format registries at once, to help you understand the contents of your digital collections."

 - title: Track Down Tools
   image: icons/dpo-tools.png
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
   link: /workflows/
   description: "Share your digital workflows, and explore how other peoples systems solve our shared challenges."

 - title: Download Test Files
   image: icons/dpo-test-files.png
   link: https://github.com/digipres/awesome-digital-preservation?tab=readme-ov-file#find-test-files
   description: "Explore all the sets of openly-available files you download and use to test tools, tactics and workflows."

 - title: Experiment with the Workbench
   image: icons/dpo-workbench.png
   link: /workbench/
   description: "Try out the experimental DigiPres Workbench. Explore your formats. Compare your collections. Play with DigiPres tools, without installing a thing!"
   action: "For Science!"

 - title: Credits
   description: '<p>The images used on this website were derived from the <a href="https://wiki.dpconline.org/index.php?title=SPRUCE_Digital_Preservation_Illustrations" class="link-body-emphasis">SPRUCE Digital Preservation Illustrations</a>, created by <a href="http://www.tomwoolley.com/" class="link-body-emphasis">Tom Woolley</a> and released under a <a href="https://creativecommons.org/licenses/by-nc/3.0/deed.en" class="link-body-emphasis">CC-BY-NC</a> license thanks to funding from <a href="http://jisc.ac.uk/" class="link-body-emphasis">Jisc</a>.</p>'
   card-class: text-bg-light
---

<main class="container mt-0">
  <div class="row">
{% for item in page.items %}
    <div class="col-6 col-sm-6 col-md-4 col-lg-3 col-xl-3 p-1">
      <div class="card h-100 {{ item.card-class | default: ''}}">
        {% if item.image %}<img src="{{ item.image }}" class="card-img" alt="{{ item.title | default: 'a decorative image' }}">{% endif %}
        <div class="card-body h-100 d-flex flex-column">
          {% if item.title %}<h5 class="card-title">{{ item.title }}</h5>{% endif %}
          {% if item.description %}<p class="card-text">{{ item.description }}</p>{% endif %}
          {% if item.link %}
          <div class="d-flex justify-content-between align-items-center mt-auto">
          <p class="card-text mb-0"><small class="text-muted">{{ item.subtext | default: ''}}</small></p>
          <a href="{{ item.link }}" target="_new" class="btn {{ item.button-class | default: 'btn-primary stretched-link'}}">{{ item.action | default: 'Go' }}</a>
          </div>
          {% endif %}
        </div>
      </div>
    </div>
{% endfor %}
  </div>

</main>

