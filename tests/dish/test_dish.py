from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish1 = Dish("Burguer", 24.99)
    dish2 = Dish("Shrimp Salad", 30.99)

    assert dish1.name == "Burguer"
    assert dish2.name == "Shrimp Salad"
    assert dish1.price == 24.99
    assert dish2.price == 30.99

    assert dish1 == dish1
    assert hash(dish1) == hash(dish1)
    assert dish1 != dish2
    assert hash(dish1) != hash(dish2)

    assert repr(dish1) == "Dish('Burguer', R$24.99)"
    assert repr(dish2) == "Dish('Shrimp Salad', R$30.99)"

    ingredient1 = Ingredient("farinha")
    ingredient2 = Ingredient("bacon")
    ingredient3 = Ingredient("carne")
    dish1_recipe = {ingredient1: 200, ingredient2: 250, ingredient3: 150}

    dish1.add_ingredient_dependency(ingredient1, 200)
    dish1.add_ingredient_dependency(ingredient2, 250)
    dish1.add_ingredient_dependency(ingredient3, 150)

    assert dish1.recipe == dish1_recipe
    assert ingredient1 in dish1.get_ingredients()
    assert ingredient2 in dish1.get_ingredients()
    assert ingredient3 in dish1.get_ingredients()

    assert dish1.get_restrictions() != set('')

    with pytest.raises(TypeError):
        Dish("BBQ", "Not a Number")

    with pytest.raises(ValueError):
        Dish("BBQ", -50.99)
