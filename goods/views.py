from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.views.generic import DetailView, TemplateView
from django.utils import timezone

from shopping.models import Inventory
from goods.forms import GoodForm, EditProductForm, PostComment, PostReview
from goods.models import Goods, Comment, Review
from users.models import User

class AddProductView(View):
	#The view to add a product in the shop system
	template_name = 'goods/addProduct.html'
	form_class = GoodForm

	def dispatch(self, request, *args, **kwargs):
		#A check that makes sure you are logged in and has the role as admin  
		if request.user.is_authenticated() and request.user.admin:
			return super(AddProductView, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')


	def get(self, request, *args, **kwargs):
		#Sends the form for the model Goods
		products = Goods.objects.all()
		return render(request, self.template_name,{'form': self.form_class, 'products': products})
	def post(self, request, *args, **kwargs):
		#Checks that the values in the form is valid and then saves it.
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return self.get(request, *args, **kwargs)
		return render(request, self.template_name,{'form': self.form_class})

class ListProductView(View):
	template_name = 'goods/listProducts.html'
	model = Goods

	def get(self, request, *args, **kwargs):
		#Sends all the values in the table goods_goods to list all the products
		productList = Goods.objects.filter(expired=False)
		return render(request, self.template_name, {'products':productList})

class ProductView(TemplateView):
	template_name = 'goods/product.html'
	model = Goods
	form = [PostComment, PostReview]

	def get(self, request, productid):
		#Sends the product information
		product = Goods.objects.get(id_good = productid)
		
		#Sends all the comments of the product
		comment_list = product.comment_set.values('name', 'comment_text', 'date', 'id').order_by("-date")
		for i in xrange(len(comment_list)):
			try:
				comment_list[i]['role'] = "Admin" if User.objects.get(username=comment_list[i]['name']).admin else "Costumer"
			except:
				comment_list[i]['role'] = "Account deleted"

		#Calculate Rating
		r = Review.objects.filter(productID=product)
		print r
		nRating = r.count()
		if not nRating == 0:
			sRating = 0
			for review in r:
				sRating += int(review.rating)
			print "number of rating", nRating
			print "all rating sum ", sRating
			average = float(sRating)/float(nRating)
			average = "{0:.2f}".format(average)
		else:
			average = "Has no rating"
		#Get if already rated
		showReview = not product.review_set.filter(userID=request.user).exists()
		print showReview
		return render(request, self.template_name, {'product':product, 'PostReviewForm': self.form[1], 'PostCommentForm': self.form[0], 'comment_list': comment_list, 'showReview': showReview, 'average': average})

	def post(self, request, *args, **kwargs):
		if "postRating" in request.POST:
			instance = Goods.objects.get(id_good=kwargs['productid'])
			form = self.form[1](request.POST)
			print "Violating integrity constraint: ", instance.review_set.filter(userID=request.user).exists()
			if form.is_valid() and not instance.review_set.filter(userID=request.user).exists():
				c = form.save(commit=False)
				c.productID = instance
				c.userID = request.user
				c.save()
		else:
			#The function for adding a comment for the specifick product
			instance = Goods.objects.get(id_good=kwargs['productid'])
			form = self.form[0](request.POST)
			if form.is_valid():
				c = form.save(commit=False)
				c.productID = instance
				c.date = timezone.now()
				c.name = request.user.username
				c.save()
		return HttpResponseRedirect(reverse('goods:ProductView', args=(kwargs['productid'],)))

class EditProductView(TemplateView):
	template_name = 'goods/editProduct.html'
	model = Goods

	def dispatch(self, request, *args, **kwargs):
		#Makes the check that the user is logged in and is an admin
		if request.user.is_authenticated() and request.user.admin:
			return super(EditProductView, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')


	def get(self, request, *args, **kwargs):
		#Get's the values, for the product that is getting edited and the form
		product = get_object_or_404(self.model, id_good = kwargs['productid'])
		form = EditProductForm(None, instance = product)
		return render(request, self.template_name, {'form':form})

	def post(self, request, *args, **kwargs):
		#Sends the new values for the product in the database
		product = get_object_or_404(self.model, id_good = kwargs['productid'])
		form = EditProductForm(request.POST, instance = product)
		if form.is_valid():
			form.save()
			Inventory.objects.filter(productID__expired=True).delete()
			return HttpResponseRedirect(reverse('goods:AddProductView'))
		return render(request, self.template_name, {'form':form})

class DeleteProductView(TemplateView):
	template_name = 'goods/deleteProduct.html'
	model = Goods
	#The class to remove the product

	def dispatch(self, request, *args, **kwargs):
	#Checks so you are logged in and the user is an admin
		if request.user.is_authenticated() and request.user.admin:
			return super(DeleteProductView, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
	#Get's the product and then deletes it from the database
		product = get_object_or_404(self.model, id_good = kwargs['productid'])
		product.delete()
		return HttpResponseRedirect(reverse('goods:AddProductView'))

class DeleteProductComment(TemplateView):


	def dispatch(self, request, *args, **kwargs):
	#Checks so you are logged in and are an admin user
		if request.user.is_authenticated() and request.user.admin:
			return super(DeleteProductComment, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
	#Removes the comment with a specifik commentid
		c = Comment.objects.get(id=kwargs['commentid'])
		productID = c.productID.id_good
		c.delete()
		return HttpResponseRedirect(reverse('goods:ProductView', args=(productID,)))
