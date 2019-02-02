import numpy as np

class Node():
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    return path[::-1]

def is_invalid_position(position, maze):
    if position[0] > (len(maze) - 1) \
        or position[0] < 0 \
        or position[1] > (len(maze[len(maze)-1]) -1) \
        or position[1] < 0:
            return True
    else:
        return False


def find_way(maze, start, end):
    start_node = Node(None, start)
    end_node = Node(None, end)

    open_list = []
    close_list = []

    open_list.append(start_node)
    
    outer_iterations = 0
    max_iterations = (len(maze) // 2) ** 2

    while len(open_list) > 0:
        outer_iterations += 1
        
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if current_node.f > item.f:
                current_node = item
                current_index = index
                
        if outer_iterations > max_iterations:
            return path(current_node)

        open_list.pop(current_index)
        close_list.append(current_node)

        if current_node == end_node:
            return path(current_node)

        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            if maze[node_position[0]][node_position[1]] != 0:
                continue

            new_node = Node(current_node, node_position)

            children.append(new_node)

        for child in children:            
            if len([closed_child for closed_child in close_list if closed_child == child]) > 0:
                continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            if len([open_node for open_node in open_list if child == open_node and child.g > open_node.g]) > 0:
                continue

            open_list.append(child)


def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start = (0, 0)
    end = (7, 6)

    for x,y in (start, end):
        maze[x][y] = 'X'

    print(np.matrix(maze))
    print()

    path = find_way(maze, start, end)

    for x,y in path:
        maze[x][y] = 'X'

    print(np.matrix(maze))


main()