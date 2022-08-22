from ataque import (AtaqueComForca, AtaqueComFraqueza, AtaqueNormal,
                    AtaqueStrategy)
from pokemon import Pokemon


class Batalha:
    """
    Classe responsável por organizar e realizar a batalha
    entre dois pokemons diferentes.

    Atributos:
        participante1 (Pokemon): Pokemon do jogador que vai batalhar.
        participante2 (Pokemon): Pokemon do inimigo que o jogador vai batalhar    
    """

    def __init__(self, pokemon: Pokemon, pokemon2: Pokemon) -> None:
        self.participante1: Pokemon = pokemon
        self.participante2: Pokemon = pokemon2

        self.participante1.mudar_estrategia_para_luta(
            self.definir_vantagens(pokemon, self.participante2))
        self.participante2.mudar_estrategia_para_luta(
            self.definir_vantagens(pokemon2, self.participante1))

    @staticmethod
    def definir_vantagens(pokemon1: Pokemon, pokemon2: Pokemon) -> AtaqueStrategy:
        """
        Método responsável por definir a estrategia de ataque de determinado 
        pokemon baseando no seu tipo e no tipo do pokemon inimigo.

        :param pokemon1: Pokemon que vai atacar.
        :type pokemon1: Pokemon
        :param pokemon2: Pokemon que vai enfrentar o pokemon1.
        :type pokemon2: Pokemon

        :return: Retorna uma classe do tipo AtaqueStrategy de acordo com os tipos dos pokemons
        :rtype: AtaqueStrategy
        """
        print()
        if pokemon1.fraqueza == pokemon2.tipo:
            print(f'{pokemon1} está em desvantagem na luta contra {pokemon2}')
            return AtaqueComFraqueza()

        if pokemon1.forte_contra == pokemon2.tipo:
            print(f'{pokemon1} está em vantagem na luta contra {pokemon2}')
            return AtaqueComForca()

        print(
            f'Parece que o/a {pokemon1} não tem nenhuma vantagem sobre {pokemon2}')
        return AtaqueNormal()

    def _restaurar_pokemons(self) -> None:
        """ Método privado para a recuperação da vida dos pokemons pós luta."""
        self.participante1.recuperar_vida()
        self.participante2.recuperar_vida()

    def batalhar(self) -> str:
        """
        Método responsável por realizar a batalha entre os dois pokemons, quem levar a vida do seu oponente
        para zero leva a vitória, após isso é feita a recuperação dos pokemons envolvidos.

        :return: Retorna uma str que especifica se foi o player ou o inimigo que ganhou a batalha.
        :rtype: str
        """
        while True:
            print('-' * 100)
            print(
                f'Vida do seu pokemon: {self.participante1}: {round(self.participante1.vida, 2)}')
            print(
                f'Vida de {self.participante2}: {round(self.participante2.vida, 2)}')

            self.participante1.atacar(self.participante2)

            if self.participante2.vida <= 0:
                print(self.participante1, 'é o vencedor')
                self._restaurar_pokemons()
                return 'Player'

            self.participante2.atacar(self.participante1)

            if self.participante1.vida <= 0:
                print(self.participante2, 'é o vencedor')
                self._restaurar_pokemons()
                return 'Inimigo'
