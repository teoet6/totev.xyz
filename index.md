# Теодор Тотев

## 📝 Публикации

{% for post in site.posts reversed %}
### [{{ post.title }}]({{ post.url }}) {{ post.date | date: "%Y-%m-%d" }}

{{ post.excerpt }}
{% endfor %}
