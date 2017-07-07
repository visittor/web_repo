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
from ..models.User import member, teacher
from ..models.Cart import cart
from ..models.Item import order_item, item

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

        student_ = member(student_id = 58340500012, first_name = 'for test', last_name = 'for test last name', email = 'test@dummy.com')
        teacher_ = teacher(first_name = 'test first teacher', last_name = 'last name', email = 'teacher@dummy.com')

        dbsession.add(student_)
        dbsession.add(teacher_)

        cart_borrow = cart(admin_approve = 0, teacher_approve = 0, start_date = datetime.datetime.now(), stop_date =datetime.datetime.now() + datetime.timedelta(days=1, hours=23), )
        cart_return = cart(admin_approve = 1, teacher_approve = 0, start_date = datetime.datetime.now(), stop_date =datetime.datetime.now() + datetime.timedelta(days=1, hours=23), )
        item_1 = item(name = 'dummy1', main_category = u'การเรียนการสอน', sub_category = 'FRA111', type_ = 'board', storage = 'FRA202', value = 1, subject_name = 'FRA111', )
        item_2 = item(name='dummy2', main_category=u'การเรียนการสอน', sub_category='FRA111', type_='board',
                     storage='FRA202', value=1, subject_name='FRA111', )

        cart_borrow.owner = student_
        cart_borrow.teacher = teacher_
        cart_borrow.items.append(item_1)

        cart_return.owner = student_
        cart_return.teacher = teacher_
        cart_return.items.append(item_2)

        dbsession.add(cart_borrow)
        dbsession.add(cart_return)

        
