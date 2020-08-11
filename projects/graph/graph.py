"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        try:
            self.vertices[v1].add(v2)
        except:
            raise

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        try:
            return self.vertices[vertex_id]
        except:
            raise

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = {starting_vertex}
        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            u = queue[0]
            for v in self.get_neighbors(u):
                if v not in visited:
                    visited.add(v)
                    queue.enqueue(v)
            queue.dequeue()
            print(u)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        order = []
        while stack.size() > 0:
            u = stack.pop()

            if u not in visited:
                visited.add(u)
                for v in self.get_neighbors(u):
                    if v not in visited:
                        stack.push(v)
                order += [u]
        print(*order, sep="\n")

    def dft_recursive(self, starting_vertex, visited=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.

        THIS IS THE WORST CODE I'VE EVER WRITTEN, I LOVE IT
        I KNOW WHY THIS WORKS BUT IT'S STILL REALLY STUPID AND
        I'D HAVE TROUBLE EXPLAINING IT BUT I AM WILLING TO TRY
        """
        vis = visited[:]
        vis.append(starting_vertex)
        for v in self.get_neighbors(starting_vertex):
            if v not in vis:
                vis = self.dft_recursive(v, visited=vis)
        if len(visited) == 0:
            print(*vis, sep="\n")
        else:
            return vis


    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()
        visited = set((starting_vertex,))
        queue.enqueue((starting_vertex,))
        while queue.size() > 0:
            path = queue[0]
            for v in self.get_neighbors(path[-1]):
                if v not in visited:
                    visited.add(v)
                    n_path = path + (v,)
                    if v == destination_vertex:
                        return list(n_path)
                    queue.enqueue(n_path)
            queue.dequeue()

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        visited = set((starting_vertex,))
        stack.push((starting_vertex,))
        while stack.size() > 0:
            u = stack.pop()

            if u not in visited:
                visited.add(u)
                for v in self.get_neighbors(u[-1]):
                    path = u + (v,)
                    if v == destination_vertex:
                        return list(path)
                    elif path not in visited:
                        stack.push(path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=[], path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        vis = visited[:]
        vis.append(starting_vertex)
        for v in self.get_neighbors(starting_vertex):
            p = path + [starting_vertex]
            if v not in vis:
                vis, p = self.dfs_recursive(v, destination_vertex, visited=vis, path=p)
                if p[-1] == destination_vertex:
                    break
        if len(visited) == 0:
            return p
        return vis, p

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("__________")
    graph.dft(1)
    print("__________")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
