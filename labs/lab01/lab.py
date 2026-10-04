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
    masks = [sum([matrix[i][j] for i in range(matrix.shape[0])])/matrix.shape[0] > cutoff for j  in range(matrix.shape[1])]
    return matrix[:, masks]

# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def filter_cutoff_np(matrix, cutoff):
    masks = np.mean(matrix, axis=0) > cutoff
    return matrix[:, masks]


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def growth_rates(A):
    A_padded = np.append(np.append(np.array([0]), A), np.array([0]))
    B = A_padded.copy()
    diffs = B[1:] - A_padded[:-1]
    rate = (diffs/A_padded[:-1])[1:-1]
    return np.round(rate, 2)

def with_leftover(A):
    cumulative_cost = np.cumsum(A)
    leftovers = 20 - cumulative_cost
    leftover = leftovers[sum(leftovers > 0) - 1]
    if leftover == 0:
        return -1
    return int(np.ceil(np.min(A)/leftover))

# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def salary_stats(salary):
    highest_salary_guy = salary.sort_values(by='Salary', ascending=False)['Player'].iloc[0]
    highest_salary_guys_team = salary[salary['Player'] == highest_salary_guy]['Team'].iloc[0]
    statistics = {
        'num_players': salary.shape[0],
        'num_steams': salary.groupby('Team').count().shape[0],
        'total_salary': salary['Salary'].sum(),
        'highest_salary': highest_salary_guy,
        'avg_los': salary[['Team', 'Salary']].groupby('Team').mean().loc['Los Angeles Lakers'].iloc[0],
        'fifth_lowest': salary.sort_values(by='Salary', ascending=True)['Player'].iloc[5],
        'duplicates': len(np.unique(np.array(list(map(lambda name : name.split()[1], salary['Player'].to_list()))))) != salary.shape[0],
        'total_highest': salary[salary['Team'] == highest_salary_guys_team]['Salary'].sum()
    }
    return pd.Series(statistics)

# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def parse_malformed(fp):
    ...
