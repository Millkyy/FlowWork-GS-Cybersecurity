# Usuário autenticado (extraído do token/JWT)
current_user = {"id": 50, "nome": "João", "team_id": 10, "role": "leader"}

dashboards = {
    10: {"team_id": 10, "score": 82, "risco_burnout": "baixo"},
    11: {"team_id": 11, "score": 95, "risco_burnout": "alto"},
}

def get_dashboard_vulneravel(requested_team_id: int):
    # VULNERÁVEL: não verifica se o usuário pertence ao time solicitado
    return dashboards.get(requested_team_id)

# "Ataque": João (time 10) acessando dashboard do time 11
print("Dashboard acessado (indev.):", get_dashboard_vulneravel(11))
