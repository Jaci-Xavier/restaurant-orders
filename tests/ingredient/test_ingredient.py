from src.models.ingredient import (
    Ingredient,
    Restriction,
)


# Req 1
def test_ingredient():
    queijo_mussarela = Ingredient("queijo mussarela")
    bacon = Ingredient("bacon")
    creme_de_leite = Ingredient("creme de leite")
    assert queijo_mussarela == Ingredient("queijo mussarela")
    assert queijo_mussarela != bacon
    assert bacon != creme_de_leite
    assert repr(queijo_mussarela) == "Ingredient('queijo mussarela')"
    assert repr(bacon) == "Ingredient('bacon')"
    assert repr(creme_de_leite) == "Ingredient('creme de leite')"
    assert queijo_mussarela.name == "queijo mussarela"
    assert bacon.name == "bacon"
    assert creme_de_leite.name == "creme de leite"
    assert queijo_mussarela.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
        }
    assert bacon.restrictions == {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED
        }
    assert creme_de_leite.restrictions == {
        Restriction.LACTOSE, Restriction.ANIMAL_DERIVED
        }
    assert hash(queijo_mussarela) != hash(bacon)
    assert hash(queijo_mussarela) != hash(creme_de_leite)
    assert hash(bacon) != hash(creme_de_leite)
    assert hash(queijo_mussarela) == hash(Ingredient("queijo mussarela"))
    assert hash(bacon) == hash(Ingredient("bacon"))
    assert hash(creme_de_leite) == hash(Ingredient("creme de leite"))
