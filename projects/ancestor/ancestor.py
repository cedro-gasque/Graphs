class Tree:
    def __init__(self, data):
        self.data = dict()
        for (j, i) in data:
            (i in self.data and not self.data[i].add(j)) or self.data.__setitem__(i, {j})

    def __contains__(self, key):
        return key in self.data

    def __getitem__(self, key):
        return self.data[key] if key in self else set()


def earliest_ancestor(ancestors, starting_node):
    queue = []
    tree = Tree(ancestors)
    queue.append((starting_node, 0))
    o_node, o_age = (-1, 0)
    while len(queue) > 0:
        node, age = queue[0]
        if node in tree:
            for n in tree[node]:
                queue.append((n, age + 1))
        elif o_age < age or (o_age == age and node < o_node):
            o_node, o_age = queue[0]
        queue.pop(0)
    return o_node
