from flask import Blueprint, render_template, flash, redirect, request, url_for
from flask_login import login_required, current_user

from website.models import Recipe, RecipeStep
from website.viewmodels import RecipeViewModel

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html", user=current_user)

@views.route('/machine')
@login_required
def machine():
    recipes = Recipe.query.all()
    return render_template("machine.html", user=current_user, recipes=recipes)

@views.route('/prepare/<string:recipe_id>', methods=['GET'])
@login_required
def prepare(recipe_id):
    size = request.args.get('size')
    recipe = Recipe.query.filter_by(id=recipe_id).one_or_none()
    if recipe:
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
        flash('Recipe does not exist.', category='error')
        return redirect(url_for('views.machine'))