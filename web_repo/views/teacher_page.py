from pyramid.view import (
    view_config,
    view_defaults
    )

from ..models.Item import order_item, item 
from ..models.Cart import cart
from ..models.User import member
from ..models.type import category_type_storage
from ..scripts import util
import datetime



@view_defaults(renderer='json', permission = 'access')
class teacher_page(object):
	def __init__(self, request):
		self.request = request

	def approve_item(self, id):
		try:
			if type(id) == str:
				id = int(id)
			cart_ = self.request.query(cart).filter_by(id = id).one()
			if cart_.teacher_approve == 0:
				cart_.teacher_approve = 1
				return 0
			return 1
		except Exception as e:
			print "\n", e,"\n"
			return 1

	@view_config(renderer='../templates/earth/rentitem_main.pt', route_name = 'teacher_home')
	def teacher_home(self):
		return  {'a' : 'hello'}


	@view_config(renderer = '../templates/earth/rentitem_template_teacher.pt', route_name = 'teacher_all_cart')
	def teacher_all_cart(self):
		return {'a' : 'hello'}

	@view_config(route_name = 'teacher_all_cart_json')
	def sent_cart_status(self):
		cart_list = [ i.dict_ for i in self.request.dbsession.query(cart).filter_by(teacher_id = self.request.user.id, teacher_approve = 0).all()]
		return cart_list

	@view_config(route_name = 'teacher_cart_info_json', request_method = 'GET')
	def cart_info(self):
		json = self.request.GET
		id = json['id']
		dic_ = get_cart_data(id)
		return dict_

	@view_config(route_name = 'teacher_approve_item_json', request_method = 'GET')
	def teacher_approve_cart(self):
		json = self.request.GET
		id = json["id"]
		return {"exception" : self.approve_item(id)}

