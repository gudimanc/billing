from os import name
from wtforms import BooleanField, StringField, SelectField, validators, IntegerField,SubmitField
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

class EditProductName(FlaskForm):
    old_name = StringField('Old Name', [validators.Length(min=1, max=25)], render_kw={"placeholder": "Old Name","id":"editpname"})
    new_name = StringField('New Name', [validators.Length(min=1, max=25)], render_kw={"placeholder": "New Name","id":"editpname"})
    edit = SubmitField('Edit')

class AvailabilityForm(FlaskForm):
    name = SelectField(u'Name')
    available_quantity =IntegerField('Product Price',[validators.NumberRange(min=0)], render_kw={"placeholder": "Quantity"})
    change = SubmitField('Change')

class BillingForm(FlaskForm):
    name = SelectField(u'Name')
    quantity  =IntegerField('Product Price',[validators.NumberRange(min=0)], render_kw={"placeholder": "Quantity"})
    add =  SubmitField('Add')

class ClearBill(FlaskForm):
    clear = SubmitField('Clear')

class UndoBill(FlaskForm):
    undo = SubmitField('Undo')

class GenerateBill(FlaskForm):
    name=StringField('Name', render_kw={"placeholder": "Customer Name"})
    genbill = SubmitField('Generate Bill')