import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS contas_bancarias (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    titular TEXT NOT NULL,
    saldo FLOAT NOT NULL,
    cpf TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
INSERT OR IGNORE INTO contas_bancarias
               (titular, saldo, cpf) VALUES
               ('Renan', 2.00, '12345678900'),
               ('Erique', 128885773.00, '12345678901')
''')

conexao.commit()

cursor.execute(''' 
    SELECT titular, saldo, cpf FROM contas_bancarias

 ''')
contas = cursor.fetchall()
for conta in contas:
    titular, saldo, cpf = conta
    print(f'Titular: {titular} - Saldo: {saldo:.2f}')


conexao.close()