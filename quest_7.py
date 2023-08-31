respostas_positivas = 0

print("responda 'sim' ou 'não' para as seguintes perguntas: ")
if input ("Telefonou para a vítima? "). lower() == "sim"
respostas_positivas += 1
if input ("Esteve no local do crime? ").lower() == "sim"
respostas_positivas += 1
if input ("Mora perto da vitima? ").lower() == "sim"
respostas_positivas += 1
if input ("Devia para a vítima? ").lower () == "sim"
respostas_positivas += 1
if input ("Já trabalhou com a vítima? ").lower() == "sim"
respostas_positivas += 1

if resposta_positiva == 2:
    print("classificação: suspeita")
elif 3 <= respostas_positivas <= 4:
    print("classificação: cumplice")
elif respostas_positivas == 5:
    print("classificação: assasino")
else
    print("classificação: inocente")

