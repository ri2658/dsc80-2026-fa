# lab.py


from pathlib import Path
import io
import pandas as pd
import numpy as np
np.set_printoptions(legacy='1.21')


# ---------------------------------------------------------------------
# QUESTION 0
# ---------------------------------------------------------------------


def consecutive_ints(ints):
    if len(ints) == 0:
        return False

    for k in range(len(ints) - 1):
        diff = abs(ints[k] - ints[k+1])
        if diff == 1:
            return True

    return False


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def median_vs_mean(nums):
    sorted_nums = sorted(nums) # O(nlogn)
    middle = len(sorted_nums) // 2

    if len(sorted_nums) == 0:
        return True # per DSC 40B, anything related to an empty array is by convention, vaccuously true

    if len(sorted_nums) % 2 == 0:
        return (sorted_nums[middle-1] + sorted_nums[middle])/2 == sum(sorted_nums)/len(sorted_nums)
    return sorted_nums[middle] == sum(sorted_nums)/len(sorted_nums)

# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def n_prefixes(s, n):
    return "".join([s[:i] for i in range(n+1)][::-1])


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def exploded_numbers(ints, n):
    pads = len(str(max(ints)+n))

    return [" ".join(
        [str(num-dx).zfill(pads) for dx in range(n,0,-1)] +
        [str(num+dx).zfill(pads) for dx in range(n+1)]
        ) for num in ints]


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def last_chars(fh):
    last_chars_str = ""
    for line in fh:
        last_chars_str += line.strip()[-1]

    return last_chars_str


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def add_root(A):
    B = A.copy()
    C = np.arange(B.shape[0])
    return B + np.sqrt(C)


def where_square(A):
    return np.array(np.sqrt(A) == np.floor(np.sqrt(A)))


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_loop(matrix, cutoff):
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_np(matrix, cutoff):
    ...


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def growth_rates(A):
    ...

def with_leftover(A):
    ...


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def salary_stats(salary):
    ...


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def parse_malformed(fp):
    ...
