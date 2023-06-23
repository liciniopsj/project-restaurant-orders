import csv
from src.models.ingredient import Ingredient
from src.models.dish import Dish


class MenuData:
    def __init__(self, source_path: str):
        self.load_file(source_path)

    def load_file(self, source_path: str):
        with open(source_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            self.dishes = set()

            for row in reader:
                dish_name = row['dish']
                dish_price = float(row['price'])
                ingredient_name = row['ingredient']
                recipe_amount = int(row['recipe_amount'])

                dish = self.get_or_create_dish(dish_name, dish_price)
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, recipe_amount)

    def get_or_create_dish(self, name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == name and dish.price == price:
                return dish

        new_dish = Dish(name, price)
        self.dishes.add(new_dish)
        return new_dish
