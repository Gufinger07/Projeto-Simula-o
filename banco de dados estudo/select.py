import sqlite3
import pandas as pd

def select_all():
    conexao = sqlite3.connect("TimesBR.db")
    cursor = conexao.cursor()
    sql = "SELECT * from tb_equipes"
    cursor.execute(sql)
    registros = cursor.fetchall()

    if len(registros) > 0:
        ct = 0
        for registro in registros:
            print(registro)
            ct += 1

    else:
        print("Lista vazia")
    df = pd.read_sql_query("SELECT * from tb_equipes",conexao)
    print(df.head())
    cursor.close()
    conexao.close()


if __name__ == '__main__':
    select_all()