from pyramid.view import (
    view_config,
    view_defaults
    )

from ..models.Item import order_item, item 
from ..models.Cart import cart
from ..models.User import member
from ..models.type import category_type_storage
from ..scripts.util import *
import datetime

@view_defaults(renderer='json', permission = 'access')
class order_item_view(object):

	def __init__(self, request):
		self.request = request

	def create_order(self, item_id):
		try:
			item_ = self.request.dbsession.query(item).filter_by(id = item_id).one()
			print "\n", item_.cart_id,"\n"
			if item_.in_cart is None and self.request.dbsession.query(order_item).filter_by(user_id = self.request.user.id, item_id = item_id).one_or_none() is None:
				order = order_item()
				order.item_id = item_id
				order.user_id = self.request.user.id
				self.request.dbsession.add(order)
				return 0
			elif item_.in_cart is not None:
				print "\nthis item is already in other cart. \n"
				return 1
			else:
				print "\nthis user already order this item. \n"
				return 1
		except Exception as e:
			print "\n", e,"\n"
			return 1

	def delete_order(self, item_id):
		try:
			order_ = self.request.dbsession.query(order_item).filter_by(item_id = item_id, user_id = self.request.user.id).all()
			for i in order_:
				self.request.dbsession.delete(i)
			return 0
		except Exception as e:
			print "\n", e, "\n"
			return 1

	def get_all_ordered_item(self):
		user_id = self.request.user.id
		all_order = self.request.dbsession.query(order_item).filter_by(user_id = user_id).all()
		items = []
		for i in all_order:
			try:
				items.append(self.request.dbsession.query(item).filter_by(id = i.item_id).one().dict_)
			except Exception as e:
				print "\n", e,"\n"
		type_obj = self.request.dbsession.query(category_type_storage).filter_by(name='type_list').one()
		type_list = eval(type_obj.list_)
		for i in items:
			i["code_name"] = str(type_list.get(i["type_"], 'NULL'))+str(i["id"])
		return items

	def get_teacher(self):
		teachers = self.request.dbsession.query(member).filter_by(role = 't').all()
		teachers_list = []
		print "\nhere\n"
		for teacher_ in teachers:
			teachers_list.append(teacher_.dict_)
		return teachers_list

	def search_item(self, kwargh):
		for i,j in kwargh.items():
			if type(j) == unicode and j == '':
				kwargh.pop(i)
			elif type(j) == int and j == -1:
				kwargh.pop(i)
		q = self.request.dbsession.query(item).filter_by(**kwargh)
		return q.all()

	def create_cart(self, teacher_id, start_date, stop_date, note):
		to_return = 0
		try:
			start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
			stop_date = datetime.datetime.strptime(stop_date, "%Y-%m-%d")
			cart_ =  cart(admin_approve = 0, teacher_approve = 0)
			cart_.owner = self.request.user
			teacher_ = self.request.dbsession.query(member).filter_by(id = teacher_id).one()
			cart_.teacher = teacher_
			cart_.student_note = note
			cart_.start_date = start_date
			cart_.stop_date = stop_date
			order_items = self.request.dbsession.query(order_item).filter_by(user_id = self.request.user.id).all()
			for order in order_items:
				item_ = self.request.dbsession.query(item).filter_by(id = order.item_id).one_or_none()
				if item_ is not None:
					cart_.items.append(item_)
					if self.delete_order_by_item_id(item_.id) == 1:
						print "\n can't delete order somehow \n"
						to_return = 1
				else: 
					print "\nno item in database\n"
					to_return = 1

			self.request.dbsession.add(cart_)
			return to_return
		except Exception as e:
			print "\n", e,"\n"
			return 1


	def delete_order_by_item_id(self, item_id):
		try:
			order_items = self.request.dbsession.query(order_item).filter_by(item_id = item_id).all()
			for order in order_items:
				self.request.dbsession.delete(order)
			return 0
		except Exception as e:
			print "\n", e," 'at class order_item.order_item_view.delete_order_by_item_id\n"
			return 1

	@view_config(route_name = 'order_item_json', request_method='POST')
	def user_order_item(self):
		json = self.request.POST
		item_id = json["id"]
		return {"exception" : self.create_order(item_id)}

	# @view_config(route_name = 'search_item_json', request_method = 'GET')
	# def user_search_item(self):
	# 	json = self.request.GET
	# 	main_category_json = json["main_category"]
	# 	sub_category_json = json["sub_category"]

	# 	category_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'main_category').one()
	# 	sub_category = eval(category_obj.list_)

	# 	type_obj = self.request.dbsession.query(category_type_storage).filter_by(name='type_list').one()
	# 	type_list = eval(type_obj.list_)

	# 	items = self.search_item({'sub_category' : sub_category_json})

	# 	items_list = []
	# 	for i in items:
	# 		dict_ = i.dict_
	# 		dict_["code_name"] = str(type_list.get(i.type_, 'NULL'))+str(i.id)
	# 		items_list.append(dict_)

	# 	return {"items" : items_list, "sub_category" : sub_category}

	@view_config(route_name = 'delete_order_json', request_method = 'POST')
	def user_delete_order(self):
		json = self.request.POST
		item_id = json["id"]
		return {"exception" : self.delete_order(item_id)}

	@view_config(route_name = 'view_order_detail_json', request_method = 'GET')
	def user_view_order_detail(self):
		items = self.get_all_ordered_item()
		teachers = self.get_teacher()
		user_list = self.request.user.dict_
		print "\nin user_view_order_detail\n"
		print "\n",teachers,"\n"
		return {"owner_id" : self.request.user.id,
				"owner" : user_list,
				"teacher" : teachers,
				"item" : items}

	@view_config(route_name = 'confirm_order_json', request_method = 'POST')
	def user_confirm_order(self):
		json = self.request.POST
		teacher_id = json["teacher_id"]
		start_date = json["start_date"]
		stop_date = json["stop_date"]
		note = json["note"]
		return {"exception" : self.create_cart(teacher_id, start_date, stop_date, note)}

@view_defaults(renderer='../templates/earth/rentitem_main.pt', permission = 'access')
class user_home(object):
	def __init__(self, request):
		self.request = request

	@view_config(route_name = 'user_home')
	def user_home(self):
		return {'a' : 'hello'}

@view_defaults(renderer = '../templates/earth/approveItem.pt', permission = 'access')
class check_order(object):
	def __init__(self, request):
		self.request = request

	@view_config(route_name = 'user_check_item')
	def check_order(self):
		print "\nsomething wrong\n"
		return  {'a' : 'hello'}

@view_defaults(renderer = 'json', permission = 'access')
class Cart_status(object):
	"""docstring for Cart_status"""
	def __init__(self, request):
		self.request = request

	@view_config(renderer = '../templates/earth/rentitem_template.pt', route_name = 'user_all_cart')
	def user_all_cart(self):
		return {'a' : 'hello'}

	@view_config(route_name = 'user_all_cart_json')
	def sent_cart_status(self):
		cart_list = [ i.dict_ for i in self.request.dbsession.query(cart).filter_by(owner_id = self.request.user.id).all()]
		return cart_list 

	@view_config(route_name = 'user_cart_info_json')
	def cart_info(self):
		json = self.request.GET
		id = json["id"]
		dic_ = get_cart_data(self.request,id)

		type_obj = self.request.dbsession.query(category_type_storage).filter_by(name='type_list').one()
		type_list = eval(type_obj.list_)
		for i in dic_["items"]:
			i["code_name"] = str(type_list.get(i["type_"].encode('utf8'), 'NULL')) + str(i["id"])
		return dic_
