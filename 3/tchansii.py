str_gamma = ""
str_epsilon = ""


with open('input.txt', 'r') as file:
    lines = file.readlines()

columns = list(zip(*lines))
for i, column in enumerate(columns, start=0):
    nb_of_1s = column.count('1')
    column_size = len(column)
    if(column_size / 2 < nb_of_1s):
        str_gamma += "1"
        str_epsilon += "0"
    else:
        str_gamma += "0"
        str_epsilon += "1"

print(int(str_gamma, 2) * int(str_epsilon, 2))
