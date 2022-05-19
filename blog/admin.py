from django.contrib import admin
from .models import Article, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'category']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_display_links = ['title']
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)