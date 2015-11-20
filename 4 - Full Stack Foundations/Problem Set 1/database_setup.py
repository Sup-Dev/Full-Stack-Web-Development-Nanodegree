import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Shelter(Base):

	__tablename__ = 'shelter'

	name = Column(String(80), nullable = False)
	address = Column(String(250))
	city = Column(String(80))
	state = Column(String(80))
	zipcode = Column(String(10))
	website = Column(String(250))
	id = Column(Integer, primary_key = True)


class Puppy(Base):
	
	__tablename__ = 'puppy'

	name = Column(String(80), nullable = False)
	date_of_brith = Column(Date)
	gender = Column(String(10))
	weight = Column(Float(2))
	shelter_id = Column(Integer, ForeignKey('shelter.id'))
	shelter = relationship(Shelter)


########insert at the end of file #########

engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)