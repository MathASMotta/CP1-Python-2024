import csv #importando a biblioteca para manipular o csv
import pandas as pd

# Listas com os tipos do titulos
tipos_com_a = []
tipos_com_k = []

# Listas com os tipos dos titulos
avaliacoes_com_a = []
avaliacoes_com_k = []

# Listas das descrições dos titulos
descricoes_com_a = []
descricoes_com_k = []

# Lista com os paises dos titulos
pais_com_k = []

# Lista com a duração de cada titulo
duracao_com_k = []

def extrair_dados(arquivo_csv):
    with open(arquivo_csv, 'r', encoding='utf-8') as csvfile:
        leitor_csv = csv.DictReader(csvfile)

        for linha in leitor_csv:
            titulo = linha['title'].lower()
            tipo = linha['type']
            avaliacao = linha['rating']
            descricao = linha['description']
            pais = linha['country']
            duracao = linha['duration']
            if titulo.startswith("a"):
                tipos_com_a.append(tipo)
                avaliacoes_com_a.append(avaliacao)
                descricoes_com_a.append(descricao)
            elif titulo.startswith("k"):
                tipos_com_k.append(tipo)
                avaliacoes_com_k.append(avaliacao)
                descricoes_com_k.append(descricao)
                pais_com_k.append(pais)
                duracao_com_k.append(duracao)

def contador(lista):
    # Dicionário para contar a ocorrência de cada item
    contagem_itens = {}

    # Contagem de cada item
    for item in lista:
        if item in contagem_itens:
            contagem_itens[item] += 1
        else:
            contagem_itens[item] = 1

    # Encontrar o item com a maior quantidade
    maior_quantidade_item = max(contagem_itens, key=contagem_itens.get)

    # Encontrar o item com a menor quantidade
    menor_quantidade_item = min(contagem_itens, key=contagem_itens.get)

    # Imprimir a contagem de cada item
    print("Contagem de cada item:")
    for item, quantidade in contagem_itens.items():
        print(f"{item}: {quantidade}")

    # Imprimir o item com a maior e menor quantidade
    print("\nItem com a maior quantidade:", maior_quantidade_item)
    print("Item com a menor quantidade:", menor_quantidade_item)
    print('')

def caracteres(lista):
    lista_quarto = []
    lista_decimo_terceiro = []

    for elemento in lista:
        elemento_tratado = elemento.replace(' ', '')
        quarto_caractere = elemento_tratado[3] if len(elemento_tratado) > 3 else None
        decimo_terceiro_caractere = elemento_tratado[12] if len(elemento_tratado) > 12 else None
        lista_quarto.append(quarto_caractere)
        lista_decimo_terceiro.append(decimo_terceiro_caractere)
    
    contador(lista_quarto)
    contador(lista_decimo_terceiro)

def quantidade_caracteres(lista):
    print("Quantidade de caracteres:")
    for elemento in lista:
        elemento_tratado = elemento.replace(' ', '')
        quantidade = len(elemento_tratado)
        print(f"{elemento}: {quantidade}")

# Chamada da função para extrair os títulos do arquivo 'netflix_titles.csv'
titulos_netflix = extrair_dados('netflix_titles.csv')

# Chamada da função para extrair a quantidade de 'type'
contador(tipos_com_a)
contador(tipos_com_k)

# Chamada da função para extrair a quantidade de 'rating'
contador(avaliacoes_com_a)
contador(avaliacoes_com_k)

# Chamada da função para extrair a quantidade de 'country'
contador(pais_com_k)

# Chamada da função para extrair a quantidade de 'duration'
contador(duracao_com_k)

caracteres(descricoes_com_a) 

quantidade_caracteres(descricoes_com_a)