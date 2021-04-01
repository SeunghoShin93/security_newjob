import csv


result = []
with open('C:\pjt\mypjt\schedules/minhyeokdb.csv', 'r', encoding='utf-8') as input:
    data = csv.reader(input)
    for row in data:
        result.append(row)



def data():
    return result
