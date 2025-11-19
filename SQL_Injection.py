import sqlite3

def buscar_tarefas_seguro(team_id: int, search_term: str):
    conn = sqlite3.connect("flowwork.db")
    cur = conn.cursor()

    # SEGURO: uso de parâmetros (prepared statement)
    query = """
        SELECT id, titulo, status
        FROM tarefas
        WHERE team_id = ?
        AND titulo LIKE ?
    """
    cur.execute(query, (team_id, f"%{search_term}%"))
    rows = cur.fetchall()
    conn.close()
    return rows

team_id = 10
resultado_seguro = buscar_tarefas_seguro(team_id, "lavagem")
print("Tarefas retornadas (seguro):", resultado_seguro)
