import utility


def sum_duplicates(data, half):
    duplicates = 0
    numbers = utility.convert_to_int(data)
    size = len(numbers)
    if half:
        offset = int(size/2)
    else:
        offset = 1

    for i in range(0, size-1):
        if (i + offset) > size:
            index = (i+offset) - size
        else:
            index = i + offset

        if index == size:
            index = index - 1

        if i == size:
            i = 0

        if numbers[i] == numbers[index]:
            duplicates = duplicates + numbers[i]

    return duplicates


def main():
    print(sum_duplicates(utility.read_input('input1.txt'), True))

if __name__ == '__main__':
    main()