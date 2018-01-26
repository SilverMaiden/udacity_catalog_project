from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item


engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)


session = DBSession()

all_cats = session.query(Category).all()


session.delete(all_cats)
session.commit()
print "Categories Cleared"


