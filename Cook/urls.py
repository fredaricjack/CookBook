from django.urls import path
from . import views

urlpatterns = [
    # Normal HTML pages (work in Chrome without JavaScript)
    path('', views.home, name='home'),
    path('recipes/', views.recipe_list, name='recipe_list'),
    path('recipes/add/', views.create_cook, name='recipe_create'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:pk>/edit/', views.update_cook, name='recipe_update'),
    path('recipes/<int:pk>/delete/', views.delete_cook, name='recipe_delete'),

    # Django REST Framework API (JSON + browsable HTML interface in Chrome)
    path('api/recipes/', views.RecipeListCreateAPIView.as_view(), name='api_recipe_list'),
    path('api/recipes/create/', views.RecipeListCreateAPIView.as_view(), name='api_recipe_create'),
    path('api/recipes/<int:pk>/', views.RecipeDetailAPIView.as_view(), name='api_recipe_detail'),
]
