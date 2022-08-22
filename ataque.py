from abc import ABC, abstractmethod
import random


class AtaqueStrategy(ABC):
    @abstractmethod
    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float: pass


class AtaqueComFraqueza(AtaqueStrategy):
    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float:
        fator_sorte = random.random()
        return (valor_ataque_base - (valor_ataque_base * 0.25) + level_atual) * fator_sorte


class AtaqueNormal(AtaqueStrategy):
    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float:
        fator_sorte = random.random()
        return (valor_ataque_base + level_atual) * fator_sorte


class AtaqueComForca(AtaqueStrategy):
    def calcular_ataque(self, valor_ataque_base: float, level_atual: int) -> float:
        fator_sorte = random.random()
        return (valor_ataque_base + (valor_ataque_base * 0.45) + level_atual) * fator_sorte
