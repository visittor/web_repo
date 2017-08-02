from pyramid.view import (
    view_config,
    view_defaults
    )

from ..models.Item import order_item, item 
from ..models.Cart import cart
from ..models.User import member
from ..models.type import category_type_storage
import datetime
from ..scripts.util import *

@view_config(route_name = 'search_item_json', request_method = 'GET', renderer = 'json')
def search_item_view(request):
	json = request.GET
	main_category_json = json["main_category"]
	sub_category_json = json["sub_category"]

	category_obj = request.dbsession.query(category_type_storage).filter_by(name = 'main_category').one()
	sub_category = eval(category_obj.list_)

	type_obj = request.dbsession.query(category_type_storage).filter_by(name='type_list').one()
	type_list = eval(type_obj.list_)

	items = search_item(request,{'sub_category' : sub_category_json})

	items_list = []
	for i in items:
		dict_ = i.dict_
		dict_["code_name"] = str(type_list.get(i.type_, 'NULL'))+str(i.id)
		items_list.append(dict_)

	return {"items" : items_list, "sub_category" : sub_category}