# Теодор Тотев

## 📝 Публикации

{% for post in site.posts reversed %}
### [{%- include lat2cyr.liquid lat=post.title -%}]({{ post.url }}) {{ post.date | date: "%Y-%m-%d" }}

{{ post.excerpt }}
{% endfor %}
