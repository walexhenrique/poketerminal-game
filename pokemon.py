from __future__ import annotations
from ataque import AtaqueStrategy, AtaqueNormal, AtaqueComForca, AtaqueComFraqueza
import random


class Pokemon:
    def __init__(self, nivel: int = 5) -> None:
        self.nivel: int = nivel
        self.vida: int = 10 * nivel
        self.ataque_base: int = 4 * nivel
        self.estrategia_luta: AtaqueStrategy = AtaqueNormal()

    def atacar(self, pokemon: Pokemon) -> None:
        assert isinstance(pokemon, Pokemon), 'Objeto precisa ser do tipo Pokemon'

    def mudar_estrategia_para_luta(self, estrategia: AtaqueStrategy) -> None:
        assert isinstance(estrategia, AtaqueStrategy), 'É preciso que seja um objeto AtaqueStrategy'
        self.estrategia_luta = estrategia

    @property
    def ataque(self) -> float:
        return round(self.estrategia_luta.calcular_ataque(self.ataque_base, self.nivel), 1)

    def recuperar_vida(self) -> None:
        self.vida = 10 * self.nivel

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def subir_nivel(self) -> None:
        self.nivel += 2
        self._reconfigurar_status()

    def _reconfigurar_status(self) -> None:
        self.vida = 10 * self.nivel
        self.ataque_base = 4 * self.nivel

    def apresentar_pokemon(self) -> None:
        print(f'pokemon: {self.__class__.__name__}')
        print(f'Level: {self.nivel}')
        print(f'Vida: {self.vida} de pontos.')
        print(f'Dano base: {self.ataque_base}')


class PokemonFogo(Pokemon):
    tipo = 'FOGO'
    fraqueza = 'AGUA'
    forte_contra = 'PEDRA'


class PokemonAgua(Pokemon):
    tipo = 'AGUA'
    fraqueza = 'ELETRICO'
    forte_contra = 'FOGO'


class PokemonEletrico(Pokemon):
    tipo = 'ELETRICO'
    fraqueza = 'PEDRA'
    forte_contra = 'AGUA'


class PokemonPedra(Pokemon):
    tipo = 'PEDRA'
    fraqueza = 'AGUA'
    forte_contra = 'ELETRICO'


class Onix(PokemonPedra):
    def atacar(self, pokemon: Pokemon) -> None:
        super().atacar(pokemon)

        dano_ataque = self.ataque
        print(f'Onix deu uma rabada no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque


class Charmander(PokemonFogo):
    def atacar(self, pokemon: Pokemon) -> None:
        super().atacar(pokemon)
        dano_ataque = self.ataque
        print(
            f'Charmander lançou um assopro de fogo no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque


class Pikachu(PokemonEletrico):
    def atacar(self, pokemon: Pokemon) -> None:
        super().atacar(pokemon)
        dano_ataque = self.ataque
        print(
            f'Pikachu usou o choque do TROVÃO!!! no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque


class Magicarpa(PokemonAgua):
    def atacar(self, pokemon: Pokemon) -> None:
        super().atacar(pokemon)
        dano_ataque = self.ataque
        print(
            f'Magicarpa deu uma cuspida fraca :/ no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque


class PokemonFactory:
    @staticmethod
    def get_pokemon(nome=None, nivel=None) -> Pokemon:
        nivel_aleatorio = nivel or random.randint(1, 100)
        pokemon = nome or random.choice(['onix', 'charmander', 'magicarpa', 'pikachu'])

        if pokemon.lower() == 'onix':
            return Onix(nivel_aleatorio)
        if pokemon.lower() == 'charmander':
            return Charmander(nivel_aleatorio)
        if pokemon.lower() == 'magicarpa':
            return Magicarpa(nivel_aleatorio)
        if pokemon.lower() == 'pikachu':
            return Pikachu(nivel_aleatorio)
