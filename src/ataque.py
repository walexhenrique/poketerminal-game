import random
from abc import ABC, abstractmethod


class AtaqueStrategy(ABC):
    """Class Interface de ataque"""
    @abstractmethod
    def calcular_ataque(self, valor_ataque_base: float,
                        level_atual: int) -> float: pass


class AtaqueComFraqueza(AtaqueStrategy):
    """ Classe com estrategia de ataque com valor reduzido """

    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float:
        """
        Método responsável por calcular o dano de ataque baseando no nível
        do pokemon e um valor aleatório gerado,
        com uma considerada desvantagem.

        :param valor_ataque_base: Valor de dano de ataque base do pokemon.
        :type valor_ataque_base: float or int
        :param level_atual: Nível atual do pokemon que vai atacar.
        :type level_atual: int

        :return: Retorna o dano de ataque que ele vai realizar.
        :rtype: float
        """
        fator_sorte = random.random()
        return (valor_ataque_base - (valor_ataque_base * 0.25) + level_atual) * fator_sorte


class AtaqueNormal(AtaqueStrategy):
    """ Classe com estrategia de ataque com valor normal """

    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float:
        """
        Método responsável por calcular o dano de ataque baseando no nível do
        pokemon e um valor aleatório gerado,
        sem qualquer vantagem ou desvantagem.

        :param valor_ataque_base: Valor de dano de ataque base do pokemon.
        :type valor_ataque_base: float or int
        :param level_atual: Nível atual do pokemon que vai atacar.
        :type level_atual: int

        :return: Retorna o dano de ataque que ele vai realizar.
        :rtype: float
        """
        fator_sorte = random.random()
        return (valor_ataque_base + level_atual) * fator_sorte


class AtaqueComForca(AtaqueStrategy):
    """ Classe com estrategia de ataque com valor potencializado """

    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float:
        """
        Método responsável por calcular o dano de ataque baseando no nível do
        pokemon e um valor aleatório gerado. com uma considerada vantagem.

        :param valor_ataque_base: Valor de dano de ataque base do pokemon.
        :type valor_ataque_base: float or int
        :param level_atual: Nível atual do pokemon que vai atacar.
        :type level_atual: int

        :return: Retorna o dano de ataque que ele vai realizar.
        :rtype: float
        """
        fator_sorte = random.random()
        return (valor_ataque_base + (valor_ataque_base * 0.45) + level_atual) * fator_sorte
