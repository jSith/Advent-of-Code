import utility


def find_path(target_horizontal, target_vertical):
    current_horizontal = 0
    current_vertical = 0
    steps = []
    while target_horizontal != current_horizontal or target_vertical != current_vertical:
        if target_vertical > current_vertical and target_horizontal < current_horizontal:
            current_vertical = current_vertical + 1
            current_horizontal = current_horizontal - 1
            steps.append('nw')
        elif target_vertical > current_vertical and target_horizontal > current_horizontal:
            current_vertical = current_vertical + 1
            current_horizontal = current_horizontal + 1
            steps.append('ne')
        elif target_vertical > current_vertical:
            if target_vertical - current_vertical >= 2:
                current_vertical = current_vertical + 2
            else:
                current_vertical = current_vertical + 1
            steps.append('n')
        elif target_vertical < current_vertical and target_horizontal > current_horizontal:
            current_vertical = current_vertical - 1
            current_horizontal = current_horizontal + 1
            steps.append('se')
        elif target_horizontal > current_horizontal:
            if target_horizontal - current_horizontal >= 2:
                current_horizontal = current_horizontal + 2
            else:
                current_horizontal = current_horizontal + 1
            steps.append('e')
        elif target_vertical < current_vertical and target_horizontal < current_horizontal:
            current_vertical = current_vertical - 1
            current_horizontal = current_horizontal - 1
            steps.append('sw')
        elif target_vertical < current_vertical:
            if current_vertical - target_vertical >= 2:
                current_vertical = current_vertical - 2
            else:
                current_vertical = current_vertical - 1
            steps.append('s')
        elif target_horizontal < current_horizontal:
            if current_horizontal - target_horizontal >= 2:
                current_horizontal = current_horizontal - 2
            else:
                current_horizontal = current_horizontal - 1
            steps.append('e')
    return steps


def track_child(data):
    directions = data.split(',')
    horizontal_position = 0
    vertical_position = 0
    for direction in directions:
        if direction == 'n':
            vertical_position = vertical_position + 2
        elif direction == 'ne':
            horizontal_position = horizontal_position + 1
            vertical_position = vertical_position + 1
        elif direction == 'e':
            horizontal_position = horizontal_position + 2
        elif direction == 'se':
            horizontal_position = horizontal_position + 1
            vertical_position = vertical_position - 1
        elif direction == 's':
            vertical_position = vertical_position - 2
        elif direction == 'sw':
            horizontal_position = horizontal_position - 1
            vertical_position = vertical_position - 1
        elif direction == 'w':
            horizontal_position = horizontal_position - 2
        else:
            horizontal_position = horizontal_position - 1
            vertical_position = vertical_position + 1

    path = find_path(horizontal_position, vertical_position)
    return len(path)


def main():
    print(track_child(utility.read_input('input_11.txt')))

if __name__ == '__main__':
    main()