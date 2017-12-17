import utility

def find_minmax(arr):
    max = float('-Inf')
    min = float('Inf')

    for num in arr:
        if num > max:
            max = num
        if num < min:
            min = num

    return [min, max]

def checksum(lines):
    checksum = 0

    for line in lines:
        minmax = find_minmax(line)
        min = minmax[0]
        max = minmax[1]
        difference = max - min
        checksum = checksum + difference

    return checksum



def main():
    print(checksum(utility.clean_input(utility.read_by_line('input2.txt'))))

if __name__ == '__main__':
    main()