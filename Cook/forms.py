from django import forms
from .models import Cook


class CookForm(forms.ModelForm):
    class Meta:
        model = Cook

        fields = [
            'title',
            'description',
            'cuisine',
            'ingredients',
            'cooking_time',
            'difficulty',
            'image'
        ]

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter recipe title'}),
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a short description'}),
            'cuisine': forms.Select(),
            'ingredients': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter ingredients, one per line'}),
            'cooking_time': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Example: 30'}),
            'difficulty': forms.Select(),
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }