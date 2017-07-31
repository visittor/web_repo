# -*- coding: utf-8 -*-
import os
import sys
import transaction

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models import MyModel
from ..models.Cart_history import cart_history, item_history_pointer
from ..models.User import member
from ..models.Cart import cart
from ..models.Item import order_item, item
from ..models.type import category_type_storage


import datetime


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        student_ = member(student_id = 58340500012, first_name = 'for test', last_name = 'for test last name', email = 'test@dummy.com', role = 's')
        student_.set_password('student')
        # teacher_ = teacher(first_name = 'test first teacher', last_name = 'last name', email = 'teacher@dummy.com', role = 't')
        teacher_2 = member(student_id = 0000, first_name ='teacher_2', last_name = 'teacher_2_l', email = 'test@dummy.com', role = 't')
        teacher_2.set_password('teacher')
        admin_ = member(student_id = 0000, first_name = 'admin_F', last_name = 'admin_L', email = 'test_admin@dummy.com', role = 'a')
        admin_.set_password('admin')

        dbsession.add(student_)
        dbsession.add(teacher_2)
        dbsession.add(admin_)

        cart_borrow = cart(admin_approve = 0, teacher_approve = 0, start_date = datetime.datetime.now(), stop_date =datetime.datetime.now() + datetime.timedelta(days=1, hours=23), )
        cart_return = cart(admin_approve = 1, teacher_approve = 0, start_date = datetime.datetime.now(), stop_date =datetime.datetime.now() + datetime.timedelta(days=1, hours=23), )
        item_1 = item(name = 'dummy1', main_category = u'การเรียนการสอน', sub_category = 'FRA111', type_ = 'board', storage = 'FRA202', value = 1, subject_name = 'FRA111', )
        item_2 = item(name='dummy2', main_category=u'การเรียนการสอน', sub_category='FRA111', type_='board',
                     storage='FRA202', value=1, subject_name='FRA111', )

        cart_borrow.owner = student_
        cart_borrow.teacher = teacher_2
        cart_borrow.items.append(item_1)

        cart_return.owner = student_
        cart_return.teacher = teacher_2
        cart_return.items.append(item_2)

        dbsession.add(cart_borrow)
        dbsession.add(cart_return)

        main_category = category_type_storage(name = 'main_category', list_ = u'{"การเรียนการสอน":["FRA111"], "ค่าย":["ROBOcamp"], "การแข่งขัน":["RObot thailand"], "class project":["FRA231"]}')
        type_list = category_type_storage(name = 'type_list', list_ = u'{"อิเล็กทรอนิค":"EL", "ไฟฟ้า":"EE", "การช่าง":"TN", "board":"BD"}')
        storage_list = category_type_storage(name = 'storage_list', list_ = u'["FRA202", "FB202", "FB203", "FB204"]')
        
        dbsession.add(main_category)
        dbsession.add(storage_list)
        dbsession.add(type_list)


        
