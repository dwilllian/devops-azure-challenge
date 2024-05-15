
import unitteste
import json
from monitoramento import uso_cpu, uso_memoria, uso_disco, atualizacoes_pendentes, estatisticas_sistema

class TesteMonitoramento(unittest.TestCase):

    def teste_uso_cpu(self):
        self.assertIsInstance(uso_cpu(), float)

    def teste_uso_memoria(self):
        memoria = uso_memoria()
        self.assertIsInstance(memoria, dict)
        self.assertIn('total', memoria)
        self.assertIn('disponivel', memoria)
        self.assertIn('percentual', memoria)

    def teste_uso_disco(self):
        disco = uso_disco()
        self.assertIsInstance(disco, dict)
        self.assertIn('total', disco)
        self.assertIn('usado', disco)
        self.assertIn('livre', disco)

    def teste_atualizacoes_pendentes(self):
        atualizacoes = atualizacoes_pendentes()
        self.assertIsInstance(atualizacoes, dict)

    def teste_estatisticas_sistema(self):
        estatisticas = json.loads(estatisticas_sistema())
        self.assertIsInstance(estatisticas, dict)
        self.assertIn('uso_cpu', estatisticas)
        self.assertIn('uso_memoria', estatisticas)
        self.assertIn('uso_disco', estatisticas)
        self.assertIn('atualizacoes_pendentes', estatisticas)
        self.assertIn('estatisticas_dstat', estatisticas)

if __name__ == "__main__":
    unitteste.main()
