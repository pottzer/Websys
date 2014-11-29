from django.conf.urls import patterns, include, url
from django.contrib import admin

from users.views import index

urlpatterns = patterns('',
    # Users URL
    url(r'^$', index, name='index'),
	url(r'^system/', include('users.urls', namespace='users')),
	# Goods URL
	url(r'^goods/', include('goods.urls', namespace='goods')),
	#Shopping URL
	url(r'^shopping/', include('shopping.urls', namespace='shopping')),
	# Orders URL
	url(r'^history/', include('orders.urls', namespace='orders')),
	# Admin URL
    url(r'^admin/', include(admin.site.urls)),
)
