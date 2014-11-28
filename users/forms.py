from django import forms

from users.models import User

class LoginForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)


class CreateUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['firstname', 'lastname', 'ssn', 'email', 'telephone', 'username', 'password']

class AdminEditUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['firstname', 'lastname', 'ssn', 'email', 'telephone', 'username', 'password', 'admin']

