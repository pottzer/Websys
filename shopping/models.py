from django.db import models

from users.models import User
from goods.models import Goods

class ShoppingCart(models.Model):
	username = models.OneToOneField(User)


class Inventory(models.Model):
	shopping_cartID = models.ForeignKey(ShoppingCart)
	productID = models.ForeignKey(Goods)
	quantity = models.IntegerField(default=1)

