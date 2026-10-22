# project.py


import pandas as pd
import numpy as np
np.set_printoptions(threshold=20, suppress=True, legacy='1.21')

from pathlib import Path

import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pd.options.plotting.backend = 'plotly'

from IPython.display import display

# DSC 80 preferred styles
pio.templates["dsc80"] = go.layout.Template(
    layout=dict(
        margin=dict(l=30, r=30, t=30, b=30),
        autosize=True,
        width=600,
        height=400,
        xaxis=dict(showgrid=True),
        yaxis=dict(showgrid=True),
        title=dict(x=0.5, xanchor="center"),
    )
)
pio.templates.default = "simple_white+dsc80"
import warnings
warnings.filterwarnings("ignore")


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def clean_loans(loans):
    loans = loans.copy()
    loans['emp_title'] = loans['emp_title'].apply(lambda x: x.lower().strip())
    loans['emp_title'] = loans['emp_title'].apply(lambda x: 'registered nurse' if x == 'rn' else x)
    loans['issue_d'] = pd.to_datetime(loans['issue_d'])
    loans['term'] = loans['term'].apply(lambda x : int(x.split()[0]))
    loans['term_end'] = loans.apply(
        lambda row: row['issue_d'] + pd.DateOffset(months=row['term']),
        axis=1
        )

    return loans


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def correlations(df, pairs):

    r_coeffs = []
    for pair in pairs:
        x = df[pair[0]]
        y = df[pair[1]]

        r_coeffs.append(np.corrcoef(x, y)[0, 1])
    return pd.Series(r_coeffs)


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def create_boxplot(loans):
    loans = loans.copy()

    edges = [580, 670, 740, 800, 850]
    group_names = ['[580, 670)', '[670, 740)', '[740, 800)', '[800, 850)']

    loans['Credit Score Range'] = pd.cut(loans['fico_range_low'], bins = edges, labels = group_names)
    
    loans = loans.rename(columns={'int_rate' : 'Interest Rate (%)', 'term' : 'Loan Length (Months)'})

    fig = px.box(
        loans,
        x = "Credit Score Range", 
        y = "Interest Rate (%)", 
        color = 'Loan Length (Months)',
        title = 'Interest Rate vs. Credit Score'
    )

    return fig


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def ps_test(loans, N):
    ...
    
def missingness_mechanism():
    ...
    
def other_missingness():
    ...


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def tax_owed(income, brackets):
    ...


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def clean_state_taxes(state_taxes_raw): 
    ...


# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def state_brackets(state_taxes):
    ...
    
def combine_loans_and_state_taxes(loans, state_taxes):
    # Start by loading in the JSON file.
    # state_mapping is a dictionary; use it!
    import json
    state_mapping_path = Path('data') / 'state_mapping.json'
    with open(state_mapping_path, 'r') as f:
        state_mapping = json.load(f)
        
    # Now it's your turn:
    ...


# ---------------------------------------------------------------------
# QUESTION 8
# ---------------------------------------------------------------------


def find_disposable_income(loans_with_state_taxes):
    FEDERAL_BRACKETS = [
     (0.1, 0), 
     (0.12, 11000), 
     (0.22, 44725), 
     (0.24, 95375), 
     (0.32, 182100),
     (0.35, 231251),
     (0.37, 578125)
    ]
    ...


# ---------------------------------------------------------------------
# QUESTION 9
# ---------------------------------------------------------------------


def aggregate_and_combine(loans, keywords, quantitative_column, categorical_column):
    ...


# ---------------------------------------------------------------------
# QUESTION 10
# ---------------------------------------------------------------------


def exists_paradox(loans, keywords, quantitative_column, categorical_column):
    ...
    
def paradox_example(loans):
    return {
        'loans': loans,
        'keywords': [..., ...],
        'quantitative_column': ...,
        'categorical_column': ...
    }
