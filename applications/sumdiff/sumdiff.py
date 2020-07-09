"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# Your code here
values = dict()
sums = dict()
diffs = dict()

for first in q:

    # if needed, compute and store f(first)
    if first not in values:
        values[first] = f(first)

    for second in q:

        # if needed, compute and store f(second)
        if second not in values:
            values[second] = f(second)

        # use a variable to keep track of the tuple
        key1 = (first, second)
        key2 = (second, first)

        # compute sums and differences
        pair_sum = values[first] + values[second]
        pair_difference = values[first] - values[second]

        # store the pairs that will generate each sum
        if pair_sum not in sums:
            sums[pair_sum] = set()

        sums[pair_sum].add(key1)
        sums[pair_sum].add(key2)

        # store the pair for difference f(first) - f(second)
        if pair_difference not in diffs:
            diffs[pair_difference] = set()

        diffs[pair_difference].add(key1)

        # store the pair for difference f(second) - f(first)
        if -pair_difference not in diffs and first != second:
            diffs[-pair_difference] = set()

        diffs[-pair_difference].add(key2)

# check for all values where the sum and difference are the same
shared_values = set(sums.keys()).intersection(
    set(diffs.keys()))


def print_solutions(show_all_possibilities=True):

    # count how many solutions were found
    solutions = 0

    # look up all tuple combinations for each sum and difference
    for value in shared_values:

        calcSums = sums[value]
        calcDiffs = diffs[value]

        solutions += len(calcSums) * len(calcDiffs)

        if show_all_possibilities:

            for sum_tuple in calcSums:

                for difference_tuple in calcDiffs:

                    a, b = sum_tuple
                    c, d = difference_tuple

                    print(
                        f"f({a}) + f({b}) = f({c}) - f({d})    {values[a]} + {values[b]} = {values[c]} - {values[d]}")

    print("\n", solutions, "solutions found for q =", q)


print_solutions()
