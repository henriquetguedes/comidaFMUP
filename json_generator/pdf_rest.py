from tika import parser
import re
import csv
import io

menu = [["" for k in range(5)] for w in range(49)]

###EuRest
with io.open("rest.txt", 'r', encoding='utf8') as myfile:
    teste = myfile.read()
teste = teste.splitlines()

for i in range(0, 5):
    menu[7 * i + 2][4] = teste[4 * i + 1]
    menu[7 * i + 3][4] = teste[4 * i + 2]
    menu[7 * i + 6][4] = teste[4 * i + 3]

### OUTPUT
#with open("output_r.csv", "w+", newline='', encoding='cp1252') as my_csv:
#   csvWriter = csv.writer(my_csv, delimiter=';')
#  csvWriter.writerows(menu)
