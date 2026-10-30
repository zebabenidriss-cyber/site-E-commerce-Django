import json

from django.shortcuts import render
from .models import Product , commande
from django.core.paginator import Paginator    
# Create your views here.

def index(request): # cette fonction est appelée lorsque l'utilisateur accède à la page d'accueil de l'application Store. Elle prend en paramètre un objet request qui contient les informations sur la requête HTTP effectuée par l'utilisateur.
    Product_object = Product.objects.all() # récupère tous les objets de la classe products à partir de la base de données. Cela permet d'afficher tous les produits disponibles dans l'application Store.
    item_name = request.GET.get('item-name') # récupère la valeur du paramètre 'item_name' de la requête GET effectuée par l'utilisateur. Cela permet de filtrer les produits en fonction du nom de l'article recherché par l'utilisateur.
    if item_name !='' and item_name is not None: # vérifie si la variable item_name contient une valeur. Si c
        Product_object = Product.objects.filter(title__icontains=item_name) # filtre les objets Product en fonction du nom de l'article recherché par l'utilisateur.
    paginator = Paginator(Product_object, 4) # crée un objet Paginator qui divise les objets Product en pages de 4 articles chacun. Cela permet d'afficher les produits sur plusieurs pages si nécessaire.
    page = request.GET.get('page') # récupère la valeur du paramètre 'page' de la requête GET effectuée par l'utilisateur. Cela permet de déterminer quelle page de produits afficher.
    Product_object = paginator.get_page(page) # récupère les objets Product correspondant à la page demandée par l'utilisateur. Cela permet d'afficher les produits de la page demandée.
    return render(request, 'Store/index.html', {'Product_object': Product_object}) # utilise la fonction render pour générer une réponse HTTP en utilisant le template 'store/index.html' et en passant les objets Product récupérés à ce template. Cela permet d'afficher les produits sur la page d'accueil de l'application Store.)

def detail(request, myid): # cette fonction est appelée lorsque l'utilisateur accède à la page de détail d'un produit spécifique. Elle prend en paramètre un objet request et l'identifiant du produit. 
    product_object = Product.objects.get(id=myid) # récupère l'objet Product correspondant à l'identifiant fourni. Cela permet d'afficher les détails du produit spécifique.
    return render(request,'Store/detail.html', {'product': product_object}) # utilise la fonction render pour générer une réponse HTTP en utilisant le template 'store/detail.html' et en passant l'objet Product récupéré à ce template. Cela permet d'afficher les détails du produit sur la page de détail de l'application Store.

def checkout(request): # cette fonction est appelée lorsque l'utilisateur accède à la page de paiement. Elle prend en paramètre un objet request.
    products = list(Product.objects.values('id', 'title', 'price'))
    if request.method == 'POST':
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        adresse = request.POST.get('adresse')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zip_code = request.POST.get('zip_code')
        submitted_items = json.loads(request.POST.get('items', '{}'))
        product_ids = [int(product_id) for product_id in submitted_items]
        products_by_id = Product.objects.in_bulk(product_ids)
        order_items = []
        for product_id, quantity in submitted_items.items():
            product_id = int(product_id)
            quantity = int(quantity)
            if product_id in products_by_id and quantity > 0:
                order_items.append({
                    'id': product_id,
                    'name': products_by_id[product_id].title,
                    'quantity': quantity,
                })
        items = json.dumps(order_items, ensure_ascii=False)
        com = commande(items=items, nom=nom, email=email, adresse=adresse, ville=ville, pays=pays, zip_code=zip_code)
        com.save()  # enregistre la commande dans la base de données.
        # Vous pouvez maintenant utiliser ces informations pour traiter le paiement ou enregistrer la commande.
    return render(request, 'Store/checkout.html', {'products': products}) ; # utilise la fonction render pour générer une réponse HTTP en utilisant le template 'store/checkout.html'. Cela permet d'afficher les produits du panier.
