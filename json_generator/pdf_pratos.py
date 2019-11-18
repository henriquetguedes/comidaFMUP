from tika import parser
import re
import csv

menu = [["" for k in range(5)] for w in range(49)]

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
        #print(texto[j][i])
        texto[j][i] = texto[j][i].splitlines()
        i += 1
    j += 1

for i in range(1, len(texto)):
    for j in range(1, len(texto[i])):
        k = 0
        for l in range(0, len(texto[i][j])):
            if len(texto[i][j][l]) > 2:
                if texto[i][j][l][0] == " " and texto[i][j][l].lstrip()[0].isupper() and k < 2:
                    #print("i: " + str(i) + " j: " + str(j) + " k: " + str(k))
                    #print(texto[i][j][l].lstrip())
                    if j == 4:
                        menu[7 * (i-1) + j+1][0] = texto[i][j][l].lstrip()
                    else:
                        menu[7 * (i-1) + j+1][1-k] = texto[i][j][l].lstrip()
                    k += 1

#print(menu)
### OUTPUT
with open("output_p.csv", "w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=';')
    csvWriter.writerows(menu)
