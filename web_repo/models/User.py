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

class member(Base):
	__tablename__ = "member"
	id = Column(Integer,primary_key = True)

	cart = relationship("cart",cascade="save-update",back_populates = "owner")

	orders = relationship("order_item",cascade="save-update,delete",back_populates = "owner")

	student_id = Column(Integer)
	first_name = Column(VARCHAR(30))
	last_name = Column(VARCHAR(30))
	email = Column(VARCHAR(30))

	@property
	def data_(self):
		dic = self.__dict__
		dic.pop("cart")
		dic.pop("orders")
		return dic

	@property
	def dict_(self):
		dic = self.__dict__
		for i in range(0, len(dic["cart"])):
			dic["cart"][i] = dic["cart"][i].data_

		for i in range(0, len(dic["orders"])):
			dic["orders"][i] = dic["orders"][i].data_

		return dic




class teacher(Base):
	__tablename__ = "teacher"
	id = Column(Integer,primary_key = True)

	responsible_cart = relationship("cart",back_populates = "teacher")

	first_name = Column(VARCHAR(15))
	last_name = Column(VARCHAR(15))
	email = Column(VARCHAR(15))

	@property
	def data_(self):
		dic = self.__dict__
		dic.pop("responsible_cart")
		return dic

	@property
	def dict_(self):
		dic = self.__dict__
		for i in range(0,len(dic["responsible_cart"])):
			dic["responsible_cart"][i] = dic["responsible_cart"][i].data_
		return dic