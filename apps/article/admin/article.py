from django.contrib import admin
from ..models.article import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ("name",)}
    autocomplete_fields = ('category', 'author',)
