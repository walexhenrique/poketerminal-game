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

import unittest

from ataque import AtaqueNormal
from pokemon import (Charmander, Magicarpa, Onix, Pikachu, Pokemon,
                     PokemonAgua, PokemonEletrico, PokemonFactory, PokemonFogo,
                     PokemonPedra)


class TestPokemon(unittest.TestCase):
    def setUp(self) -> None:
        self.nivel_pokemon = 5
        self.pokemon = Pokemon(nivel=self.nivel_pokemon)

    def test_pokemon_attr_nivel_tem_o_valor_correto(self):
        self.assertEqual(self.pokemon.nivel, self.nivel_pokemon)

    def test_pokemon_attr_vida_tem_o_valor_correto_de_acordo_com_o_nivel(self):
        self.assertEqual(self.pokemon.vida, self.nivel_pokemon * 10)

    def test_pokemon_attr_ataque_base_tem_o_valor_correto_de_acordo_com_o_nivel(self):
        self.assertEqual(self.pokemon.ataque_base, self.nivel_pokemon * 4)

    def test_pokemon_attr_estrategia_luta_foi_inicializado_com_objeto_ataque_normal(self):
        self.assertIsInstance(self.pokemon.estrategia_luta, AtaqueNormal)

    def test_atacar_deve_levantar_assertion_caso_o_parametro_nao_seja_um_pokemon(self):
        with self.assertRaises(AssertionError):
            self.pokemon.atacar('pokemon')

    def test_mudar_estrategia_para_luta_deve_levantar_assertion_caso_o_argumento_passado_nao_seja_do_tipo_ataque_strategy(self):
        with self.assertRaises(AssertionError):
            self.pokemon.mudar_estrategia_para_luta('estrategia')

    def test_ataque_retorna_o_valor_de_ataque_em_float(self):
        self.assertIsInstance(self.pokemon.ataque, float)

    def test_recuperar_vida_esta_restaurando_a_vida_corretamente_de_acordo_com_o_seu_level(self):
        vida_completa_pokemon = self.pokemon.vida
        self.pokemon.vida -= 20
        self.pokemon.recuperar_vida()
        self.assertEqual(vida_completa_pokemon, self.pokemon.vida)

    def test_subir_nivel_deve_aumentar_o_attr_nivel_do_pokemon(self):
        nivel_antes_de_subir = self.pokemon.nivel
        self.pokemon.subir_nivel()
        self.assertEqual(nivel_antes_de_subir + 2, self.pokemon.nivel)

    def test_reconfigurar_status_deve_reconfigurar_todos_os_attr_de_acordo_com_o_novo_nivel(self):
        vida_antes_pokemon = self.pokemon.vida
        ataque_base_antes_pokemon = self.pokemon.ataque_base
        self.pokemon.subir_nivel()
        self.assertNotEqual(self.pokemon.vida, vida_antes_pokemon)
        self.assertNotEqual(self.pokemon.ataque_base,
                            ataque_base_antes_pokemon)


class TestPokemonAgua(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_agua = PokemonAgua(5)

    def test_pokemon_agua_attr_tipo_esta_definido_como_atributo_de_classe_corretamente(self):
        self.assertEqual(self.pokemon_agua.tipo, 'AGUA')

    def test_pokemon_agua_attr_fraqueza_como_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_agua.fraqueza, 'ELETRICO')

    def test_pokemon_agua_attr_forte_contra_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_agua.forte_contra, 'FOGO')


class TestPokemonFogo(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_fogo = PokemonFogo(5)

    def test_pokemon_fogo_attr_tipo_esta_definido_como_atributo_de_classe_corretamente(self):
        self.assertEqual(self.pokemon_fogo.tipo, 'FOGO')

    def test_pokemon_fogo_attr_fraqueza_como_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_fogo.fraqueza, 'AGUA')

    def test_pokemon_fogo_attr_forte_contra_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_fogo.forte_contra, 'PEDRA')


class TestPokemonEletrico(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_eletrico = PokemonEletrico(5)

    def test_pokemon_eletrico_attr_tipo_esta_definido_como_atributo_de_classe_corretamente(self):
        self.assertEqual(self.pokemon_eletrico.tipo, 'ELETRICO')

    def test_pokemon_eletrico_attr_fraqueza_como_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_eletrico.fraqueza, 'PEDRA')

    def test_pokemon_eletrico_attr_forte_contra_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_eletrico.forte_contra, 'AGUA')


class TestPokemonPedra(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_pedra = PokemonPedra(5)

    def test_pokemon_pedra_attr_tipo_esta_definido_como_atributo_de_classe_corretamente(self):
        self.assertEqual(self.pokemon_pedra.tipo, 'PEDRA')

    def test_pokemon_pedra_attr_fraqueza_como_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_pedra.fraqueza, 'AGUA')

    def test_pokemon_pedra_attr_forte_contra_atributo_de_classe_esta_definido_corretamente(self):
        self.assertEqual(self.pokemon_pedra.forte_contra, 'ELETRICO')


class TestOnix(unittest.TestCase):
    def setUp(self) -> None:
        self.onix = Onix(5)

    def test_atacar_esta_removendo_a_vida_do_outro_pokemon_ao_realizar_o_ataque(self):
        pokemon_apanha = Pokemon(5)
        pokemon_apanha_vida_antes_da_luta = pokemon_apanha.vida
        self.onix.atacar(pokemon_apanha)
        self.assertGreater(pokemon_apanha_vida_antes_da_luta,
                           pokemon_apanha.vida)


class TestCharmander(unittest.TestCase):
    def setUp(self) -> None:
        self.charmander = Charmander(5)

    def test_atacar_esta_removendo_a_vida_do_outro_pokemon_ao_realizar_o_ataque(self):
        pokemon_apanha = Pokemon(5)
        pokemon_apanha_vida_antes_da_luta = pokemon_apanha.vida
        self.charmander.atacar(pokemon_apanha)
        self.assertGreater(pokemon_apanha_vida_antes_da_luta,
                           pokemon_apanha.vida)


class TestPikachu(unittest.TestCase):
    def setUp(self) -> None:
        self.pikachu = Pikachu(5)

    def test_atacar_esta_removendo_a_vida_do_outro_pokemon_ao_realizar_o_ataque(self):
        pokemon_apanha = Pokemon(5)
        pokemon_apanha_vida_antes_da_luta = pokemon_apanha.vida
        self.pikachu.atacar(pokemon_apanha)
        self.assertGreater(pokemon_apanha_vida_antes_da_luta,
                           pokemon_apanha.vida)


class TestMagicarpa(unittest.TestCase):
    def setUp(self) -> None:
        self.magicarpa = Magicarpa(5)

    def test_atacar_esta_removendo_a_vida_do_outro_pokemon_ao_realizar_o_ataque(self):
        pokemon_apanha = Pokemon(5)
        pokemon_apanha_vida_antes_da_luta = pokemon_apanha.vida
        self.magicarpa.atacar(pokemon_apanha)
        self.assertGreater(pokemon_apanha_vida_antes_da_luta,
                           pokemon_apanha.vida)


class TestPokemonFactory(unittest.TestCase):
    def test_get_pokemon_esta_retornando_um_objeto_do_tipo_pokemon(self):
        self.assertIsInstance(PokemonFactory.get_pokemon(), Pokemon)
