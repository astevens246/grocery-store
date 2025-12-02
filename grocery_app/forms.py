from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField, FloatField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Length, URL
from grocery_app.models import GroceryStore, ItemCategory


class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    # TODO: Add the following fields to the form class:
    title = StringField("Title", validators=[DataRequired(), Length(min=3, max=80)])
    address = StringField(
        "Address", validators=[DataRequired(), Length(min=3, max=200)]
    )
    submit = SubmitField("Submit")


class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    # TODO: Add the following fields to the form class:
    name = StringField("Name", validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField("Price", validators=[DataRequired()])
    category = SelectField("Category", choices=ItemCategory.choices())
    photo_url = StringField("Photo URL", validators=[DataRequired(), URL()])
    store = QuerySelectField(
        "Store",
        query_factory=lambda: GroceryStore.query,
        get_label="title",
        validators=[DataRequired()],
    )
    submit = SubmitField("Submit")
