from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("manteiga")
    ingredient3 = Ingredient("farinha")

    # Check hashes
    assert hash(ingredient1) == hash(ingredient1)
    assert hash(ingredient1) != hash(ingredient2)
    # Check equality
    assert ingredient1 == ingredient1
    assert ingredient1 != ingredient2
    # check name and not undefined/none
    assert ingredient1.name == "bacon"
    assert ingredient1 is not None
    # check for invalid entry
    assert ingredient1 != "66"
    assert ingredient1 != 6
    # check __repr__
    assert repr(ingredient1) == repr(ingredient1)
    assert repr(ingredient1) != repr(ingredient2)
    assert repr(ingredient1) == "Ingredient('bacon')"
    # check restrictions
    bacon_restrictions = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    butter_restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    flour_restrictions = {Restriction.GLUTEN}
    assert ingredient1.restrictions == bacon_restrictions
    assert ingredient2.restrictions == butter_restrictions
    assert ingredient3.restrictions == flour_restrictions
