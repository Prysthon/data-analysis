from src.models.ingredient import Ingredient


# Req 1
def test_ingredient():
    # Act
    shrimp = Ingredient("camarão")
    ham = Ingredient("ham")

    # Asserts
    # TestIngredientInvalidName
    assert shrimp.name == "camarão"
    # TestIngredientInvalidHashDifferent e TestIngredientInvalidHashEqual
    assert hash(shrimp) == hash("camarão")
    # TestIngredientInvalidRepr
    assert repr(shrimp) == "Ingredient('camarão')"
    # TestIngredientInvalidRestrictionMap
    assert ham.restrictions == set()
    # TestIngredientInvalidEqualDifferent] e TestIngredientInvalidEqualEqual
    assert shrimp == Ingredient("camarão")
