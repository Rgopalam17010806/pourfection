from datetime import datetime
from sqlalchemy.orm import relationship

from website import db
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(500))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    phone = db.Column(db.String(50))
    type = db.Column(db.String(10))

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)


class Step(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text, nullable=False)




class RecipeStep(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    step_id = db.Column(db.Integer, db.ForeignKey('step.id'), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    recipe = relationship('Recipe', foreign_keys='RecipeStep.recipe_id')
    step = relationship('Step', foreign_keys='RecipeStep.step_id')


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    size = db.Column(db.String(10), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = relationship('User', backref='orders')
    recipe = relationship('Recipe', backref='orders')