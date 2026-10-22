from lib.pokemon import Pokemon

class PokemonRepository:
    def __init__(self, conn):
        self.connection = conn
    
    def all(self):
        poke_dicts = self.connection.execute("SELECT * FROM pokemons")

        pokemons = []

        for poke_dict in poke_dicts:
            pokemon = Pokemon(poke_dict['id'], poke_dict['name'], poke_dict['power_type'])
            pokemons.append(pokemon)

        return pokemons