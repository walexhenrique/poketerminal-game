import pickle

from pessoa import Jogador, PokemonFactory


class Backup:
    """
    Classe responsável por realizar o save e recuperar o save em formato json.
    """

    @staticmethod
    def realizar_save(jogador: Jogador) -> None:
        """
        Método responsável por salvar o save do jogo, salvando o seu
        nome e os pokemons.

        :param jogador: Objeto do jogador.
        :type jogador: Jogador

        :return: None
        :rtype: None
        """

        save = {
            'nome': jogador.nome,
            'pokemons_nome': [pokemon.__class__.__name__ for pokemon in jogador.lista_pokemons],
            'pokemons_nivel': [pokemon.nivel for pokemon in jogador.lista_pokemons]
        }
        with open('data.json', 'wb') as fp:
            pickle.dump(save, fp)

    @staticmethod
    def carregar_save() -> Jogador:
        """
        Método responsável por carregar o save .json e transformar isso
        em jogador novamente.

        :return: Retorna o objeto do jogador do save.
        :rtype: Jogador.
        """

        with open('data.json', 'rb') as fp:
            save = pickle.load(fp)

        jogador = Jogador(save['nome'])
        for i in range(len(save['pokemons_nome'])):
            pokemon_save = PokemonFactory.get_pokemon(
                save['pokemons_nome'][i], save['pokemons_nivel'][i])
            jogador.capturar_pokemon(pokemon_save)

        return jogador
