---
title: Blogs
layout: template
filename: blog
--- 

# Blogs

Text here describing why we have the following posts as insights.

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
      {{ post.excerpt }}
    </li>
  {% endfor %}
</ul>
