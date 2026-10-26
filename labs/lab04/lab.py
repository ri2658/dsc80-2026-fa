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
    ...

def car_alt_hypothesis():
    ...

def car_test_statistic():
    ...

def car_p_value():
    ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def superheroes_test_statistic():
    ...
    
def bhbe_col(heroes):
    ...

def superheroes_observed_statistic(heroes):
    ...

def simulate_bhbe_null(heroes, N):
    ...

def superheroes_p_value(heroes):
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def diff_of_means(data, col='orange'):
    ...


def simulate_null(data, col='orange'):
    ...


def color_p_value(data, col='orange'):
    ...


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
