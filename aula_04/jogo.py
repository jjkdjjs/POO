import sqlite3

conexao = sqlite3.connect('jogo.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS personagens (
               id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               classe TEXT NOT NULL,
               vida INTEGER NOT NULL,
               ouro INTEGER NOT NULL)

''')

cursor.execute('''
INSERT INTO personagens (nome, classe, vida, ouro) VALUES
                ('Renan', 'Mendigo', 10, 5),
                ('Erique', 'Mago', 100, 1000000000)
''')


cursor.execute('''
SELECT nome, classe, vida, ouro FROM personagens

''')

personagens = cursor.fetchall()
for personagem in personagens:
    nome, classe, vida, ouro = personagem
    print(f'Nome: {nome} - Classe: {classe} - Vida: {vida} - Ouro: {ouro}')

cursor.execute('''
UPDATE personagens SET vida = 0 WHERE id = 7 AND 

''')

conexao.commit()
conexao.close()