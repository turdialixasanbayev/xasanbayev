from django.contrib import admin
from .models import ContactUS

@admin.register(ContactUS)
class ContactUSAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'phone')
