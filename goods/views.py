from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.views.generic import DetailView, TemplateView
from goods.forms import GoodForm, EditProductForm
from goods.models import Goods

class AddProductView(View):
	template_name = 'goods/addProduct.html'
	form_class = GoodForm
	
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name,{'form': self.form_class})
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()		
			return HttpResponseRedirect('/')
		print("Failed")
		return render(request, self.template_name,{'form': self.form_class})

class ListProductView(TemplateView):
	template_name = 'goods/listProducts.html'
	model = Goods
	
	def get_context_data(self, **kwargs):
		context = super(ListProductView, self).get_context_data(**kwargs)
		context['products']=Goods.objects.all()

		return context

class ProductView(TemplateView):
	template_name = 'goods/product.html'
	model = Goods

	def get(self, request, productid):
		product = Goods.objects.get(id_good = productid)
		print productid
		return render(request, self.template_name, {'product':product})

class EditProductView(TemplateView):
	template_name = 'goods/editProduct.html'
	model = Goods

	def get(self, request, *args, **kwargs):
		product = get_object_or_404(self.model, id_good = kwargs['productid'])
		form = EditProductForm(None, instance = product)
		return render(request, self.template_name, {'form':form})

	def post(self, request, *args, **kwargs):
		product = get_object_or_404(self.model, id_good = kwargs['productid'])
		form = EditProductForm(request.POST, instance = product)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('goods:ListProductView'))
		return render(request, self.template_name, {'form':form})
			
class DeleteProductView(TemplateView):
	template_name = 'goods/deleteProduct.html'
	model = Goods
	
	def get(self, request, *args, **kwargs):
		product = get_object_or_404(self.model, id_good = kwargs['productid'])
		product.delete()
		return HttpResponseRedirect(reverse('goods:ListProductView'))		
