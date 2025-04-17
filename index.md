---
title: Campfire Chat Schedule
layout: withtable
---

This "campfire chat" (rather than a "[fireside chat](https://en.wikipedia.org/wiki/Fireside_chats)") is a series of informal conversations between young aspiring economists (initially, as part of various LDI-related internships in <a href="https://aeadataeditor.github.io/projects/project6" alt="Link to internship in economics">economics</a> and <a href="https://transparency-certified.github.io/jobs/cornell" alt="Link to internship in computer science">computer science</a>) and economists who are starting, or are well under way, in a career as ... economists? Participants include graduate students, data scientists (who started as economists), economists working for the private sector as well as those working for, or even leading, major statistical agencies. 

> Participation is by invitation only, but please do reach out if you think you would like to be invited to this or similar events.

<div class="tabs">
  <button class="tablinks active" onclick="openTab(event, 'tab2025')">2025</button>
  <button class="tablinks" onclick="openTab(event, 'tab2024')">2024</button>
</div>

<div id="tab2025" class="tabcontent" style="display: block;">
  <h2>Summer 2025 Schedule</h2>
  <table class="display">
    {% for row in site.data.schedule_2025 %}
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
      <td> {% if row["Who"] %} {{ row["Who"] }} {% else %} TBA {% endif %}
      {% if row["Current affiliation"] %}(<em>{{ row["Current affiliation"] }}</em>){% endif %} </td>
      <td> {{ row["Brief vitae"] }} 
      {% if row["Personal website"] %}
          <br/><em>For more information, see the <a href='{{ row["Personal website"] }}' alt="Link to personal website">personal webpage</a>.</em> 
          {% endif %}
          </td>
    </tr>
    {% endfor %}
  </table>
</div>

<div id="tab2024" class="tabcontent">
  <h2>Summer 2024 Schedule</h2>
  <table class="display">
    {% for row in site.data.schedule_2024 %}
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
      <td> {% if row["Who"] %} {{ row["Who"] }} {% else %} TBA {% endif %}
      {% if row["Current affiliation"] %}(<em>{{ row["Current affiliation"] }}</em>){% endif %} </td>
      <td> {{ row["Brief vitae"] }} 
      {% if row["Personal website"] %}
          <br/><em>For more information, see the <a href='{{ row["Personal website"] }}' alt="Link to personal website">personal webpage</a>.</em> 
          {% endif %}
          </td>
    </tr>
    {% endfor %}
  </table>
</div>

<script>
function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  // Force a layout recalculation to ensure proper width
  document.getElementById(tabName).style.width = "100%";
  document.getElementById(tabName).querySelector("table").style.width = "100%";
  evt.currentTarget.className += " active";
}

// Execute after page load to ensure initial tab is properly sized
document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("tab2025").style.width = "100%";
  document.getElementById("tab2025").querySelector("table").style.width = "100%";
});
</script>

