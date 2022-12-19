from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, TextAreaField, IntegerField, URLField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Optional, NumberRange

class ItemForm(FlaskForm):
    id = HiddenField("id", validators=[Optional()])
    name = StringField("name", validators=[DataRequired(), Length(max=30)])
    description = TextAreaField("description", validators=[DataRequired()])
    category = StringField("category", validators=[DataRequired(), Length(max=30)])
    stock = IntegerField("stock", validators=[NumberRange(min=0)])
    unit_price = IntegerField("unit price", validators=[NumberRange(min=0)])
    visibility = BooleanField("Visibility")
    image = URLField("image", validators=[Optional()])
    submit = SubmitField("Save")

class CheckoutForm(FlaskForm):
    first_name = StringField("first name", validators=[DataRequired(), Length(max=30)])
    last_name = StringField("last name", validators=[DataRequired(), Length(max=30)])
    payment_method = StringField("payment method", validators=[DataRequired(), Length(max=30)])
    money_received = IntegerField("Money received", validators=[NumberRange(min=0)])
    address = StringField("Address", validators=[DataRequired(), Length(max=120)])
    submit = SubmitField("Save")

