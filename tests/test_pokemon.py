from lib.pokemon import Pokemon

def test_pokemon_instantiates():
    pokemon = Pokemon(1, 'Raichu', 'electric')

    assert pokemon.id == 1
    assert pokemon.name == 'Raichu'
    assert pokemon.power_type == 'electric'

def test_pokemon_prints_nicely():
    pokemon = Pokemon(1, 'Raichu', 'electric')

    assert str(pokemon) == "Pokemon(1, Raichu, electric)"

def test_pokemons_with_same_attributes_are_equals():
    pokemon = Pokemon(1, 'Raichu', 'electric')
    pokemon_2 = Pokemon(1, 'Raichu', 'electric')

    assert pokemon == pokemon_2