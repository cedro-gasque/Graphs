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
def deepest():
    """
    Return a list containing a path
    that travels through every room at least once.
    """
    longest = 0
    path = ['n']
    back = ['s']
    graph = {0: {'n': -1, 's': -1, 'w': -1, 'e': 1}}
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
            graph[room] = {k: -1 for k in exits.keys()}
            graph[room][inverse(path_dir)] = previous_room
        deadend = True
        for dir, r in exits.items():
            if graph[room][dir] is -1 and r not in visited:
                graph[room][dir] = r
                previous_room, room = room, r
                path_dir = dir
                exits = room_graph[room][1]
                deadend = False
                break
            elif graph[room][dir] is -1 and r in visited:
                graph[room][dir] = r
                deadend = True
                break
        if deadend:
            s = False
            if len(back) > longest:
                s = True
                longest = len(back)
            while -1 not in graph[room].values() and len(back) > 0:
                dir = back.pop()
                path.append(dir)
                previous_room, room = room, graph[room][dir]
                path_dir = dir
                exits = room_graph[room][1]
            if longest is 42 and s:
                print(room)
                print(back[::-1])
        else:
            path.append(path_dir)
            back.append(inverse(path_dir))
    print(longest)
    return path
traversal_path = deepest()
print(traversal_path[-25:])
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
print(player.current_room.id)
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
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
