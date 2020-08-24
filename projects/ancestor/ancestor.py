def earliest_ancestor(ancestors, starting_node):

    graph = {}

    for each in ancestors:
        if each[1] not in graph:
            graph[each[1]] = {each[0]}
        else:
            graph[each[1]].add(each[0])

    my_Stack = []
    my_Stack.append(starting_node)
    visited = set()

    while len(my_Stack) != 0:
        current_vert = my_Stack.pop()
        if current_vert not in visited and current_vert in graph:
            visited.add(current_vert)
            if min(graph[current_vert]) in graph:
                smallest_val = min(graph[current_vert])
                my_Stack.append(smallest_val)
            elif min(graph[current_vert]) not in graph:
                return min(graph[current_vert])
        elif current_vert not in graph:
            return -1
