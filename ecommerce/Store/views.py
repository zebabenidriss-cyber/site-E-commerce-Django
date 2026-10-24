from django.shortcuts import render
from .models import Product
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
    return render(request, 'Store/checkout.html') ; # utilise la fonction render pour générer une réponse HTTP en utilisant le template 'store/checkout.html'. Cela permet d'afficher la page de paiement de l'application Store.