from __future__ import annotations
from typing import List
from pokemon import Pokemon, PokemonFactory
from batalha import Batalha
import random


class Pessoa:
    """ Classe abstrata """
    lista_pokemons: List[Pokemon]
    nome: str

    def capturar_pokemon(self, pokemon: Pokemon) -> None:
        assert isinstance(pokemon, Pokemon), 'O objeto precisa ser um Pokemon'
        self.lista_pokemons.append(pokemon)

    def __str__(self) -> str:
        return f'{self.nome}'


class Inimigo(Pessoa):
    def __init__(self) -> None:
        self.nome: str = 'Desconhecido'
        self.lista_pokemons: List[Pokemon] = []


class InimigoFactory:
    @staticmethod
    def get_inimigo() -> Inimigo:
        quantidade_de_pokemons = random.randint(1, 4)
        inimigo = Inimigo()
        for i in range(quantidade_de_pokemons):
            inimigo.capturar_pokemon(PokemonFactory.get_pokemon())

        return inimigo


class Jogador(Pessoa):
    def __init__(self, nome: str) -> None:
        self.nome: str = nome
        self.lista_pokemons: List[Pokemon] = []
        self.quantidade_vitorias: int = 0

    def batalhar(self, id_pokemon: int, inimigo: Inimigo, id_pokemon_inimigo: int) -> bool:
        assert isinstance(inimigo, Inimigo), 'Para batalhar precisa ser um objeto do tipo Inimigo'

        if id_pokemon >= len(self.lista_pokemons) or id_pokemon < 0:
            return False

        batalha = Batalha(self.lista_pokemons[id_pokemon], inimigo.lista_pokemons[id_pokemon_inimigo])

        self._resultado_da_batalha(batalha.batalhar(), id_pokemon)
        return True

    def _resultado_da_batalha(self, vencedor: str, id_pokemon: int) -> None:
        if vencedor == 'Player':
            self.lista_pokemons[id_pokemon].subir_nivel()
            print(f'VOCÊ!!! {self.nome} GANHOU A BATALHA!!!')
            print(f'Após vencer o seu pokemon subiu 2 leveis!!!!!!')
            return

        print('Infelizmente você perdeu, quem sabe na próxima! E por causa disso o seu pokemon não subiu de nível')

    def apresentar_pokemons(self) -> None:
        for indice, pokemon in enumerate(self.lista_pokemons):
            print(f'Digite = {indice} para escolher o/a {pokemon.__class__.__name__} de nível {pokemon.nivel} e dano '
                  f'base de {pokemon.ataque_base}')
