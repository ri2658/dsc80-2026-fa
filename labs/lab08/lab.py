# lab.py


import pandas as pd
import numpy as np
np.set_printoptions(legacy='1.21')
import itertools
import plotly.express as px
import statsmodels.api as sm
from pathlib import Path
from sklearn.preprocessing import Binarizer, QuantileTransformer, FunctionTransformer

import warnings
warnings.filterwarnings('ignore')


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def best_transformation():
    return 1


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def create_ordinal(df):

    map_list = [
        {
        'Fair' : 0,
        'Good' : 1,
        'Very Good' : 2,
        'Premium' : 3,
        'Ideal' : 4
        },
        {
            'J' : 0,
            'I' : 1,
            'H' : 2,
            'G' : 3,
            'F' : 4,
            'E' : 5,
            'D' : 6
        },
        {
            'I1' : 0,
            'SI2' : 1,
            'SI1' : 2,
            'VS2' : 3,
            'VS1' : 4,
            'VVS2' : 5,
            'VVS1' : 6,
            'IF' : 7
        }
    ]

    new = pd.DataFrame()

    for i, column in enumerate(['cut', 'color', 'clarity']):
        new[f'ordinal_{column}'] = df[column].map(map_list[i])

    return new

# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def create_one_hot(df):
    new = pd.DataFrame()

    for column in ['cut', 'color', 'clarity']:
        for i, subcolumn in enumerate(df[column].unique()):
            new[f'one_hot_{column}_{subcolumn}'] = (df[column] == subcolumn).astype(int)

    return new

def create_proportions(df):
    new = pd.DataFrame()
    ordinals = create_ordinal(df)

    for column in ['cut', 'color', 'clarity']:
            new[f'proportion_{column}'] = ordinals[f'ordinal_{column}'].map(ordinals[f'ordinal_{column}'].value_counts(normalize=True))

    return new


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def create_quadratics(df):
    quantitative_variables = ['carat', 'depth', 'table', 'x', 'y', 'z']

    return pd.DataFrame(
        {
            f'{combination[0]} * {combination[1]}' : 
            df[combination[0]].astype(float)*df[combination[1]].astype(float)
            for combination in itertools.combinations(quantitative_variables, 2)
        }
    )

# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def comparing_performance():
    return [
        0.8493305264354858, 
        1548.5331930613174,
        'x',
        'carat * x',
        'ordinal_color',
        1434.8400089047336
    ]


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


class TransformDiamonds(object):
    
    def __init__(self, diamonds):
        self.data = diamonds
        
    # Question 6.1
    def transform_carat(self, data):
        ...
    
    # Question 6.2
    def transform_to_quantile(self, data):
        ...
    
    # Question 6.3
    def transform_to_depth_pct(self, data):
        ...
