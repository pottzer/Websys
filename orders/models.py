from django.db import models
from users.models import User
from goods.models import Goods
from django.utils import timezone

class Order(models.Model):
	id = models.AutoField(primary_key=True, default=None)
	username = models.ForeignKey(User)
	date = models.DateTimeField(default=timezone.now())


class OrderItems(models.Model):
	productID = models.ForeignKey(Goods)
	orderID = models.ForeignKey(Order)
	price = models.IntegerField()
	name = models.CharField(max_length=255)
	quantity = models.IntegerField(default=1)
