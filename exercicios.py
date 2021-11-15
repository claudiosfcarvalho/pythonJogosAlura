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
fruta_pedida = input('Qual é a fruta que deseja consultar? ')
if(fruta_pedida in frutas):
    print('Sim, temos a fruta')
else:
    print('Não temos a fruta')

precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026 ]
print(min(precos))
print(len(precos))