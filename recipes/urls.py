from django.urls import path
from .views import RecipeDetailView
from .views import RecipeListView

urlpatterns = [
    path('',RecipeListView.as_view(),name='recipes' ),
    path('recipe/<int:pk>/',RecipeDetailView.as_view(), name = "recipe-detail"),
]
