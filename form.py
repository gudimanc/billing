from wtforms import BooleanField, StringField, PasswordField, validators, IntegerField,SubmitField
from flask_wtf import FlaskForm
class ProductForm(FlaskForm):
    name = StringField('Product Name', [validators.Length(min=1, max=25)], render_kw={"placeholder": "Product Name","id":"addname"})
    price = IntegerField('Product Price',[validators.NumberRange(min=1)], render_kw={"placeholder": "Product Price"})
    add = SubmitField('Add')

class DeleteProduct(FlaskForm):
    name = StringField('Product Name', [validators.Length(min=1, max=25)], render_kw={"placeholder": "Product Name","id":"removename"})
    remove = SubmitField('Remove')

class EditProduct(FlaskForm):
    name = StringField('Product Name', [validators.Length(min=1, max=25)], render_kw={"placeholder": "Product Name","id":"editname"})
    price = IntegerField('Product Price',[validators.NumberRange(min=1)], render_kw={"placeholder": "Product Price"})
    edit = SubmitField('Edit')