from tika import parser
import re
import csv
import io
import pandas
import os
import json
from datetime import datetime
from datetime import timedelta

menu = [["" for k in range(5)] for w in range(49)]

# Sopas s.joao
if os.path.isfile('./sopas.txt'):
    with open("sopas.txt", "r") as myfile:
        teste = myfile.read()

    teste = teste.lstrip()
    teste = teste.rstrip()
    teste = teste.split("ALMOÇO")
    for i in range(1, len(teste)):
        teste[i] = teste[i].replace(" Sopa Legumes passada", "SOSOSO")
        teste[i] = teste[i].replace(" Sopa Legumes", "SOSOSO")
        teste[i] = teste[i].split("SOSOSO")
        for j in range(0, len(teste[i])):
            teste[i][j] = teste[i][j].splitlines()
            # print(teste[i][j])

    for i in range(1, 8):
        menu[7 * (i - 1)][0] = teste[i][0][4]
        menu[7 * (i - 1)][1] = teste[i][1][1]
        menu[7 * (i - 1) + 1][0] = teste[i][1][3]
        menu[7 * (i - 1) + 1][1] = teste[i][2][1]
elif os.path.isfile('./sopas.xlsx'):
    teste = pandas.ExcelFile('sopas.xlsx')
    folha = pandas.read_excel(teste, 0)
    for i in range(1, 8):
        menu[7 * (i - 1)][0] = folha.iloc[3*i+2][1]
        menu[7 * (i - 1)][1] = folha.iloc[3*i+2][3]
        menu[7 * (i - 1) + 1][0] = folha.iloc[3*i+3][1]
        menu[7 * (i - 1) + 1][1] = folha.iloc[3*i+3][3]

# Prato s. joao
if os.path.isfile('./pratos.txt'):
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
            i += 1
        j += 1
    sentido = int(input("que sentido usar? 0=normal, 1=reverso   "))
    if sentido == 0:
        for i in range(1, len(texto)):
            for j in range(1, len(texto[i])):
                k = 0
                for l in range(0, len(texto[i][j])):
                    if len(texto[i][j][l]) > 2:
                        if texto[i][j][l][0] == " " and texto[i][j][l].lstrip()[0].isupper() and k < 2:
                            #print("i: " + str(i) + " j: " + str(j) + " k: " + str(k))
                            # print(texto[i][j][l].lstrip())
                            if j == 4:
                                menu[7 * (i-1) + j + 1][0] = texto[i][j][l].lstrip()
                            else:
                                menu[7 * (i-1) + j + 1][k] = texto[i][j][l].lstrip()
                            k += 1
    elif sentido == 1:
        for i in range(1, len(texto)):
            for j in range(1, len(texto[i])):
                k = 0
                for l in range(0, len(texto[i][j])):
                    if len(texto[i][j][l]) > 2:
                        if texto[i][j][l][0] == " " and texto[i][j][l].lstrip()[0].isupper() and k < 2:
                            #print("i: " + str(i) + " j: " + str(j) + " k: " + str(k))
                            # print(texto[i][j][l].lstrip())
                            if j == 4:
                                menu[7 * (i-1) + j + 1][0] = texto[i][j][l].lstrip()
                            else:
                                menu[7 * (i-1) + j+1][1 - k] = texto[i][j][l].lstrip()
                            k += 1
    else:
        print("you fool, só se pode responder 0 ou 1!!!")

# SASUP
if os.path.isfile('./sasup.txt'):
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
    semana = int(input("que semana de SASUP imprimir?   ")) - 1

    for i in range(0, len(texto)):
        for j in range(0, len(texto[i])):
            k = 0
            for l in range(0, len(texto[i][j])):
                #print("i= "+ str(i)+" out of "+str(len(texto)))
                #print("j= "+ str(j)+" out of "+str(len(texto[i]) - 1))
                #print("l= "+ str(l)+" out of "+str(len(texto[i][j])))
                if len(texto[i][j][l]) > 2:
                    # print(texto[i][j][l])
                    if texto[i][j][l][0] == " " and texto[i][j][l].lstrip(
                    )[0].isupper():
                        cont += 1
                        # print(cont)
                        # print(texto[i][j][l])
                        #print("i=" + str(i) + "; j=" + str(j) + "; k=" + str(l))
                        # print(ementa[i][j][k])
                        # print(texto[i][j][k])
                        ementa[i][j][k] = texto[i][j][l].lstrip()
                        #print("semana " + str(i) + " dia " + str(k) + " prato " + str(j))
                        # print(texto[i][j][k])
                        k += 1

    for dia in range(0, 5):
        menu[7 * dia][2] = ementa[semana][0][dia]
        menu[7 * dia + 2][2] = ementa[semana][1][dia]
        menu[7 * dia + 3][2] = ementa[semana][2][dia]
        menu[7 * dia + 6][2] = ementa[semana][3][dia]

# EuRest
if os.path.isfile('./rest.txt'):
    with io.open("rest.txt", 'r', encoding='utf8') as myfile:
        teste = myfile.read()
    teste = teste.splitlines()

    for i in range(0, 5):
        menu[7 * i + 2][4] = teste[4 * i + 1]
        menu[7 * i + 3][4] = teste[4 * i + 2]
        menu[7 * i + 6][4] = teste[4 * i + 3]

# OUTPUT EXCEL
with open("output_t.csv", "w+", newline='', encoding='cp1252') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=';')
    csvWriter.writerows(menu)
# OUTPUT JSON
datainicio = str(input("qual o primeiro dia da semana, formato AAAA-MM-DD?   "))

cardap = []

for m in range(6,-1,-1):
    if m < 5:
        datax = datetime(int(datainicio[:4]),int(datainicio[5:7]),int(datainicio[8:19])) + timedelta(days=m)
        datax = datax.strftime("%Y-%m-%d")
        cardap = cardap + [{'date': datax, "locations":[\
            {"name":"Refeitório HSJ", "meals":[\
            {"name":"Almoço","soup":[menu[7*m+0][0],menu[7*m+1][0]],"meat":[menu[7*m+2][0]],"fish":[menu[7*m+3][0]],"diet":[menu[7*m+4][0]],"vegie":[menu[7*m+6][0]],"opti":[menu[7*m+5][0]]},\
            {"name":"Jantar","soup":[menu[7*m+0][1],menu[7*m+1][1]],"meat":[menu[7*m+2][1]],"fish":[menu[7*m+3][1]],"diet":[menu[7*m+4][1]],"vegie":[menu[7*m+6][1]]}\
            ]},\
            {"name":"Cantina UP", "meals":[\
            {"name":"Almoço","soup":[menu[7*m+0][2]],"meat":[menu[7*m+2][2]],"fish":[menu[7*m+3][2]],"vegie":[menu[7*m+6][2]]}\
            ]},\
            {"name":"Health Bar", "meals":[\
            {"name":"Almoço","soup":"O HEALTH","meat":"não fornece","fish":"a ementa","vegie":"É uma pena"}\
            ]},\
            {"name":"Yellow Bar & restCIM", "meals":[\
            {"name":"Almoço","meat":[menu[7*m+2][4]],"fish":[menu[7*m+3][4]],"vegie":[menu[7*m+6][4]]}\
            ]}\
            ]},]
    else:
        datax = datetime(int(datainicio[:4]),int(datainicio[5:7]),int(datainicio[8:19])) + timedelta(days=m)
        datax = datax.strftime("%Y-%m-%d")
        cardap = cardap + [{'date': datax, "locations":[\
            {"name":"Refeitório HSJ", "meals":[\
            {"name":"Almoço","soup":[menu[7*m+0][0],menu[7*m+1][0]],"meat":[menu[7*m+2][0]],"fish":[menu[7*m+3][0]],"diet":[menu[7*m+4][0]],"vegie":[menu[7*m+6][0]],"opti":[menu[7*m+5][0]]},\
            {"name":"Jantar","soup":[menu[7*m+0][1],menu[7*m+1][1]],"meat":[menu[7*m+2][1]],"fish":[menu[7*m+3][1]],"diet":[menu[7*m+4][1]],"vegie":[menu[7*m+6][1]]}\
            ]}]}]


with open('novo.json', 'w', encoding='utf-8') as fp:
    json.dump(cardap, fp, ensure_ascii=False)