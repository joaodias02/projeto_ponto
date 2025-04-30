class Ponto
    def__init__(self,id_ponto,id_funcionario,data,hora_entrada,hora_saida,observacao)
        self.id_ponto = id_ponto
        self.id_funcionario = id_funcionario
        self.data = data
        self.hora_entrada = hora_entrada
        self.hora_sai = hora_saida
        self.observacao = observacao

    def horas_trab(self):
        horas_trab = self.hora_saida - self.hora_entrada
        return horas_trab