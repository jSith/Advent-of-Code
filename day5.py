import utility


def maze(jumps):
    jump_values = {}
    escape = len(jumps)

    for i in range(0, escape):
        jump_values[i] = jumps[i]

    location = 0
    jump_counter = 0
    while location < escape:
        offset = jump_values.get(location)
        if offset >= 3:
            jump_values[location] = offset - 1
        else:
            jump_values[location] = offset + 1
        location = location + offset
        jump_counter = jump_counter + 1
    return jump_counter


def main():
    print(maze(utility.convert_to_int(utility.read_by_line('input5.txt'))))


if __name__ == '__main__':
    main()