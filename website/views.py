from datetime import datetime
from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_login import login_required, current_user

from website.models import Orders, Recipe, RecipeStep
from website.viewmodels import RecipeViewModel
from website import db

views = Blueprint('views', __name__)


#route for the home page
@views.route('/')
def home():
    return render_template("home.html", user=current_user)

#route for the machine page
@views.route('/machine')
@login_required
def machine():
    recipes = Recipe.query.all()
    return render_template("machine.html", user=current_user, recipes=recipes)

    
# route for saving the user's order. 
@views.route('/submit_order', methods=['POST'])
@login_required
def submit_order():
    recipe_id = request.form.get('recipe_id')
    size = request.form.get('size')
    recipe = Recipe.query.filter_by(id=recipe_id).one_or_none()
    if recipe and size:
        new_order = Orders(user_id=current_user.id, recipe_id=recipe_id, size=size, order_date=datetime.utcnow())
        db.session.add(new_order)
        db.session.commit()
        recipe_steps = (RecipeStep.query
                        .filter_by(recipe_id=recipe.id)
                        .order_by(RecipeStep.order.asc())
                        .all())
        # Create the view model
        recipe_view_model = RecipeViewModel(
            recipe_name=recipe.name,
            description=recipe.description,
            steps=[rs.step.description for rs in recipe_steps]
        )
        return render_template("prepare.html", user=current_user, recipeview=recipe_view_model, size=size)
    else:
        flash('Failed to place order. Please try again.', category='error')
        return redirect(url_for('views.machine'))
