from django.contrib import admin
from .models import category, Product , commande # Import des modèles

#python manage.py createsuperuser : creation d'un super utilisateur pour accéder à l'interface d'administration
#python manage.py runserver : pour lancer le serveur de développement et accéder à l'interface d'administration via l'URL /admin
#python manage.py migrate : pour appliquer les migrations et créer les tables dans la base de données
#python manage.py makemigrations : pour créer de nouvelles migrations en fonction des modifications apportées aux modèles

# username : benizeba5@gmail.com
# mot de passe : Cadrage@223
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom', 'date_ajout') # Affiche les champs nom et date_ajout dans la liste des catégories
    search_fields = ('nom',) # Permet de rechercher les catégories par nom

class productAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'date_ajout') # Affiche les champs title, price, category et date_ajout dans la liste des produits
    search_fields = ('title', 'description') # Permet de rechercher les produits par title et description
    list_filter = ('category',) # Permet de filtrer les produits par catégorie


admin.site.register(category, CategoryAdmin) # Register le modèle Category dans l'interface d'administration
admin.site.register(Product, productAdmin) # Register le modèle Product dans l'interface d'administration
admin.site.register(commande) # Register le modèle commande dans l'interface d'administration

