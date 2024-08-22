import sqlite3

conexao = sqlite3.connect('banco_sqlite')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
# cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
# cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), email VARCHAR(100));')


# cursor.execute('ALTER TABLE usuarios RENAME TO usuario')

# cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
# cursor.execute('ALTER TABLE gerentes ADD COLUMN endereco VARCHAR(100)')


# cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

# cursor.execute('DROP TABLE produtos')

# cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1, "Ema","Rua benjamin", "ema@gmail.com",33344477)')
# cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(2, "Luz","Av. Pietro", "lu@gmail.com",33344412)')
# cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(3, "Lua","Rua Nete", "lua@gmail.com",3334400)')
# cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(4, "He","Rua Jang", "he@gmail.com",33344111)')

# cursor.execute('INSERT INTO gerentes(id,nome,email) VALUES(4, "He","he@gmail.com")')


# cursor.execute('DELETE FROM usuario where id=4')
# cursos.execute('DELETE FROM clientes WHERE id=1')

# visualizar = cursor.execute('SELECT * FROM usuario')
# visualizar = cursor.execute('SELECT nome FROM usuario')
# cursor.execute('UPDATE usuario SET endereco="Mavael da silva" WHERE nome="Luz"')
# cursor.execute('UPDATE gerentes SET endereco="Rua Jang" WHERE id="4"')
# cursor.execute('UPDATE gerentes SET id="1" WHERE id="4"')


# ORDER BY E DESC
# visualizar = cursor.execute('SELECT * FROM usuario ORDER BY nome')
# visualizar = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC')

# LIMIT E DISTINCT

# visualizar = cursor.execute('SELECT * FROM usuario LIMIT 2')
# visualizar = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 2')

# GROUP BY E HAVING
# GROUP BY NÃO TRABALHA COM WHERE
# visualizar = cursor.execute('SELECT nome, id FROM usuario GROUP BY nome')
#visualizar = cursor.execute('SELECT nome, id FROM usuario GROUP BY nome HAVING id<2')


# JOIN(RIGHT, LEFT, FULL, INNER)
# visualizar = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

# LEFT JOIN 
# visualizar = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')

# RIGHT JOIN 
# visualizar = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.id = gerentes.id')

# FULL JOIN 
# visualizar = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.id = gerentes.id')

# SUB-CONSUlTAS
# visualizar = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome from gerentes)')
for usuario in visualizar:
    print(usuario)



conexao.commit()
conexao.close



