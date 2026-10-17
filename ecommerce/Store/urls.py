# fait en sorte que l'application soit utilisable dans un projet Django en définissant les URL pour l'application Store
from django.urls import path
from Store.views import index , detail

urlpatterns = [
    path('', index, name='home'),  # définit l'URL de la page d'accueil de l'application Store. Lorsque l'utilisateur accède à l'URL racine de l'application, la fonction index est appelée pour afficher la page d'accueil.
    path('<int:myid>/', detail, name='detail'),  # définit l'URL de la page de détail d'un produit spécifique. Lorsque l'utilisateur accède à cette URL, la fonction detail est appelée pour afficher les détails du produit.
]