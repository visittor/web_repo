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

class item(Base):
	__tablename__ = "item"
	id = Column(Integer,primary_key = True)

	cart_id = Column(Integer,ForeignKey("cart.id"))
	in_cart = relationship("cart",back_populates = "items")

	order = relationship("order_item",cascade = "delete",back_populates = "item")

	name = Column(VARCHAR(15))
	main_category = Column(VARCHAR(3))
	sub_category = Column(VARCHAR(3))
	type_ = Column(VARCHAR(10))
	storage = Column(VARCHAR(50))
	value = Column(Integer)
	subject_name = Column(VARCHAR(50))
	note = Column(VARCHAR(150))

class order_item(Base):
	__tablename__ = "order_temp"
	id = Column(Integer,primary_key = True)

	item_id = Column(Integer,ForeignKey("item.id"))
	item = relationship("item",back_populates = "order")

	user_id = Column(Integer,ForeignKey("member.id"))
	owner = relationship("member",back_populates = "orders")
