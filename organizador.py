"""
Organizador de Arquivos por Extensão

Este script organiza automaticamente todos os arquivos de um diretório,
movendo-os para pastas baseadas na sua extensão (ex.: .txt, .pdf).

Autor: Jhonny Marcelo de Oliveira
Data: Julho/2025
"""



import os  # Importa o módulo 'os' para interagir com o sistema operacional

# Altera o diretório de trabalho para a pasta que será organizada
os.chdir(r"C:\Users\JhonnyOliveira\Downloads")

# Cria uma lista com os nomes dos arquivos, convertidos para minúsculo
# Isso evita duplicação de pastas como 'TXT' e 'txt'
lista_arquivos = [
    arquivo.lower()
    for arquivo in os.listdir()
    if os.path.isfile(arquivo)  # Filtra apenas arquivos, ignorando subpastas
]

# Gera um conjunto (set) com os tipos de arquivo (extensões) encontrados
lista_tipos = {
    tipo.split('.')[-1]  # Pega o texto após o último ponto (a extensão)
    for tipo in lista_arquivos
}

# Cria uma pasta para cada tipo de arquivo, caso não exista
for tipo in lista_tipos:
    if os.path.exists(tipo):
        pass  # Se a pasta já existe, não faz nada
    else:
        os.mkdir(tipo)  # Cria a nova pasta com o nome da extensão

# Move cada arquivo para a pasta correspondente ao seu tipo
for arquivo in lista_arquivos:
    pasta_destino = arquivo.split('.')[-1]  # Define a pasta com base na extensão
    de = os.path.join(os.getcwd(), arquivo)  # Caminho atual do arquivo
    para = os.path.join(os.getcwd(), pasta_destino, arquivo)  # Caminho de destino
    if os.path.exists(de):
        os.replace(de, para)  # Move o arquivo para a pasta correspondente