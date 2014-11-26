from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from orders import views


urlpatterns = [
		#url(r'^$', views.log, name='log'),
		#url(r'^user/(?P<username>.*)/$', views.EditUser.as_view(), name='user'),
		url(r'^user/(?P<username>.*)/$', views.ListUserOrders.as_view(), name='ListUserOrders'),
		url(r'^order/(?P<orderID>[0-9]+)/$', views.ListUserOrderItems.as_view(), name='ListUserOrderItems'),
		]
