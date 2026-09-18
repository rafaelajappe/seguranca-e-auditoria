import sqlite3

def conectar_banco():
    # ERRO DE SEGURANÇA 1 (SAST): Credencial exposta no código.
    # O SAST vai detectar a palavra 'password' recebendo uma string fixa.
    db_password = "super_senha_secreta_123"
    print(f"Conectando ao banco de forma insegura com a senha: {db_password}") #mera simulação

def buscar_usuario(nome_usuario):
    # ERRO DE SEGURANÇA 2 (SAST): Risco crítico de SQL Injection.
    conn = sqlite3.connect('banco_exemplo.db')
    cursor = conn.cursor()
    query = "SELECT * FROM usuarios WHERE nome = '" + nome_usuario + "'"
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    conectar_banco()