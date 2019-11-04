from tika import parser
import re
import csv
import pandas
import os

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

# OUTPUT
with open("output_s.csv", "w+", newline='') as my_csv:
    csvWriter = csv.writer(my_csv, delimiter=';')
    csvWriter.writerows(menu)
