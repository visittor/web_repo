# -*- coding: utf-8 -*-
# category_list = {"การเรียนการสอน":["FRA111"], "ค่าย":["ROBOcamp"], "การแข่งขัน":["RObot thailand"], "class project":["FRA231"]}

# type_list = {"อิเล็กทรอนิค":"EL", "ไฟฟ้า":"EE", "การช่าง":"TN", "board":"BD"}

# storage_list = ["FRA202", "FB202", "FB203", "FB204"]

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

class category_type_storage(Base):
	__tablename__ = "category_type_storage"

	id = Column(Integer,primary_key = True)
	name = Column(VARCHAR(30))
	list_ =  Column(VARCHAR(500))