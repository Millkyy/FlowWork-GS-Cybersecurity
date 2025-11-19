import os

def enviar_metricas_vulneravel(team_slug: str):
    # VULNERÁVEL: comando de shell montado com input direto
    cmd = f"python enviar_metricas.py {team_slug}"
    print("Executando:", cmd)
    os.system(cmd)

# Ataque de laboratório
team_slug_malicioso = "time_lavanderia && echo INJETADO_NO_SERVIDOR"
enviar_metricas_vulneravel(team_slug_malicioso)
