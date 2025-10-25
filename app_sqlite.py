"""
Avaliação – Python + SQLite
Tema: CRUD em 'alunos'

O que o script deve fazer:
1) Criar 'escola.db'
2) Criar tabela 'alunos' -> Seguindo o diagrama
3) Inserir registros na tabela alunos
4) Listar todos
5) Buscar por id
6) Atualizar registros
7) Deletar registros

"""

import sqlite3

# Passo 1 - CONECTAR/CRIAR o banco 
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# PAsso 2 Criar tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               idade INTEGER,
               email TEXT
               )''')
print ('Tabela criada com sucesso!')

# # Passo 3 - INSERIR dados
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Luiz Davi', 18,'luizindugrau@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Emanoelly Miranda', 17,'manuzinha15@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Adja Camilly', 23,'adjazinha00@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Danilo Ferreira', 21,'df060615@gmail.com'))
cursor.execute('INSERT INTO alunos(nome, idade, email) VALUES(?,?,?)',
               ('Brenda', 19,'Breh1515@gmail.com'))
conn.commit()
print("Dados segue tudo ok e pronto!!")

# PAsso 4 - LISTAR TODOS
print("Lista de cadastro dos aluno")
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

#Passo 5 - Atualizar um registro
cursor.execute('UPDATE alunos SET email = ? WHERE id = ?',
               ('luizmiguel18100@gmail.com', 1 ))
conn.commit()

print("Após a alteração ")
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Passo 6- Deletar um registro
cursor.execute('DELETE FROM alunos WHERE id = ? ',(5,))
conn.commit()

print('Após o id deletado')
cursor.execute('SELECT * FROM alunos')
for linha in cursor.fetchall():
    print(linha)
print()

# Encerrar a conexão
conn.close()
