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
	first_name = Column(VARCHAR(15))
	last_name = Column(VARCHAR(15))
	email = Column(VARCHAR(15))

class teacher(Base):
	__tablename__ = "teacher"
	id = Column(Integer,primary_key = True)

	responsible_cart = relationship("cart",back_populates = "teacher")

	first_name = Column(VARCHAR(15))
	last_name = Column(VARCHAR(15))
	email = Column(VARCHAR(15))