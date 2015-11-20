from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
 
from puppies import Base, Shelter, Puppy

import datetime


engine = create_engine('sqlite:///puppyshelter.db')

Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)

session = DBSession()

# 1. Query all of the puppies and return the results in ascending alphabetical order
all_puppies = session.query(Puppy).order_by(Puppy.name).all()
print "The puppies are:\n"
for puppy in all_puppies:
	print puppy.name

# 2. Query all of the puppies that are less than 6 months old organized by the youngest first	
young_puppies = session.query(Puppy).filter(Puppy.dateOfBirth > (datetime.datetime.now() - datetime.timedelta(days=180))).order_by(desc(Puppy.dateOfBirth))
print "\nYoungest puppies are:\n"
for puppy in young_puppies:
	print(puppy.name, puppy.dateOfBirth)

# 3. Query all puppies by ascending weight	
all_puppies = session.query(Puppy).order_by(Puppy.weight).all()
print "\nPuppies by weight are:\n"
for puppy in all_puppies:
	print (puppy.name, puppy.weight)

# 4. Query all puppies grouped by the shelter in which they are staying
all_puppies = session.query(Puppy).group_by(Puppy.shelter_id).all()
print "\nPuppies by shelter are:\n"
for puppy in all_puppies:
	print (puppy.name, puppy.shelter_id)