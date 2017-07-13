# -*- coding: utf-8 -*-
from pyramid.view import (
    view_config,
    view_defaults
    )
from ..models.Item import item
from ..models.Cart import cart
from ..models.type import category_type_storage
# from ..models.type import category_list, type_list, storage_list
import transaction

try:
	from ConfigParser import ConfigParser
except ImportError:
	from configParser import ConfigParser #ver. > 3


@view_defaults(renderer='../templates/fluke/temp.pt', permission = 'access')
class admin_home(object):
	def __init__(self, request):
		self.request = request

	@view_config(route_name = 'admin_home')
	def admin_home(self):
		return {'a' : 'hello'}


@view_defaults(renderer='json', permission = 'access')
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
		cart_ = self.request.dbsession.query(cart).filter_by(id = id).one()
		return cart_

	def get_cart_data(self, id):
		if type(id) == str :
			id = int(id)
		cart_ = self.get_cart(id)
		dic = cart_.dict_
		print "\n", cart_.items, "\n"
		items = self.request.dbsession.query(item).filter_by(cart_id = id).all()
		for i in items:
			dic["items"].append(i.data_)
		print "\n", dic, "\n"
		return dic

	def delete_cart(self, id):
		if type(id) == str:
			id = int(id)
		try:
			cart_ = self.request.dbsession.query(cart).filter_by(id = id).one()
			# request.dbsession.delete(cart_)
			cart_.admin_approve = -1
			return 0
		except Exception as e:
			print "\n",e,"\n"
			return 1

	def search_item(self, kwargh):
		for i,j in kwargh.items():
			if type(j) == unicode and j == '':
				kwargh.pop(i)
			elif type(j) == int and j == -1:
				kwargh.pop(i)
		q = self.request.dbsession.query(item).filter_by(**kwargh)
		return q.all()

	def delete_item(self, item_id):
		try:
			item_ = self.request.dbsession.query(item).filter_by(id = item_id).one()
			self.request.dbsession.delete(item_)
			return 0
		except Exception as e:
			print "\n",e,"\n"
			return 1

	def create_item(self, **kwargh):
		try:
			item_ = item(kwargh)
			self.request.dbsession.add(item_)
		except Exception as e:
			print "\n", e,"\n"

	@view_config(route_name='test_admin_borrow_json')
	def test_admin_borrow(self):
		print '+++++++++++\n\n'
		json = self.request.GET
		print json
		cart_ = {'id': 1,
				'owner_id': 2,
				'owner': {'id': 3,
						'student_id': 4,
						'first_name': 'dummy_fist_name',
						'last_name': 'dummy_last_name',
						'email': 'dummy@dummy.com',},
				'teacher_id': 5,
				'teacher':{'id': 5,
						'first_name': 'dummy_teacher',
						'last_name': 'teacher_dummy',
						'email':  'dummy@dummy.com',},
				'item': [ { 'id': 6,
						'name': 'dummy',
						'main_category':'DM',
						'sub_category': 'dm',
						'type_': 'd_m',
						'storage': 'dm301',
						'value': 1,
						'subject_name': 'dmm301',
						'note': 'it a dummy',}],
				'admin_approve': 0,
				'teacher_approve': 1,
				'start_date': '2017-07-05',
				'stop_date': '2030-07-05',
				'student_note': '',
				'admin2student': '',
				'admin2teacher': '',
				'teacher2student': '',
				'teacher2admin': '',}

		return cart_

	@view_config(route_name = 'test_admin_return_json')
	def test_admin_return(self):
		json = self.request.GET
		print json
		list_cart = [ {'id': 1,
				'owner_id': 2,
				'owner': {'first_name': 'dummy_fist_name',
						'last_name': 'dummy_last_name',},
				'teacher_id': 5,
				'teacher':{'first_name': 'dummy_teacher',
						'last_name': 'teacher_dummy',},
				'admin_approve': 0,
				'teacher_approve': 1,
				'start_date': '2017-07-05',
				'stop_date': '2030-07-05',
				'student_note': '',
				'admin2student': '',
				'admin2teacher': '',
				'teacher2student': '',
				'teacher2admin': '',},
				{'id': 1,
				'owner_id': 2,
				'owner': {'first_name': 'dummy_fist_name',
						'last_name': 'dummy_last_name',},
				'teacher_id': 5,
				'teacher':{'first_name': 'dummy_teacher',
						'last_name': 'teacher_dummy',},
				'admin_approve': 0,
				'teacher_approve': 1,
				'start_date': '2017-07-05',
				'stop_date': '2030-07-05',
				'student_note': '',
				'admin2student': '',
				'admin2teacher': '',
				'teacher2student': '',
				'teacher2admin': '',}, ]

		return list_cart

	@view_config(route_name = 'admin_borrow_json')
	def admin_borrow(self):
		cart_list = self.borrow_list
		for i in range (0, len(cart_list) ):
			cart_list[i] = cart_list[i].dict_
		return cart_list

	@view_config(route_name = 'admin_edit_borrow_json', request_method='GET')
	def admin_edit_borrow_get(self):
		json = self.request.GET
		cart_id = json["id"]
		dic = self.get_cart_data(cart_id)
		return dic

	@view_config(route_name = 'admin_edit_borrow_json', request_method='POST')
	def admin_edit_borrow_post(self):
		json = self.request.POST
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

	@view_config(route_name  = 'admin_delete_borrow_json', request_method = 'POST')
	def admin_delete_borrow(self):
		json = self.request.POST
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
		json = self.request.GET
		cart_id = json["id"]
		print '\nadmin edit return\n'
		dic = self.get_cart_data(cart_id)
		return dic

	@view_config(route_name = 'admin_edit_return_json', request_method = 'POST')
	def admin_edit_return_post(self):
		json = self.request.POST
		cart_id = json['id']
		note = json['note']
		to_student = json['to_student']
		to_advisor = json['to_advisor']
		try:
			cart_ = self.get_cart(cart_id)
			cart_.admin2student = to_student
			cart_.admin2teacher = to_advisor
			cart_.student_note =  note
			cart_.admin_approve = 2
			return {'exception' : 0}
		except Exception as e:
			return {'exception' : 1}

	@view_config(route_name = 'admin_device_json', request_method = 'GET')
	def admin_device_list(self):
		json = self.request.GET
		type_json = json.get("type_", ''.decode('utf8'))
		sub_category_json = json.get("sub_category", ''.decode('utf8'))
		storage_json = json.get("storage", ''.decode('utf8'))

		category_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'main_category').one()
		sub_category = eval(category_obj.list_)

		type_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'type_list').one()
		type_list = eval(type_obj.list_)

		storage_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'storage_list').one()
		storage_list = eval(storage_obj.list_)

		items = self.search_item({'type_' : type_json, 'sub_category' : sub_category_json, 'storage' : storage_json})
		items_list = []
		for i in items:
			dict_ = i.dict_
			dict_["code_name"] = str(type_list.get(i.type_, 'NULL'))+str(i.id)
			items_list.append(dict_)

		return {"items" : items_list, "type_list" :type_list, "sub_category" : sub_category, "storage" : storage_list}

	@view_config(route_name = 'admin_delete_device_json', request_method = 'POST')
	def admin_delete_device(self):
		json = self.request.POST
		device_id = json["id"]
		return {'exception' : self.delete_item(device_id)}

	@view_config(route_name = 'admin_add_device_json', request_method = 'GET')
	def admin_device_list(self):
		category_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'main_category').one()
		sub_category = eval(category_obj.list_)

		type_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'type_list').one()
		type_list = eval(type_obj.list_)

		storage_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'storage_list').one()
		storage_list = eval(storage_obj.list_)

		return {"type_list" :type_list, "sub_category" : sub_category, "storage" : storage_list}

	@view_config(route_name = 'admin_add_device_json', request_method = 'POST')
	def admin_add_device(self):
		json = self.request.POST
		name = json["name"]
		main_category = json["main_category"]
		sub_category = json["sub_category"]
		type_ = json["type_"]
		storage = json["storage"]
		note = json["note"]

		category_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'main_category').one()
		sub_category_list = eval(category_obj.list_)

		type_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'type_list').one()
		type_list = eval(type_obj.list_)

		storage_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'storage_list').one()
		storage_list = eval(storage_obj.list_)

		if type_list.has_key(type_):
			if sub_category_list.has_key(main_category):
				if sub_category in sub_category_list[main_category]:
					if storage in storage_list:
						kwargh = {"main_category" : main_category, "sub_category" : sub_category, "type_" : type_, "storage" : storage, "note" : note}
						return {"exception" : self.create_item(**kwargh)}
					else:
						print "\nno storage in database\n"
						return {"exception" : 1}
				else:
					print "\nno sub_category in database\n"
					return {"exception" : 1}
			else:
				print "\nno main_Category in database\n"
				return {"exception" : 1}
		else:
			print "\nno type in database\n"
			return {"exception" : 1}
	

	

@view_defaults( renderer = 'json', permission = 'access')
class category_type_manager(object):

	def __init__(self, request):
		self.request = request
		# self.__file_path = self.request.static_url('web_repo:static/category.ini')
		# self.__file_path = 'web_repo:static/category/category.ini'
		# self.__file_path = "category.ini"

	def __save_config_file(self, section, option, value):
		# with open(self.__file_path) as f:
		# 	cfg = ConfigParser()
		# 	cfg.readfp(f)
		# 	cfg.set(section, option, value)
		# 	cfg.write(f)
		category_obj = self.request.dbsession.query(category_type_storage).filter_by(name = option).one()
		category_obj.list_ = str(value)


	def change_mainCat_name(self, old_name, new_name):
		category_list = self.category_list
		try:
			if category_list.has_key(old_name):
				category_list[new_name] = category_list.pop(old_name)
				self.__save_config_file('category', 'main_category', category_list)
				return 0
			print '\n*****************************\n','not has key','\n******************************\n'
			return 1
		except Exception as e:
			print '\n*****************************\n',e,'\n******************************\n'
			return 1

	def delete_mainCat(self, name):
		category_list = self.category_list
		try:
			if category_list.has_key(name):
				category_list.pop(name)
				self.__save_config_file('category', 'main_category', category_list)
				return 0
			return 1
		except Exception as e:
			print e
			return 1

	def insert_mainCat(self, name):
		category_list = self.category_list
		try:
			if category_list.has_key(name):
				return 1
			else:
				category_list[name] = []
				self.__save_config_file('category', 'main_category', category_list)
				return 0
		except Exception as e:
			print e 
			return 1

	def change_subCat(self, main_category, old_name, new_name):
		category_list = self.category_list
		try:
			if category_list.has_key(main_category) and old_name in category_list[main_category]:
				category_list[main_category].remove(old_name)
				category_list[main_category].append(new_name)
				self.__save_config_file('category', 'main_category', category_list)
				print "\n", "return 0", "\n"
				return 0
			else:
				print "\n", "not has key or not have old name","\n"
				return 1
		except Exception as e:
			print "\n",e,"\n"
			return 1

	def delete_subCat(self, main_category, sub_category):
		category_list = self.category_list
		try:
			if category_list.has_key(main_category) and sub_category in category_list[main_category]:
				category_list[main_category].remove(sub_category)
				self.__save_config_file('category', 'main_category', category_list)
				return 0
			else:
				return 1
		except Exception as e:
			print e 
			return 1

	def insert_subCat(self, main_category, sub_category):
		category_list = self.category_list
		try:	
			if category_list.has_key(main_category):
				if sub_category in category_list[main_category]:
					return 1
				else:
					category_list[main_category].append(sub_category)
					self.__save_config_file('category', 'main_category', category_list)
					return 0
			else:
				return 1
		except Exception as e:
			print e 
			return 1

	def change_type(self, old_name, new_name, code):
		type_ = self.type_
		try:
			if type_.has_key(old_name):
				type_.pop(old_name)
				type_[new_name] = code
				self.__save_config_file('category', 'type_list', type_)
				return 0
			else:
				type_[new_name] = code
				self.__save_config_file('category', 'type_list', type_)
				return 0
		except Exception as e:
			print "\n",e,"\n"
			return 1

	def delete_type(self, name):
		type_ = self.type_
		try:
			if type_.has_key(name):
				type_[name].pop()
				self.__save_config_file('category', 'type_list', type_)
				return 0
			else:
				return 1
		except Exception as e:
			print e 
			return 1

	def insert_type(self, name, code):
		type_ = self.type_
		try:
			if type_.has_key(name):
				return 1
			else:
				type_[name] = code
				self.__save_config_file('category', 'type_list', type_)
				return 0
		except Exception as e:
			print e 
			return 1

	def change_storage(self, old_name, new_name):
		if not self.delete_storage(old_name) and not self.insert_storage(new_name):
			return 0
		else: 
			return 1

	def delete_storage(self, name):
		storage = self.storage
		try:
			if name in storage:
				storage.remove(name)
				self.__save_config_file('category', 'storage_list', storage)
				return 0
			else:
				print "\n", "delete storage dont have key", "\n"
				return 1
		except Exception as e:
			print "\n",e,"\n"
			return 1

	def insert_storage(self, name):
		storage = self.storage
		try:
			if name in storage:
				return 0
			else:
				storage.append(name)
				self.__save_config_file('category', 'storage_list', storage)
				return 0
		except Exception as e:
			print "\n", e, "\n"
			return 1


	@property
	def category_list(self):
		# with open(self.__file_path, "r") as f:
		# 	cfg = ConfigParser()
		# 	cfg.readfp(f)
		# 	category_list = eval(cfg.get('category', 'main_category'))
		category_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'main_category').one()
		category_list = eval(category_obj.list_)
		return category_list

	@property
	def main_category(self):
		return self.category_list.keys()

	@property
	def sub_category(self):
		return self.category_list

	@property
	def type_(self):
		# with open(self.__file_path) as f:
		# 	cfg = ConfigParser()
		# 	cfg.readfp(f)
		# 	type_list = eval(cfg.get('category', 'type_list'))
		type_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'type_list').one()
		type_list = eval(type_obj.list_)
		return type_list

	@property
	def storage(self):
		# with open(self.__file_path) as f:
		# 	cfg = ConfigParser()
		# 	cfg.readfp(f)
		# 	storage_list = eval(cfg.get('category', 'storage_list'))
		storage_obj = self.request.dbsession.query(category_type_storage).filter_by(name = 'storage_list').one()
		storage_list = eval(storage_obj.list_)
		return storage_list

	@view_config(route_name = 'admin_main_category_json')
	def show_main_category(self):
		main_category = self.main_category
		return main_category

	@view_config(route_name = 'admin_edit_main_category_json', request_method = 'POST')
	def submit_edit_main_category(self):
		json = self.request.POST
		old_name = json["old_name"].encode('utf8')
		new_name = json["new_name"].encode('utf8')
		return {"exception" : self.change_mainCat_name(old_name, new_name)}

	@view_config(route_name = 'admin_delete_main_category_json', request_method = 'POST')
	def submit_delete_main_category(self):
		json = self.request.POST
		name = json["name"].encode('utf8')
		return {"exception" : self.delete_mainCat(name)}

	@view_config(route_name = 'admin_insert_main_category_json', request_method = 'POST')
	def submit_insert_main_category(self):
		json = self.request.POST
		name = json["name"].encode('utf8')
		return {"exception" : self.insert_mainCat(name)}

	@view_config(route_name = 'admin_sub_category_json')
	def show_sub_category(self):
		sub_category = self.sub_category
		return sub_category

	@view_config(route_name = 'admin_edit_sub_category_json', request_method = 'POST')
	def submit_edit_sub_category(self):
		json = self.request.POST
		print "\n", "am here", "\n"
		main_category = json["main_category"].encode('utf8')
		old_name = json["old_name"].encode('utf8')
		new_name = json["new_name"].encode('utf8')
		return {'exception' : self.change_subCat(main_category, old_name, new_name)}

	@view_config(route_name = 'admin_delete_sub_Category_json', request_method = 'POST')
	def submit_delete_sub_category(self):
		json = self.request.POST
		main_category = json["main_category"].encode('utf8')
		sub_category = json["sub_category"].encode('utf8')
		return {'exception' : self.delete_subCat(main_category, sub_category)}

	@view_config(route_name = 'admin_insert_sub_category_json', request_method = 'GET')
	def submit_insert_sub_category_get(self):
		return self.main_category

	@view_config(route_name = 'admin_insert_sub_category_json', request_method = 'POST')
	def submit_insert_sub_category_post(self):
		json = self.request.POST
		main_category = json['main_category'].encode('utf8')
		sub_category = json['sub_category'].encode('utf8')
		return {'exception' : self.insert_subCat(main_category, sub_category)}

	@view_config(route_name = 'admin_type_json', request_method = 'GET')
	def show_type(self):
		return self.type_

	@view_config(route_name = 'admin_edit_type_json', request_method = 'POST')
	def submit_edit_type(self):
		json = self.request.POST
		old_name = json['old_name'].encode('utf8')
		new_name = json['new_name'].encode('utf8')
		code = json ['code'].encode('utf8')
		return {'exception' : self.change_type(old_name, new_name, code)}

	@view_config(route_name = 'admin_delete_type_json', request_method = 'POST')
	def submit_delete_type(self):
		json = self.request.POST
		name = json['name'].encode('utf8')
		return { 'exception' : self.delete_type(name)}

	@view_config(route_name = 'admin_insert_type_json', request_method = 'POST')
	def submit_insert_type(self):
		json = self.request.POST
		name = json['name'].encode('utf8')
		code = json['code'].encode('utf8')
		return self.insert_type(name, code)

	@view_config(route_name = 'admin_storage_json', request_method = 'GET')
	def show_storage(self):
		return self.storage

	@view_config(route_name = 'admin_edit_storage_json', request_method = 'POST')
	def submit_edit_storage(self):
		json = self.request.POST
		old_name = json['old_name'].encode('utf8')
		new_name = json['new_name'].encode('utf8')
		return {'exception' : self.change_storage(old_name, new_name)}

	@view_config(route_name = 'admin_delete_storage_json', request_method = 'POST')
	def submit_delete_storage(self):
		json = self.request.POST
		name = json['name'].encode('utf8')
		return {'exception' : self.delete_storage(name)}

	@view_config(route_name = 'admin_insert_storage_json', request_method = 'POST')
	def submit_insert_storage(self):
		json = self.request.POST
		name = json['name'].encode('utf8')
		return {'exception' : self.insert_storage(name)}














