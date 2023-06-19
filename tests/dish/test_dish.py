from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    # Act
    shrimp = Dish("camarão", 30.00)
    ham = Dish("ham", 15.00)
    bacalhau = Dish("bacalhau", 30.00)

    cheese = Ingredient("queijo parmesão")
    shrimp.add_ingredient_dependency(cheese, 1)

    # Assert
    assert shrimp.name == "camarão"
    assert hash(shrimp) == hash(shrimp)
    assert hash(shrimp) != hash(ham)
    assert shrimp == Dish("camarão", 30.00)
    assert repr(shrimp) == "Dish('camarão', R$30.00)"
    assert shrimp.get_ingredients() == {cheese}
    assert bacalhau.get_restrictions() == set()

    with pytest.raises(TypeError):
        Dish("presunto", "30.00")

    with pytest.raises(ValueError):
        Dish("presunto", 0)
