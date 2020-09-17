"""
A BFS can be used here. The two algorithms that can be applied here are
Dijkstra's algorithm and the Bellman–Ford algorithm.

## BFS
1. Create graph using the given `flights` list. For each city we need to know
its possible destinations and the cost to travel to that destination. A
hashmap of lists can be used to represent this graph.
2. We then create a queue to store the next stop and the cost needed to reach
that stop.
3. Now we start from `src` (add it to the queue) and check all its destinations.
If one of them is `dest` then update the minimum cost from the current cost.
4. Then we start from the cities neighboring `src` and check their destinations
in the same fashion. If there's no destinations or the path length has exceeded
`K`, then we stop and remove this path. We also terminate the search if the
price exceeds the current minimum price.

## Dijkstra's algorithm
This is an algorithm for finding the shortest paths between nodes in a graph.

1. Mark all nodes as unvisited.
2. Assign tentative distances to all nodes. Set the distance to 0 for `src` and
infinity for all other nodes. Set `src` as the current node.
3. For the current node A, traverse all its unvisited neighbors (B) and update
their tentative distances by taking min(tentative_dist, distA + distB).
4. After going through all the neighbors, mark the current node as visited.
5. If the `dst` node has been marked visited, stop; otherwise, selected the
unvisited node that has the smallest tentative distance and go to step 3.

## Bellman–Ford algorithm
This is slower than Dijkstra's algorithm, but is more versatile as it is capable
of handling graphs in which some of the edge weights are negative numbers.
See https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm for details.
"""
#
# @lc app=leetcode id=787 lang=python3
#
# [787] Cheapest Flights Within K Stops
#
# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# Tagged "breadth-first-search" (BFS).
import unittest
from collections import defaultdict, deque
from typing import List

# @lc code=start
import heapq


class Solution:
    # Dijkstra's algorithm
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        graph = defaultdict(list)
        # source, destination, price
        for s, d, p in flights:
            graph[s].append((d, p))

        dist = [float("inf")] * n
        dist[src] = 0

        city_queue = []
        # tentative price, city, k
        heapq.heappush(city_queue, [0, src, -1])
        while city_queue:
            price, city, k = heapq.heappop(city_queue)
            # if we've hit the destination, return the lowest overall price we've found
            if city == dst:
                return price

            if k < K:
                for c, p in graph[city]:
                    dist[c] = min(dist[c], price + p)
                    heapq.heappush(city_queue, [price + p, c, k + 1])
        return -1


# @lc code=end
class SolutionBFS:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        graph = defaultdict(list)
        # source, destination, price
        for s, d, p in flights:
            graph[s].append((d, p))

        # the queue has to track [current city, current price, num of visited cities]
        city_queue = deque([[src, 0, -1]])
        min_price = float("inf")
        while city_queue:
            # get next city in city_queue
            city, price, k = city_queue.popleft()

            # proceed if we haven't reached K stops, and there's a next stop, and
            # the current price doesn't exceed the already found minimum
            if k < K and graph[city] and price < min_price:
                for c, p in graph[city]:
                    city_queue.append([c, price + p, k + 1])

            # update min_price when we've reached the final destination
            if city == dst:
                min_price = min(min_price, price)

        return min_price if min_price != float("inf") else -1


class SolutionBellmanFord:
    """
    Find the shortest distance from `src` to all other cities allowing up to K+1 flights.
    `dist` tracks the shortest from `src` to each city.
    The inner loop updates `dist` to see whether taking one more stop would lower the
    overall cost.
    """

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        dist = [float("inf")] * n
        dist[src] = 0
        for _ in range(K + 1):
            old_dist = dist[:]
            for f in flights:
                dist[f[1]] = min(dist[f[1]], old_dist[f[0]] + f[2])
        return dist[dst] if dist[dst] < float("inf") else -1


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_cheaper_more_stops(self):
        edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        n, src, dst, K = 3, 0, 2, 1
        self.assertEqual(self.s.findCheapestPrice(n, edges, src, dst, K), 200)

    def test_direct_flight(self):
        edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
        n, src, dst, K = 3, 0, 2, 0
        self.assertEqual(self.s.findCheapestPrice(n, edges, src, dst, K), 500)

    def test_larger_graph(self):
        edges = [
            [0, 1, 20],
            [1, 2, 20],
            [2, 3, 30],
            [3, 4, 30],
            [4, 5, 30],
            [5, 6, 30],
            [6, 7, 30],
            [7, 8, 30],
            [8, 9, 30],
            [0, 2, 9999],
            [2, 4, 9998],
            [4, 7, 9997],
        ]
        n, src, dst, K = 10, 0, 9, 4
        self.assertEqual(self.s.findCheapestPrice(n, edges, src, dst, K), 30054)


if __name__ == "__main__":
    unittest.main()
