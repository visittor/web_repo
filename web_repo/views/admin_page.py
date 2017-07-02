from pyramid.view import (
    view_config,
    view_defaults
    )
from ..models.Item import item
from ..models.Cart import cart
from ..models.type import category_list, type_list, storage_list
import transaction


class borrow_return(object):

	arg_for_cart = 

	def __init__(self, request):
		self.request = request

	@property
	def borrow_list(self):
		a = []
		a = self.request.dbsession.query(item).filter_by(admin_approve = 0).all()
		return a

	@property
	def wait_return(self):
		a = []
		a = self.request.dbsession.query(item).filter_by(admin_approve = 1).all()
		return a


class category_type_manager(object):

	def __init__(self, request):
		self.request = request

	@property
	def main_category(self):
		return category_list.keys()

	@property
	def sub_category(self):
		return category_list

	@property
	def type_(self):
		return type_list

	@property
	def storage(self):
		return storage_list