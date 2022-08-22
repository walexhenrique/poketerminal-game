from pessoa import Jogador
import pickle
from pessoa import PokemonFactory


class Backup:
    @staticmethod
    def realizar_save(jogador: Jogador) -> None:

        save = {
            'nome': jogador.nome,
            'pokemons_nome': [pokemon.__class__.__name__ for pokemon in jogador.lista_pokemons],
            'pokemons_nivel': [pokemon.nivel for pokemon in jogador.lista_pokemons]
        }
        with open('data.json', 'wb') as fp:
            pickle.dump(save, fp)

    @staticmethod
    def carregar_save() -> Jogador:

        with open('data.json', 'rb') as fp:
            save = pickle.load(fp)

        jogador = Jogador(save['nome'])
        for i in range(len(save['pokemons_nome'])):
            pokemon_save = PokemonFactory.get_pokemon(save['pokemons_nome'][i], save['pokemons_nivel'][i])
            jogador.capturar_pokemon(pokemon_save)

        return jogador
