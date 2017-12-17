import re


def read_input(filename):
    path = 'data\\'
    file = open(path+filename, 'r', encoding='UTF-8')
    data = file.read()
    file.close()
    return data


def read_by_line(filename):
    path = 'data\\'
    file = open(path+filename, 'r')
    data = []

    for line in file:
        data.append(line)
    file.close()

    return data


def clean_input(data, convert=True):
    clean_data = []
    for line in data:
        line = re.sub('[\n]', '', line)
        line = re.sub('[ï»¿]', '', line)
        line = line.split('\t')
        if convert:
            clean_data.append(convert_to_int(line))
        else:
            clean_data.extend(line)
    return clean_data


def convert_to_int(data):
    numbers = []
    for char in data:
        numbers.append(int(char))
    return numbers
