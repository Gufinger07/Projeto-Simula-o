import sqlite3
database = "TimesBR.db"

conexao = sqlite3.connect("TimesBR.db")         #criei a conexao com o bd

cursor = conexao.cursor()       #executar os comandor

cursor.execute("""CREATE TABLE if not exists tb_equipes(
    equipe text,
    pontos integer,
    sg integer 
    )""")

conexao.commit()
cursor.close()
conexao.close()




