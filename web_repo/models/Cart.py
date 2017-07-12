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

class cart(Base):
	__tablename__ = "cart"
	id = Column(Integer,primary_key = True)

	owner_id = Column(Integer, ForeignKey("member.id"))
	teacher_id = Column(Integer,ForeignKey("member.id"))

	owner = relationship("member", foreign_keys='[cart.owner_id]')
	teacher = relationship("member", foreign_keys='[cart.teacher_id]')

	items = relationship("item",back_populates = "in_cart")

	admin_approve = Column(Integer)
	teacher_approve = Column(Integer)
	start_date = Column(Date)
	stop_date = Column(Date)
	student_note = Column(VARCHAR(150))
	admin2student = Column(VARCHAR(150))
	admin2teacher = Column(VARCHAR(150))
	teacher2student = Column(VARCHAR(150))
	teacher2admin = Column(VARCHAR(150))

	@property
	def data_(self):
		dic = self.__dict__
		dic['start_date'] = str(self.start_date)
		dic['stop_date'] = str(self.stop_date)

		dic.pop('_sa_instance_state')

		return dic

	@property
	def dict_(self):
		dic = self.__dict__
		dic['start_date'] = str(self.start_date)
		dic['stop_date'] = str(self.stop_date)
		dic["owner"] = self.owner.data_
		dic["teacher"] = self.teacher.data_
		dic["items"] = []
		for i in self.items:
			dic["items"].append(i.data_)

		dic.pop('_sa_instance_state')

		return dic

