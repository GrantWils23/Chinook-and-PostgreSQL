from sqlalchemy import (
    create_engine, Column, Integer, String,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create a class-based model for the "Gun" table
class Gun(base):
    ''' the model for gun object '''
    __tablename__ = "Gun"
    id = Column(Integer, primary_key=True)
    gun_name = Column(String)
    gun_type = Column(String)
    manufacturer = Column(String)
    variations = Column(String)
    ammunition = Column(String)
    production_year = Column(Integer)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (to db)
Session = sessionmaker(db)


# opens an actual session by calling the session() sublclass defined above
session = Session()


# create the database using declarative_base sublckass
base.metadata.create_all(db)

# create records on our guns table
m4 = Gun(
    gun_name = "M4",
    gun_type = "Assult Rifle",
    manufacturer = "Colt",
    variations = "carabine, rifle"
)




# query the database to find all programmers
guns = session.query(Gun)
for gun in guns:
    print(
        gun.id,
        gun.gun_name,
        gun.gun_type,
        gun.manufacturer,
        gun.variations,
        gun.ammunition,
        gun.production_year,
        sep= " | "
    )

# add each instance of our programmers to our session
session.add(m4)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(grant_wilsmore)


# commit our session to the database
session.commit()