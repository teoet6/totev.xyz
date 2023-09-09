# Теодор Тотев

На тази страница ще има повече неща, но засега има само

## 📝 Публикации

{% for post in site.posts reversed %}
### [{%- include lat2cyr lat=post.title -%}]({{ post.url }}) | {{ post.date | date: "%Y-%m-%d" }}

{{ post.excerpt }}

{% endfor %}
