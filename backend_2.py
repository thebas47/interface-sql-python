import sqlite3

# Caminho para o banco de dados
database = "clientes.db"

# Função para conectar ao banco
def connect():
    return sqlite3.connect(database)

# Inicializa o banco (executado no início da aplicação)
def init_db():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            sobrenome TEXT,
            email TEXT,
            cpf TEXT
        )
    """)
    conn.commit()
    conn.close()

# Insere um novo cliente
def insert(nome, sobrenome, email, cpf):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO clientes VALUES (NULL, ?, ?, ?, ?)", (nome, sobrenome, email, cpf))
    conn.commit()
    conn.close()

# Retorna todos os registros
def view():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes")
    rows = cur.fetchall()
    conn.close()
    return rows

# Busca registros com base em qualquer campo
def search(nome="", sobrenome="", email="", cpf=""):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM clientes WHERE
        nome = ? OR sobrenome = ? OR email = ? OR cpf = ?
    """, (nome, sobrenome, email, cpf))
    rows = cur.fetchall()
    conn.close()
    return rows

# Atualiza um cliente existente
def update(id, nome, sobrenome, email, cpf):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        UPDATE clientes
        SET nome = ?, sobrenome = ?, email = ?, cpf = ?
        WHERE id = ?
    """, (nome, sobrenome, email, cpf, id))
    conn.commit()
    conn.close()

# Deleta um cliente
def delete(id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()


# Executa a criação do banco se este arquivo for rodado diretamente
if __name__ == "__main__":
    init_db()
