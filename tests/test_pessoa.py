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

from pessoa import Inimigo, InimigoFactory, Jogador, Pessoa
from pokemon import Charmander, Magicarpa, Onix, Pikachu, Pokemon


class TestPessoa(unittest.TestCase):
    def setUp(self) -> None:
        self.pessoa = Pessoa()
        self.pessoa.lista_pokemons = [Pokemon(), Pokemon()]

    def test_capturar_pokemon_deve_levantar_assertion_error_caso_parametro_nao_seja_um_objeto_do_tipo_pokemon(self):
        with self.assertRaises(AssertionError):
            self.pessoa.capturar_pokemon('pokemon')

    def test_capturar_pokemon_deve_adicionar_pokemon_a_lista_de_pokemons_caso_seja_objeto_do_tipo_pokemon(self):
        tamanho_lista = len(self.pessoa.lista_pokemons)
        self.pessoa.capturar_pokemon(Pokemon())
        self.assertEqual(tamanho_lista + 1, len(self.pessoa.lista_pokemons))


class TestInimigo(unittest.TestCase):
    def setUp(self) -> None:
        self.inimigo = Inimigo()

    def test_inimigo_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.inimigo.nome, 'Desconhecido')

    def test_inimigo_attr_lista_pokemons_foi_inicializado_corretamente(self):
        self.assertIsInstance(self.inimigo.lista_pokemons, list)
        self.assertEqual(len(self.inimigo.lista_pokemons), 0)


class TestInimigoFactory(unittest.TestCase):
    def test_verificando_o_retorno_se_e_um_objeto_do_tipo_inimigo(self):
        self.assertIsInstance(InimigoFactory.get_inimigo(), Inimigo)

    def test_verificando_se_os_pokemons_adicionados_ao_objeto_inimigo_sao_realmente_objetos_do_tipo_pokemon(self):
        pokemons = [
            pokemon for pokemon in InimigoFactory.get_inimigo().lista_pokemons]

        for pokemon in pokemons:
            with self.subTest(pokemon=pokemon):
                self.assertIsInstance(pokemon, Pokemon)

    def test_verificando_se_os_pokemons_foram_adicionados_ao_objeto_inimigo(self):
        pokemons = InimigoFactory.get_inimigo().lista_pokemons
        self.assertGreaterEqual(len(pokemons), 1)


class TestJogador(unittest.TestCase):
    def setUp(self) -> None:
        self.jogador = Jogador('walex')
        self.jogador.lista_pokemons = [Onix(20)]
        self.inimigo = Inimigo()
        self.inimigo.lista_pokemons = [Onix(10), Charmander(2)]
        self.pessoa = Pessoa()

    def test_jogador_attr_nome_tem_o_valor_correto(self):
        self.assertEqual(self.jogador.nome, 'walex')

    def test_batalhar_deve_levantar_uma_assertion_error_caso_quem_ele_enfrente_nao_seja_um_objeto_do_tipo_inimigo(self):
        with self.assertRaises(AssertionError):
            self.jogador.batalhar(
                id_pokemon=0, inimigo=self.pessoa, id_pokemon_inimigo=1)

    def test_batalhar_deve_retornar_false_caso_o_id_de_pokemon_nao_seja_um_indice_valido_para_a_lista_pokemons_do_jogador(self):
        indices_invalidos = (-5, -2, -1, len(self.jogador.lista_pokemons) + 1)

        for indice_invalido in indices_invalidos:
            with self.subTest(indice_invalido=indice_invalido):
                self.assertFalse(
                    self.jogador.batalhar(id_pokemon=indice_invalido, inimigo=self.inimigo, id_pokemon_inimigo=1))

    def test_batalhar_conseguiu_realizar_a_batalha_com_sucesso(self):
        self.assertTrue(self.jogador.batalhar(
            id_pokemon=0, inimigo=self.inimigo, id_pokemon_inimigo=1))

    def test_resultado_da_batalha_o_jogador_nao_ganhou_a_batalha(self):
        nivel_pokemon_que_lutou_antes_da_luta = self.jogador.lista_pokemons[0].nivel
        self.jogador._resultado_da_batalha('Inimigo', 0)
        self.assertEqual(nivel_pokemon_que_lutou_antes_da_luta,
                         self.jogador.lista_pokemons[0].nivel)

    def test_resultado_da_batalha_o_jogador_ganhou_a_batalha_upando_assim_o_pokemon(self):
        nivel_pokemon_que_lutou_antes_da_luta = self.jogador.lista_pokemons[0].nivel

        self.jogador._resultado_da_batalha('Player', 0)
        self.assertNotEqual(nivel_pokemon_que_lutou_antes_da_luta,
                            self.jogador.lista_pokemons[0].nivel)
