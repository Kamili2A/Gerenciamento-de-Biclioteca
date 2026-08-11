import csv
import os

def carregar_dados(nome_arquivo):
    biblioteca = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                biblioteca.append(linha)
    return biblioteca 

def salvar_dados(biblioteca, nome_arquivo): 
    with open(nome_arquivo, mode='w', encoding='utf-8', newline='') as arquivo:
        campos = ['titulo', 'autor', 'ano', 'isnb', 'status']
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(biblioteca)
    return True

def buscar_livros(biblioteca, termo_busca):
    resultados = []
    termo_busca = termo_busca.lower()
    for livro in biblioteca:
        if termo_busca in livro['titulo'].lower() or ['autor'].lower():
            resultados.append(livro)
    return resultados

def menu_cadastrar(lista_livros):
    print("Cadastrar novo livro")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano de publicação: ")
    isbn = input("Código/ISBN: ")

    novo_livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'isbn': isbn,
        'status': 'disponível'
    }
    lista_livros.append(novo_livro)
    print("Livro cadastrado com sucesso!")

def menu_emprestar(lista_livros): 
    print("Emprestar Livro")
    isbn_busca = input("Digite o ISBN do livro para emprestar: ")
    encontrado = False
    for livro in lista_livros:
        if livro['status'] == 'disponivel':
        livro['status'] = 'emprestado'
        print("Empréstimo realizado com sucesso!")
    else:
        print("O livro já está emprestado.")
    break 
if not encontrado:
    print("Livro não encontrado.")
    
