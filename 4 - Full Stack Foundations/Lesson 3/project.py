from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#Making an API Endpoint (GET Request)
@app.route('/restaurants/JSON')
def restaurantJSON():
    restaurants = session.query(Restaurant).all()
    return jsonify(Restaurant=[i.serialize for i in restaurants])

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    return jsonify(MenuItems=[i.serialize for i in items]) 

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def restaurantMenuSpecificJSON(restaurant_id, menu_id):       
    item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_id).one()
    return jsonify(Item=item.serialize)


@app.route('/')
def restaurant():
    restaurants = session.query(Restaurant).all()

    return render_template('restaurant.html', restaurants=restaurants)

@app.route('/new', methods=['GET', 'POST'])
def newRestaurant():
    if request.method == 'POST':
        newItem = Restaurant(name=request.form['name'])
        session.add(newItem)
        session.commit()
        flash("new restaurant created!")
        return redirect(url_for('restaurant'))
    else:
        return render_template('newrestaurant.html')

@app.route('/<int:restaurant_id>/edit/', methods=['GET', 'POST'])
def editRestaurant(restaurant_id):
    if request.method == 'POST':
        editItem = session.query(Restaurant).filter_by(id=restaurant_id).first()
        editItem.name = request.form['name']
        session.commit()
        flash("restaurant name edited!")
        return redirect(url_for('restaurant'))
    else:
        return render_template('editrestaurant.html', restaurant_id=restaurant_id)
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('/<int:restaurant_id>/delete/', methods=['GET', 'POST'])
def deleteRestaurant(restaurant_id):
    if request.method == 'POST':
        session.query(Restaurant).filter_by(id=restaurant_id).delete()
        flash("restaurant deleted!")
        return redirect(url_for('restaurant'))
    else:
        item = session.query(Restaurant).filter_by(id=restaurant_id).first()
        return render_template('deleterestaurant.html', restaurant_id=restaurant_id, item=item)
    return "page to delete a menu item. Task 3 complete!"        


@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    
    return render_template('menu.html', restaurant=restaurant, items=items)

# Task 1: Create route for newMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/new/', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):
    if request.method == 'POST':
        newItem = MenuItem(name=request.form['name'], restaurant_id=restaurant_id)
        session.add(newItem)
        session.commit()
        flash("new menu item created!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('newmenuitem.html', restaurant_id=restaurant_id)

# Task 2: Create route for editMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit/', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    if request.method == 'POST':
        editItem = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).first()
        editItem.name = request.form['name']
        session.commit()
        flash("menu item edited!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id)
    return "page to edit a menu item. Task 2 complete!"

# Task 3: Create a route for deleteMenuItem function here

@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete/', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    if request.method == 'POST':
        session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_id).delete()
        flash("menu item deleted!")
        return redirect(url_for('restaurantMenu', restaurant_id=restaurant_id))
    else:
        item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_id).first()
        return render_template('deletemenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=item)
    return "page to delete a menu item. Task 3 complete!"


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(port=5000)
