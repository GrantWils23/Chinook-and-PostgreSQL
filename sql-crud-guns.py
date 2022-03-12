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
    gun_name="M4",
    gun_type="Assult Rifle",
    manufacturer="Colt",
    variations="carabine, rifle",
    ammunition="5.56 x 45mm NATO",
    production_year=1987
)

# create records on our guns table
mp5 = Gun(
    gun_name="MP5",
    gun_type="Submachine Gun",
    manufacturer="H&K",
    variations="MP5, MP5 A1-5, MP5-K, MP5-SD",
    ammunition="9 x 19mm Parabellum",
    production_year=1966
)

# create records on our guns table
ak47 = Gun(
    gun_name="AK 47",
    gun_type="Assult Rifle",
    manufacturer="Arms Kalashnikov",
    variations="carabine, rifle",
    ammunition="7.62 x 39mm",
    production_year=1948
)

# create records on our guns table
g36 = Gun(
    gun_name="G36",
    gun_type="Assult Rifle",
    manufacturer="H&K",
    variations="G36K, G36C, G36V, MG36",
    ammunition="5.56 x 45mm NATO",
    production_year=1996
)

# create records on our guns table
fnscar = Gun(
    gun_name="FN SCAR",
    gun_type="Assult Rifle",
    manufacturer="FN Herstal",
    variations="SCAR H, SCAR L",
    ammunition="7.62 x 51mm",
    production_year=2004
)

# create records on our guns table
famas = Gun(
    gun_name="FAMAS",
    gun_type="Assult Rifle",
    manufacturer="Fusil d'Assaut de la Manufacture d'Armes de Saint-Étienne",
    variations="F1, G1, G2",
    ammunition="7.62 x 39mm",
    production_year=1975
)

# create records on our guns table
sa80 = Gun(
    gun_name="SA 80",
    gun_type="Assult Rifle",
    manufacturer="RSAF Enfield",
    variations="L85A1, L85A2",
    ammunition="5.56 x 45mm NATO",
    production_year=1985
)

# create records on our guns table
hk417 = Gun(
    gun_name="HK 417",
    gun_type="Assult Rifle, Marksman Rifle",
    manufacturer="H&K",
    variations="417 'Recce', 417 'Assaulter', 417 'Sniper' 417A2",
    ammunition="7.62 x 51mm MATO",
    production_year=2006
)

# create records on our guns table
hk416 = Gun(
    gun_name="HK 416",
    gun_type="Assult Rifle",
    manufacturer="H&K",
    variations="416D, 416C, 416A5",
    ammunition="5.56  x 45mm NATO",
    production_year=2004
)

# create records on our guns table
mp7 = Gun(
    gun_name="MP7",
    gun_type="Submachine Gun, PDW, Machine Pistol",
    manufacturer="H&K",
    variations="MP7A1, MP7A2",
    ammunition="4.6 x 30mm HK",
    production_year=1999
)

# create records on our guns table
deserteagle = Gun(
    gun_name="Desert Eagle",
    gun_type="Semi-Automatic Pistol",
    manufacturer="Magnum Research and Israel Military Industries",
    variations="Mark I, Mark VII, Mark XIX",
    ammunition=".50 Action Express, .44 Magnum, .41 Magnum, .357 Magnum",
    production_year=1983
)

# create records on our guns table
m249 = Gun(
    gun_name="M249",
    gun_type="Light Machine Gun, Belt-Fed LMG",
    manufacturer="FN Herstal",
    variations="M249, M249 Paratrooper, MK 46, MK 48, M249 Special Purpose Weapon",
    ammunition="5.56 x 45mm NATO",
    production_year=1977
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
        sep=" | "
    )

# add each instance of our programmers to our session
session.add(m4)
session.add(mp5)
session.add(ak47)
session.add(g36)
session.add(fnscar)
session.add(famas)
session.add(sa80)
session.add(hk417)
session.add(hk416)
session.add(mp7)
session.add(deserteagle)
session.add(m249)


# # Deleting a single record
# gname = input("Enter the gun name you are searching for: ")

# gun = session.query(Gun).filter_by(gun_name=gname).first()
# # Defensive programming
# if gun is not None:
#     print("Gun Found: " + gun.gun_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(gun)
#         session.commit()
#         print("Gun has been deleted")
#     else:
#         print("Gun not deleted")
# else:
#     print("Gun not found")


# commit our session to the database
session.commit()
