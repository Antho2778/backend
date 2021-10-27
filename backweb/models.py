from django.db import models


class Prestation(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()

    def _str_(self):
        return self.title

class Realisation(models.Model):
    title = models.CharField(max_length=120)
    lieu = models.CharField(max_length=120)
    date = models.DateField()
    photo_before = models.CharField(max_length=300)
    photo_after = models.CharField(max_length=300)
    description = models.TextField()
# imageField image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    def _str_(self):
        return self.title
    

class Review(models.Model):
    last_name = models.CharField(max_length=120)
    date = models.DateField()
    description = models.TextField()
    rating = models.IntegerField()
    
    def _str_(self):
        return self.last_name
# Create your models here.
