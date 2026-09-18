from django.db import models

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
