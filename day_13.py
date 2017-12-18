import utility


def parse_input(lines):
    firewall = {}
    for line in lines:
        split_line = line.split(': ')
        layer = int(split_line[0])
        depth = int(split_line[1])
        firewall[layer] = depth
    return firewall


def test_severity(data):
    firewall = parse_input(data)
    total_severity = 0
    firewall_layers = firewall.keys()

    for position in range(0, max(firewall_layers)+1):
        if position in firewall_layers:
            scanner_range = firewall[position]
            scanner_position = position % (2*scanner_range-2)
            if scanner_position == 0:
                severity = position * scanner_range
                total_severity = total_severity + severity
    return total_severity


def main():
    print(test_severity(utility.read_by_line('input_13.txt')))


if __name__ == '__main__':
    main()