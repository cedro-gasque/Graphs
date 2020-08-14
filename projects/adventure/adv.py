from room import Room
from player import Player
from world import World
from util import Stack, Queue

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

def deepest():
    """
    Return a list containing a path
    that travels through every room at least once.
    """
    longest = 0
    stack = Stack()
    path = []
    back = []
    visited = set()
    stack.push((0, ) + tuple(room_graph[0]))
    room, coords, exits = stack.pop()
    visited.add(room)
    deadend = True
    for dir, r in exits.items():
        if r not in visited:
            stack.push((r, dir) + tuple(room_graph[r]))
            deadend = False
    while stack.size() > 0:
        room, path_dir, coords, exits = stack.pop()
        path.append(path_dir)
        back.append(inverse(path_dir))
        visited.add(room)
        deadend = True
        for dir, r in exits.items():
            if r not in visited:
                stack.push((r, dir) + tuple(room_graph[r]))
                deadend = False
        if deadend:
            if len(back) > longest:
                longest = len(back)
            back.reverse()
            path.extend(back)
            back.clear()
    return path
traversal_path = deepest()
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
print(player.current_room.id)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)
    pass
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
