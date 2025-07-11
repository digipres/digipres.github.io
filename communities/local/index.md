---
title: Local & Regional Groups
---

This page lists local and regional groups dedicated to digital preservation. They don't necessarily meet face to face, but the members are close enough that it's possible some of them could meet in person from time to time.

{% assign locals = site.pages | where_exp: "item", "item.dir contains page.dir" %}

<!-- Leaflet support -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css"
     integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY="
     crossorigin=""/>
<!-- Make sure you put this AFTER Leaflet's CSS -->
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"
     integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo="
     crossorigin=""></script>

<div id="map" class="my-3"></div>
<style>
    #map { height: 500px; }
</style>
<script type="module">
    var map = L.map('map').setView([19, 15], 2);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 7,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

{% for item in locals %}
{% if item.dir != page.dir %}
{% if item.location != nil %}
    L.geoJSON(JSON.parse({{ item.location | jsonify }})).bindPopup(
        "<div class='text-center'><b>{{ item.title }}</b><br>{{ item.region }}<br><a class='btn btn-primary btn-sm text-white' role='button' href='{{ item.url }}'>Find out more...</a></div>"
    ).addTo(map);
{% endif %}
{% endif %}
{% endfor %}

</script>

<p class="text-center">
<a href="/admin/#/collections/local-groups/new" class="btn btn-primary m-2">Add A Group To This Map</a>
<a href="../start/" class="btn btn-primary m-2">Start Your Own Group</a>
</p>

<div class="row mx-0">
{% for item in locals %}
{% if item.dir != page.dir %}
<div class="col-6 col-sm-6 col-md-4 col-lg-3 col-xl-3 p-1 py-0">
    <div class="card h-100 {{ item.card-class | default: ''}}">
    <div class="card-body h-100 d-flex flex-column">
        {% if item.title %}<h5 class="card-title">{{ item.title }}</h5>{% endif %}
        {% if item.region %}<p class="card-text">{{ item.region }}</p>{% endif %}
        {% if item.url %}
        <div class="d-flex justify-content-between align-items-center mt-auto">
        <p class="card-text m-0"><small class="text-muted">{{ item.subtext | default: ''}}</small></p>
        </div>
        <a href="{{ item.url }}" class="btn {{ item.button-class | default: 'btn-primary stretched-link'}}">{{ item.action | default: 'Find out more...' }}</a>
        {% endif %}
    </div>
    </div>
</div>
{% endif %}
{% endfor %}
</div>