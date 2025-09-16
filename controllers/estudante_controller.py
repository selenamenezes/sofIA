from utils.db import get_connection
from models.estudante_model import Estudante

def adicionar_estudante(nome, nota1=None, nota2=None, nota3=None):
    media = None
    if nota1 is not None and nota2 is not None and nota3 is not None:
        media = (nota1 + nota2 + nota3) / 3

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO estudantes (nome, nota1, nota2, nota3, media) VALUES (?, ?, ?, ?, ?)",
        (nome, nota1, nota2, nota3, media)
    )
    conn.commit()
    conn.close()


def listar_estudantes():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, nota1, nota2, nota3, media FROM estudantes")
    rows = cursor.fetchall()
    conn.close()
    return [Estudante(*row) for row in rows]
