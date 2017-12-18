import utility


def valid_passphrases(lines):
    valid_count = 0
    for line in lines:
        line = line.split(' ')
        if is_unique(line) and not contains_anagram(line):
            valid_count = valid_count+1
    return valid_count


def is_unique(line):
    unique_words = []
    for word in line:
        if word not in unique_words:
            unique_words.append(word)
        else:
            return False
    return True


def contains_anagram(line):
    for word in line:
        for test_word in line:
            if word != test_word:
                if is_anagram(word, test_word):
                    return True
    return False


def is_anagram(test, word):
    for char in test:
        if char in word:
            word = word.replace(char, '', 1)
        else:
            return False

    if len(word) == 0:
        return True
    else:
        return False


def main():
    print(valid_passphrases(utility.clean_input(utility.read_by_line('input4.txt'), False)))


if __name__ == '__main__':
    main()