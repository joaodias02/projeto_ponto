import sqlite3
from datetime import datetime

class BancoDeDados:
    def __init__(self, nome_banco='qrcodes.db'):
        self.nome_banco = nome_banco
        self.conectar()

    def conectar(self):
        self.conexao = sqlite3.connect(self.nome_banco)
        self.cursor = self.conexao.cursor()

def registrar_ponto(self, id_funcionario, tipo_registro):
        """Registra entrada ou saída"""
        data_atual = datetime.now().strftime('%Y-%m-%d')
        hora_atual = datetime.now().strftime('%H:%M:%S')
