import csv

path_vendas = 'C:/Users/victor.costa/PycharmProjects/formulário/venv/dadosvendas.csv'

# Lê CSV e retorna lista
def read_csv(path):
    data = []
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return data

# Escreve lista em CSV
def write_csv(path, data):
    with open(path, 'a', newline='') as csv_file:
        id = 1 if not data else int(data[-1][3]) + 1
        csv.writer(csv_file).writerow([input("Waht's ur name? "), input("What's the matter? "), input("Ur department: "), id, 0, '', ''])

    return id

def write_calling(path, name, depto, problem):
    with open(path, 'a', newline= '') as csv_file:
        data = read_csv(path)
        id = 1 if not data else int(data[-1][3]) + 1
        csv.writer(csv_file).writerow(
            [name, problem, depto, id, 0, '', ''])