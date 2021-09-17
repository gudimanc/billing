from flask import Flask, render_template, redirect,url_for
from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
from form import ProductForm,DeleteProduct,EditProduct
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
app = Flask(__name__)
app.config['SECRET_KEY']='LongAndRandomSecretKey'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Products(db.Model):
    id = db.Column('product_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer())  

    def __init__(self,name,price):
        self.name=name
        self.price=price


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products',methods=['GET','POST'])
def products():
    try:
        add_form = ProductForm()
        delete_form = DeleteProduct()
        edit_form = EditProduct()
        if add_form.validate_on_submit() and add_form.add.data:
            p=Products(add_form.name.data.capitalize(),add_form.price.data)
            db.session.add(p)
            db.session.commit()
            return redirect(url_for('products'))
        if delete_form.validate_on_submit() and delete_form.remove.data:
            r=Products.query.filter_by(name=delete_form.name.data.capitalize()).first()
            db.session.delete(r)
            db.session.commit()
            return redirect(url_for('products'))
        if edit_form.validate_on_submit() and edit_form.edit.data:
            e=Products.query.filter_by(name=edit_form.name.data.capitalize()).first()
            e.price = edit_form.price.data
            db.session.add(e)
            db.session.commit()
            return redirect(url_for('products'))
        return render_template('products.html',add_form=add_form,delete_form=delete_form,edit_form=edit_form,all_products=Products.query.all())
    except Exception as e:
        print(e)
        return redirect(url_for('products'))

@app.route('/availability',methods=['GET','POST'])
def availability():
    
    return render_template('availability.html')

@app.route('/billing',methods=['GET','POST'])
def billing():
    return render_template('billing.html')


if __name__=="__main__":
    app.run(debug=True)