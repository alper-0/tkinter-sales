from conexao import conectar
from datetime import datetime


def listar_produtos():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id_produtos, nome, valor FROM produtos")
        produtos = cursor.fetchall()
        cursor.close()
        conexao.close()
        return produtos
    
    return []
    

def listar_clientes():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id_cliente, nome FROM cliente ORDER BY id_cliente")
        clientes = cursor.fetchall()
        cursor.close()
        conexao.close()
        return clientes
    return []

def listar_funcionarios():
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT id_funcionarios, nome FROM funcionarios ORDER BY id_funcionarios")
        funcionarios = cursor.fetchall()
        cursor.close()
        conexao.close()
        # move funcionario id=1 para primeira posição
        funcionarios.sort(key=lambda x: 0 if x[0] == 1 else 1)
        return funcionarios
    return []


def inserir_vendas(produto, quantidade, valor, funcionario, cliente):
    now = datetime.now()
    data = now.strftime("%Y-%m-%d %H:%M:%S")

    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO vendas (id_produto, quantidade, valor_compra, id_funcionario, id_cliente, data_venda) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (produto, quantidade, valor, funcionario, cliente, data)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()



listar_produtos()
