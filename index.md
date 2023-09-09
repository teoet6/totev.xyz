На тази страница ще има повече неща, но засега има само

## 📝 Публикации

{% for post in site.posts reversed %}
### [{%- include lat2cyr lat=post.title -%} | {{ post.date | date: "%Y-%m-%d" }}]({{ post.url }})

{{ post.excerpt }}

{% endfor %}
