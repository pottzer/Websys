from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.views.generic import DetailView, TemplateView


from orders.models import Order, OrderItems
from goods.models import Goods
from users.models import User
from shopping.models import ShoppingCart, Inventory
# Create your views here.

class Shoppingcart(View):
	model = ShoppingCart
	template_name = 'shopping/shoppingcart.html'

	def dispatch(self, request, *args, **kwargs):
		#Checks if you are logged in.
		if request.user.is_authenticated() and kwargs['userid'] == str(request.user.id):
			u = User.objects.get(username=request.user)
			#Checks if you got a shoppingcart if not it creates one
			try:
				u.shoppingcart
			except:
				S = ShoppingCart(username=u)
				S.save()
			return super(Shoppingcart, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')


	def get(self, request, *args, **kwargs):
		#Prints out all the products from the users inventory list
		u = request.user
		s = ShoppingCart.objects.get(username=u)
		products = s.inventory_set.filter(shopping_cartID = s.id )
		print(products)
		sum = 0
		
		for item in products:	
			sum = sum + item.productID.price*item.quantity
		
		return render(request, self.template_name, {'inventory':products, 'sum': sum})

class AddProductShoppingcart(View):
	
	def dispatch(self, request, *args, **kwargs):
	
		if request.user == 'AnonymousUser':
			return HttpResponseRedirect('/')
		return super(AddProductShoppingcart, self).dispatch(request, *args, **kwargs)

	def get(self, request, *args, **kwargs):
		productID = kwargs['productid'] 
		p = Goods.objects.get(id_good=productID)
		try: 
			s = ShoppingCart.objects.get(username=request.user.id)
		except:
			s = ShoppingCart(username=request.user)
			s.save()
			
		i = s.inventory_set.filter(productID = p.id_good)
		if len(i) == 0 and p.expired==False:
			s.inventory_set.create(productID = p, shopping_cartID = s, quantity = '1')
		elif p.expired==False:
			i[0].quantity += 1
			i[0].save()		
		return HttpResponseRedirect(reverse('goods:ListProductView'))	 

class RemoveProductShoppingcart(View):

 	def get(self, request, *args, **kwargs):
		productID = kwargs['productid']
		product = Goods.objects.get(id_good=productID)
		shoppingcart = ShoppingCart.objects.get(username=request.user.id)
		inventory = shoppingcart.inventory_set.filter(productID = product.id_good)
	
		if (inventory[0].quantity) == 1:
			inventory[0].delete()

		elif (inventory[0].quantity) > 1:
			productQuantity = inventory[0].quantity
			inventory.delete()
			shoppingcart.inventory_set.create(productID = product, shopping_cartID = shoppingcart, quantity = productQuantity-1)

		return HttpResponseRedirect(reverse('shopping:Shoppingcart', args=(request.user.id,)))

class CheckOutView(View):
	error_template ='shopping/checkOutError.html' 
 
	def get(self, request, *args, **kwargs):
		O = Order(username = request.user) #Creating the Order.
	
		shoppingcart = ShoppingCart.objects.get(username = request.user.id)
		inventoryList = Inventory.objects.filter(shopping_cartID = shoppingcart.id)
		lengthInventory = len(inventoryList)
		
		if lengthInventory == 0:
			return render(request, self.error_template,)
				
		O.save()
		for i in xrange(lengthInventory):
			item = inventoryList[i]
			product = item.productID
			productPrice = product.price
			productName = product.name
			ShoppingQuantity = inventoryList[i].quantity
			
			good = Goods.objects.get(id_good = product.id_good)
			if (good.stock - ShoppingQuantity) >= 0:
				good.stock = (good.stock - ShoppingQuantity)
			else:
				O.delete()
				return render(request, self.error_template,{'product': product})	
			good.save()
			OI = OrderItems(productID = product, orderID = O, price = productPrice, name = productName, quantity = ShoppingQuantity)		
			OI.save()		
		
		for i in xrange(lengthInventory):
			inventoryList[i].delete()
		
		return HttpResponseRedirect(reverse('shopping:Shoppingcart', args=(request.user.id,)))	
		
		 
			 
	
	
	
	

	

