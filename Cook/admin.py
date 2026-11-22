from django.contrib import admin
from .models import Cook


@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cuisine', 'cooking_time', 'difficulty')
    list_filter = ('cuisine', 'difficulty')
    search_fields = ('title', 'description', 'ingredients')
