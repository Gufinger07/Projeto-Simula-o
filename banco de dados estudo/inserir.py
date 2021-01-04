import sqlite3
import random


def qtdregistros():
    sql = "SELECT * from tb_equipes"
    cursor.execute(sql)
    registros = cursor.fetchall()
    qtd = len(registros)
    return qtd

conexao = sqlite3.connect("TimesBR.db")
cursor = conexao.cursor()
sql = "insert into tb_equipes(equipe, pontos, sg) values(?,?,?)"
g = 32
lista_times = [
    ('Grêmio', random.randint(0,90), 0),
    ('Vasco', random.randint(0,90), 0),
    ('Botafogo', random.randint(0,90), 0),
    ('Internacional', random.randint(0,90), 0),
    ('Chapecoense', random.randint(0,90), 0),
    ('Cruzeiro', random.randint(0,90), 0),
    ('Corinthians', random.randint(0,90), 0),
    ('Flumisense', random.randint(0,90), 0),
    ('Atlético MG', random.randint(0,90), 0),
    ('Atlhetico Pr', random.randint(0,90), 0),
    ('Avaí', random.randint(0,90), 0),
    ('Flamengo', random.randint(0,90), 0),
    ('Palmeiras', random.randint(0,90), 0),
    ('Santos', random.randint(0,90), 0),
    ('Bahia', random.randint(0,90), 0),
    ('Ceará', random.randint(0,90), 0),
    ('Fortaleza', random.randint(0,90), 0),
    ('Csa', random.randint(0,90), 0),
    ('São Paulo', random.randint(0,90), 0),
    ('Goiás', random.randint(0,90), 0)

]


cursor.executemany(sql, lista_times)
conexao.commit()
print("Dado inserido com sucesso!!")
print(f"Quantidade de registros: {qtdregistros()}")
cursor.close()
conexao.close()
print()
