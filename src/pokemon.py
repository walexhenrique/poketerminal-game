from __future__ import annotations

try:
    import os
    import sys

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise


import random

from ataque import AtaqueNormal, AtaqueStrategy


class Pokemon:
    """
    Classe abstrata pokemon responsável por configurar o comportamento
    genérico de todos os pokemons.

    Atributos:
    nivel (int): Nível do pokemon.
    vida (float): Vida do pokemon.
    ataque_base (int): dano base de ataque do pokemon.
    estrategia_luta (AtaqueStrategy): Estrategia de ataque, variando de acordo
    com o oponente.
    """
    tipo: str
    fraqueza: str
    forte_contra: str

    def __init__(self, nivel: int = 5) -> None:
        self.nivel: int = nivel
        self.vida: float = 10 * nivel
        self.ataque_base: int = 4 * nivel
        self.estrategia_luta: AtaqueStrategy = AtaqueNormal()

    def atacar(self, pokemon: Pokemon) -> None:
        """
        Método responsável por atacar o outro oponente, porém o mesmo será implementado
        nas classes filhas.

        :param pokemon: Pokemon que vai sofrer o ataque.
        :type pokemon: Pokemon

        :raise AssertionError: Parâmetro não é um objeto de pokemon.
        :return: None
        :rtype: None
        """
        assert isinstance(
            pokemon, Pokemon), 'Objeto precisa ser do tipo Pokemon'

    def mudar_estrategia_para_luta(self, estrategia: AtaqueStrategy) -> None:
        """
        Método responsável por mudar a estrategia de ataque de acordo
        com o oponente que irá enfrentar.

        :param estrategia: Estrategia que será adicionada ao pokemon.
        :type estrategia: AtaqueStrategy

        :raise AssertionError: Parâmetro não é um objeto AtaqueStrategy.

        :return: None
        :rtype: None
        """
        assert isinstance(
            estrategia,
            AtaqueStrategy
        ), 'É preciso que seja um objeto AtaqueStrategy'
        self.estrategia_luta = estrategia

    @property
    def ataque(self) -> float:
        """
        Método responsável por retornar o dano de ataque
        baseando no seu nivel, dano base e estrategia de ataque.

        :return: Retorna o dano de ataque.
        :rtype: float
        """
        return round(self.estrategia_luta.calcular_ataque(
            self.ataque_base,
            self.nivel
        ), 1)

    def recuperar_vida(self) -> None:
        """
        Método responsável por recuperar a vida do pokemon basendo
        em seu nível atual.

        :return: None
        :rtype: None
        """
        self.vida = 10 * self.nivel

    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def subir_nivel(self) -> None:
        """
        Método responsável por subir 2 níveis do pokemon e reconfigurar-lo.

        :return: None
        :rtype: None
        """
        self.nivel += 2
        self._reconfigurar_status()

    def _reconfigurar_status(self) -> None:
        """
        Método privado responsável por reconfigurar os atributos
        baseando-se no novo nível do pokemon.

        :return: None
        :rtype: None
        """
        self.vida = 10 * self.nivel
        self.ataque_base = 4 * self.nivel

    def apresentar_pokemon(self) -> None:
        """
        Método responsável por mostrar todas as informações do pokemon.

        :return: None
        :rtype: None
        """
        print(f'pokemon: {self.__class__.__name__}')
        print(f'Level: {self.nivel}')
        print(f'Vida: {self.vida} de pontos.')
        print(f'Dano base: {self.ataque_base}')


class PokemonFogo(Pokemon):
    """
    Classe abstrata para os pokemons do tipo Fogo.

    Atributos:
    nivel (int): Nível do pokemon.
    vida (float): Vida do pokemon.
    ataque_base (int): dano base de ataque do pokemon.
    estrategia_luta (AtaqueStrategy): Estrategia de ataque, variando de acordo
    com o oponente.

    Atributos de classe:
    tipo (str): define o tipo do pokemon.
    fraqueza (str): define o tipo de pokemon que é fraco contra.
    forte_contra (str): define o tipo de pokemon que é forte contra.
    """
    tipo = 'FOGO'
    fraqueza = 'AGUA'
    forte_contra = 'PEDRA'


class PokemonAgua(Pokemon):
    """
    Classe abstrata para os pokemons do tipo Água.

    Atributos:
    nivel (int): Nível do pokemon.
    vida (float): Vida do pokemon.
    ataque_base (int): dano base de ataque do pokemon.
    estrategia_luta (AtaqueStrategy): Estrategia de ataque, variando de acordo
    com o oponente.

    Atributos de classe:
    tipo (str): define o tipo do pokemon.
    fraqueza (str): define o tipo de pokemon que é fraco contra.
    forte_contra (str): define o tipo de pokemon que é forte contra.
    """
    tipo = 'AGUA'
    fraqueza = 'ELETRICO'
    forte_contra = 'FOGO'


class PokemonEletrico(Pokemon):
    """
    Classe abstrata para os pokemons do tipo Elétrico.

    Atributos:
    nivel (int): Nível do pokemon.
    vida (float): Vida do pokemon.
    ataque_base (int): dano base de ataque do pokemon.
    estrategia_luta (AtaqueStrategy): Estrategia de ataque, variando de acordo
    com o oponente.

    Atributos de classe:
    tipo (str): define o tipo do pokemon.
    fraqueza (str): define o tipo de pokemon que é fraco contra.
    forte_contra (str): define o tipo de pokemon que é forte contra.
    """
    tipo = 'ELETRICO'
    fraqueza = 'PEDRA'
    forte_contra = 'AGUA'


class PokemonPedra(Pokemon):
    """
    Classe abstrata para os pokemons do tipo Pedra.

    Atributos:
    nivel (int): Nível do pokemon.
    vida (float): Vida do pokemon.
    ataque_base (int): dano base de ataque do pokemon.
    estrategia_luta (AtaqueStrategy): Estrategia de ataque, variando de acordo
    com o oponente.

    Atributos de classe:
    tipo (str): define o tipo do pokemon.
    fraqueza (str): define o tipo de pokemon que é fraco contra.
    forte_contra (str): define o tipo de pokemon que é forte contra.
    """
    tipo = 'PEDRA'
    fraqueza = 'AGUA'
    forte_contra = 'ELETRICO'


class Onix(PokemonPedra):
    """
    Classe concreta pokemon Onix que herda da classe PokemonPedra.

    Atributos:
    nivel (int): Nível do pokemon.
    vida (float): Vida do pokemon.
    ataque_base (int): dano base de ataque do pokemon.
    estrategia_luta (AtaqueStrategy): Estrategia de ataque, variando de acordo
    com o oponente.

    Atributos de classe:
    tipo (str): define o tipo do pokemon.
    fraqueza (str): define o tipo de pokemon que é fraco contra.
    forte_contra (str): define o tipo de pokemon que é forte contra.
    """

    def atacar(self, pokemon: Pokemon) -> None:
        """
        Método responsável por realizar o ataque no oponente do seu pokemon
        baseando-se de acordo com sua força total calculada.
        :param pokemon: Pokemon que vai sofrer o ataque.
        :type pokemon: Pokemon

        :raise AssertionError: Parâmetro não é um objeto de pokemon.

        :return: None
        :rtype: None
        """
        super().atacar(pokemon)

        dano_ataque = self.ataque
        print(
            f'Onix deu uma rabada no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque


class Charmander(PokemonFogo):
    """
    Classe concreta pokemon Charmander que herda da classe PokemonFogo.

    Atributos:
    nivel (int): Nível do pokemon.
    vida (float): Vida do pokemon.
    ataque_base (int): dano base de ataque do pokemon.
    estrategia_luta (AtaqueStrategy): Estrategia de ataque, variando de acordo
    com o oponente.

    Atributos de classe:
    tipo (str): define o tipo do pokemon.
    fraqueza (str): define o tipo de pokemon que é fraco contra.
    forte_contra (str): define o tipo de pokemon que é forte contra.
    """

    def atacar(self, pokemon: Pokemon) -> None:
        """
        Método responsável por realizar o ataque no oponente do seu pokemon
        baseando-se de acordo com sua força total calculada.
        :param pokemon: Pokemon que vai sofrer o ataque.
        :type pokemon: Pokemon

        :raise AssertionError: Parâmetro não é um objeto de pokemon.

        :return: None
        :rtype: None
        """
        super().atacar(pokemon)
        dano_ataque = self.ataque
        print(
            f'Charmander lançou um assopro de fogo no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque


class Pikachu(PokemonEletrico):
    """
    Classe concreta pokemon Pikachu que herda da classe PokemonEletrico.

    Atributos:
    nivel (int): Nível do pokemon.
    vida (float): Vida do pokemon.
    ataque_base (int): dano base de ataque do pokemon.
    estrategia_luta (AtaqueStrategy): Estrategia de ataque, variando de acordo
    com o oponente.

    Atributos de classe:
    tipo (str): define o tipo do pokemon.
    fraqueza (str): define o tipo de pokemon que é fraco contra.
    forte_contra (str): define o tipo de pokemon que é forte contra.
    """

    def atacar(self, pokemon: Pokemon) -> None:
        """
        Método responsável por realizar o ataque no oponente do seu pokemon
        baseando-se de acordo com sua força total calculada.
        :param pokemon: Pokemon que vai sofrer o ataque.
        :type pokemon: Pokemon

        :raise AssertionError: Parâmetro não é um objeto de pokemon.

        :return: None
        :rtype: None
        """
        super().atacar(pokemon)
        dano_ataque = self.ataque
        print(
            f'Pikachu usou o choque do TROVÃO!!! no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque


class Magicarpa(PokemonAgua):
    """
    Classe concreta pokemon Magicarpa que herda da classe PokemonAgua.

    Atributos:
    nivel (int): Nível do pokemon.
    vida (float): Vida do pokemon.
    ataque_base (int): dano base de ataque do pokemon.
    estrategia_luta (AtaqueStrategy): Estrategia de ataque, variando de acordo
    com o oponente.

    Atributos de classe:
    tipo (str): define o tipo do pokemon.
    fraqueza (str): define o tipo de pokemon que é fraco contra.
    forte_contra (str): define o tipo de pokemon que é forte contra.
    """

    def atacar(self, pokemon: Pokemon) -> None:
        """
        Método responsável por realizar o ataque no oponente do seu pokemon
        baseando-se de acordo com sua força total calculada.
        :param pokemon: Pokemon que vai sofrer o ataque.
        :type pokemon: Pokemon

        :raise AssertionError: Parâmetro não é um objeto de pokemon.

        :return: None
        :rtype: None
        """
        super().atacar(pokemon)
        dano_ataque = self.ataque
        print(
            f'Magicarpa deu uma cuspida fraca :/ no {pokemon.__class__.__name__} e removeu {dano_ataque} pontos de vida')
        pokemon.vida -= dano_ataque


class PokemonFactory:
    """
    Classe fábrica de pokemon responsável por gerar pokemons a serem
    capturados por inimigos e jogadores.
    """

    @staticmethod
    def get_pokemon(nome: str = None, nivel: int = None) -> Pokemon:
        """
        Método responsável por retornar um pokemon aleatório ou
        de acordo com os parâmetros passados.

        :param nome: Nome do pokemon desejado. (opcional)
        :type nome: str
        :param nivel: Nível do pokemon desejado. (opcional)
        :type nivel: int

        :return: Retorna o pokemon aleatorio ou de acordo com os parâmetros.
        :rtype: Pokemon
        """
        nivel_aleatorio = nivel or random.randint(1, 100)
        pokemon = nome or random.choice(
            ['onix', 'charmander', 'magicarpa', 'pikachu'])

        if pokemon.lower() == 'onix':
            return Onix(nivel_aleatorio)
        if pokemon.lower() == 'charmander':
            return Charmander(nivel_aleatorio)
        if pokemon.lower() == 'magicarpa':
            return Magicarpa(nivel_aleatorio)
        if pokemon.lower() == 'pikachu':
            return Pikachu(nivel_aleatorio)
