import random


def heuristic(next, dest):
    h = abs(next.x - dest.x) + abs(next.y - dest.y)
    return h


def a_star_search(muddy_grid, src, dest):
    queue = PriorityQueue()
    queue.push(0, src)
    predecessors = {src: None}
    costs = {src: 0}
    visited = set()

    #Barriers enabled check
    barriers = muddy_grid.allow_barriers

    while not queue.empty():
        current = queue.pop()
        if current == dest:
            break
        if current in visited:
            continue
        visited.add(current)

        for next in muddy_grid.neighbors(current):
            if next.cost(barriers_enabled = barriers) >= 999:
                continue
            next_cost_so_far = costs[current] + next.cost(barriers_enabled = barriers)
            if next not in costs or next_cost_so_far < costs[next]:
                costs[next] = next_cost_so_far
                priority = next_cost_so_far + heuristic(next, dest)
                queue.push(priority, next)
                predecessors[next] = current

    if dest not in predecessors:
        return "No path exists from chosen source to destination"

    path = []
    pred = dest
    while pred != None:
        path.append(pred)
        pred = predecessors.get(pred, None)
    path.reverse()
    return path


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def push(self, priority, item):
        self.elements.append((priority, item))

    def pop(self):
        if self.empty():
            return None
        min = 0
        for i in range(len(self.elements)):
            if self.elements[i][0] < self.elements[min][0]:
                min = i
        item = self.elements[min]
        del self.elements[min]
        return item[1]


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def cost(self, barriers_enabled = False):
        random.seed(hash(self))
        bucket = random.randint(1, 3)
        if bucket == 1:
            cost = random.randint(1, 5)
        elif bucket == 2:
            cost = random.randint(15, 20)
        else:
            if barriers_enabled:
                cost = 999
            else:
                cost = random.randint(15, 20)
        return cost

    def __eq__(self, other):
        if other is None:
            return False
        if type(other) is tuple:
            return self.x == other[0] and self.y == other[1]
        else:
            return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x * 1000) + self.y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class TrafficGrid:
    def __init__(self, width, height, allow_barriers = False):
        self.width = width
        self.height = height
        self.allow_barriers = allow_barriers

    def in_bounds(self, tile):
        return 0 <= tile.x < self.width and 0 <= tile.y < self.height

    def neighbors(self, tile):
        neighbors = [
            Tile(tile.x + 1, tile.y),
            Tile(tile.x - 1, tile.y),
            Tile(tile.x, tile.y - 1),
            Tile(tile.x, tile.y + 1),
        ]
        results = filter(self.in_bounds, neighbors)
        return results

    def __repr__(self):
        s = ""
        for y in range(self.height - 1, -1, -1):
            for x in range(self.width):
                t = Tile(x, y)
                s += f"[{t.cost(barriers_enabled = self.allow_barriers):02d}]"
            s += "\n"
        return s