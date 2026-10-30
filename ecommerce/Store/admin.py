import json

from django.contrib import admin
from django.utils.html import format_html_join

from .models import category, Product, commande # Import des modèles

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

class commandeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'produits_commandes', 'ville', 'pays', 'date_ajout')
    search_fields = ('nom', 'email', 'adresse', 'ville', 'pays', 'zip_code')
    list_filter = ('date_ajout',)

    @admin.display(description='Produits commandés')
    def produits_commandes(self, obj):
        try:
            items = json.loads(obj.items)
        except (TypeError, json.JSONDecodeError):
            return 'Données invalides'

        if isinstance(items, dict):
            product_ids = [int(product_id) for product_id in items]
            products_by_id = Product.objects.in_bulk(product_ids)
            legacy_items = []
            for product_id, quantity in items.items():
                product = products_by_id.get(int(product_id))
                if product:
                    legacy_items.append({
                        'name': product.title,
                        'quantity': quantity,
                    })
            items = legacy_items
        elif not isinstance(items, list):
            return 'Aucun produit'

        return format_html_join(
            '<br>',
            '{} x{}',
            (
                (item.get('name', 'Produit inconnu'), item.get('quantity', 0))
                for item in items
                if isinstance(item, dict)
            ),
        ) or 'Aucun produit'


admin.site.register(category, CategoryAdmin) # Register le modèle Category dans l'interface d'administration
admin.site.register(Product, productAdmin) # Register le modèle Product dans l'interface d'administration
admin.site.register(commande, commandeAdmin) # Register le modèle commande dans l'interface d'administration
