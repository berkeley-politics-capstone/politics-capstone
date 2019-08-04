---
title: Blogs
layout: template
filename: blog
--- 

# Blogs

Using data science techniques like panel modeling and natural language processing, we've uncovered some interesting insights thus far into the 2020 Democratic primary. Feel free to take a look below.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
