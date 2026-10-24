from django.db import models

#info : 
#Tu modifies models.py.
#tu executes les commandes suivantes pour créer les tables dans la base de données :
#python manage.py makemigrations (tu peux préciser l’app : makemigrations nom_app).
#python manage.py migrate.

#creation des lodels ici 
class category(models.Model):
    nom = models.CharField(max_length=200)
    date_ajout = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_ajout']
    def __str__(self):
        return self.nom

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(category,related_name='categories', on_delete=models.CASCADE)
    image = models.CharField(max_length=5000)
    date_ajout = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
            return self.title

class commande(models.Model):
    items = models.CharField(max_length=300)
    nom = models.CharField(max_length=200)
    email = models.EmailField()
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=20)
    date_ajout = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_ajout']

    def __str__(self):
        return self.nom
