import mysql.connector


# Create database connection
def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",      # MySQL user
            password="",      # MySQL password
            database="loja"   # Database name
        )
    except mysql.connector.Error as e:
        print(f"Erro na conexão: {e}")
        return None
