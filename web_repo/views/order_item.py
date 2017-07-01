from pyramid.view import (
    view_config,
    view_defaults
    )

from ..models.Item import order_item
import transaction

class order_item_view(object):

	def __init__(self, request):
		self.request = request

	def create_order(self, item_id, user_id):
		with transaction.manager:
			session = self.request.dbsession
			order = order_item()
			order.item_id = item_id
			order.user_id = self.request.user.id
	


