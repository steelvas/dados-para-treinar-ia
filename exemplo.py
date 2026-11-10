"""Simulação: entregar o serviço e guardar dados são operações distintas."""

base_treinamento = []

def prestar_servico(solicitacao):
    resultado = "análise entregue"
    base_treinamento.append(solicitacao)
    return resultado

pedido = {"texto": "Exemplo fictício"}
print(prestar_servico(pedido))
print("Registros guardados para treinamento:", len(base_treinamento))
