from sqlalchemy import create_engine,String,Integer, Column
from sqlalchemy.orm import declarative_base
engine = create_engine("sqlite:///data.db")

base = declarative_base()

class User(base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    loc = Column(String)
    userId = Column(String)
    description = Column(String)
    price = Column(Integer)
    status = Column(String)

base.metadata.create_all(engine)