from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

Bootstrap(app)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



@app.route('/')
@app.route('/catalog/')
def showLandingPage():
    categories = session.query(Category).all()
    ### TO CLEAR OUT DB ###
    #items = session.query(Item).all()
    #for item in items:
    #    session.delete(item)
    #    session.commit()

    #for category in categories:
    #    session.delete(category)
    #    session.commit()

    return render_template('catalog.html', categories = categories)

@app.route('/catalog/<string:category_name>/items/')
def showCategoryItems(category_name):
    category = session.query(Category).filter_by(name = category_name).one()
    items = session.query(Item).filter_by(category_id = category.id).all()
    return render_template('items.html', items = items, category = category)

@app.route('/catalog/<string:category_name>/<string:item_name>/')
def showItemDescription(category_name, item_name):
    category = session.query(Category).filter_by(name = category_name).one()
    item = session.query(Item).filter_by(name = item_name).one()
    return render_template('itemdescription.html', item = item, category = category)

@app.route('/catalog/s_item/edit/')
def editItem():
    return render_template('edititem.html')

@app.route('/catalog/s_item/delete/')
def deleteItem():
    return render_template('deleteitem.html')

@app.route('/catalog/add/')
def addItem():
    return render_template('additem.html')






if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
