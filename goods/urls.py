from django.conf.urls import url
from goods.views import AddProductView, ListProductView, ProductView, EditProductView, DeleteProductView


urlpatterns = [
	url(r'^addproduct/$', AddProductView.as_view(), name = 'AddProductView'),
	url(r'^products/$', ListProductView.as_view(), name = 'ListProductView'),
	url(r'^products/(?P<productid>.*)/$', ProductView.as_view(), name = 'ProductView'),
	url(r'^editproducts/(?P<productid>.*)/$', EditProductView.as_view(), name = 'EditProductView'),
	url(r'^deleteproduct/(?P<productid>.*)/$', DeleteProductView.as_view(), name = 'DeleteProductView'),
]
