from __future__ import annotations

import random
from typing import List

from batalha import Batalha
from pokemon import Pokemon, PokemonFactory


class Pessoa:
    """ Classe abstrata """
    lista_pokemons: List[Pokemon]
    nome: str

    def capturar_pokemon(self, pokemon: Pokemon) -> None:
        """
        Método responsável por adicionar o pokemon na lista_pokemons da pessoa.

        :param pokemon: Pokemon que será adicionado a lista.
        :type pokemon: Pokemon

        :raise AssertionError: paramêtro pokemon não ser um objeto do tipo pokemon.
        :return: None
        :rtype: None
        """
        assert isinstance(pokemon, Pokemon), 'O objeto precisa ser um Pokemon'
        self.lista_pokemons.append(pokemon)

    def __str__(self) -> str:
        return f'{self.nome}'


class Inimigo(Pessoa):
    """
    Classe responsável pela gerenciamento do inimigo.

    Atributos:
    nome (str): Nome do inimigo. sempre será ("Desconhecido").
    lista_pokemons (List[Pokemon]): Lista de pokemons do inimigo.
    """

    def __init__(self) -> None:
        self.nome: str = 'Desconhecido'
        self.lista_pokemons: List[Pokemon] = []


class InimigoFactory:
    """
    Classe fábrica responsável por gerar inimigos para o jogo.
    """
    @staticmethod
    def get_inimigo() -> Inimigo:
        """
        Método responsável por gerar um inimigo para o jogo, gerando aleatoriamente de 1 a 4 pokemons para ele.

        :return: Retorna o inimigo que o jogador vai enfrentar.
        :rtype: Inimigo
        """
        quantidade_de_pokemons = random.randint(1, 4)
        inimigo = Inimigo()
        for i in range(quantidade_de_pokemons):
            inimigo.capturar_pokemon(PokemonFactory.get_pokemon())

        return inimigo


class Jogador(Pessoa):
    """
    Classe responsável pela configuração do jogador e funcionalidades do mesmo.

    Atributos:
    nome (str): Nome do jogador.
    lista_pokemons (List[Pokemon]): Lista de pokemons do jogador.
    """

    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.lista_pokemons: List[Pokemon] = []

    def batalhar(self, id_pokemon: int, inimigo: Inimigo, id_pokemon_inimigo: int) -> bool:
        """
        Método responsável por organizar a batalha do jogador e o inimigo.

        :param id_pokemon: Indice do pokemon que o jogador vai usar na batalha.
        :type id_pokemon: int
        :param inimigo: Objeto inimigo que vai enfrentar o jogador.
        :type inimigo: Inimigo
        :param id_pokemon_inimigo: Indice do pokemon inimigo.
        :type id_pokemon_inimigo: int

        :raise AssertionError: parâmetro inimigo não é um objeto Inimigo.
        :return: Retorna False caso não seja possível realizar a batalha, True
        caso deu certo.
        :rtype: bool
        """
        assert isinstance(inimigo,
                          Inimigo
                          ), 'Para batalhar precisa ser objeto do tipo Inimigo'

        if id_pokemon >= len(self.lista_pokemons) or id_pokemon < 0:
            return False

        print('#'*50)
        print(f'{self.lista_pokemons[id_pokemon]} EU ESCOLHO VOCÊ!!!!')
        print('#'*50)
        batalha = Batalha(
            self.lista_pokemons[id_pokemon],
            inimigo.lista_pokemons[id_pokemon_inimigo]
        )

        self._resultado_da_batalha(batalha.batalhar(), id_pokemon)
        return True

    def _resultado_da_batalha(self, vencedor: str, id_pokemon: int) -> None:
        """
        Método privado que configura o nível do pokemon do jogador
        caso ele ganhe.

        :param vencedor: Vencedor da luta. pode ser "Player" ou "Inimigo".
        :type vencedor: str
        :param id_pokemon: Indice do pokemon do jogador.
        :type id_pokemon: int

        :return: None
        :rtype: None
        """
        if vencedor == 'Player':
            self.lista_pokemons[id_pokemon].subir_nivel()
            print(f'VOCÊ!!! {self.nome} GANHOU A BATALHA!!!')
            print(f'Após vencer o seu pokemon subiu 2 leveis!!!!!!')
            return

        print('Infelizmente você perdeu, quem sabe na próxima! E por causa disso o seu pokemon não subiu de nível')

    def apresentar_pokemons(self) -> None:
        """Apresenta os pokemons do jogador antes da luta.
        :return: None
        :rtype: None
        """
        for indice, pokemon in enumerate(self.lista_pokemons):
            print(f'Digite = {indice} para escolher o/a {pokemon.__class__.__name__} de nível {pokemon.nivel} e dano '
                  f'base de {pokemon.ataque_base}')
