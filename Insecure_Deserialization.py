import json

def importar_missoes_seguro(json_string: str):
    try:
        dados = json.loads(json_string)
    except json.JSONDecodeError:
        raise ValueError("Arquivo de configuração inválido")

    if not isinstance(dados, list):
        raise ValueError("Esperada lista de missões")

    missoes = []
    for missao in dados:
        if not isinstance(missao, dict):
            raise ValueError("Missão inválida")
        if "nome" not in missao or "pontos" not in missao:
            raise ValueError("Campos obrigatórios ausentes")

        missoes.append({
            "nome": str(missao["nome"]),
            "pontos": int(missao["pontos"])
        })

    print("Missões importadas com segurança:", missoes)
    return missoes

json_missoes = """
[
  {"nome": "Pausa ativa", "pontos": 15},
  {"nome": "Check-in de humor", "pontos": 20}
]
"""
importar_missoes_seguro(json_missoes)
