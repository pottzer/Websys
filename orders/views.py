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
			order_list.append({'orderID': order.id, 'date': order.date})
		print 'Finished list: ', order_list

		return render(request, self.template_name, {'order_list': order_qeury})

class ListUserOrderItems(GenericView):
	template_name = 'orders/listUserOrderItems.html'

	def dispatch(self, request, *args, **kwargs):
		if request.user.order_set.filter(id=kwargs['orderID']).count() > 0:
			return super(ListUserOrderItems, self).dispatch(request, *args, **kwargs)
		return HttpResponseRedirect('/')

	def get(self, request, *args, **kwargs):
		order = get_object_or_404(Order, id=kwargs['orderID'])
		sum = 0
		for item in order.orderitems_set.all():
			sum = sum + (item.price*item.quantity)
		return render(request, self.template_name, {'order':order, 'sum': sum})
