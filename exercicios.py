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