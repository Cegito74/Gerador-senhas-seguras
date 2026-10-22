
import unittest
import string

from gerador_senhas import gerar_senha


class TestGeradorSenhas(unittest.TestCase):

    def test_senha_8_caracteres(self):
        senha = gerar_senha(8)
        self.assertEqual(len(senha), 8)

    def test_senha_12_caracteres(self):
        senha = gerar_senha(12)
        self.assertEqual(len(senha), 12)

    def test_senha_16_caracteres(self):
        senha = gerar_senha(16)
        self.assertEqual(len(senha), 16)

    def test_senha_abaixo_do_minimo(self):
        with self.assertRaises(ValueError):
            gerar_senha(5)

    def test_apenas_letras_minusculas(self):
        senha = gerar_senha(
            12,
            usar_maiusculas=False,
            usar_numeros=False,
            usar_especiais=False
        )

        self.assertTrue(senha.islower())
        self.assertTrue(senha.isalpha())

    def test_caracteres_selecionados(self):
        senha = gerar_senha(16)

        self.assertTrue(any(c.islower() for c in senha))
        self.assertTrue(any(c.isupper() for c in senha))
        self.assertTrue(any(c.isdigit() for c in senha))
        self.assertTrue(
            any(c in "!@#$%&*?" for c in senha)
        )

    def test_sem_caracteres_especiais(self):
        senha = gerar_senha(
            12,
            usar_especiais=False
        )

        self.assertTrue(
            all(c in string.ascii_letters + string.digits
                for c in senha)
        )


if __name__ == "__main__":
    unittest.main()
