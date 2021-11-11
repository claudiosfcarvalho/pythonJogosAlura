#Aula 5 - Praticando format
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