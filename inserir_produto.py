from conexao import conectar

def inserir_produto(nome, descricao, valor):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO produtos (nome, descricao, valor) VALUES (%s, %s, %s)"
        valores = (nome, descricao, valor)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()