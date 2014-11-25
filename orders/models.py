from django.db import models
from users.models import User
from goods.models import Goods
from django.utils import timezone

class Order(models.Model):
	orderID = models.IntegerField(primary_key=True)
	username = models.ForeignKey(User)
	date = models.DateTimeField(default=timezone.now())


class OrderItems(models.Model):
	id_goods = models.ForeignKey(Goods)
	orderID = models.ForeignKey(Order)
	price = models.IntegerField()
	name = models.CharField(max_length=255)


