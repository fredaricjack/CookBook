from django.core.validators import MinValueValidator
from django.db import models


class Cook(models.Model):
    CUISINE_CHOICES = [
        ('Indian', 'Indian'), ('Chinese', 'Chinese'), ('Italian', 'Italian'),
        ('Mexican', 'Mexican'), ('Continental', 'Continental'), ('Other', 'Other'),
    ]
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'), ('Medium', 'Medium'), ('Hard', 'Hard'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    cuisine = models.CharField(max_length=100, choices=CUISINE_CHOICES)
    ingredients = models.TextField()
    cooking_time = models.IntegerField(validators=[MinValueValidator(1)])
    difficulty = models.CharField(max_length=50, choices=DIFFICULTY_CHOICES)
    image = models.ImageField(upload_to='recipes/',blank=True,null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
