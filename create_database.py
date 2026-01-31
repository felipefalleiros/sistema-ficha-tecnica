import sqlite3

conexao = sqlite3.connect('database.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS insumos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    peso REAL NOT NULL,
    custo_grama REAL NOT NULL
)
""")

conexao.commit()
conexao.close()

print('Banco e tabela criados com sucesso!')
