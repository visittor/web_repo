from pyramid.view import (
    view_config,
    view_defaults
    )
from ..models.Item import item
from ..models.Cart import cart
from ..models.type import category_list, type_list, storage_list
import transaction


@view_defaults(renderer='../templates/fluke/temp.pt')
class admin_home(object):
	def __init__(self, request):
		self.request = request

	@view_config(route_name = 'admin_home')
	def admin_home(self):
		return {'a' : 'hello'}


@view_defaults(renderer='json')
class admin_borrow_return(object):

	def __init__(self, request):
		self.request = request

	@property
	def borrow_list(self):
		a = []
		a = self.request.dbsession.query(cart).filter_by(admin_approve = 0).all()
		return a

	@property
	def wait_return(self):
		a = []
		a = self.request.dbsession.query(cart).filter_by(admin_approve = 1).all()
		return a

	def get_cart(self, id):
		if type(id) == str :
			id = int(id)
		cart_ = request.dbsession.query(cart).filter_by(id = id).one()
		return cart_

	def get_cart_data(self, id):
		if type(id) == str :
			id = int(id)
		cart_ = self.get_cart(id)
		dic = cart.dict_
		return dic

	def delete_cart(self, id):
		if type(id) == str:
			id = int(id)
		try:
			cart_ = request.dbsession.query(cart).filter_by(id = id).one()
			request.dbsession.delete(cart_)
			return 0
		except Exception as e:
			return 1

	@view_config(route_name='test_admin_borrow_json')
	def test_admin_borrow(self):
		print '+++++++++++\n\n'
		json = self.request.GET
		print '**********\n\n'
		print json
		print '\n\n#########\n\n'
		return [{'a' :0}, {'a':1}]

	@view_config(route_name = 'test_admin_return_json')
	def test_admin_return(self):
		json = self.request.json_body
		print json
		return {'a' : 'hello_return'}

	@view_config(route_name = 'admin_borrow_json')
	def admin_borrow(self):
		cart_list = self.borrow_list
		for i in range (0, len(cart_list) ):
			cart_list[i] = cart_list[i].dict_
		return cart_list

	@view_config(route_name = 'admin_edit_borrow_json', request_method='GET')
	def admin_edit_borrow_get(self):
		json = self.request.json_body
		cart_id = json["id"]
		return self.get_cart_data(cart_id)

	@view_config(route_name = 'admin_edit_borrow_json', request_method='POST')
	def admin_edit_borrow_post(self):
		json = self.request.json_body
		cart_id = json['id']
		note = json['note']
		to_student = json['to_student']
		to_advisor = json['to_advisor']
		try:
			cart_ = self.get_cart(cart_id)
			cart_.admin2student = to_student
			cart_.admin2teacher = to_advisor
			cart_.student_note =  note
			cart_.admin_approve  = 1
			return {'exception' : 0}
		except Exception as e:
			return {'exception' : 1}

	@view_config(route_name  = 'admin_delete_borrow_json')
	def admin_delete_borrow(self):
		json = self.request.json_body
		cart_id = json["id"]
		exception = self.delete_cart(cart_id)
		return {'exception': exception}

	@view_config(route_name = 'admin_return_json')
	def admin_return(self):
		cart_list = self.wait_return
		for i in range(0, len(cart_list) ):
			cart_list[i] = cart_list[i].dict_
		return cart_list

	@view_config(route_name = 'admin_edit_return_json', request_method = 'GET')
	def admin_edit_return_get(self):
		json = self.request.json_body
		cart_id = json["id"]
		return self.get_cart_data(id)

	@view_config(route_name = 'admin_edit_return_json', request_method = 'POST')
	def admin_edit_return_post(self):
		json - self.request.json_body
		cart_id = json['id']
		note = json['note']
		to_student = json['to_student']
		to_advisor = json['to_advisor']
		try:
			cart_ = self.get_cart(cart_id)
			cart_.admin2student = to_student
			cart_.admin2teacher = to_advisor
			cart_.student_note =  note
			return {'exception' : 0}
		except Exception as e:
			return {'exception' : 1}


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

