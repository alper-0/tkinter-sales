from conexao import conectar


def listar_vendas():
    con = conectar()
    cursor = con.cursor()
    cursor.execute("SELECT id, id_cliente, id_funcionario, id_produto, valor_total, data_venda FROM vendas")
    resultado = cursor.fetchall()  # retorna lista de tuplas
    cursor.close()
    con.close()
    return resultado

def excluir_venda(id):
    con = conectar()
    cursor = con.cursor()
    cursor.execute("DELETE FROM vendas WHERE id = %s", (id,))
    con.commit()
    cursor.close()
    con.close()