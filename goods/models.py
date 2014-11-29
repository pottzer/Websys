from django.db import models

# Create your models here.

class Goods(models.Model):
	id_good = models.CharField(max_length=32, primary_key=True, unique=True)
	name = models.CharField(max_length=64, unique=True)
	price = models.IntegerField(max_length=32)
	image = models.ImageField(upload_to="pictures", blank=True, null=True)
	stock = models.IntegerField(default=0, max_length=32)
	description = models.CharField(max_length=1000)
	expired = models.BooleanField(default=False)
	#expired = models.BooleanField(default=False)

