import utility
import re

def remove_garbage(stream):
    stream = re.sub('!.', '', stream)
    delete = False
    new_stream = []
    for index in range(0, len(stream)):
        char = stream[index]
        if not delete and char != '<':
            new_stream.append(char)
        if char == '<':
            delete = True
        elif char == '>':
            delete = False

    return new_stream

def group_score(data):
    stream = remove_garbage(data)
    current_score = 0
    total_score = 0
    for char in stream:
        if char == '{':
            current_score = current_score + 1
        elif char == '}':
            total_score = total_score + current_score
            current_score = current_score - 1
    return total_score

def main():
    print(group_score(utility.read_input('input9.txt')))

if __name__ == '__main__':
    main()