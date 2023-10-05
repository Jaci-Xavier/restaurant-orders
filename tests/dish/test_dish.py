import pytest
from src.models.dish import Dish, Ingredient

# Utilizei o método union para unir os conjuntos de restrições de
# ingredientes em um único conjunto.


# Req 2
def test_dish():
    # Prato válido
    dish1 = Dish("Lasanha", 25.0)
    assert dish1 == Dish("Lasanha", 25.0)
    assert dish1 != Dish("Ravioli", 20.0)
    assert repr(dish1) == "Dish('Lasanha', R$25.00)"
    assert dish1.name == "Lasanha"
    assert dish1.price == 25.0
    dish2 = Dish("Ravioli", 20.0)
    assert hash(dish1) != hash(dish2)
    assert hash(dish1) == hash(Dish("Lasanha", 25.0))
    with pytest.raises(ValueError):
        Dish("Cuscuz", -10.0)
    with pytest.raises(TypeError):
        Dish("Feijoada", "20.0")
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("bacon")
    dish1.add_ingredient_dependency(ingredient1, 200)
    dish1.add_ingredient_dependency(ingredient2, 150)
    assert dish1.recipe.get(ingredient1) == 200
    assert dish1.recipe.get(ingredient2) == 150
    ingredient3 = Ingredient("salmão")
    dish2.add_ingredient_dependency(ingredient3, 300)
    assert dish1.get_restrictions() == ingredient1.restrictions.union(
        ingredient2.restrictions
    )
    assert dish2.get_restrictions() == ingredient3.restrictions

    assert dish1.get_ingredients() == {ingredient1, ingredient2}
    assert dish2.get_ingredients() == {ingredient3}
