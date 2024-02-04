import math
import random


class SimulatedAnnealingSolver:
    def __init__(self, temperature, tickets_n_k, tickets_n_j):
        self.init_temp = temperature
        self.tickets_n_k = tickets_n_k
        self.tickets_n_j = tickets_n_j
        self.curr_sol_i = None
        self.curr_eval = None
        self.n_iterations = 10_000
        self.range = 100


    def get_initial_candidate_solution(self):
        ticket_i = random.choice(len(self.tickets_n_k))
        return self.tickets_n_k[ticket_i]

    
    def solve(self):
        for i in range(self.n_iterations):
            candidate_i = self.peturbation(self.curr_sol_i)
            candidate_eval = self.energy(candidate_i)
            diff = candidate_eval - self.curr_eval
            t = self.init_temp / (i + 1)
            metropolis = math.exp(-diff, t)
            if diff < 0 or random.random() < metropolis:
                self.curr_sol_i = candidate_i
                self.curr_eval = candidate_eval
                print(f"curr best solution: {self.{}}")


    def energy():
        pass
        


    def peturbation(self, sol_i):
        return sol_i + random.randint(-self.range, self.range)
