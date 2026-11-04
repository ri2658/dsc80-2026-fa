# lab.py


from pathlib import Path
import pandas as pd
import numpy as np
from scipy import stats


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def after_purchase():
    # 1. NMAR; unhappier people are more likely to respond. 

    # 2. MD; if this 'customer_id' did not make a purchase, then they are 
    # guaranteed to have not answered the satisfaction form.

    # 3. MAR because if they returned the item, they are likely to have not 
    # liked the item to begin with. However, this not give a guarantee, so it's 
    # not MD.

    # 4. Same as 1.

    # 5. MAR because higher-priced items are likely of higher quality and are
    # less likely to displease a customer.
    
    return ['NMAR', 'MD', 'NMAR', 'MAR', 'MAR']


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def multiple_choice():
    # 1. MAR; the questions says the column is 'OFTEN missing for UCSD 
    # students.' This means the missingness depends on the restaurant's presence 
    # on- or off-campus. 

    # 2. MAR; certain ethnicities can CHOOSE to have middle names. NMAR is 
    # possible, as people that have a middle name are more likely to report it, 
    # but because we're in a database of student data, we can assume that 
    # students with a middle name will always report it.

    # 3. MD; if 'number_of_sports_played' is zero, then they can't possibly have
    # a 'sport_previously_played'.

    # 4. NMAR; those unsatisifed are more likely to answer.

    # 5. DUO requires a phone number, so it's not on the students. It must've 
    # been some random event that caused the data to disappear.

    return ['MAR', 'MAR', 'MD', 'NMAR', 'MCAR']


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------



def first_round():
    ...


def second_round():
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def verify_child(heights):
    ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def cond_single_imputation(new_heights):
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def quantitative_distribution(child, N):
    ...


def impute_height_quant(child):
    ...


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def answers():
    ...
