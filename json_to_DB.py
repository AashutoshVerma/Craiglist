from sqlalchemy import  *
from sqlalchemy.orm import  *
from model import  User, engine

import json
data = []
with open("./data.json","r") as f:
    data = json.load(f)

Session = sessionmaker(bind=engine)
session = Session()

# print(data[0]['id'])
# for users in data :
#     session.add(User(id = users['id'], loc =  ', '.join(str(item) for item in users['loc']), userId = users['userId'], description = users['description'], price = users['price'], status = users['status']))
    # print(users['id'])
# session.commit()
data = session.query(User).all()
for person in data:
    print(f"id : {person.id} loc : {person.loc} userId : {person.userId} description : {person.description} price : {person.price} status : {person.status}")

# print(data)
