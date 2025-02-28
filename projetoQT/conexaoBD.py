import mysql.connector
def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "meu banco"
    )

def adicionar_user (login , senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT usuario (email, senha_hash)VALUES (%S, SHA(%S,256))"
    valores = (login, senha)
    cursor.execute(sql , valores)
    conexao.commit()
    cursor.close()
    conexao.close()