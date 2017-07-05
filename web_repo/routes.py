def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('admin_home', '/admin')

    config.add_route('test_admin_borrow_json', '/test_admin_borrow.json')
    config.add_route('test_admin_return_json', '/test_admin_return.json')

    config.add_route('admin_borrow_json', '/admin_borrow.json')
    config.add_route('admin_edit_borrow_json', '/admin_edit_borrow.json')
    config.add_route('admin_delete_borrow_json', '/admin_delete_borrow.json')

    config.add_route('admin_return_json', '/admin_return.json')
    config.add_route('admin_edit_return_json', '/admin_edit_return.json')

    config.add_route('admin_main_category_json','/admin_main_category.json')
    config.add_route('admin_edit_main_category_json', '/admin_edit_main_category.json')
    config.add_route('admin_delete_main_category_json', '/admin_delete_main_category.json')
    config.add_route('admin_insert_main_category_json', '/admin_insert_main_category.json')

    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    