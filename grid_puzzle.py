from itertools import permutations


def render(l):
    """Render a 3x3 grid of a list `l`."""
    try:
        assert len(l) == 9
    except AssertionError:
        print(f"Expected list of length 9. Got length {len(l)}")

    first_row = f"{l[0]} - {l[1]} = {l[2]}"
    second_row = f"{l[3]} ÷ {l[4]} = {l[5]}"
    third_row = f"{l[6]} + {l[7]} = {l[8]}"
    leading_1 = " " * 8 + "x"
    leading_2 = " " * 8 + "="
    padding = '-' * len(first_row)

    rows = [padding, first_row, leading_1, second_row, leading_2, third_row, padding]
    for row in rows:
        print(row)


def generate_lists():
    """Generate all permutations of range(1, 10)."""
    all_perms = list(permutations(range(1, 10)))

    return all_perms


def check_solution(p):
    """Given a permutation of range(1, 10), return True if p solves the puzzle."""
    try:
        assert p[0] - p[1] == p[2]
    except AssertionError:
        return False

    try:
        assert p[3] / p[4] == p[5]
    except AssertionError:
        return False

    try:
        assert p[6] + p[7] == p[8]
    except AssertionError:
        return False

    try:
        assert p[2] * p[5] == p[8]
    except AssertionError:
        return False

    return True


def main():
    all_permutations = generate_lists()
    all_solutions = []
    for index, p in enumerate(all_permutations):
        solved = check_solution(p)
        # print(f'Trying permutation #{index + 1}...')
        if solved:
            print('Solution found! 🔥')
            render(p)
            # print(f'Took {index + 1} guesses to solve.')
            all_solutions.append(p)

    print(f'The total number of solutions is {len(all_solutions)}')


if __name__ == '__main__':
    main()
