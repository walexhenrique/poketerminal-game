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

from ataque import (AtaqueComForca, AtaqueComFraqueza, AtaqueNormal,
                    AtaqueStrategy)
from batalha import Batalha
from pokemon import Charmander, Magicarpa, Onix, Pikachu


class TestBatalha(unittest.TestCase):
    def setUp(self) -> None:
        self.pokemon_onix = Onix(1)
        self.pokemon_magicarpa = Magicarpa(1)
        self.pokemon_pikachu = Pikachu(1)
        self.pokemon_charmander = Charmander(1)
        self.batalha = Batalha(self.pokemon_onix, self.pokemon_magicarpa)

    def test_batalha_attr_participante1_foi_inicializado_corretamente_com_o_seu_pokemon(self):
        self.assertEqual(self.batalha.participante1, self.pokemon_onix)

    def test_batalha_attr_participante2_foi_inicializado_corretamente_com_o_seu_pokemon(self):
        self.assertEqual(self.batalha.participante2, self.pokemon_magicarpa)

    def test_batalha_inicializador_adicionou_corretamente_a_estrategia_luta_do_participante1_da_luta(self):
        self.assertIsInstance(
            self.batalha.participante1.estrategia_luta, AtaqueStrategy)

    def test_batalha_inicializador_adicionou_corretamente_a_estrategia_luta_do_participante2_da_luta(self):
        self.assertIsInstance(
            self.batalha.participante2.estrategia_luta, AtaqueStrategy)

    def test_definir_vantagens_verifica_se_retorna_um_objeto_do_tipo_estrategia_de_ataque(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_onix,
                                                        pokemon2=self.pokemon_magicarpa), AtaqueStrategy)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_pedra_enfrenta_pokemon_agua(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_onix,
                                                        pokemon2=self.pokemon_magicarpa), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_agua_enfrenta_pokemon_eletrico(
            self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_magicarpa,
                                                        pokemon2=self.pokemon_pikachu), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_eletrico_enfrenta_pokemon_pedra(
            self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_pikachu,
                                                        pokemon2=self.pokemon_onix), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_fraqueza_quando_pokemon_fogo_enfrenta_pokemon_agua(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_charmander,
                                                        pokemon2=self.pokemon_magicarpa), AtaqueComFraqueza)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_pedra_enfrenta_pokemon_eletrico(
            self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_onix,
                                                        pokemon2=self.pokemon_pikachu), AtaqueComForca)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_eletrico_enfrenta_pokemon_agua(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_pikachu,
                                                        pokemon2=self.pokemon_magicarpa), AtaqueComForca)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_agua_enfrenta_pokemon_fogo(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_magicarpa,
                                                        pokemon2=self.pokemon_charmander), AtaqueComForca)

    def test_definir_vantagens_verifica_se_retorna_ataque_com_forca_quando_pokemon_fogo_enfrenta_pokemon_pedra(self):
        self.assertIsInstance(Batalha.definir_vantagens(pokemon1=self.pokemon_charmander,
                                                        pokemon2=self.pokemon_onix), AtaqueComForca)

    def test_definir_vantagens_retorna_ataque_normal_quando_um_pokemon_enfrenta_outro_que_o_elemento_nao_interfere(
            self):
        sem_vantagem_no_combate = [(self.pokemon_onix, self.pokemon_onix),
                                   (self.pokemon_onix, self.pokemon_charmander),
                                   (self.pokemon_pikachu, self.pokemon_pikachu),
                                   (self.pokemon_pikachu, self.pokemon_charmander),
                                   (self.pokemon_magicarpa,
                                    self.pokemon_magicarpa),
                                   (self.pokemon_magicarpa, self.pokemon_onix),
                                   (self.pokemon_charmander,
                                    self.pokemon_charmander),
                                   (self.pokemon_charmander, self.pokemon_pikachu)
                                   ]
        for pokemon1, pokemon2 in sem_vantagem_no_combate:
            with self.subTest(pokemon1=pokemon1, pokemon2=pokemon2):
                self.assertIsInstance(Batalha.definir_vantagens(
                    pokemon1=pokemon1, pokemon2=pokemon2), AtaqueNormal)

    def test_batalhar_verifica_se_retorna_player_quando_o_jogador_vence_o_inimigo(self):
        batalha_teste = Batalha(Onix(50), Pikachu(1))
        self.assertEqual(batalha_teste.batalhar(), 'Player')

    def test_batalhar_verifica_se_retorna_inimigo_quando_o_jogador_perde_para_o_inimigo(self):
        batalha_teste = Batalha(Pikachu(1), Onix(50))
        self.assertEqual(batalha_teste.batalhar(), 'Inimigo')

    def test_batalhar_verifica_se_a_vida_dos_pokemons_foi_restaurada_apos_a_luta(self):
        onix = Onix(50)
        pikachu = Pikachu(1)
        vida_pikachu_antes_da_luta = pikachu.vida
        vida_onix_antes_da_luta = onix.vida
        batalha_teste = Batalha(pikachu, onix)
        batalha_teste.batalhar()
        self.assertEqual(vida_pikachu_antes_da_luta,
                         batalha_teste.participante1.vida)
        self.assertEqual(vida_onix_antes_da_luta,
                         batalha_teste.participante2.vida)
