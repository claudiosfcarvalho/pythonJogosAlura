import random
print("Tentativa {} de {}".format(3,10))

print("Tentativa {1} de {0}".format(3,10))

print("R$ {}".format(1.59))

print("R$ {:f}".format(1.59))

print("R$ {:.2f}".format(1.59))

print("R$ {:7.2f}".format(1234.59))

print("R$ {:7.2f}".format(4.59))

print("R$ {:07.2f}".format(4.59))

print("R$ {:09.2f}".format(4.59))

print("R$ {:07d}".format(4))

print("R$ {:7d}".format(4))

print("Data {:2d}/{:2d}".format(19, 11))

nome = "Claudio"
print(f"Meu nome é {nome}")

print(f"Meu nome é {nome.lower()}")

print(f"Meu nome é {nome.upper()}")

print(f"Meu nome é {nome.capitalize()}")

print("numero randomico ",random.random())

print("numero randomico de 0 a 100 ", random.randrange(0, 101))

print("numero randomico de 1 a 100 ", random.randrange(1, 101))

print("numero absoluto  ", abs(-10.8))

print("numero arredondado ", round(10.8))

print("divisao resultado float ", 3/2)

print("divisao resultado float ", 2/2)

#Sempre devolve valor inteiro sem arredondar
print("divisao resultado abs com //  ", 3//2)


def soma(a, b):
    print(f"Funcao SOMA : a ({a}) + b ({b})")
    return a + b

print(f"usando funcao soma 10 + 2 = {soma(10,2)}")

print("bool(0) ", bool(0))

print("bool("") ", bool(""))

print("bool(None) ", bool(None))

print("bool(1) ", bool(1))

print("bool(-100) ", bool(-100))

print("bool(13.5) ", bool(13.5))

print("bool(\"teste\") ", bool("teste"))

print("bool(True) ", bool(True))

# busca a primeira ocorrencia
palavra = "banana"
print(palavra.find("b"))

for letra in palavra:
    print(letra)

print("BANANA".lower())

print("banana".upper())

print("    BANANA   ".strip())

frutas = ['banana', 'maca', 'pera']
# fruta_pedida = input('Qual é a fruta que deseja consultar? ')
# if(fruta_pedida in frutas):
#     print('Sim, temos a fruta')
# else:
#     print('Não temos a fruta')

precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026 ]
print(min(precos))
print(len(precos))

print(precos.count(1200))
teste_range = range(3, 10)
print(teste_range[0],teste_range[1])

dias_da_semana_normal = ['S','T','Q','Q','S','S','D']
print(dias_da_semana_normal)
#lista do tipo tuple
dias_da_semana_imutavel = ('S','T','Q','Q','S','S','D')
print(dias_da_semana_imutavel)
print(len(dias_da_semana_imutavel))

p1 = (3,5)
p2 = (4,6)
p3 = (5,7)
linha = [p1, p2, p3]
print(linha)

#converter lista em tuple e tuple em lista
lista_tuple = tuple(dias_da_semana_normal)
print(lista_tuple)
lista_normal = list(lista_tuple)
print(lista_normal)

#usando set - lista que nao permite numeros repetidos
lista_set = {1,2,3}
print(lista_set)
lista_set.add(1)
print(lista_set)

#set nao possui indice e para acessar usar um for
for item in lista_set:
    print(item)

#dictionary - utiliza as chaves como num set, mas sempre em pares (chave e valor)
instrutores = {'Nico': 39, 'Flavio': 37, 'Marcos': 30}
print(instrutores)

#list comprehension
lista_de_frutas = [fruta.upper() for fruta in frutas]
print(lista_de_frutas)

inteiros = [1,3,4,5,7,8]
lista_quadrados = [n*n for n in inteiros]
print(lista_quadrados)

lista_divisao_por_dois = [n for n in inteiros if n % 2 == 0]
print(lista_divisao_por_dois)

#arquivos com python
#nome arquivo, w - escrita | r - leitura | a - adicionar conteudo | rb - abrir uma imagem (b de binario) e wb para gravar
arquivo = open("palavras.txt","w")
arquivo.write("banana\n")
arquivo.write("laranja\n")
arquivo.write("morango\n")
arquivo.write("melancia\n")
arquivo.write("melao")
print(arquivo)
arquivo.close()