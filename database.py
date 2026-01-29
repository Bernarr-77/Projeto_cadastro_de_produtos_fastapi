import sqlite3

conexao = sqlite3.connect("database.db")

cursor = conexao.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            quantidade INTERGER,
            valor REAL 
            )
''')
conexao.commit()
conexao.close()
