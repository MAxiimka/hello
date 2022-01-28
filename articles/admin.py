from django.contrib import admin
from .models import Article, Comment
# Register your models here.(Возможно редактировать,в админки приложение )

admin.site.register(Article)
admin.site.register(Comment)