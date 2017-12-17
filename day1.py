import utility

def sum_duplicates(data):
    duplicates = 0
    numbers = utility.convert_to_int(data)
    size = len(numbers)

    for i in range(0, size-1):
        if numbers[i] == numbers[i+1]:
            duplicates = duplicates + numbers[i]

    if numbers[size-1] == numbers[0]:
        duplicates = duplicates + numbers[0]

    return duplicates


def main():
    print(sum_duplicates(utility.read_input('input1.txt')))

if __name__ == '__main__':
    main()