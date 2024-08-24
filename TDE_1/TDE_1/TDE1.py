#Andressa de Oliveira Barros - BCC turma U - noite

from itertools import product #biblioteca para fazer a operacao produto cartesiano
def diferenca(conjunto_um, conjunto_dois):
     return conjunto_um.difference(conjunto_dois)

def uniao(conjunto_um, conjunto_dois):
    return conjunto_um.union(conjunto_dois)

def interseccao(conjunto_um, conjunto_dois):
    return conjunto_um.intersection(conjunto_dois)

def produto_cartesiano(conjunto_um, conjunto_dois):
    return set(product(conjunto_um, conjunto_dois))

with open("teste_3.txt", "r") as arquivo: #abrir o arquivo txt
    file = arquivo.readlines()
    numero_operacoes = int((file[0]).strip())

ultima_linha = 1 #Variavel para ler as linhas
operacao = file[ultima_linha].strip() #Variavel para saber o tipo de operacao e executar as funcoes

for a in range(ultima_linha):#tentar trocar pra while #a = 0 atualizar esse a

    if ultima_linha == 1:
        try:
            operacao = file[ultima_linha].strip()
            conjunto_um = set(((file[ultima_linha+1]).strip()).split(','))
            conjunto_dois= set(((file[ultima_linha+2]).strip()).split(','))
            ultima_linha = ultima_linha + 3 #É somado 3 na variavel para ir para a proxima operacao do arquivo.txt
            if operacao == 'D':
                print(f"Difrença: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ", diferenca(conjunto_um, conjunto_dois))
            elif operacao == 'U':
                print(f"União: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ", uniao(conjunto_um, conjunto_dois))
            elif operacao == 'I':
                print(f"Intersecção: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ", interseccao(conjunto_um, conjunto_dois))
            elif operacao == 'C':
                print(f"Produto Cartesiano: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ", produto_cartesiano(conjunto_um,conjunto_dois))
        except IndexError: #Para caso não haver o index e não corromper o código
            break

    if ultima_linha == 4:
        try:
            operacao = file[ultima_linha].strip()
            conjunto_um = set(((file[ultima_linha + 1]).strip()).split(','))
            conjunto_dois = set(((file[ultima_linha + 2]).strip()).split(','))
            ultima_linha = ultima_linha + 3
            if operacao == 'D':
                print(f"Difrença: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      diferenca(conjunto_um, conjunto_dois))
            elif operacao == 'U':
                print(f"União: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      uniao(conjunto_um, conjunto_dois))
            elif operacao == 'I':
                print(f"Intersecção: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      interseccao(conjunto_um, conjunto_dois))
            elif operacao == 'C':
                print(f"Produto Cartesiano: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      produto_cartesiano(conjunto_um, conjunto_dois))
        except IndexError:
            break

    if ultima_linha == 7:
        try:
            operacao = file[ultima_linha].strip()
            conjunto_um = set(((file[ultima_linha + 1]).strip()).split(','))
            conjunto_dois = set(((file[ultima_linha + 2]).strip()).split(','))
            ultima_linha = ultima_linha + 3
            if operacao == 'D':
                print(f"Difrença: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      diferenca(conjunto_um, conjunto_dois))
            elif operacao == 'U':
                print(f"União: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      uniao(conjunto_um, conjunto_dois))
            elif operacao == 'I':
                print(f"Intersecção: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      interseccao(conjunto_um, conjunto_dois))
            elif operacao == 'C':
                print(f"Produto Cartesiano: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      produto_cartesiano(conjunto_um, conjunto_dois))
        except IndexError:
            break

    if ultima_linha == 10:
        try:
            operacao = file[ultima_linha].strip()
            conjunto_um = set(((file[ultima_linha + 1]).strip()).split(','))
            conjunto_dois = set(((file[ultima_linha + 2]).strip()).split(','))
            ultima_linha = ultima_linha + 3
            if operacao == 'D':
                print(f"Difrença: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      diferenca(conjunto_um, conjunto_dois))
            elif operacao == 'U':
                print(f"União: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      uniao(conjunto_um, conjunto_dois))
            elif operacao == 'I':
                print(f"Intersecção: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      interseccao(conjunto_um, conjunto_dois))
            elif operacao == 'C':
                print(f"Produto Cartesiano: conjunto 1: {conjunto_um}, conjunto 2: {conjunto_dois}. Resultado: ",
                      produto_cartesiano(conjunto_um, conjunto_dois))
        except IndexError:
            break