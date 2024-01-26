# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

import random
from optimizn.combinatorial.branch_and_bound import BnBProblem


class TravelingSalesmanProblem(BnBProblem):
    def __init__(self, params):
        self.input_graph = params['input_graph']
        # sort all distance values, for computing lower bounds
        self.sorted_dists = []
        for i in range(self.input_graph.dists.shape[0]):
            for j in range(0, i):
                self.sorted_dists.append(self.input_graph.dists[i, j])
        self.sorted_dists.sort()
        super().__init__(params)

    def get_initial_solution(self):
        # path of cities in increasing, numerical order
        return list(range(self.input_graph.num_cities))
    
    def get_root(self):
        # return empty path
        return []

    def complete_solution(self, sol):
        # path completed by random ordering of unvisited cities
        unvisited_cities = set(range(self.input_graph.num_cities)).difference(
            set(sol))
        unvisited_cities = list(unvisited_cities)
        random.shuffle(unvisited_cities)
        return sol + unvisited_cities

    def cost(self, sol):
        # sum of distances between adjacent cities in path, and from last
        # city to first city in path
        path_cost = 0
        for i in range(self.input_graph.num_cities - 1):
            path_cost += self.input_graph.dists[sol[i], sol[i + 1]]
        path_cost += self.input_graph.dists[
            sol[self.input_graph.num_cities - 1], sol[0]]
        return path_cost

    def lbound(self, sol):
        # sum of distances between cities in path and smallest distances
        # to account for remaining cities and start city
        num_cities_in_path = len(sol)
        lb_path_cost = 0
        for i in range(num_cities_in_path - 1):
            lb_path_cost += self.input_graph.dists[sol[i], sol[i + 1]]
        if num_cities_in_path == self.input_graph.num_cities:
            lb_path_cost += self.input_graph.dists[
                sol[num_cities_in_path - 1], sol[0]]
        elif num_cities_in_path == 0:
            lb_path_cost += sum(self.sorted_dists[
                :self.input_graph.num_cities])
        else:
            lb_path_cost += sum(self.sorted_dists[
                :self.input_graph.num_cities - num_cities_in_path + 1])
        return lb_path_cost

    def is_complete(self, sol):
        # check that all cities covered once, path length is equal to the
        # number of cities
        check_all_cities_covered = set(sol) == set(
            range(self.input_graph.num_cities))
        check_cities_covered_once = len(sol) == len(set(sol))
        check_path_length = len(sol) == self.input_graph.num_cities
        return (check_path_length and check_cities_covered_once and
                check_all_cities_covered)

    def is_feasible(self, sol):
        # check that covered cities are only covered once and path length is
        # less than or equal to the number of cities
        check_cities_covered_once = len(sol) == len(set(sol))
        check_path_length = len(sol) <= self.input_graph.num_cities
        return check_cities_covered_once and check_path_length

    def branch(self, sol):
        # build the path by creating a new solution for each uncovered city,
        # where the uncovered city is the next city in the path
        if len(sol) == self.input_graph.num_cities:
            return []
        visited = set(sol)
        new_sols = []
        for new_city in range(self.input_graph.dists.shape[0]):
            if new_city not in visited:
                new_sols.append(sol + [new_city])
        return new_sols
