from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Programmer" table
class Programmer(base):
    ''' This class holds all the fields of info for programmer objects '''
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (to db)
Session = sessionmaker(db)


# opens an actual session by calling the session() sublclass defined above
session = Session()


# create the database using declarative_base sublckass
base.metadata.create_all(db)


# creating records on our programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name= "Lovelace",
    gender= "F",
    nationality= "British",
    famous_for= "First Programmer"
)


# creating records on our programmer table
alan_turing = Programmer(
    first_name="Alan",
    last_name= "Turing",
    gender= "M",
    nationality= "British",
    famous_for= "Modern Computing"
)


# creating records on our programmer table
grace_hopper = Programmer(
    first_name="Grace",
    last_name= "Hopper",
    gender= "F",
    nationality= "American",
    famous_for= "COBOL language"
)


# creating records on our programmer table
margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name= "Hamilton",
    gender= "F",
    nationality= "American",
    famous_for= "Apollo 11"
)


# creating records on our programmer table
bill_gates = Programmer(
    first_name="Bill",
    last_name= "Gates",
    gender= "M",
    nationality= "American",
    famous_for= "Microsoft"
)


# creating records on our programmer table
tim_berners_lee = Programmer(
    first_name="Tim",
    last_name= "Berners-Lee",
    gender= "M",
    nationality= "British",
    famous_for= "World Wide Web"
)


# creating records on our programmer table
grant_wilsmore = Programmer(
    first_name="Grant",
    last_name= "Wilsmore",
    gender= "M",
    nationality= "British",
    famous_for= "Nothing"
)

# add each instance of our programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(grant_wilsmore)


# commit our session to the database
# session.commit()


# updating a single record
# programmer = session.query(Programmer).filter_by(id=10).first()
# programmer.famous_for = "Airsoft"


# commit our session to the database
# session.commit()


# update multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()


# Deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()
# Defensive programming
# if programmer is not None:
#     print("Programmer Found: " + programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("Programmer not found")


# Deleting multiple records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

## ------------------------------------------------------------------------------------------------------------------------


# query the database to find all programmers
# programmers = session.query(Programmer)
# for Programmer in programmers:
#     print(
#         Programmer.id,
#         Programmer.first_name + " " + Programmer.last_name,
#         Programmer.gender,
#         Programmer.nationality,
#         Programmer.famous_for,
#         sep= " | "
    )

# updating a single record
# enterID = int(input("enter a key: "))
# programmer = session.query(Programmer).filter_by(id=enterID).first()
# print(str(programmer.id) + " | " + programmer.first_name + " " + programmer.last_name)
# newId = input(" what number do you want to update the ID to? ")
# programmer.id = newId
# # commit our session to the database
# session.commit()

## -------------------------------------------------------------------------------------------------------------------------

# Updating the primary key
# pkey = input("what key do you want to change")
# programmer = session.query(Programmer).filter_by(pkey).first()
# # Defensive programming
# if programmer is not None:
#     print("Programmer Found: " + programmer.id + " | " + programmer.first_name + " " + programmer.last_name,)
#     confirmation = input("Are you sure you want to change the ID for this record? (y/n) ")
#     if confirmation.lower() == "y":
#         programmer.id = input("select new ID Number: ")
#         session.commit()
#         print("Programmer ID has been updated")
#     else:
#         print("Programmer ID has not been deleted")
# else:
#     print("Programmer not found")

## --------------------------------------------------------------------------------------------------------------------------


# query the database to find all programmers
programmers = session.query(Programmer)
for Programmer in programmers:
    print(
        Programmer.id,
        Programmer.first_name + " " + Programmer.last_name,
        Programmer.gender,
        Programmer.nationality,
        Programmer.famous_for,
        sep= " | "
    )

