from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from generic.views import GenericView
from orders.models import Order
from users.models import User

class ListUserOrders(GenericView):
	template_name = 'orders/listUserOrders.html'

	def dispatch(self, request, *args, **kwargs):
		if str(request.user) == kwargs['username']:
			return super(ListUserOrders, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
		u = get_object_or_404(User, username=kwargs['username'])
		order_qeury = u.order_set.all()
		order_list = []
		for order in order_qeury:
			order_list.append({'orderID': order.orderID, 'date': order.date})
		print 'Finished list: ', order_list

		return render(request, self.template_name, {'order_list': order_qeury})

class ListUserOrderItems(GenericView):
	template_name = 'orders/listUserOrderItems.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.order_set.filter(orderID=kwargs['orderID']).count() > 0:
			return super(ListUserOrderItems, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
		order = get_object_or_404(Order, orderID=kwargs['orderID'])
		return render(request, self.template_name, {'order':order})
