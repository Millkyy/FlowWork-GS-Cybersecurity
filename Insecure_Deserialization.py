import pickle

def importar_missoes_vulneravel(file_bytes: bytes):
    # VULNERÁVEL: desserializa input arbitrário com pickle
    missoes = pickle.loads(file_bytes)
    print("Missões importadas:", missoes)
    return missoes

# No exemplo abaixo o payload é inocente, mas em produção poderia conter código malicioso
payload = pickle.dumps([{"nome": "Pausa de 5 minutos", "pontos": 10}])
importar_missoes_vulneravel(payload)
