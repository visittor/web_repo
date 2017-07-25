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

import bcrypt

class member(Base):
	__tablename__ = "member"
	id = Column(Integer,primary_key = True)

	cart = relationship("cart",cascade="save-update",back_populates = "owner", foreign_keys='[cart.owner_id]')

	responsible_cart = relationship("cart",back_populates = "teacher", foreign_keys='[cart.teacher_id]')

	orders = relationship("order_item",cascade="save-update,delete",back_populates = "owner")

	student_id = Column(Integer)
	role = Column(VARCHAR(5))
	first_name = Column(VARCHAR(30))
	last_name = Column(VARCHAR(30))
	email = Column(VARCHAR(30))

	password_hash = Column(Text)

	def set_password(self, pw):
		pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
		self.password_hash = pwhash.decode('utf8')

	def check_password(self, pw):
		if self.password_hash is not None:
			expected_hash = self.password_hash.encode('utf8')
			return bcrypt.checkpw(pw.encode('utf8'), expected_hash)
		return False

	@property
	def data_(self):
		dic = self.__dict__.copy()

		dic.pop('_sa_instance_state')

		print "\n", dic,"\n"
		return dic

	@property
	def dict_(self):
		dic = self.__dict__.copy()
		dic["cart"] = []
		for i in self.cart:
			dic["cart"].append(i.data_)
		dic["responsible_cart"] = []
		for i in self.responsible_cart:
			dic["responsible_cart"].append(i.data_)
		dic["orders"] = []
		for i in self.orders:
			dic["orders"].append(i.data_)

		dic.pop('_sa_instance_state')

		return dic




# class teacher(Base):
# 	__tablename__ = "teacher"
# 	id = Column(Integer,primary_key = True)

# 	responsible_cart = relationship("cart",back_populates = "teacher")

# 	role = Column(VARCHAR(5))
# 	first_name = Column(VARCHAR(15))
# 	last_name = Column(VARCHAR(15))
# 	email = Column(VARCHAR(15))

# 	@property
# 	def data_(self):
# 		dic = self.__dict__

# 		dic.pop('_sa_instance_state')

# 		return dic

# 	@property
# 	def dict_(self):
# 		dic = self.__dict__
# 		dic["responsible_cart"] = []
# 		for i in self.responsible_cart:
# 			dic["responsible_cart"].append(i.data_)

# 		dic.pop('_sa_instance_state')

# 		return dic