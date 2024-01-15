from sqlalchemy.orm import  sessionmaker
from model import  User, engine
Session = sessionmaker(bind=engine)
session = Session()
# user = User(id = "1235", loc = "0.0", userId = "123", description = "null", price = -1, status = "Removed" )
# session.add(User(id = "12345", loc = "0.0", userId = "123", description = "null", price = -1, status = "Removed" ))
# session.add(user)
users = session.query(User).all()
for person in users:
    print(f"id : {person.id} loc : {person.loc} userId : {person.userId} description : {person.description} price : {person.price} status : {person.status}")
session.commit()