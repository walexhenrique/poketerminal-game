import unittest
from ataque import AtaqueComFraqueza, AtaqueComForca, AtaqueNormal


class TestAtaqueComFraqueza(unittest.TestCase):
    def setUp(self) -> None:
        self.ataque_com_fraqueza = AtaqueComFraqueza()

    def test_verificando_se_o_calcular_ataque_retorna_um_numero_int_ou_float(self):
        self.assertIsInstance(self.ataque_com_fraqueza.calcular_ataque(valor_ataque_base=10, level_atual=2), (float, int))


class TestAtaqueComForca(unittest.TestCase):
    def setUp(self) -> None:
        self.ataque_com_forca = AtaqueComForca()

    def test_verificando_se_o_calcular_ataque_retorna_um_numero_int_ou_float(self):
        self.assertIsInstance(self.ataque_com_forca.calcular_ataque(valor_ataque_base=10, level_atual=2), (float, int))


class TestAtaqueNormal(unittest.TestCase):
    def setUp(self) -> None:
        self.ataque_normal = AtaqueNormal()

    def test_verificando_se_o_calcular_ataque_retorna_um_numero_int_ou_float(self):
        self.assertIsInstance(self.ataque_normal.calcular_ataque(valor_ataque_base=10, level_atual=2), (float, int))
