import sqlite3
conexao = sqlite3.connect('bd.sqlite3')
cursor = conexao.cursor()
sql = '''

INSERT INTO cadastro (nome, cpf, endereco, usuario, celular, email, senha)
VALUES ('alissonr', '12343234546', 'rua do caraif', 'caraisoÔf', '23994345693', 'alis@ali', 'abacaxiverd');

'''
cursor.execute(sql)
conexao.commit()
conexao.close()
