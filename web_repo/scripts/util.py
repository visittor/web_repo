from ..models.Item import item
from ..models.Cart import cart
from ..models.type import category_type_storage
from ..models.Cart_history import cart_history, item_history_pointer
import time

def create_cart_history(cart_, request):
	try:
		cart_history_ = cart_history()
		cart_history_.owner_id = cart_.owner_id
		cart_history_.teacher_id = cart_.teacher_id
		cart_history_.admin_approve = cart_.admin_approve
		cart_history_.teacher_approve = cart_.teacher_approve
		cart_history_.start_date = cart_.start_date
		cart_history_.stop_date = cart_.stop_date
		cart_history_.actual_stop_date = datetime.datetime.now()
		cart_history_.student_note = cart_.student_note
		cart_history_.admin2student = cart_.admin2student
		cart_history_.admin2teacher = cart_.admin2teacher
		cart_history_.teacher2student = cart_.teacher2student
		cart_history_.teacher2admin = cart_.teacher2admin

		request.session.add(cart_history_)

		items = cart_.items

		for i in items:
			item_history_pointer_ = item_history_pointer(item_id = i.id, cart_history_id = cart_history_.id)
			request.session.add(item_history_pointer_)
		request.session.delete(cart_)
		return 0
	except Exception as e:
		print "\n", e,"\n"
		return 1

def get_cart_data(id):
	if type(id) == str :
		id = int(id)
	cart_ = self.get_cart(id)
	dic = cart_.dict_
	# print "\n", cart_.items, "\n"
	# items = self.request.dbsession.query(item).filter_by(cart_id = id).all()
	# for i in items:
	# 	dic["items"].append(i.data_)
	return dic

def search_item(request, kwargh):
	for i,j in kwargh.items():
		if type(j) == unicode and j == '':
			kwargh.pop(i)
		elif type(j) == int and j == -1:
			kwargh.pop(i)
	q = request.dbsession.query(item).filter_by(**kwargh)
	return q.all()

