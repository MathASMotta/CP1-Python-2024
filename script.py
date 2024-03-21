import csv #importando a biblioteca para manipular o csv

# Lista dos dos titulos
diretores = []

# Lista com os paises dos titulos
pais = []

# Lista com a duração de cada titulo
duracao = []

def extrair_dados(arquivo_csv):
    with open(arquivo_csv, 'r', encoding='utf-8') as csvfile:
        leitor_csv = csv.DictReader(csvfile)

        for linha in leitor_csv:
            diretores.append(linha['director'])
            pais.append(linha['country']) 
            duracao.append(linha['duration']) 

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
        quarto_caractere = elemento[3] if len(elemento) > 3 else None
        decimo_terceiro_caractere = elemento[12] if len(elemento) > 12 else None
        lista_quarto.append(quarto_caractere)
        lista_decimo_terceiro.append(decimo_terceiro_caractere)
    
    contador(lista_quarto)
    contador(lista_decimo_terceiro)

def quantidade_caracteres(lista):
    print("Quantidade de caracteres:")
    for elemento in lista:
        #elemento_tratado = elemento.replace(' ', '')
        quantidade = len(elemento)
        print(f"{elemento}: {quantidade}")

# Chamada da função para extrair as informações do arquivo 'netflix_titles.csv'
titulos_netflix = extrair_dados('netflix_titles.csv')

# Chamada da função para extrair a quantidade de 'country'
contador(pais)

# Chamada da função para extrair a quantidade de 'duration'
contador(duracao)

# Chamada da função para extrair o quarto e o décimo-terceiro caractere de 'director'
caracteres(diretores)

# Chamada da função para extrair a quantidade dos caracteres de 'director'
quantidade_caracteres(diretores)
