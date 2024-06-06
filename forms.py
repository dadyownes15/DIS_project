from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, NumberRange

from GreenGroceries.queries import get_user_by_user_name, get_farmer_by_pk, get_customer_by_pk
from GreenGroceries.utils.choices import ProduceItemChoices, ProduceCategoryChoices, UserTypeChoices, \
    ProduceVarietyChoices, ProduceUnitChoices

class FilterProduceForm(FlaskForm):
    category = SelectField('Category',
                           choices=ProduceCategoryChoices.choices())
    item = SelectField('Item',
                       choices=ProduceItemChoices.choices())
    variety = SelectField('Variety',
                          choices=ProduceVarietyChoices.choices())
    sold_by = StringField('Sold by')
    price = FloatField('Price (lower than or equal to)',
                       validators=[NumberRange(min=0, max=100)])

    submit = SubmitField('Filter')

