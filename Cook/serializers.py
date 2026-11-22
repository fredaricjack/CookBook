from rest_framework import serializers
from .models import Cook


class CookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cook
        fields = ['id', 'title', 'description', 'cuisine', 'ingredients', 'cooking_time', 'difficulty', 'image']
        read_only_fields = ['id']
