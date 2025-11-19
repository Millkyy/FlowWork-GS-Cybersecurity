import re
import subprocess

def enviar_metricas_seguro(team_slug: str):
    # Allowlist: apenas letras, números, _ e -
    if not re.fullmatch(r"[a-zA-Z0-9_-]+", team_slug):
        raise ValueError("Identificador de time inválido")

    # Execução sem shell, passando args em lista
    cmd = ["python", "enviar_metricas.py", team_slug]
    print("Executando seguro:", cmd)
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    print("Saída:", result.stdout)
    return result.stdout

enviar_metricas_seguro("time_lavanderia")
