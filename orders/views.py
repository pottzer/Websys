from django.shortcuts import render, get_object_or_404

from generic.views import GenericView
from orders.models import Order
from users.models import User

class ListUserOrders(GenericView):
	template_name = 'orders/listUserOrders.html'

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

	def get(self, request, *args, **kwargs):
		order = get_object_or_404(Order, orderID=kwargs['orderID'])
		return render(request, self.template_name, {'order':order})
