from src.models.dish import Dish


# Req 2
def test_dish():
    # Arrange
    # Act
    shrimp = Dish("camarão", 30.00)
    ham = Dish("ham", 15.00)
    # Assert
    assert shrimp.name == "camarão"
    assert hash(shrimp) == hash(shrimp)
    assert shrimp == Dish("camarão", 30.00)
    assert shrimp != ham
