import utility


def breadth_first_search(graph, source, destination):
    queue = [source]
    marked = {}

    for vertex in graph.keys():
        marked[vertex] = False

    marked[source] = True

    while queue:
        current = queue.pop(0)
        if current == destination:
            return True
        for neighbor in graph[current]:
            if not marked[neighbor]:
                marked[neighbor] = True
                queue.append(neighbor)
    return False


def parse_input(data):
    graph = {}
    for line in data:
        split = line.split(' <-> ')
        vertex = int(split[0])
        neighbors = utility.convert_to_int(split[1].split(', '))
        graph[vertex] = neighbors
    return graph


def group_size(data):
    graph = parse_input(data)
    zero_group = []

    for vertex in graph.keys():
        for neighbor in graph[vertex]:
            if neighbor in zero_group and vertex not in zero_group:
                zero_group.append(vertex)
                continue
        if vertex not in zero_group and breadth_first_search(graph, vertex, 0):
            zero_group.append(vertex)
    return len(zero_group)


def main():
    print(group_size(utility.read_by_line('input_12.txt')))


if __name__ == '__main__':
    main()
