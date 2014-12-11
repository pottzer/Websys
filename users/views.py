from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from django.contrib import auth
from generic.views import GenericView
from users.backend import Backend
from users.forms import LoginForm, CreateUserForm, AdminEditUserForm
from users.models import User
from shopping.models import ShoppingCart, Inventory

def index(request):
	print index
	form = LoginForm()
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = Backend().authenticate(username=username, password=password)
			print "User was: ", user
			if user is not None:
				user.backend='users.backend.Backend'
				user.save()
				auth.login(request, user)
				return HttpResponseRedirect('/')
				#return render(request, 'users/mainPage.html')
				#mainPage(request)
			else:
				auth_fail = True
				return render(request, 'users/index.html', {'form': form, 'auth_fail': auth_fail})
	auth_fail = False
	return render(request, 'users/index.html', {'form': form, 'auth_fail': auth_fail})



#'
def log(request):
	print "User is authencated: ",request.user.is_authenticated()
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/')
	return render(request, 'users/mainPage.html')

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')


def createUser(request):
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/')
	else:
		form = CreateUserForm()
	return render(request, 'users/createUser.html', {'form': form})


#def AdminEditUser(request):
#	if request.method == 'POST':
#		print "Delete ", request.POST.get("", "Remove")
#	user_query = User.objects.values('username', 'firstname', 'lastname').distinct()
#	#for user in user_query:
#	#	context.append(user['username'])
#	return render(request, 'users/listUser.html', {'userlist': user_query})

def delUser(request, username):
	#user = User.objects.get(username=username)
	user = get_object_or_404(User, username=username)
	user.delete()
	return HttpResponseRedirect(reverse('users:editUser'))

#def user(request, username):
#	instance = get_object_or_404(User, username=username)
#	form = CreateUserForm(request.POST or None, instance=instance)
#	if form.is_valid():
#		form.save()
#		return HttpResponseRedirect('/system/')
#	return render(request, 'users/profile.html', {'form': form})

class AdminEditUser(GenericView):
	template_name = 'users/profile.html'
	form = AdminEditUserForm

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated() and request.user.admin:
			return super(AdminEditUser, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
		instance = get_object_or_404(User, username=kwargs['username'])
		S = ShoppingCart.objects.get(username = instance.id)
		I = Inventory.objects.filter(shopping_cartID = S.id)
		print(I)	
		form = self.form(None, instance=instance)
		return render(request, self.template_name, {'form': form, 'Inventory': I, 'customer':instance,})

	def post(self, request, *args, **kwargs):
		instance = get_object_or_404(User, username=kwargs['username'])
		form = self.form(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('users:editUser'))
		return render(request, self.template_name, {'form': form})

class AdminListUser(GenericView):
	template_name = 'users/listUser.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated() and request.user.admin:
			return super(AdminListUser, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
		user_query = User.objects.values('username', 'firstname', 'lastname', 'admin').distinct()
		return render(request, self.template_name, {'userlist': user_query})

class EditUser(GenericView):
	model = User
	template_name = 'users/profile.html'

	def dispatch(self, request, *args, **kwargs):
		if kwargs['username'] == str(request.user):
			return super(EditUser, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
		super(EditUser, self).get(request, *args, **kwargs)
		instance = get_object_or_404(User, username=kwargs['username'])
		form = CreateUserForm(None, instance=instance)
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		instance = get_object_or_404(User, username=kwargs['username'])
		form = CreateUserForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/system/')
		return render(request, self.template_name, {'form': form})
