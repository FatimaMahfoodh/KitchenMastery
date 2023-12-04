from .models import Recipe
from django.views.generic import ListView, DetailView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipedetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients'] = self.object.get_ingredients()
        context['instructions'] = self.object.get_instructions()
        return context
    