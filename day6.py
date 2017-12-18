import math


def allocation(mem_bank):
    hash_bank = []
    realloc_counter = 0
    new_hash = -1
    while new_hash not in hash_bank:
        hash_bank.append(new_hash)
        to_alloc = find_max(mem_bank)
        max_index = to_alloc[0]
        max_element = to_alloc[1]
        new_array = realloc(mem_bank, max_element, max_index)
        new_hash = generate_hash(new_array)
        realloc_counter = realloc_counter + 1
    # return realloc_counter this was the first part
    return loop_size(new_hash, mem_bank)


def loop_size(repeated_hash, mem_bank):
    loop_counter = 0
    new_hash = -1
    while new_hash != repeated_hash:
        to_alloc = find_max(mem_bank)
        max_index = to_alloc[0]
        max_element = to_alloc[1]
        new_array = realloc(mem_bank, max_element, max_index)
        new_hash = generate_hash(new_array)
        loop_counter = loop_counter + 1
    return loop_counter


def generate_hash(array):
    hash_val = 0
    for i in range(0, len(array)):
        hash_val = hash_val + (array[i] * 11)/math.exp(i)
    return hash_val % 16


def deep_copy(array):
    new_list = []
    for element in array:
        new_list.append(element)
    return new_list


def realloc(mem_bank, blocks, start_index):
    mem_bank[start_index] = 0
    current_index = start_index + 1
    end = len(mem_bank)

    while blocks > 0:
        if current_index == end:
            current_index = 0
        mem_bank[current_index] = mem_bank[current_index] + 1
        blocks = blocks - 1
        current_index = current_index + 1

    return mem_bank


def find_max(arr):
    # returns max; first returned value is index, second is element
    max_element = float('-Inf')
    index = -1
    for i in range(0, len(arr)):
        element = arr[i]
        if element > max_element:
            max_element = element
            index = i
    return [index, max_element]


def main():
    input = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
    print(allocation(input))


if __name__ == '__main__':
    main()