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

def menu_listar(lista_livros):
    print("Lista de Livros")
    if len(lista_livros) == 0:
        print("Nenhum livro cadastrado.")
    else: 
        for livro in lista_livros:
            print(f"Título: {livro['titulo']} | Autor: {livro['autor']} | Status: {livro['status']}")

def menu_ordenar(lista_livros):
    print("Ordenar Livros")
    print("A - Por título | B - Por Autor | C - Por Ano")
    ordem = input("Escolha a ordenação: ").upper()

    if ordem == 'A':
        lista_livros.sort(key=lambda x: x['titulo'])
        print("Livros ordenados por título!")
    elif ordem == 'B':
        lista_livros.sort(key=lambda x: x['autor'])
        print("Livros ordenados por autor!")
    elif ordem == 'C':
        lista_livros.sort(key=lambda x: x['ano'])
        print("Livros ordenados por ano!")
    else:
        print("Opção inválida")

def principal():
    arquivo_csv = "livros.csv"
    lista_livros = carregar_dados(arquivo_csv)

    while True:
        print("Sistema de Gerenciamento de Biblioteca")
        print("1 - Cadastrar livro")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("4 - Listar livros")
        print("5 - Buscar livro")
        print("6 - Ordenar livros")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_cadastrar(lista_livros)
        elif opcao == "2":
            menu_emprestar(lista_livros)
        elif opcao == "3":
            menu_devolver(lista_livros)
        elif opcao "4":
            menu_listar(lista_livros)
        elif opcao "5":
            print("Buscar livro")
            termo = input("Digite o título ou autor: ")
            resultados = buscar_livros(lista_livros, termo)
            if len(resultados) == 0:
                print("Nenhum livro encontrado.")
            else:
                print("Resultados encontrados:")
                for livro in resultados:
                    print(f"- {livro['titulo']} ({livro['autor']}) - {livro['status']}") 
        elif opcao == "6":
            menu_ordenar(lista_livros)
        elif opcao == "0":
            salvar_dados(lista_livros, arquivo_csv)
            print("Dados salvos com sucesso. Saindo do sistema...")
            break 
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    principal()       
    
