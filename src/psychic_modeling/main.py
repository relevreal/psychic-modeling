import sys

from psychic_modeling_solver import PsychicModelingSolver


def main():
    n, k, j = parse_arguments(sys.argv)
    solver = PsychicModelingSolver(n, k, j, build=True)
    tickets = solver.solve()
    print(f"tickets: {tickets}")


def parse_arguments(argv):
    if len(argv) != 4:
        raise SystemExit(f"usage: {argv[0]} <n> <k> <j>")
    try:
        n = int(argv[1])
        k = int(argv[2])
        j = int(argv[3])
    except ValueError:
        raise ValueError(f"all arguments must be integers")
    return n, k, j 

    
if __name__ == "__main__":
    main()
