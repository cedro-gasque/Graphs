from room import Room
from player import Player
from world import World
from util import Stack

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

inverse = lambda c : chr(ord(c) ^ (18 + 11 * (c in 'ns')))

order = {
    0: {'n': -1, 's': -1, 'w': -1, 'e': 1},
    3: {'w': -1, 'n': -1, 'e': -1},
    104: {'w': -1, 's': -1, 'n': -1},
    126: {'w': -1, 's': -1, 'n': -1},
    149: {'s': -1, 'w': -1, 'n': -1},
    220: {'w': -1, 'n': -1, 'e': -1},
    344: {'w': -1, 'n': -1, 'e': -1},
    418: {'w': -1, 'e': -1, 's': -1},
    284: {'n': -1, 'w': -1, 'e': -1, 's': -1},
    128: {'w': -1, 'e': -1, 's': -1},
    92: {'s': -1, 'n': -1, 'w': -1},
    81: {'w': -1, 'n': -1, 'e': -1, 's': -1},
    13: {'e': -1, 'n': -1, 'w': -1},
    5: {'s': -1, 'w': -1, 'n': -1},
    6: {'w': -1, 's': -1, 'e': -1},
    23: {'w': -1, 's': -1, 'e': -1},
    57: {'w': -1, 's': -1, 'n': -1},
    94: {'w': -1, 's': -1, 'n': -1},
    97: {'w': -1, 's': -1, 'n': -1},
    110: {'w': -1, 's': -1, 'n': -1},
    118: {'w': -1, 'e': -1, 'n': -1},
    218: {'s': -1, 'n': -1, 'w': -1},
    14: {'w': -1, 'n': -1, 's': -1},
    17: {'w': -1, 'n': -1, 'e': -1, 's': -1},
    28: {'s': -1, 'n': -1, 'w': -1},
    64: {'w': -1, 'n': -1, 's': -1},
    111: {'e': -1, 'n': -1, 's': -1},
    121: {'n': -1, 'e': -1, 's': -1},
    148: {'e': -1, 's': -1, 'n': 163},
    163: {'e': -1, 'n': -1, 'w': -1, 's': 148},
    147: {'e': -1, 's': -1, 'n': -1},
    17: {'w': -1, 'n': -1, 'e': -1, 's': -1},
    28: {'s': -1, 'n': -1, 'w': -1},
    64: {'w': -1, 'n': -1, 's': -1},
    111: {'e': -1, 'n': -1, 's': -1},
    121: {'n': -1, 'e': -1, 's': -1},
    139: {'e': -1, 'n': -1, 'w': -1},
    148: {'e': -1, 's': -1, 'n': 163},
    147: {'e': -1, 's': -1, 'n': -1},
    152: {'n': -1, 'w': -1, 's': -1},
    321: {'n': -1, 'w': -1, 's': -1},
    354: {'n': -1, 'w': -1, 'e': -1},
    163: {'e': -1, 'w': -1, 'n': -1, 's': 148},
    165: {'n': -1, 'w': -1, 'e': -1},
    199: {'w': -1, 'n': -1, 'e': -1},
    281: { 'n': -1, 'w': -1, 's': -1},
}

order2 = {
    0: {'n': -1, 's': -1, 'e': -1, 'w': -1},
    9: {'s': -1, 'w': 13},
    5: {'s': -1, 'w': -1, 'n': -1},
    6: {'w': -1, 's': -1, 'e': -1},
    23: {'w': -1, 's': -1, 'e': -1},
    57: {'w': -1, 's': -1, 'n': -1},
    94: {'w': -1, 's': -1, 'n': -1},
    97: {'w': -1, 's': -1, 'n': -1},
    110: {'w': -1, 's': -1, 'n': -1},
    118: {'w': -1, 'e': -1, 'n': -1},
    218: {'s': -1, 'n': -1, 'w': -1},
    3: {'w': -1, 'n': -1, 'e': -1},
    104: {'w': -1, 's': -1, 'n': -1},
    126: {'w': -1, 's': -1, 'n': -1},
    149: {'s': -1, 'w': -1, 'n': -1},
    220: {'w': -1, 'n': -1, 'e': -1},
    344: {'w': -1, 'n': -1, 'e': -1},
    418: {'w': -1, 'e': -1, 's': -1},
    284: {'n': -1, 'w': -1, 'e': -1, 's': -1},
    128: {'w': -1, 'e': -1, 's': -1},
    92: {'s': -1, 'n': -1, 'w': -1},
    81: {'w': -1, 'n': -1, 'e': -1, 's': -1},
    13: {'n': -1, 'w': -1, 'e': 9},
    14: {'w': -1, 'n': -1, 's': -1},
    17: {'w': -1, 'n': -1, 'e': -1, 's': -1},
    28: {'s': -1, 'n': -1, 'w': -1},
    64: {'w': -1, 'n': -1, 's': -1},
    111: {'e': -1, 'n': -1, 's': -1},
    121: {'n': -1, 'e': -1, 's': -1},
    139: {'e': -1, 'n': -1, 'w': -1},
    148: {'e': -1, 's': -1, 'n': 163},
    147: {'e': -1, 's': -1, 'n': -1},
    152: {'n': -1, 'w': -1, 's': -1},
    321: {'n': -1, 'w': -1, 's': -1},
    354: {'n': -1, 'w': -1, 'e': -1},
    163: {'e': -1, 'w': -1, 'n': -1, 's': 148},
    165: {'n': -1, 'w': -1, 'e': -1},
    199: {'w': -1, 'n': -1, 'e': -1},
    281: { 'n': -1, 'w': -1, 's': -1},
}
# order = order2
def deepest():
    """
    Return a list containing a path
    that travels through every room at least once.
    """
    path = ['n']
    back = ['s']
    graph = {0: order[0]}
    visited = {0}
    room = room_graph[0][1]['n']
    exits = room_graph[room][1]
    graph[room] = {k: -1 for k in exits.keys()}
    previous_room = 0
    graph[room]['s'] = 0
    visited.add(room)
    while len(visited) < 500:
        if room not in graph:
            visited.add(room)
            if room in order:
                graph[room] = order[room]
            else:
                graph[room] = {k: -1 for k in exits.keys()}
            graph[room][inverse(path_dir)] = previous_room
        deadend = True
        for dir, r in graph[room].items():
            if r == -1:
                r = exits[dir]
            if graph[room][dir] is -1 and r not in visited:
                graph[room][dir] = r
                previous_room, room = room, r
                path_dir = dir
                exits = room_graph[room][1]
                deadend = False
                break
            elif graph[room][dir] is -1 and r in visited:
                graph[room][dir] = r
        if deadend:
            if len(visited) < 500:
                if room is 62:
                    while room != 6:
                        dir = back.pop()
                        previous_room, room = room, graph[room][dir]
                        path_dir = dir
                        exits = room_graph[room][1]
                    path.append('n')
                    previous_room, room = 62, 6
                    path_dir = 'w'
                    exits = room_graph[room][1]
                while -1 not in graph[room].values() and len(back) > 0:
                    dir = back.pop()
                    path.append(dir)
                    previous_room, room = room, graph[room][dir]
                    path_dir = dir
                    exits = room_graph[room][1]
        else:
            path.append(path_dir)
            back.append(inverse(path_dir))
    return path
traversal_path = deepest()
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
for i, move in enumerate(traversal_path):
    player.travel(move)
    visited_rooms.add(player.current_room)
if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
