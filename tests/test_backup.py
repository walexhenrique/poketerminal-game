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

from backup import Backup
from pessoa import Jogador


class TestBackup(unittest.TestCase):
    def test_verifica_se_ao_carregar_o_backup_ele_retorna_o_objeto_jogador_quando_ja_existe_um_arquivo_data(self):
        # para realizar esse teste, precisa existir o arquivo data.json
        self.assertIsInstance(Backup.carregar_save(), Jogador)
