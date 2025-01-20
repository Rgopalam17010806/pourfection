import pandas as pd


def load_data(db):
    from .models import Recipe, Step, RecipeStep
    # Load Excel file
    excel_data = pd.ExcelFile("init_data/recipe_data.xlsx")
    # Read each sheet
    recipe_data = excel_data.parse("recipe")
    step_data = excel_data.parse("step")
    recipe_step_data = excel_data.parse("recipe_step")
    # Insert data into Recipe table
    for _, row in recipe_data.iterrows():
        recipe = Recipe(**row.to_dict())  # Adjust to map columns to model fields
        db.session.add(recipe)
    # Insert data into Step table
    for _, row in step_data.iterrows():
        step = Step(**row.to_dict())
        db.session.add(step)
    # Insert data into RecipeStep table
    for _, row in recipe_step_data.iterrows():
        recipe_step = RecipeStep(**row.to_dict())
        db.session.add(recipe_step)
    # Commit changes
    db.session.commit()
