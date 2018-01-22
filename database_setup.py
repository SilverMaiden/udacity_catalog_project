from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine


Base = declarative_base()

class Category(Base):
    __tablename__ = 'catalog'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id
        }

class Item(Base):
    __tablename__ = 'item'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    category_id = Column(Integer, ForeignKey('catalog.id'))
    category = relationship(Category)

    @property
    def serialize(self):
        return {
            'category_id': self.category_id,
            'description': self.description,
            'name': self.name,
            'id': self.id

        }

###INSERT AT END OF FILE###

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
