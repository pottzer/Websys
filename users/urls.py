from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from users import views


urlpatterns = [
		#url(r'^$', views.log, name='log'),
		url(r'^$', views.log, name='log'),
		url(r'^logout/', views.logout, name='logout'),
		url(r'^create/', views.createUser, name='createUser'),
		url(r'^admin/edituser/$', views.AdminEditUser, name='editUser'),
		#url(r'^editUser/del/$', views.delUser, name='delUser'),
		url(r'^admin/editUser/del/(?P<username>.*)/$', views.delUser, name='delUser'),
		#url(r'^user/(?P<username>.*)/$', views.user, name='user'),
		url(r'^user/(?P<username>.*)/$', views.EditUser.as_view(), name='user'),
		]
