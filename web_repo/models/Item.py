from sqlalchemy import (
	Column,
	Index,
	Integer,
	Text,
	VARCHAR,
	Date,
	ForeignKey,
	String,
	)
from sqlalchemy.orm import relationship

from .meta import Base

class item(Base):
	__tablename__ = "item"
	id = Column(Integer,primary_key = True)

	cart_id = Column(Integer,ForeignKey("cart.id"))
	in_cart = relationship("cart",back_populates = "items")

	order = relationship("order_item",cascade = "delete",back_populates = "item")

	name = Column(VARCHAR(15))
	main_category = Column(VARCHAR(15))
	sub_category = Column(VARCHAR(15))
	type_ = Column(VARCHAR(10))
	storage = Column(VARCHAR(50))#where item can found
	value = Column(Integer)
	subject_name = Column(VARCHAR(50))
	note = Column(VARCHAR(150))

	@property
	def data_(self):
		dic = self.__dict__
		dic.pop("in_cart")
		dic.pop("order")

	@property
	def dict_(self):
		dic = self.__dict__
		dic["in_cart"] = in_cart.data_
		for i in range(0, len(dic["order"])):
			dic["order"][i] = dic["order"][i].data_

		return dic

class order_item(Base):
	__tablename__ = "order_temp"
	id = Column(Integer,primary_key = True)

	item_id = Column(Integer,ForeignKey("item.id"))
	item = relationship("item",back_populates = "order")

	user_id = Column(Integer,ForeignKey("member.id"))
	owner = relationship("member",back_populates = "orders")

	extra_data =  Column(String(50))

	@property
	def data_(self):
		dic = self.__dict__
		dic.pop("item")
		dic.pop("owner")
		return dic

	@property
	def dict_(self):
		dic = self.__dict__
		dic["item"] = item.data_
		dic["owner"] = owner.data_
		return dic
