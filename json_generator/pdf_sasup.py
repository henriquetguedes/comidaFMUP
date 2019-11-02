from tika import parser
import re
import csv

menu = [["" for k in range(5)] for w in range(49)]

###SASUP

with open("sasup.txt", "r") as myfile:
    texto = myfile.read()

texto = texto.replace("NOTAS", "separatsia")
texto = texto.split("separatsia")

for i in range(0, len(texto)):
    texto[i] = texto[i].replace("SOPA", "BLABLAB")
    texto[i] = texto[i].replace("CARNE", "BLABLAB")
    texto[i] = texto[i].replace("PESCADO", "BLABLAB")
    texto[i] = texto[i].replace("VEGETARIANO 1", "BLABLAB")

    texto[i] = texto[i].split("BLABLAB")
    for x in range(0, len(texto[i]) - 1):
        #print(str(texto[x]) +" "+ str(texto[x+1]))
        texto[i][x] = texto[i][x + 1]

ementa = [[["" for k in range(5)] for j in range(4)] for i in range(4)]

for i in range(0, len(texto)):
    for j in range(0, len(texto[i]) - 1):
        texto[i][j] = texto[i][j].splitlines()

cont = 0
semana = int(input("que semana de SASUP imprimir?")) - 1

for i in range(0, len(texto)):
    for j in range(0, len(texto[i])):
        k =0
        for l in range(0, len(texto[i][j])):
            #print("i= "+ str(i)+" out of "+str(len(texto)))
            #print("j= "+ str(j)+" out of "+str(len(texto[i]) - 1))
            #print("l= "+ str(l)+" out of "+str(len(texto[i][j])))
            if len(texto[i][j][l])>2:
                #print(texto[i][j][l])
                if texto[i][j][l][0] == " " and texto[i][j][l].lstrip()[0].isupper():
                    cont += 1
                    #print(cont)
                    #print(texto[i][j][l])
                    #print("i=" + str(i) + "; j=" + str(j) + "; k=" + str(l))
                    #print(ementa[i][j][k])
                    #print(texto[i][j][k])
                    ementa[i][j][k] = texto[i][j][l].lstrip()
                    #print("semana " + str(i) + " dia " + str(k) + " prato " + str(j))
                    #print(texto[i][j][k])
                    k += 1


for dia in range(0, 5):
    menu [7 * dia][2] = ementa[semana][0][dia]
    menu [7 * dia+2][2] =ementa[semana][1][dia]
    menu [7 * dia+3][2] = ementa[semana][2][dia]
    menu [7 * dia+6][2] = ementa[semana][3][dia]

#print(ementa)
#print(menu)

### OUTPUT
with open("output_sa.csv", "w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=';')
    csvWriter.writerows(menu)
