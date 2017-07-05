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
	owner = relationship("member", back_populates = "cart")

	teacher_id = Column(Integer,ForeignKey("teacher.id"))
	teacher = relationship("teacher",back_populates = "responsible_cart")

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
		dic['start_date'] = str(start_date)
		dic['stop_date'] = str(stop_date)
		dic.pop('owner')
		dic.pop('teacher')
		dic.pop('items')
		return dic

	@property
	def dict_(self):
		dic = self.__dict__
		dic["owner"] = owner.data_
		dic["teacher"] = teacher.data_
		for i in range(0, len(dic["items"])):
			dic["items"][i] = dic["items"][i].data_
		return dic

