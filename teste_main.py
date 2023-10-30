import unittest
from main import *

CHAMANDO_BIA = "audios/bia.wav"
CHAMANDO_OUTRO_NOME = "audios/carolina_pesquisar_receitas.wav"
COMANDO_PESQUISAR_RECEITAS = "audios/bia_pesquisar_receitas.wav"
COMANDO_INSTRUCOES_PREPARO = "audios/bia_como_preparar_lasanha.wav"
COMANDO_LISTAR_INGREDIENTES = "audios/bia_igredientes_pizza.wav"
COMANDO_CRIA_RECEITA = "audios/bia_cria_uma_receita.wav"
COMANDO_ENCERRAR_PROGRAMA = "audios/bia_encerrar_programa.wav"


class TesteNomeAssistente(unittest.TestCase):
    def setUp(self):
        iniciar()

    def testar_reconhecer_nome(self):
        comando = processar_audio_do_comando(CHAMANDO_BIA)
        comando = comando.split()
        nome_assistente = ""
        if len(comando):
            nome_assistente = comando[0].lower()
            print(f"nome do assistente: {nome_assistente}")
        self.assertIn("bia", nome_assistente)

    def testar_nao_reconhecer_outro_nome(self):
        comando = processar_audio_do_comando(CHAMANDO_OUTRO_NOME)
        comando = comando.split()
        nome_assistente = ""
        if len(comando):
            nome_assistente = comando[0].lower()
            print(f"nome do assistente: {nome_assistente}")
        self.assertNotIn("bia", nome_assistente)


class TestePesquisarReceitas(unittest.TestCase):
    def setUp(self):
        iniciar()

    def testar_pesquisar_receitas(self):
        comando = processar_audio_do_comando(COMANDO_PESQUISAR_RECEITAS)
        print(f"comando reconhecido: {comando}")
        acao = processar_comando(comando)
        self.assertEqual(acao, "pesquisar receitas")


class TesteListarIngredientes(unittest.TestCase):
    def setUp(self):
        iniciar()

    def testar_listar_ingredientes(self):
        comando = processar_audio_do_comando(COMANDO_LISTAR_INGREDIENTES)
        print(f"comando reconhecido: {comando}")
        acao = processar_comando(comando)
        self.assertEqual(acao, "listar ingredientes")


class TesteInstrucoesPreparo(unittest.TestCase):
    def setUp(self):
        iniciar()

    def testar_instrucoes_preparo(self):
        comando = processar_audio_do_comando(COMANDO_INSTRUCOES_PREPARO)
        print(f"comando reconhecido: {comando}")
        acao = processar_comando(comando)
        self.assertEqual(acao, "obter instruções de preparo")


class TesteCriaReceitas(unittest.TestCase):
    def setUp(self):
        iniciar()

    def testar_cria_receitas(self):
        comando = processar_audio_do_comando(COMANDO_CRIA_RECEITA)
        print(f"comando reconhecido: {comando}")
        acao = processar_comando(comando)
        self.assertEqual(acao, "gerar receitas aleatórias")


class TesteEncerrar(unittest.TestCase):
    def setUp(self):
        iniciar()

    def testar_encerrar(self):
        comando = processar_audio_do_comando(COMANDO_ENCERRAR_PROGRAMA)
        print(f"comando reconhecido: {comando}")
        acao = processar_comando(comando)
        self.assertEqual(acao, "encerrar")


if __name__ == "__main__":
    carregador = unittest.TestLoader()
    testes = unittest.TestSuite()
    testes.addTest(carregador.loadTestsFromTestCase(TesteNomeAssistente))
    testes.addTest(carregador.loadTestsFromTestCase(TestePesquisarReceitas))
    testes.addTest(carregador.loadTestsFromTestCase(TesteInstrucoesPreparo))
    testes.addTest(carregador.loadTestsFromTestCase(TesteInstrucoesPreparo))
    testes.addTest(carregador.loadTestsFromTestCase(TesteCriaReceitas))
    testes.addTest(carregador.loadTestsFromTestCase(TesteEncerrar))
    executor = unittest.TextTestRunner()
    executor.run(testes)
