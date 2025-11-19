import sqlite3

def buscar_tarefas(team_id: int, search_term: str):
    conn = sqlite3.connect("flowwork.db")
    cur = conn.cursor()

    # VULNERÁVEL: concatenação direta de dados externos na query
    query = f"""
        SELECT id, titulo, status
        FROM tarefas
        WHERE team_id = {team_id}
        AND titulo LIKE '%{search_term}%'
    """
    print("Executando:", query)
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

# "Ataque": manipula o termo de busca para quebrar o WHERE
team_id = 10
search_term_malicioso = "%' OR '1'='1"
resultado = buscar_tarefas(team_id, search_term_malicioso)
print("Tarefas retornadas (ataque):", resultado)
