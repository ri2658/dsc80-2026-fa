# lab.py


import pandas as pd
import numpy as np
import io
from pathlib import Path
import os


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def prime_time_logins(login):
    times = pd.to_datetime(login['Time'])
    is_prime = (times.dt.hour >= 16) & (times.dt.hour < 20)

    return login.assign(Time=is_prime).groupby('Login Id')[['Time']].sum()


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def count_frequency(login):

    def freq(times):
        now = pd.Timestamp('2024-01-31 23:59:00')
        total_days = (now - times.min()).days
        logged_in = times.count()

        return logged_in / total_days

    return (
        login
        .assign(Time=pd.to_datetime(login['Time']))
        .groupby('Login Id')['Time']
        .agg(freq)
    )


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def cookies_null_hypothesis():
    return [1,2]
                         
def cookies_p_value(N):
    prop_burnt_obs = 15/250

    # [unburnt, burnt]
    prop_burnt = (np.random.multinomial(250, [0.96, 0.04], N)[:, 1])/250

    return np.mean(prop_burnt >= prop_burnt_obs)


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def car_null_hypothesis():
    return [1, 4]

def car_alt_hypothesis():
    return [2, 6]

def car_test_statistic():
    return [1, 4]

def car_p_value():
    return 4

# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def superheroes_test_statistic():
    return [1, 2]
    
def bhbe_col(heroes):
    blondes = heroes['Hair color'].str.lower().str.contains('blond')
    blue_eyed = heroes['Eye color'].str.lower().str.contains('blue')
    return blondes & blue_eyed

def superheroes_observed_statistic(heroes):
    mask = bhbe_col(heroes)

    blue_blonde = heroes[mask]
    prop_good_blue_blond = (blue_blonde['Alignment'] == 'good').mean()
    
    return prop_good_blue_blond

def simulate_bhbe_null(heroes, N):
    mask = bhbe_col(heroes)
    sample_size = mask.sum()

    prop_good_population = (heroes['Alignment'] == 'good').mean()
    prop_bad_population = 1 - prop_good_population

    prop_good_null = np.random.multinomial(sample_size, [prop_good_population, prop_bad_population], N)[:, 0]/sample_size

    return prop_good_null

def superheroes_p_value(heroes):

    simulated = simulate_bhbe_null(heroes, 100_000)
    observed = superheroes_observed_statistic(heroes)

    p = np.mean(observed <= simulated)
    return [p, 'Reject' if p < 0.01 else 'Fail to reject']

# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def diff_of_means(data, col='orange'):
    yorkville_mean = data[data['Factory'] == 'Yorkville'][col].mean()
    waco_mean = data[data['Factory'] == 'Waco'][col].mean()

    return np.abs(yorkville_mean - waco_mean)

def simulate_null(data, col='orange'):
    shuffled = data.assign(Factory=np.random.permutation(data['Factory']))

    return diff_of_means(shuffled, col)

def color_p_value(data, col='orange'):
    obs_stat = diff_of_means(data, col)

    simulated_results = np.array([simulate_null(data, col) for _ in range(1000)])

    return np.mean(simulated_results >= obs_stat)


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def ordered_colors():
    ...


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


    
def same_color_distribution():
    ...


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def perm_vs_hyp():
    ...
