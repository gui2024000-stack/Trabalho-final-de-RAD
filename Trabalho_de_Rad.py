import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# ==========================
# BANCO DE DADOS
# ==========================

conn = sqlite3.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER,
    categoria TEXT,
    status TEXT DEFAULT 'Disponível'
)
""")

conn.commit()

# ==========================
# FUNÇÕES
# ==========================

def limpar_campos():
    entry_titulo.delete(0, tk.END)
    entry_autor.delete(0, tk.END)
    entry_ano.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)

def carregar_livros():
    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    for livro in livros:
        tree.insert("", tk.END, values=livro)

    atualizar_contador()

def atualizar_contador():
    cursor.execute("SELECT COUNT(*) FROM livros")
    total = cursor.fetchone()[0]
    lbl_total.config(text=f"Total de livros: {total}")

def adicionar_livro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    ano = entry_ano.get()
    categoria = entry_categoria.get()

    if titulo == "" or autor == "":
        messagebox.showwarning(
            "Atenção",
            "Preencha Título e Autor."
        )
        return

    cursor.execute("""
    INSERT INTO livros(titulo, autor, ano, categoria)
    VALUES (?, ?, ?, ?)
    """, (titulo, autor, ano, categoria))

    conn.commit()

    carregar_livros()
    limpar_campos()

def selecionar_livro(event):
    item = tree.focus()

    if not item:
        return

    dados = tree.item(item, "values")

    limpar_campos()

    entry_titulo.insert(0, dados[1])
    entry_autor.insert(0, dados[2])
    entry_ano.insert(0, dados[3])
    entry_categoria.insert(0, dados[4])

def atualizar_livro():
    item = tree.focus()

    if not item:
        messagebox.showwarning(
            "Aviso",
            "Selecione um livro."
        )
        return

    dados = tree.item(item, "values")
    id_livro = dados[0]

    cursor.execute("""
    UPDATE livros
    SET titulo=?, autor=?, ano=?, categoria=?
    WHERE id=?
    """,
    (
        entry_titulo.get(),
        entry_autor.get(),
        entry_ano.get(),
        entry_categoria.get(),
        id_livro
    ))

    conn.commit()

    carregar_livros()
    limpar_campos()

def excluir_livro():
    item = tree.focus()

    if not item:
        messagebox.showwarning(
            "Aviso",
            "Selecione um livro."
        )
        return

    dados = tree.item(item, "values")
    id_livro = dados[0]

    resposta = messagebox.askyesno(
        "Confirmar",
        "Deseja excluir este livro?"
    )

    if resposta:
        cursor.execute(
            "DELETE FROM livros WHERE id=?",
            (id_livro,)
        )

        conn.commit()
        carregar_livros()
        limpar_campos()

def emprestar_livro():
    item = tree.focus()

    if not item:
        return

    dados = tree.item(item, "values")
    id_livro = dados[0]

    cursor.execute("""
    UPDATE livros
    SET status='Emprestado'
    WHERE id=?
    """, (id_livro,))

    conn.commit()
    carregar_livros()

def devolver_livro():
    item = tree.focus()

    if not item:
        return

    dados = tree.item(item, "values")
    id_livro = dados[0]

    cursor.execute("""
    UPDATE livros
    SET status='Disponível'
    WHERE id=?
    """, (id_livro,))

    conn.commit()
    carregar_livros()

def pesquisar():
    termo = entry_pesquisa.get()

    for item in tree.get_children():
        tree.delete(item)

    cursor.execute("""
    SELECT * FROM livros
    WHERE titulo LIKE ?
    """, ('%' + termo + '%',))

    resultados = cursor.fetchall()

    for livro in resultados:
        tree.insert("", tk.END, values=livro)

# ==========================
# INTERFACE
# ==========================

janela = tk.Tk()
janela.title("Sistema de Biblioteca")
janela.geometry("900x600")

titulo = tk.Label(
    janela,
    text="Sistema de Biblioteca",
    font=("Arial", 18, "bold")
)
titulo.pack(pady=10)

frame_form = tk.Frame(janela)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Título").grid(row=0, column=0)
entry_titulo = tk.Entry(frame_form, width=30)
entry_titulo.grid(row=0, column=1)

tk.Label(frame_form, text="Autor").grid(row=1, column=0)
entry_autor = tk.Entry(frame_form, width=30)
entry_autor.grid(row=1, column=1)

tk.Label(frame_form, text="Ano").grid(row=2, column=0)
entry_ano = tk.Entry(frame_form, width=30)
entry_ano.grid(row=2, column=1)

tk.Label(frame_form, text="Categoria").grid(row=3, column=0)
entry_categoria = tk.Entry(frame_form, width=30)
entry_categoria.grid(row=3, column=1)

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

tk.Button(
    frame_botoes,
    text="Adicionar",
    command=adicionar_livro
).grid(row=0, column=0, padx=5)

tk.Button(
    frame_botoes,
    text="Atualizar",
    command=atualizar_livro
).grid(row=0, column=1, padx=5)

tk.Button(
    frame_botoes,
    text="Excluir",
    command=excluir_livro
).grid(row=0, column=2, padx=5)

tk.Button(
    frame_botoes,
    text="Emprestar",
    command=emprestar_livro
).grid(row=0, column=3, padx=5)

tk.Button(
    frame_botoes,
    text="Devolver",
    command=devolver_livro
).grid(row=0, column=4, padx=5)

frame_pesquisa = tk.Frame(janela)
frame_pesquisa.pack(pady=10)

tk.Label(frame_pesquisa, text="Pesquisar Título").pack(side=tk.LEFT)

entry_pesquisa = tk.Entry(frame_pesquisa)
entry_pesquisa.pack(side=tk.LEFT, padx=5)

tk.Button(
    frame_pesquisa,
    text="Buscar",
    command=pesquisar
).pack(side=tk.LEFT)

tk.Button(
    frame_pesquisa,
    text="Mostrar Todos",
    command=carregar_livros
).pack(side=tk.LEFT, padx=5)

colunas = (
    "ID",
    "Título",
    "Autor",
    "Ano",
    "Categoria",
    "Status"
)

tree = ttk.Treeview(
    janela,
    columns=colunas,
    show="headings",
    height=15
)

for coluna in colunas:
    tree.heading(coluna, text=coluna)
    tree.column(coluna, width=130)

tree.pack(fill="both", expand=True, padx=10)

tree.bind("<<TreeviewSelect>>", selecionar_livro)

lbl_total = tk.Label(
    janela,
    text="Total de livros: 0",
    font=("Arial", 12, "bold")
)

lbl_total.pack(pady=10)

carregar_livros()

janela.mainloop()

conn.close()