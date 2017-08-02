from pyramid.httpexceptions import (
    HTTPNotFound,
    HTTPFound,
)
from pyramid.security import (
    Allow,
    Everyone,
)

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('admin_home', '/admin', factory = admin_page_factory)
    config.add_route('user_home', '/user', factory = user_page_foctory)
    config.add_route('teacher_home', '/teacher_home', factory = teacher_page_foctory)
    config.add_route('user_check_item', '/user_check_item', factory = user_page_foctory)

    config.add_route('search_item_json', '/search_item.json')

    config.add_route('test_admin_borrow_json', '/test_admin_borrow.json')
    config.add_route('test_admin_return_json', '/test_admin_return.json')

    config.add_route('admin_borrow_json', '/admin_borrow.json', factory = admin_page_factory)
    config.add_route('admin_edit_borrow_json', '/admin_edit_borrow.json', factory = admin_page_factory)
    config.add_route('admin_delete_borrow_json', '/admin_delete_borrow.json', factory = admin_page_factory)

    config.add_route('admin_return_json', '/admin_return.json', factory = admin_page_factory)
    config.add_route('admin_edit_return_json', '/admin_edit_return.json', factory = admin_page_factory)

    config.add_route('admin_main_category_json','/admin_main_category.json', factory = admin_page_factory)
    config.add_route('admin_edit_main_category_json', '/admin_edit_main_category.json', factory = admin_page_factory)
    config.add_route('admin_delete_main_category_json', '/admin_delete_main_category.json', factory = admin_page_factory)
    config.add_route('admin_insert_main_category_json', '/admin_insert_main_category.json', factory = admin_page_factory)

    config.add_route('admin_sub_category_json', '/admin_sub_category.json', factory = admin_page_factory)
    config.add_route('admin_edit_sub_category_json', '/admin_edit_sub_category.json', factory = admin_page_factory)
    config.add_route('admin_delete_sub_Category_json', '/admin_delete_sub_Category.json', factory = admin_page_factory)
    config.add_route('admin_insert_sub_category_json', '/admin_insert_sub_category.json', factory = admin_page_factory)

    config.add_route('admin_type_json', '/admin_type.json', factory = admin_page_factory)
    config.add_route('admin_edit_type_json', '/admin_edit_type.json', factory = admin_page_factory)
    config.add_route('admin_delete_type_json', '/admin_delete_type.json', factory = admin_page_factory)
    config.add_route('admin_insert_type_json', '/admin_insert_type.json', factory = admin_page_factory)

    config.add_route('admin_storage_json', '/admin_storage.json', factory = admin_page_factory)
    config.add_route('admin_edit_storage_json', '/admin_edit_storage.json', factory = admin_page_factory)
    config.add_route('admin_delete_storage_json', '/admin_delete_storage.json', factory = admin_page_factory)
    config.add_route('admin_insert_storage_json', '/admin_insert_storage.json', factory = admin_page_factory)

    config.add_route('admin_device_json', '/admin_device.json', factory = admin_page_factory)
    config.add_route('admin_delete_device_json', '/admin_delete_device.json', factory = admin_page_factory)
    config.add_route('admin_add_device_json', '/admin_add_device.json', factory = admin_page_factory)

    config.add_route('order_item_json', '/order_item.json', factory = user_page_foctory)
    config.add_route('delete_order_json', '/delete_order.json', factory = user_page_foctory)
    config.add_route('view_order_detail_json', '/view_order_detail.json', factory = user_page_foctory)
    config.add_route('confirm_order_json', '/confirm_order.json', factory = user_page_foctory)

    config.add_route('user_all_cart_json', '/user_all_cart.json', factory = user_page_foctory)
    config.add_route('user_all_cart', '/user_all_cart', factory = user_page_foctory)

    config.add_route('teacher_all_cart', '/teacher_all_cart', factory = teacher_page_foctory)
    config.add_route('teacher_all_cart_json', '/teacher_all_cart.json', factory = teacher_page_foctory)

    config.add_route('login', '/login')
    config.add_route('logout', '/logout')


def admin_page_factory(request):
    return admin_page_resource()

class admin_page_resource(object):

    def __init__(self):
        pass

    def __acl__(self):
        return [(Allow, 'role:a', 'access')]

def user_page_foctory(request):
    return user_page_resource()

class user_page_resource(object):

    def __init__(self):
        pass

    def __acl__(self):
        return [(Allow, 'role:s', 'access'),
                (Allow, 'role:t', 'access'),]

def teacher_page_foctory(request):
    return user_page_resource()

class teacher_page_resource(object):

    def __init__(self):
        pass

    def __acl__(self):
        return [(Allow, 'role:t', 'access'),]

