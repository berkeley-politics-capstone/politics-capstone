---
title: Blogs
layout: template
filename: blog
--- 

# Blogs

Text here describing why we have the following posts as insights.

{% for post in site.posts %}
  <a href="{{ post.url }}">
  <h2>{{ post.title }}</h2></a><br />
  {{ post.date | date_to_string }}
  <p>{{ post.excerpt }}</p>
{% endfor %}
