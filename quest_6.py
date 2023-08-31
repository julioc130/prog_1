turno = input("Em qual turno você estuda? (M - Matutino, V - Vespertino, N - Noturno): ")

if turno == "M" or turno == "m":
    print("Bom dia! ")
elif turno == "V" or turno == "v":
    print("Boa tarde! ")
elif turno == "N" or turno == "n":
    print("Boa noite! ")
else:
    print("Opção inválida. Por favor, escolha entre M, V ou N.")