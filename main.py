# Problem 62:
#     Cubic Permutations
#
# Description:
#     The cube, 41063625 (345^3), can be permuted to produce two other cubes:
#       56623104 (384^3) and 66430125 (405^3).
#     In fact, 41063625 is the smallest cube which has exactly
#       three permutations of its digits which are also cube.
#
#     Find the smallest cube for which exactly five permutations of its digits are cube.

from collections import defaultdict
from math import ceil, floor


def digit_key(n):
    """
    Returns the digits of `n` as an ordered string.

    Args:
        n (int): Natural number

    Returns:
        (str):
            Ordered string of all digits in `n`

    Raises:
        AssertError: if incorrect args are given
    """
    return ''.join(sorted(list(str(n))))


def main(c):
    """
    Returns the first (least) set of exactly `c` cubes
      whose digits permute to each other,
      as an ordered list.

    Args:
        c (int): Natural number

    Returns:
        (List[int]):
            Ordered list of the first set of `c` cubes permuting to each other.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(c) == int and c > 0 
    
    # Confine search by number of digits,
    #   as only numbers of same digit-count could permute to each other.
    n = 1
    while True:
        # Collect all n-digit cubes
        b_min = ceil(10**((n-1)/3))
        b_max = floor(10**(n/3))+1
        digits_to_cubes = defaultdict(lambda: [])
        for b in range(b_min, b_max):
            x = b**3
            digits_to_cubes[digit_key(x)].append(x)

        # Check for sets of `c` permuted cubes
        # Return least if there are multiple
        valid = [cs for cs in digits_to_cubes.values() if len(cs) == c]
        if len(valid) > 0:
            # Find the cube set with the least cube in it
            # Cubes within a permuted set will already be sorted,
            #   due to ascending insertion order
            least = min(valid, key=lambda cs: cs[0])
            return least
        else:
            n += 1
            continue


if __name__ == '__main__':
    permutation_count = int(input('Enter a natural number: '))
    cubic_permutations = main(permutation_count)
    print('The set of {} cubes whose digits permute to each other:'.format(permutation_count))
    for cubic_permutation in cubic_permutations:
        print('  {}'.format(cubic_permutation))
