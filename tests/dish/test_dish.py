import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish = Dish("Salada", 10.5)

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("Salada", "10.5")
    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("Salada", -1)
    assert dish.name == "Salada"
    assert repr(dish) == "Dish('Salada', R$10.50)"
    assert dish == Dish("Salada", 10.5)
    assert hash(dish) == hash("Dish('Salada', R$10.50)")

    bacon = Ingredient("bacon")
    manteiga = Ingredient("manteiga")
    dish.add_ingredient_dependency(bacon, 2)
    dish.add_ingredient_dependency(manteiga, 1)
    assert dish.recipe == {bacon: 2, manteiga: 1}
    assert dish.get_ingredients() == {bacon, manteiga}
    assert dish.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.LACTOSE,
    }
