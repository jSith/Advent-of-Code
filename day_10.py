def twist_list(lengths):
    num_list = []
    for i in range(0, 256):
        num_list.append(i)
    current_position = 0
    skip = 0
    for length in lengths:
        num_list = flip_subarray(num_list, current_position, current_position+length)
        current_position = current_position + length + skip
        if current_position > len(num_list):
            current_position = current_position - len(num_list)
        skip = skip + 1
    return num_list[0] * num_list[1]


def flip_subarray(array, start_index, end_index):
    wraparound = 0
    if end_index > len(array):
        wraparound = end_index - len(array)
        end_index = len(array)
    sub_array = array[start_index:end_index]
    sub_array.extend(array[:wraparound])
    sub_array = list(reversed(sub_array))
    i = 0
    for i in range(0, len(sub_array)-wraparound):
        array[i+start_index] = sub_array[i]
    k = 0
    i = i + 1
    for j in range(i, i+wraparound):
        array[k] = sub_array[j]
        k = k + 1

    return array


def main():
    data = [63, 144, 180, 149, 1, 255, 167, 84, 125, 65, 188, 0, 2, 254, 229, 24]
    print(twist_list(data))


if __name__ == '__main__':
    main()