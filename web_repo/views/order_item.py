from pyramid.view import (
    view_config,
    view_defaults
    )

from ..models.Item import order_item, item 
import datetime

@view_defaults(renderer='json')
class order_item_view(object):

	def __init__(self, request):
		self.request = request

	def create_order(self, item_id):
		try:
			item_ self.request.dbsession.query(item).filter_by(id = item_id).one()
			if item_.cart_id is None and self.request.dbsession.query(order_item).filter_by(user_id = self.request.user.id, item_id = item_id).one_or_none() is None:
				order = order_item()
				order.item_id = item_id
				order.user_id = self.request.user.id
				self.request.dbsession.add(order)
				return 0
			else:
				print "\nthis item is already in other cart or this user already order this item. \n"
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
		return items

	def search_item(self, kwargh):
		for i,j in kwargh.items():
			if type(j) == unicode and j == '':
				kwargh.pop(i)
			elif type(j) == int and j == -1:
				kwargh.pop(i)
		q = self.request.dbsession.query(item).filter_by(**kwargh)
		return q.all()

	@view_config(route_name = 'order_item_json', request_method='POST')
	def user_order_item(self):
		json = self.request.POST
		item_id = json["id"]
		return {"exception" : self.create_order(item_id)}

	@view_config(route_name = 'search_item_json', request_method = 'GET')
	def user_search_item(self):
		json = self.request.GET
		main_category_json = json["main_category"]
		sub_category_json = json["sub_category"]

		category_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'main_category').one()
		sub_category = eval(category_obj.list_)

		items = self.search_item({'sub_category' : sub_category_json})

		items_list = []
		for i in items:
			dict_ = i.dict_
			dict_["code_name"] = str(type_list.get(i.type_, 'NULL'))+str(i.id)
			items_list.append(dict_)

		return {"items" : items_list, "sub_category" : sub_category}

	@view_config(route_name = 'delete_order_json', request_method = 'POST')
	def user_delete_order(self):
		json = self.request.POST
		item_id = json["id"]
		return {"exception" : self.delete_order(item_id)}

	@view_config(route_name = 'view_order_detail_json', request_method = 'GET')
	def user_view_order_detail(self):
		items = self.get_all_ordered_item()
		return {"owner_id" : self.request.user.id,
				"owner" : self.request.user.dict_,
				"item" : items}

	# @view_config(route_name = 'confirm_order_json', request_method = 'POST')
	# def user_confirm_order(self):
	# 	json = self.request.POST
	# 	teacher_name = json["teacher_name"]
	# 	start_date = json["start_date"]
	# 	stop_date = json["stop_date"]
	# 	datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S.%f")
		


