from django.db import models
from django.utils import timezone

class Goods(models.Model):
	id_good = models.CharField(max_length=32, primary_key=True, unique=True)
	name = models.CharField(max_length=64, unique=True)
	price = models.IntegerField(max_length=32)
	image = models.ImageField(blank=True, null=True)
	stock = models.IntegerField(default=0, max_length=32)
	description = models.CharField(max_length=1000)
	expired = models.BooleanField(default=False)

class Comment(models.Model):
	productID = models.ForeignKey(Goods)
	name = models.CharField(max_length=30, default='nameless')
	comment_text = models.CharField(max_length=1024)
	date = models.DateTimeField(default=timezone.now())
