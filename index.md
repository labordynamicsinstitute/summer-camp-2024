---
title: Summer "campfire chat" schedule 2024
layout: withtable
---

This "campfire chat" (rather than a "fireplace chat") is a series of informal conversations between young aspiring economists (initially, as part of various LDI-related internships in [economics] and [computer science]) and economists who are starting, or are well under way, in a career as ... economists? Participants include graduate students, data scientists (who started as economists), economists working for the private sector as well as those working for, or even leading, major statistical agencies. 

> Participation is by invitation only, but please do reach out if you think you would like to be invited to this or similar events.


<table class="display">
  {% for row in site.data.schedule %}
    {% if forloop.first %}
    <thead>
    <tr>
      <td> Week </td>
      <td> Date </td>
      <td> Time </td>
      <td> Presenter </td>
      <td> Brief vitae </td>
    </tr>
    </thead>
    {% endif %}

  <!-- manually constructing table -->
  <!-- Week,Date,Time,Who,Current affiliation,Brief vitae,Personal website -->
  <tr>
    <td> {{ row["Week"] }} </td>
    <td> {{ row["Date"] }} </td>
    <td> {{ row["Time"] }} </td>
    <td> {{ row["Who"] }} (<em>{{ row["Current affiliation"] }}</em>) </td>
    <td> {{ row["Brief vitae"] }} 
    {% if row["Personal website"] %}
        <br/><em>For more information, see the [personal webpage]({{ row["Personal website"] }})</em> 
        {% endif %}
        </td>
  </tr>
  {% endfor %}
</table>

