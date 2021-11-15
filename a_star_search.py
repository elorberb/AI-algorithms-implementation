import pandas as pd
from queue import PriorityQueue
import route_grid

# The function initializes and returns open
def init_open():
    open_list = PriorityQueue()
    return open_list

# The function inserts s into open
def insert_to_open(open_list, s):  # Should be implemented according to the open list data structure
    open_list.put(s)

# The function returns the best node in open (according to the search algorithm)
def get_best(open_list):
    # best_node = open_list[0]
    # node_index = 0;
    # best_f = best_node[0]
    # for i in range(len(open_list)):
    #     n = open_list[i]
    #     if n[0] == best_f and n[1] < best_node[1] or n[0] < best_f:
    #         best_f = n[0]
    #         best_node = n
    #         node_index = i
    #
    return open_list.get()
# The function returns neighboring locations of s_location
def get_neighbors(grid, s_location):
    neighbors = []
    x = s_location[0]
    y = s_location[1]
    upper_boundary = len(grid)
    lower_boundary = 0

    # check upper location
    if y + 1 < upper_boundary:
        if grid[x, y + 1] != '@':
            neighbors.append((x, y + 1))
    # check right location
    if x + 1 < upper_boundary:
        if grid[x + 1, y] != '@':
            neighbors.append((x + 1, y))
    # check left location
    if x - 1 > lower_boundary:
        if grid[x - 1, y] != '@':
            neighbors.append((x - 1, y))
    # check under location
    if y - 1 > lower_boundary:
        if grid[x, y - 1] != '@':
            neighbors.append((x, y - 1))

    return neighbors

# The function returns whether or not s_location is the goal location
def is_goal(s_location, goal_location):
    return s_location[0] == goal_location[0] and s_location[1] == goal_location[1]

# The function estimates the cost to get from s_location to goal_location
def calculate_heuristic(s_location, goal_location):
    h = (goal_location[0] - s_location[0]) + (goal_location[1] - s_location[1])
    return h

# Locations are tuples of (x, y)
def astar_search(grid, start_location, goal_location):
    # State = (f, g, h, x, y, s_prev) # f = g + h (For Priority Queue)
    # Start_state = (0, 0, 0, x_0, y_0, False)
    start = (0, 0, 0, start_location[0], start_location[1], False)
    open_list = init_open()
    closed_list = set()
    # Mark the source node as
    # visited and enqueue it
    insert_to_open(open_list, start)
    while not open_list.empty():
        # Dequeue a vertex from
        # queue and print it
        s = get_best(open_list)
        s_location = (s[3], s[4])
        if s_location in closed_list:
            continue
        if is_goal(s_location, goal_location):
            print("The number of states visited by AStar Search:", len(closed_list))
            return s
        neighbors_locations = get_neighbors(grid, s_location)
        for n_location in neighbors_locations:
            if n_location in closed_list:
                continue
            h = calculate_heuristic(n_location, goal_location)
            g = s[2] + 1
            f = g + h
            n = (f, h, g, n_location[0], n_location[1], s)
            insert_to_open(open_list, n)
        closed_list.add(s_location)

def print_route(s):
    for r in s:
        print(r)

def get_route(s):
    route = []
    while s:
        s_location = (s[3], s[4])
        route.append(s_location)
        s = s[5]
    route.reverse()
    return route

def print_grid_route(route, grid):
    for location in route:
        grid[location] = 'x'
    print(pd.DataFrame(grid))
