import sqlite3

def conectar():
    return sqlite3.connect('Locadora.db')
        
def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carros (
            modelo TEXT,
            marca TEXT,
            diaria REAL
        )
    ''')
    conexao.commit()
    conexao.close()

def cadastrar_carro(modelo, marca, diaria):
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO carros VALUES (?, ?, ?)', (modelo, marca, diaria))
    conexao.commit()
    conexao.close()
    print(f"{modelo} cadastrado!")

criar_tabela()
cadastrar_carro("Onix", "Chevrolet", 120.00)
cadastrar_carro("Compass", "Jeep", 250.00)