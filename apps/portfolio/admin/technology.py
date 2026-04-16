from django.contrib import admin
from ..models.technology import Technology

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
