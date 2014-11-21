from django.views.generic import TemplateView
from users.models import User
from django.http import HttpResponseRedirect

class GenericView(TemplateView):
	def get(self, request, *args, **kwargs):
		try:
			if not request.user.is_authenticated():
				print 'inerror'
				raise NameError
			return super(GenericView, self).get(request, args, kwargs)
		except NameError:
			print 'in except'
			return HttpResponseRedirect('/')
