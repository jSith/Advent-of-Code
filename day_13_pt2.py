import utility


def parse_input(lines):
    firewall = {}
    for line in lines:
        split_line = line.split(': ')
        layer = int(split_line[0])
        depth = int(split_line[1])
        firewall[layer] = depth
    return firewall


def test_severity(firewall, delay):
    total_severity = 0
    firewall_layers = firewall.keys()
    time = delay
    caught = False

    for position in range(0, max(firewall_layers)+1):
        if position in firewall_layers:
            scanner_range = firewall[position]
            scanner_position = time % (2*scanner_range-2)
            if scanner_position == 0:
                total_severity = total_severity + position * scanner_range
                caught = True
        time = time + 1
    return caught


def minimum_delay(data):
    firewall = parse_input(data)
    delay = 0
    while test_severity(firewall, delay):
        delay = delay + 1
    return delay


def main():
    print(minimum_delay(utility.read_by_line('input_13.txt')))


if __name__ == '__main__':
    main()