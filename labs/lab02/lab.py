# lab.py


import os
import io
from pathlib import Path
import pandas as pd
import numpy as np


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def trick_me():
    return 3


def trick_bool():
    return [4, 10, 13]


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def population_stats(df):
    new = pd.DataFrame()

    new['num_nonnull'] = df.notna().sum()
    new['prop_nonnull'] = df.notna().sum() / df.shape[0]
    new['num_distinct'] = df.nunique()
    new['prop_distinct'] = df.nunique() / df.notna().sum()
    return new


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def most_common(df, N=10):
    r = pd.DataFrame(index=range(N))
    for col in df.columns:
        r[f'{col}_values'] = pd.Series(df[col].value_counts().index[:N])
        r[f"{col}_counts"] = df[col].value_counts().iloc[:N].reset_index(drop=True)
    return r


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def super_hero_powers(powers):
    r = []
    mask = powers.drop(columns='hero_names').sum(axis=1) == 1

    r.append(powers.set_index('hero_names').sum(axis=1).sort_values(ascending=False).head(1).index[0])
    r.append(powers[powers['Flight'] == True].drop(columns='Flight').set_index('hero_names').sum(axis=0).sort_values(ascending=False).head(1).index[0])
    r.append(powers[mask].drop(columns='hero_names').sum(axis=0).sort_values(ascending=False).head(1).index[0])
    return r


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def clean_heroes(heroes):
    cleaned = heroes.replace('-', np.nan).replace(-99, np.nan)
    return cleaned


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def super_hero_stats():
    return ['Onslaught', 'George Lucas', 'bad', 'Marvel Comics', 'NBC - Heroes', 'Groot']


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def clean_universities(df):
    df = df.copy()
    df['institution'] = df['institution'].str.replace('\n', ', ')
    df['broad_impact'] = df['broad_impact'].map(int)
    df['nation'] = df['national_rank'].apply(
        lambda x: 
        'United States' if x.split(', ')[0] == 'USA' else 
        'United Kingdom' if x.split(', ')[0] == 'UK' else 
        'Czech Republic' if x.split(', ')[0] == 'Czechia' 
        else x.split(', ')[0])
    df['national_rank_cleaned'] = df['national_rank'].apply(lambda x: int(x.split(', ')[1]))
    df.drop(columns=['national_rank'], inplace=True)
    df['is_r1_public'] = (df['control'].apply(lambda x: False if pd.isna(x) else 'Public' in x )) & (df[['control', 'city', 'state']].notna().all(axis=1))

    return df

def university_info(cleaned):
    counts = cleaned['state'].value_counts()
    states_more_than_3 = cleaned.copy()[cleaned['state'].isin(counts[counts >= 3].index)]
    r = []

    top_100 = cleaned[cleaned['world_rank'] <= 100]
    
    not_r1 = ~cleaned['is_r1_public']
    cleaned_copy = cleaned.copy()
    cleaned_copy['not_r1'] = not_r1
    
    top_1_in_nation = cleaned[cleaned['national_rank_cleaned'] == 1]

    r.append(
        states_more_than_3[['state', 'score']].groupby('state').mean().sort_values(by='score', ascending=True).index[0]
    )
    r.append(
        top_100[top_100['quality_of_faculty'] <= 100].shape[0]/top_100.shape[0]
    )
    r.append(
        (cleaned_copy[['state', 'not_r1']].groupby('state').mean()['not_r1'] >= 0.5).sum(axis=0)
    )
    r.append(
        top_1_in_nation.sort_values(by='world_rank', ascending=False)['institution'].iloc[0]
    )
    return r





