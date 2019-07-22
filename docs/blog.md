---
title: Blogs
layout: template
filename: blog
--- 

# Blogs

Text here describing why we have the following posts as insights.

{% for post in site.posts %}
  ###<a href="{{ post.url }}">{{ post.title }}</a>
  {{ post.excerpt }}
{% endfor %}
