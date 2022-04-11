from itertools import permutations


def render(l):
    """Render a 3x3 grid of a list `l`."""
    try:
        assert len(l) == 9
    except AssertionError:
        print(f"Expected list of length 9. Got length {len(l)}")

    first_row = f"{l[0]}  {l[1]}  {l[2]}"
    second_row = f"{l[3]}  {l[4]}  {l[5]}"
    third_row = f"{l[6]}  {l[7]}  {l[8]}"
    leading = " " * len(first_row)
    padding = '-' * len(first_row)

    rows = [padding, first_row, leading, second_row, leading, third_row, padding]
    for row in rows:
        print(row)


def verify_set(s):
    """Make sure only range(9) nums in s."""
    golden = set(list(range(1, 10)))
    st = set(s)

    return st == golden


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
    for index, p in enumerate(all_permutations):
        solved = check_solution(p)
        if solved:
            print('Solution found! 🟢')
            render(p)
            break
        print(f'Trying permutation #{index}...')

    # print(f'The length of all permutations is {len(all_permutations)}')


if __name__ == '__main__':
    main()
