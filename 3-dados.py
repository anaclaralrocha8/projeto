import sqlite3

# 1- Conectando no BD
conexao = sqlite3.connect('titulo.db')

cursor = conexao.cursor()

# 2-Inserindo Dados
cursor.execute(
    """
        INSERT INTO livro(nome, ano, nota)
        VALUES ('catecismo da igreja católica', 2022, 9.5)
    """
)

conexao.commit()
conexao.close()