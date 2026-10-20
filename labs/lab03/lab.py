# lab.py


import os
import io
from pathlib import Path
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def read_linkedin_survey(dirname):

    df = pd.DataFrame()

    path = Path(dirname)

    for child in path.iterdir():
        try:
            child_df = pd.read_csv(child)
            child_df.columns = [colname.lower().strip().replace('_', '').replace(' ', '') for colname in child_df.columns]
            df = pd.concat([df, child_df], axis=0, ignore_index=True).fillna('')
        except FileNotFoundError:
            raise(FileNotFoundError)

    df = df.rename(columns={
        'firstname' : 'first name',
        'lastname' : 'last name',
        'currentcompany' : 'current company',
        'jobtitle' : 'job title',
        'email' : 'email',
        'university' : 'university'
    })

    return df.reset_index()[['first name', 'last name', 'current company', 'job title', 'email', 'university']]


def com_stats(df):
    results = []

    copy = df.copy()

    copy['title length'] = copy['job title'].apply(lambda x: len(x))
    
    results.append(
        df[df['university'].str.contains('Ohio')]['job title'].str.contains('Programmer').mean()
    )
    results.append(
        len(list(filter(lambda x: x[-8:] == 'Engineer', df['job title'].unique())))
    )
    results.append(
        copy.sort_values(by='title length', ascending=False)['job title'].head(1).iloc[0]
    )
    results.append(
        df['job title'].str.lower().str.contains('manager').sum()
    )

    return results



# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def read_student_surveys(dirname):
    df = pd.DataFrame({'id': np.arange(1, 1001)})

    path = Path(dirname)

    for child in path.iterdir():
        try:
            child_df = pd.read_csv(child)
            df = pd.merge(df, child_df, on='id')
        except FileNotFoundError:
            raise(FileNotFoundError)

    return df.set_index('id')


def check_credit(df):
    r = df[['name']].copy()

    valid = (df.notnull() & (df != '(no genres listed)'))

    r['ec'] = 5*(df[valid].notnull().drop(columns='name').sum(axis=1) >= 0.5*valid.shape[1]) + min(2, sum((df[valid].notnull().drop(columns='name').sum(axis=0)/valid.shape[0]) >= 0.90))

    return r


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def most_popular_procedure(pets, procedure_history):
    ...

def pet_name_by_owner(owners, pets):
    ...


def total_cost_per_city(owners, pets, procedure_history, procedure_detail):
    ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def average_seller(sales):
    ...

def product_name(sales):
    ...

def count_product(sales):
    ...

def total_by_month(sales):
    ...
