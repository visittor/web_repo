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
	cart_history = relationship("item_history_pointer", back_populates = "item")

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
		dic = self.__dict__.copy()

		dic.pop('_sa_instance_state')

		return  dic

	@property
	def dict_(self):
		dic = self.__dict__.copy()
		print "\n",dic,"\n"
		dic["in_cart"] =self.in_cart.data_ if self.in_cart is not None else {}
		dic["order"] = []
		for i in self.order:
			dic["order"].append(i.data_)
		dic.pop('_sa_instance_state')

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
		dic = self.__dict__.copy()

		dic.pop('_sa_instance_state')

		return dic

	@property
	def dict_(self):
		dic = self.__dict__.copy()
		dic["item"] = self.item.data_
		dic["owner"] = self.owner.data_

		dic.pop('_sa_instance_state')

		return dic
