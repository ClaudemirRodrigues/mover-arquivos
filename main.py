import os
import shutil

tamanhos = list()
tamanhos_2 = list()
lista = list()

try:
    os.makedirs('./duplicadas')
except FileExistsError:
    pass

if not os.path.exists('./duplicadas'):
    os.makedirs('./duplicadas')

lista = os.listdir('./img')  # varre o diretório e gera uma lista com os nomes dos arquivos
for arquivo in lista:
    dados = list()
    size = os.path.getsize(f'img\\{arquivo}')  # pega o tamanho do arquivo em bytes
    dados.append(arquivo)
    dados.append(size)
    tamanhos.append(dados)  # adiciona o valor a lista
    tamanhos_2 = tamanhos.copy()

flag = 0
for indice in tamanhos_2:
    flag_1 = 0
    for dado in tamanhos:
        if (dado[1] == indice[1]) and (dado[0] != indice[0]):  # verifica se os tamanhos são iguais e se os nomes são diferentes
            source = rf'img\{dado[0]}'  # caso seja, designa as variáveis de diretório
            destination = r'duplicadas'
            try:
                shutil.move(source, destination)  # e move os arquivos
            except shutil.Error:
                pass
            tamanhos[flag_1][1] = 0  # aqui eu altero o valor analisado para não mover os dois arquivos
        flag_1 += 1
    flag += 1
