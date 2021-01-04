import sqlite3
def delete():
    sql = "delete from tb_equipes"
    cursor.execute(sql)
    conexao.commit()
    print("Dados excluidos com sucesso")



if __name__ == '__main__':
    conexao = sqlite3.connect("TimesBR.db")
    cursor = conexao.cursor()
    delete()
    cursor.close()
    conexao.close()