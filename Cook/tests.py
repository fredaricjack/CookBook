from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Cook


class RecipeWebsiteTests(TestCase):
    def setUp(self):
        self.cook = Cook.objects.create(
            title='Masala Dosa', description='Crispy dosa', cuisine='Indian',
            ingredients='Rice, urad dal, potato', cooking_time=30, difficulty='Medium'
        )

    def test_homepage_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Masala Dosa')

    def test_recipe_list_search(self):
        response = self.client.get(reverse('recipe_list'), {'search': 'Dosa'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Masala Dosa')

    def test_create_recipe(self):
        response = self.client.post(reverse('recipe_create'), {
            'title': 'Pasta', 'description': 'Creamy pasta', 'cuisine': 'Italian',
            'ingredients': 'Pasta, cream', 'cooking_time': 20, 'difficulty': 'Easy'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Cook.objects.filter(title='Pasta').exists())


class RecipeAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_api_create_and_list(self):
        payload = {
            'title': 'Veg Noodles', 'description': 'Stir fried noodles',
            'cuisine': 'Chinese', 'ingredients': 'Noodles, vegetables',
            'cooking_time': 15, 'difficulty': 'Easy'
        }
        create_response = self.client.post('/api/recipes/', payload, format='json')
        self.assertEqual(create_response.status_code, 201)
        list_response = self.client.get('/api/recipes/')
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(len(list_response.data), 1)
