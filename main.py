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