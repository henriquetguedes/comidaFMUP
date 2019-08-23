from tika import parser
import re
import csv

menu = [["" for k in range(4)] for w in range(49)]

###Sopas s.joao
raw = parser.from_file('sopas.pdf')
teste = raw['content']
teste = teste.lstrip()
teste = teste.rstrip()
teste = teste.replace("\n\n", "\n")
teste = teste.replace(" Sopa Legumes passada ", "SOSOS")
teste = teste.replace(" Sopa Legumes ", "SOSOS")
teste = teste.splitlines()

i = 0
while i < len(teste):
    lele = str(teste[i])
    lele = lele.split("SOSOS")
    teste[i] = lele
    print(teste[i])
    i += 1

for j in range(0, 7):
    menu[7 * j][0] = teste[3 * j + 1][0]
    menu[7 * j][1] = teste[3 * j + 1][1]
    menu[7 * j + 1][0] = teste[3 * j + 2][0]
    menu[7 * j + 1][1] = teste[3 * j + 2][1]

###Prato s. joao

### OUTPUT
with open("output_s.csv", "w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=';')
    csvWriter.writerows(menu)
