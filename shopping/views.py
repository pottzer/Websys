from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.views.generic import DetailView, TemplateView

from goods.models import Goods
from users.models import User
from shopping.models import ShoppingCart, Inventory
# Create your views here.

class Shoppingcart(View):
	model = ShoppingCart
	template_name = 'shopping/shoppingcart.html'

	def dispatch(self, request, *args, **kwargs):
		print str(request.user.id)
		if kwargs['userid'] == str(request.user.id):
			u = User.objects.get(username=request.user)
			try:
				u.shoppingcart
			except:
				ShoppingCart(username=u)

			print("hej")
			return super(Shoppingcart, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
		u = request.user
		s = ShoppingCart.objects.get(username=u)
		products = s.inventory_set.filter(shopping_cartID = s.id)
		print(products)
		
		return render(request, self.template_name, {'inventory':products})

class AddProductShoppingcart(View):

	def get(self, request, *args, **kwargs):
		productID = kwargs['productid'] 
		p = Goods.objects.get(id_good=productID)
		s = ShoppingCart.objects.get(username=request.user.id)
		i = s.inventory_set.filter(productID = p.id_good)
		if len(i) == 0:
			print ("HEJ")
			s.inventory_set.create(productID = p, shopping_cartID = s, quantity = '1')
		else:
			print ("fulfan")
			q = i[0].quantity
			i.delete()
			s.inventory_set.create(productID = p, shopping_cartID =s, quantity = q+1)	
		
		return HttpResponseRedirect(reverse('goods:ListProductView'))	 

class RemoveProductShoppingcart(View):
	
	def get(self, request, *args, **kwargs):
		productID = kwargs['productid']
		product = Goods.objects.get(id_good=productID)
		shoppingcart = ShoppingCart.objects.get(username=request.user.id)
		inventory = shoppingcart.inventory_set.filter(productID = product.id_good)
		print (inventory[0].quantity)
		
		if (inventory[0].quantity) == 1:
			inventory[0].delete()
		elif (inventory[0].quantity) > 1:
			productQuantity = inventory[0].quantity
			inventory.delete()
			shoppingcart.inventory_set.create(productID = product, shopping_cartID = shoppingcart, quantity = productQuantity-1)
	
	#	return HttpResponseRedirect('/')	
		return HttpResponseRedirect(reverse('shopping:Shoppingcart', args=(request.user.id,)))
							


	
