from tika import parser
import re
import csv

menu = [["" for k in range(4)] for w in range(49)]

###Sopas s.joao


###Prato s. joao

with open("pratos.txt", "r") as myfile:
    texto = myfile.read()

texto = texto.replace("Segunda", "SOSOSO")
texto = texto.replace("Terça", "SOSOSO")
texto = texto.replace("Quarta", "SOSOSO")
texto = texto.replace("Quinta", "SOSOSO")
texto = texto.replace("Sexta", "SOSOSO")
texto = texto.replace("Sábado", "SOSOSO")
texto = texto.replace("Domingo", "SOSOSO")

texto = texto.split("SOSOSO")

j = 0
while j < len(texto):
    texto[j] = texto[j].replace("CARNE", "BLABLAB")
    texto[j] = texto[j].replace("PEIXE", "BLABLAB")
    texto[j] = texto[j].replace("DIETA", "BLABLAB")
    texto[j] = texto[j].replace("OPÇÃO", "BLABLAB")
    texto[j] = texto[j].replace("VEGET.", "BLABLAB")

    texto[j] = texto[j].split("BLABLAB")

    i = 0
    while i < len(texto[j]):
        texto[j][i] = texto[j][i].splitlines()
        #print(str(i),"\n")
        #print(texto[j][i][2])
        i += 1
    j += 1

#for i in range(0,len(texto[1])):
#    print(texto[1][i])

for i in range(0, 7):
    for k in range(0, 5):
        if texto[i + 1][k + 1][3].lstrip() != "":
            menu[7 * i + 2 + k][0] = texto[i + 1][k + 1][2].lstrip()
            menu[7 * i + 2 + k][1] = texto[i + 1][k + 1][3].lstrip()

### OUTPUT
with open("output_p.csv", "w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=';')
    csvWriter.writerows(menu)
