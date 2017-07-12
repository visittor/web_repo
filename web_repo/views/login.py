from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    remember,
    forget,
    )
from pyramid.view import (
    forbidden_view_config,
    view_config,
)

from ..models.User import member

@view_config(route_name='login', renderer='../templates/login/login.pt')
def login(request):
    next_url = request.params.get('next', request.route_url('admin_home'))
    if not next_url:
        next_url = request.route_url('admin_home')
    message = ''
    user_name = ''
    if 'login_submitted' in request.params:
        user_name = request.params['user_name']
        password = request.params['password']
        user_name =  [i for i in user_name.split(' ') if i != '']
        user = request.dbsession.query(member).filter_by(first_name=user_name[0]).filter_by(last_name=user_name[1]).first()
        if user is not None and user.check_password(password):
            headers = remember(request, user.id)
            print "\nsuccess\n"
            return HTTPFound(location=next_url, headers=headers)
        print "\nFail\n"
        message = 'Failed login'

    return dict(
        message=message,
        url=request.route_url('login'),
        next_url=next_url,
        user_name=user_name,
        )

@view_config(route_name='logout')
def logout(request):
    headers = forget(request)
    next_url = request.route_url('login')
    return HTTPFound(location=next_url, headers=headers)