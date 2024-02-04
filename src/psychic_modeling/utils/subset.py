def print_subsets(subset_generator):
    for i, ss in enumerate(subset_generator):
        print(f"{i}: {ss}")


def generate_subsets(k, n):
    yield from _generate_subsets(k, n, 1, None)


def _generate_subsets(k, n, s, curr_set):
    if curr_set is None:
        curr_set = []
    if len(curr_set) < k:
        for i in range(s, n + 1):
            curr_set.append(i)
            yield from _generate_subsets(k, n, i + 1, curr_set)
            curr_set.pop()
    else:    
        yield curr_set


def generate_subsets_from_list(k, l):
    yield from _generate_subsets_from_list(k, l, 0, None)    


def _generate_subsets_from_list(k, l, s, curr_set):
    if curr_set is None:
        curr_set = []
    if len(curr_set) < k:
        for i, elem in enumerate(l[s:], 1):
            curr_set.append(elem)
            yield from _generate_subsets_from_list(k, l, s + i, curr_set)
            curr_set.pop()
    else:    
        yield curr_set