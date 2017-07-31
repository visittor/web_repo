from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	VARCHAR,
	Date,
	ForeignKey,
	)
from sqlalchemy.orm import relationship

from .meta import Base

class cart_history(Base):
	__tablename__ = "cart_history"
	id = Column(Integer,primary_key = True)

	owner_id = Column(Integer, ForeignKey("member.id"))
	teacher_id = Column(Integer,ForeignKey("member.id"))

	# owner = relationship("member", back_populates = "history_cart", foreign_keys='[cart_history.owner_id]')
	# teacher = relationship("member", back_populates = "history_responsible_cart", foreign_keys='[cart_history.teacher_id]')

	# items = relationship("item_history_pointer",back_populates = "cart_history")

	admin_approve = Column(Integer)
	teacher_approve = Column(Integer)
	start_date = Column(Date)
	stop_date = Column(Date)
	actual_stop_date = Column(Date)
	student_note = Column(VARCHAR(150))
	admin2student = Column(VARCHAR(150))
	admin2teacher = Column(VARCHAR(150))
	teacher2student = Column(VARCHAR(150))
	teacher2admin = Column(VARCHAR(150))

	@property
	def data_(self):
		dic = self.__dict__.copy()
		dic['start_date'] = str(self.start_date)
		dic['stop_date'] = str(self.stop_date)

		dic.pop('_sa_instance_state')

		return dic

	@property
	def dict_(self):
		dic = self.__dict__.copy()
		dic['start_date'] = str(self.start_date)
		dic['stop_date'] = str(self.stop_date)
		dic["owner"] = self.owner.data_ if self.owner is not None else {}
		dic["teacher"] = self.teacher.data_ if self.teacher is not None else {}
		dic["items"] = []
		for i in self.items:
			try:
				dic["items"].append(i.item.data_)
			except Exception as e:
				print "\nin cart_historry.dict_ : ", e,"\n"

		dic.pop('_sa_instance_state')

		return dic

class item_history_pointer(Base):
	__tablename__ = "item_history_pointer"
	id = Column(Integer, primary_key = True)

	item_id = Column(Integer,ForeignKey("item.id"))
	# item = relationship("item",back_populates = "order")

	cart_history_id = Column(Integer,ForeignKey("cart_history.id"))
	# cart_history = relationship("cart_history",back_populates = "items")