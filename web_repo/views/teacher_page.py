from pyramid.view import (
    view_config,
    view_defaults
    )

from ..models.Item import order_item, item 
from ..models.Cart import cart
from ..models.User import member
from ..models.type import category_type_storage
import datetime


@view_defaults(renderer='json', permission = 'access')
class teacher_page(object):
	def __init__(self, request):
		self.request = request

	@view_config(renderer='../templates/earth/rentitem_main.pt', route_name = 'teacher_home')
	def teacher_home(self):
		return  {'a' : 'hello'}


	@view_config(renderer = '../templates/earth/rentitem_template.pt', route_name = 'teacher_all_cart')
	def teacher_all_cart(self):
		return {'a' : 'hello'}

	@view_config(route_name = 'teacher_all_cart_json')
	def sent_cart_status(self):
		cart_list = [ i.dict_ for i in self.request.dbsession.query(cart).filter_by(teacher_id = self.request.user.id, teacher_approve = 0).all()]
		return cart_list