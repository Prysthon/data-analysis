from models.dish import Dish
from models.ingredient import Ingredient
import pandas as pd


class MenuData:
    def __init__(self, source_path: str) -> None:
        database = pd.read_csv(source_path)
        self.dishes = set()

        for food in database.groupby(["dish"]):
            plate, data = food
            price = data.iloc[0]["price"]
            dish = Dish(plate, price)

            recipe = list(zip(data["ingredient"], data["recipe_amount"]))

            for ingredients, amount in recipe:
                ingredient = Ingredient(ingredients)
                dish.add_ingredient_dependency(ingredient, amount)
            self.dishes.add(dish)

