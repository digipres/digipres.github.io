---
title: COPTR
subtitle: User Contributions
---

<div class="row">

<div class="col-xs-12 col-sm-4 col-md-4">
</div>

<div class="col-xs-12 col-sm-4 col-md-4">
</div>

<div class="col-xs-12 col-sm-4 col-md-4">
<div class="panel panel-default">
  <div class="panel-heading">Top Contributors (All-Time)</div>
  <div class="panel-body">

<table class="table">
<thead>
<tr><th>Username</th><th>Edit Count</th></tr>
</thead>
<tbody>
{% for u in site.data.coptr-users %}
  <tr>
  <td>
    <a href="http://coptr.digipres.org/User:{{ u.name }}">
      {{ u.name }}
    </a>
  </td>
  <td>
    <a href="http://coptr.digipres.org/Special:Contributions/{{ u.name }}">
      {{ u.editcount }}
    </a>
  </td>
  </tr>
{% endfor %}
</tbody>
</table>

  </div>
</div>

</div>
