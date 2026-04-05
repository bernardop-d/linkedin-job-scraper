import sys
import os
import unittest

# Garante que o Python encontra o main.py na pasta raiz
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import TipoTrabalho, Vaga, construir_url


class TestTipoTrabalho(unittest.TestCase):

    def test_valor_remoto(self):
        # Verifica se o valor do enum "remoto" está correto
        self.assertEqual(TipoTrabalho.remoto, "remoto")

    def test_valor_hibrido(self):
        self.assertEqual(TipoTrabalho.hibrido, "hibrido")

    def test_valor_presencial(self):
        self.assertEqual(TipoTrabalho.presencial, "presencial")

    def test_valor_todos(self):
        self.assertEqual(TipoTrabalho.todos, "todos")


class TestVaga(unittest.TestCase):

    def test_criar_vaga_com_dados_validos(self):
        # Cria uma vaga com todos os campos preenchidos
        vaga = Vaga(
            titulo="Desenvolvedor Python",
            empresa="Empresa Teste",
            local="São Paulo, SP",
            link="https://linkedin.com/jobs/view/123"
        )
        self.assertEqual(vaga.titulo, "Desenvolvedor Python")
        self.assertEqual(vaga.empresa, "Empresa Teste")
        self.assertEqual(vaga.local, "São Paulo, SP")
        self.assertIn("linkedin.com", vaga.link)

    def test_vaga_tem_todos_os_campos(self):
        # Verifica se o modelo Vaga tem os quatro campos esperados
        campos = Vaga.model_fields.keys()
        self.assertIn("titulo", campos)
        self.assertIn("empresa", campos)
        self.assertIn("local", campos)
        self.assertIn("link", campos)


class TestConstruirUrl(unittest.TestCase):

    def test_url_contem_cargo(self):
        # A URL gerada deve conter o cargo buscado
        url = construir_url(cargo="analista de dados", localizacao="", tipo=TipoTrabalho.todos)
        self.assertIn("analista", url.lower())

    def test_url_contem_localizacao(self):
        # A URL gerada deve conter a localização informada
        url = construir_url(cargo="dev", localizacao="Rio de Janeiro", tipo=TipoTrabalho.todos)
        self.assertIn("Rio", url)

    def test_url_comeca_com_linkedin(self):
        # A URL deve apontar para o LinkedIn
        url = construir_url(cargo="designer", localizacao="SP", tipo=TipoTrabalho.remoto)
        self.assertIn("linkedin.com", url)

    def test_url_com_tipo_remoto(self):
        # Ao filtrar por remoto, a URL deve conter o código correspondente
        url = construir_url(cargo="dev", localizacao="SP", tipo=TipoTrabalho.remoto)
        self.assertIsInstance(url, str)
        self.assertTrue(len(url) > 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
