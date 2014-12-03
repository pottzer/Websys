from django.conf.urls import url
from shopping import views

urlpatterns = [
	url(r'^shoppingcart/(?P<userid>.*)/$', views.Shoppingcart.as_view(), name='Shoppingcart'),
	url(r'^add/(?P<productid>.*)/$', views.AddProductShoppingcart.as_view(), name='AddProductShoppingcart'),
	url(r'^remove/(?P<productid>.*)/$', views.RemoveProductShoppingcart.as_view(), name='RemoveProductShoppingcart'),
	url(r'^checkout/$', views.CheckOutView.as_view(), name='CheckOutView'),

]

