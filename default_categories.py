from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item


engine = create_engine('sqlite:///catalog.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)


session = DBSession()

category1 = Category(name="Tops")
session.add(category1)
session.commit()

category2 = Category(name="Bottoms")
session.add(category2)
session.commit()

category3 = Category(name="Shoes")
session.add(category3)
session.commit()

category4 = Category(name="Hats")
session.add(category4)
session.commit()

category5 = Category(name="Accessories")
session.add(category5)
session.commit()


print "Default Categories Added"


item1 = Item(name="Tank Top", description = "A simple tank top for your every day needs", category_id = category1.id)
session.add(item1)
session.commit()

item2 = Item(name="Crop Top", description = "A simple top with stylish flair", category_id = category1.id)
session.add(item2)
session.commit()

item3 = Item(name="Skinny Jeans", description = "Classic, skinny blue jeans", category_id = category2.id)
session.add(item3)
session.commit()

item4 = Item(name="High Waisted Jeans", description = "For a fitted, retro look", category_id = category2.id)
session.add(item4)
session.commit()

item5 = Item(name="Flower Converse Shoes", description = "Classy, flowery converse", category_id = category3.id)
session.add(item5)
session.commit()

item6 = Item(name="Converse High Kicks", description = "The original converse high kicks", category_id = category3.id)
session.add(item6)
session.commit()

item7 = Item(name="Wide Brim Hat", description = "For your sun protection needs", category_id = category4.id)
session.add(item7)
session.commit()

item8 = Item(name="GaymerX Limited Edtion Cap", description = "A limited edition cap from GaymerX 2015, complete with a rainbow patch", category_id = category4.id)
session.add(item8)
session.commit()

print "Default Items Added"
