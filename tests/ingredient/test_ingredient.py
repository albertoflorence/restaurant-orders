from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient = Ingredient("bacon")
    assert ingredient.name == "bacon"
    assert ingredient.restrictions == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }
    assert ingredient == Ingredient("bacon")
    assert hash(ingredient) == hash("bacon")
    assert repr(ingredient) == "Ingredient('bacon')"
