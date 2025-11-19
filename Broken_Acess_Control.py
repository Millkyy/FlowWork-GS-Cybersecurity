def get_dashboard_seguro(requested_team_id: int, current_user: dict):
    # Admin pode ver qualquer time
    if current_user["role"] == "admin":
        return dashboards.get(requested_team_id)

    # Líder ou membro só podem ver o próprio time
    if requested_team_id != current_user["team_id"]:
        raise PermissionError("Acesso negado ao dashboard de outro time")

    return dashboards.get(requested_team_id)

try:
    print("Dashboard seguro:", get_dashboard_seguro(11, current_user))
except PermissionError as e:
    print("Erro:", e)
