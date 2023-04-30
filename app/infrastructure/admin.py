from django.contrib import admin
from app.infrastructure.db.models import List, Item


@admin.register(List)
class ListResource(admin.ModelAdmin):
    list_display = ["id", "name"]


@admin.register(Item)
class ItemResource(admin.ModelAdmin):
    list_display = ["id", "text", "list"]
