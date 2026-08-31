from __future__ import annotations

import sys
from collections import deque
from typing import TYPE_CHECKING, Protocol, TypeVar

if TYPE_CHECKING:
    from collections.abc import Callable

T = TypeVar("T")


class AlwaysGreaterFloat(float):
    def __gt__(self, other):
        return True  # Always greater than anything else

    def __lt__(self, other):
        return False  # Never less than anything else

    def __ge__(self, other):
        return True

    def __le__(self, other):
        return False

    def __eq__(self, other):
        return isinstance(other, AlwaysGreaterFloat)


INFINITY = AlwaysGreaterFloat(sys.float_info.max)


class Frontier(Protocol[T]):
    """Defines the interface for a search frontier."""

    def add(self, item: T, parent: T | None = None) -> None: ...

    def next(self) -> T: ...

    def __bool__(self) -> bool: ...


class QueueFrontier:
    """FIFO frontier for Breadth-First Search (BFS)."""

    def __init__(self) -> None:
        self.deque: deque[T] = deque()

    def add(self, item: T, parent: T | None = None) -> None:
        self.deque.append(item)

    def next(self) -> T:
        return self.deque.popleft()

    def __bool__(self) -> bool:
        return bool(self.deque)


class StackFrontier:
    """LIFO frontier for Depth-First Search (DFS)."""

    def __init__(self) -> None:
        self.stack: list[T] = []

    def add(self, item: T, parent: T | None = None) -> None:
        self.stack.append(item)

    def next(self) -> T:
        return self.stack.pop()

    def __bool__(self) -> bool:
        return bool(self.stack)


class GreedyBestFirstFrontier:
    """Greedy Best-First Search frontier expanding the node closest to the goal using $h(n)$."""

    def __init__(
        self,
        cost_to_destination: Callable[[T], float] | None = None,
    ) -> None:
        self._cost_to_destination = cost_to_destination or (lambda n: 0.0)
        self._elements: list[tuple[float, T]] = []
        self._seen: set[T] = set()

    def add(self, item: T, parent: T | None = None) -> None:
        if item not in self._seen:
            self._seen.add(item)
            h_val = self._cost_to_destination(item)
            self._elements.append((h_val, item))

    def next(self) -> T:
        min_index = 0
        min_h = self._elements[0][0]
        for i in range(1, len(self._elements)):
            if self._elements[i][0] < min_h:
                min_h = self._elements[i][0]
                min_index = i

        _, current_node = self._elements.pop(min_index)
        return current_node

    def __bool__(self) -> bool:
        return bool(self._elements)


class AStarFrontier:
    """Manual priority list frontier for A* Search ($f(n) = g(n) + h(n)$)."""

    def __init__(
        self,
        cost_from_start: Callable[[T], float] | None = None,
        cost_to_destination: Callable[[T], float] | None = None,
    ) -> None:
        self._cost_from_start = cost_from_start or (lambda n: 1.0)
        self._cost_to_destination = cost_to_destination or (lambda n: 0.0)
        self._elements: list[tuple[float, T]] = []
        self._g_costs: dict[T, float] = {}

    def add(self, item: T, parent: T | None = None) -> None:
        edge_cost = self._cost_from_start(item)
        new_g = self._g_costs.get(parent, 0.0) + edge_cost

        if new_g < self._g_costs.get(item, INFINITY):
            self._g_costs[item] = new_g
            f_val = new_g + self._cost_to_destination(item)
            self._update_node(item, f_val)

    def _update_node(self, item: T, priority: float) -> None:
        for i, (_, node) in enumerate(self._elements):
            if node == item:
                self._elements[i] = (priority, item)
                return
        self._elements.append((priority, item))

    def next(self) -> T:
        min_index = 0
        min_f = self._elements[0][0]
        for i in range(1, len(self._elements)):
            if self._elements[i][0] < min_f:
                min_f = self._elements[i][0]
                min_index = i

        _, current_node = self._elements.pop(min_index)
        return current_node

    def __bool__(self) -> bool:
        return bool(self._elements)


def generic_search[T](
    graph: dict[T, set[T]],
    start_node: T,
    frontier: Frontier[T],
    goal_node: T | None = None,
) -> list[T]:
    """Performs an iterative graph search with a fully polymorphic frontier interface."""
    visited: set[T] = set()
    traversal_order: list[T] = []

    frontier.add(start_node)

    while frontier:
        current_node = frontier.next()

        if current_node in visited:
            continue

        visited.add(current_node)
        traversal_order.append(current_node)

        if goal_node is not None and current_node == goal_node:
            break

        for neighbor in graph.get(current_node, set()):
            if neighbor not in visited:
                frontier.add(neighbor, parent=current_node)

    return traversal_order


Coord = tuple[int, int]


def grid_to_graph(grid) -> tuple[Coord, Coord, dict[Coord, set[Coord]]]:
    graph: dict[Coord, set[Coord]] = {}
    rows = len(grid)
    cols = len(grid[0])

    start_node: Coord | None = None
    goal_node: Coord | None = None

    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell != "W":
                node = (r, c)
                if cell == "S":
                    start_node = node
                elif cell == "F":
                    goal_node = node

                graph[node] = set()
                # Check 4-way neighbors (up, down, left, right)
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "W":
                        graph[node].add((nr, nc))

    return start_node, goal_node, graph


def manhattan_distance(node: Coord) -> float:
    return float(abs(node[0] - goal[0]) + abs(node[1] - goal[1]))


def euclidean_distance(node: Coord) -> float:
    return float(((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5)


# Example usage:
if __name__ == "__main__":
    grid = [
        ["U", "W", "U", "W", "U", "W", "W", "W", "U", "U", "W", "F"],
        ["U", "W", "U", "W", "U", "U", "U", "W", "U", "W", "W", "U"],
        ["U", "U", "U", "W", "U", "W", "U", "U", "U", "W", "W", "U"],
        ["W", "U", "W", "W", "U", "W", "U", "W", "U", "W", "W", "U"],
        ["W", "U", "U", "U", "U", "W", "U", "W", "U", "U", "U", "U"],
        ["W", "W", "W", "U", "W", "W", "U", "W", "W", "W", "W", "W"],
        ["S", "U", "U", "U", "W", "W", "U", "U", "U", "U", "U", "U"],
    ]

    start, goal, graph = grid_to_graph(grid)

    results = {
        "BFS": generic_search(graph, start, QueueFrontier(), goal),
        "DFS": generic_search(graph, start, StackFrontier(), goal),
        "Greedy best-first, manhattan": generic_search(
            graph,
            start,
            GreedyBestFirstFrontier(cost_to_destination=manhattan_distance),
            goal,
        ),
        "A*": generic_search(
            graph,
            start,
            AStarFrontier(
                cost_to_destination=euclidean_distance,
            ),
            goal_node=goal,
        ),
    }

    for k, v in results.items():
        print(k)
        print(f"    {len(v)}")
        print(f"    {v}")
