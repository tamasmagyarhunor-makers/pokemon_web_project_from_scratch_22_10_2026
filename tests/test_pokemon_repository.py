from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon


def test_get_all_pokemons(db_connection):
    db_connection.seed("seeds/pokemon_seed.sql")
    repository = PokemonRepository(db_connection)

    pokemons = repository.all()

    assert pokemons == [
        Pokemon(1, 'Pikachu', 'electric'),
        Pokemon(2, 'Charmander', 'fire'),
        Pokemon(3, 'Bulbasaur', 'water-earth'),
        Pokemon(4, 'MewTwo', 'psychio'),
    ]