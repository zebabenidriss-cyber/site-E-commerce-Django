# fait en sorte que l'application soit utilisable dans un projet Django en définissant les URL pour l'application Store
from django.urls import path
from Store.views import index

urlpatterns = [
    path('', index, name='home'), # définit l'URL de la page d'accueil de l'application Store. Lorsque l'utilisateur accède à l'URL racine de l'application, la fonction index est appelée pour afficher la page d'accueil.
]