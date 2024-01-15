from sqlalchemy.orm import *
from model import User, engine

Session = sessionmaker(bind=engine)

session = Session()

data = session.query(User).all()

for person in data:
    print(f"id : {person.id} loc : {person.loc} userId : {person.userId} description : {person.description} price : {person.price} status : {person.status}")

session.commit()