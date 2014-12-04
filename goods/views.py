from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.views.generic import DetailView, TemplateView
from django.utils import timezone

from shopping.models import Inventory
from goods.forms import GoodForm, EditProductForm, PostComment
from goods.models import Goods, Comment
from users.models import User

class AddProductView(View):
	template_name = 'goods/addProduct.html'
	form_class = GoodForm

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated() and request.user.admin:
			return super(AddProductView, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')


	def get(self, request, *args, **kwargs):
		products = Goods.objects.all()
		return render(request, self.template_name,{'form': self.form_class, 'products': products})
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			#return HttpResponseRedirect('/')
			return self.get(request, *args, **kwargs)
		print("Failed")
		return render(request, self.template_name,{'form': self.form_class})

class ListProductView(View):
	template_name = 'goods/listProducts.html'
	model = Goods

	def get(self, request, *args, **kwargs):
		productList = Goods.objects.filter(expired=False)
	#	context['products']=Goods.objects.all()
		return render(request, self.template_name, {'products':productList})

class ProductView(TemplateView):
	template_name = 'goods/product.html'
	model = Goods
	form = PostComment

	def get(self, request, productid):
		product = Goods.objects.get(id_good = productid)
		comment_list = product.comment_set.values('name', 'comment_text', 'date', 'id').order_by("-date")
		for i in xrange(len(comment_list)):
			try:
				comment_list[i]['role'] = "Admin" if User.objects.get(username=comment_list[i]['name']).admin else "Costumer"
			except:
				comment_list[i]['role'] = "Account deleted"
		return render(request, self.template_name, {'product':product, 'PostCommentForm': self.form, 'comment_list': comment_list})

	def post(self, request, *args, **kwargs):
		instance = Goods.objects.get(id_good=kwargs['productid'])
		form = self.form(request.POST)
		if form.is_valid():
			print form
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
		if request.user.is_authenticated() and request.user.admin:
			return super(EditProductView, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')


	def get(self, request, *args, **kwargs):
		product = get_object_or_404(self.model, id_good = kwargs['productid'])
		form = EditProductForm(None, instance = product)
		return render(request, self.template_name, {'form':form})

	def post(self, request, *args, **kwargs):
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

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated() and request.user.admin:
			return super(DeleteProductView, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
		product = get_object_or_404(self.model, id_good = kwargs['productid'])
		product.delete()
		return HttpResponseRedirect(reverse('goods:AddProductView'))

class DeleteProductComment(TemplateView):


	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated() and request.user.admin:
			return super(DeleteProductComment, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
		c = Comment.objects.get(id=kwargs['commentid'])
		print kwargs
		productID = c.productID.id_good
		c.delete()
		return HttpResponseRedirect(reverse('goods:ProductView', args=(productID,)))
