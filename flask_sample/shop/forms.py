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