from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .forms import CookForm
from .models import Cook
from .serializers import CookSerializer


def home(request):
    cooks = Cook.objects.all()[:6]
    return render(request, 'home.html', {'cooks': cooks})


def recipe_list(request):
    cooks = Cook.objects.all()
    search_query = request.GET.get('search', '').strip()
    cuisine = request.GET.get('cuisine', '').strip()

    if search_query:
        cooks = cooks.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(ingredients__icontains=search_query)
        )
    if cuisine:
        cooks = cooks.filter(cuisine__iexact=cuisine)

    return render(request, 'recipe_list.html', {
        'cooks': cooks,
        'search_query': search_query,
        'selected_cuisine': cuisine,
        'cuisine_choices': Cook.CUISINE_CHOICES,
    })


def recipe_detail(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    return render(request, 'recipe_detail.html', {'cook': cook})


def create_cook(request):
    if request.method == 'POST':
        form = CookForm(request.POST,request.FILES)
        if form.is_valid():
            cook = form.save()
            messages.success(request,'Recipe created successfully.')
            return redirect('recipe_detail', pk=cook.pk)
    else:
        form = CookForm()
    return render(request,'create.html',{'form': form, 'page_title': 'Add Recipe'})


def update_cook(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    if request.method == 'POST':
        form = CookForm(request.POST, request.FILES, instance=cook)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe updated successfully.')
            return redirect('recipe_detail', pk=cook.pk)
    else:
        form = CookForm(instance=cook)
    return render(request, 'update.html', {'form': form,'cook': cook})


def delete_cook(request, pk):
    cook = get_object_or_404(Cook, pk=pk)
    if request.method == 'POST':
        cook.delete()
        messages.success(request, 'Recipe deleted successfully.')
        return redirect('recipe_list')
    return render(request, 'delete.html', {'cook': cook})


# ------------------------------ REST API ----------------------------------

class RecipeListCreateAPIView(ListCreateAPIView):
    queryset = Cook.objects.all()
    serializer_class = CookSerializer

    def get_queryset(self):
        queryset = Cook.objects.all()
        search_query = self.request.query_params.get('search')
        cuisine = self.request.query_params.get('cuisine')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
                | Q(description__icontains=search_query)
                | Q(ingredients__icontains=search_query)
            )
        if cuisine:
            queryset = queryset.filter(cuisine__iexact=cuisine)
        return queryset


class RecipeDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Cook.objects.all()
    serializer_class = CookSerializer
