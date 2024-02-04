import math
from pprint import pprint

from bit_vector import BitVector
from utils.subset import (
    generate_subsets,
    generate_subsets_from_list,
)


class PsychicModelingSolver:
    def __init__(self, n, k, j, build=False):
        self.n= n
        self.k = k
        self.j = j
        self.i2s_n_k = None
        self.i2s_n_j = None
        self.s2i_n_j = None
        self.n_choose_k = math.comb(n, k)
        self.n_choose_j = math.comb(n, j)
        
        if build:
            self.build()

    
    def build(self):
        self.i2s_n_k = _generate_i2s_dict(self.n, self.k)
        assert len(self.i2s_n_k) == self.n_choose_k
        self.i2s_n_j, self.s2i_n_j = _generate_i2s_dict(self.n, self.j, bilaterally=True)
        assert len(self.i2s_n_j) == self.n_choose_j

    
    def solve(self):
        if not (self.i2s_n_k and self.i2s_n_j and self.s2i_n_j):
            self.build()
        
        all_tickets = self.n_choose_k
        all_potential_winner_tickets = self.n_choose_j

        print(f"{pow(2, all_tickets)}")

        cover_state = BitVector(n_bits=all_potential_winner_tickets)

        i = 0
        for n_tickets in range(1, all_tickets + 1):
            print(f"SEARCHING {n_tickets} ticket solutions")
            for candidate_tickets in generate_subsets(n_tickets, all_tickets):
                print(f"checking candidate tickets: {candidate_tickets}")
                coverings = []
                for ticket_i in candidate_tickets:
                    ticket = self.i2s_n_k[ticket_i - 1]
                    for covering in generate_subsets_from_list(self.j, ticket):
                        covering_i = self.s2i_n_j[tuple(covering)]
                        if cover_state[covering_i] != 1:
                            cover_state[covering_i] = 1
                            coverings.append(covering_i)

                i += 1
                print(f"trying for {i} time")
                
                if cover_state.is_full():
                    print("SUCCESS") 
                    print(f"cover state: [{cover_state.n_filled}/{cover_state.n_bits}]")
                    print(f"winner: {[self.i2s_n_k[ticket_i - 1] for ticket_i in candidate_tickets]}")
                    print("i2s_n_k")
                    pprint(self.i2s_n_k)
                    print("i2s_n_j")
                    pprint(self.i2s_n_j)
                    print("s2i_n_j")
                    pprint(self.s2i_n_j)
                    return [
                        self.i2s_n_k[ticket_i - 1] 
                        for ticket_i in candidate_tickets
                    ]
                
                print(f"cover state: [{cover_state.n_filled}/{cover_state.n_bits}]")
                
                for covering_i in coverings:
                    cover_state[covering_i] = 0


def _generate_i2s_dict(n, k, l=None, bilaterally=False):
    if not bilaterally:
        i2s = {}
        if l is None:
            for i, s in enumerate(generate_subsets(k, n)):
                i2s[i] = tuple(s)
        else:
            for i, s in enumerate(generate_subsets_from_list(n, l)):
                i2s[i] = tuple(s)
        return i2s 

    i2s = {}
    s2i = {}
    if l is None:
        for i, s in enumerate(generate_subsets(k, n)):
            st = tuple(s)
            i2s[i] = st
            s2i[st] = i
    else:
        for i, s in enumerate(generate_subsets_from_list(n, l)):
            st = tuple(s)
            i2s[i] = st
            s2i[st] = i
    return i2s, s2i
