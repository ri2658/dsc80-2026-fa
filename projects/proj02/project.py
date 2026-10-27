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

    r_coeffs, names = [], []
    for col1, col2, in pairs:
        r_coeffs.append(np.corrcoef(df[col1], df[col2])[0, 1])
        names.append(f'r_{col1}_{col2}')

    return pd.Series(r_coeffs, index=names)


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def create_boxplot(loans):
    loans = loans.copy()

    edges = [580, 670, 740, 800, 850]
    group_names = ['[580, 670)', '[670, 740)', '[740, 800)', '[800, 850)']

    loans['Credit Score Range'] = pd.cut(loans['fico_range_low'], bins = edges, labels = group_names, right = False).astype(str)
    
    loans = loans.rename(columns={'int_rate' : 'Interest Rate (%)', 'term' : 'Loan Length (Months)'})
    loans['Loan Length (Months)'] = loans['Loan Length (Months)'].astype(str)

    fig = px.box(
        loans,
        x = "Credit Score Range", 
        y = "Interest Rate (%)", 
        color = 'Loan Length (Months)',
        title = 'Interest Rate vs. Credit Score',
        category_orders = {'Credit Score Range' : group_names,
                           'Loan Length (Months)' : ['36', '60']},
        color_discrete_map = {'36' : 'purple', '60' : 'gold'}
    )

    return fig


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


def ps_test(loans, N):
    copy = loans.copy()

    w_desc_mean = copy[copy['desc'].notna()]['int_rate'].mean()
    wo_desc_mean = copy[~copy['desc'].notna()]['int_rate'].mean()
    stat = w_desc_mean - wo_desc_mean

    results = np.empty(N)

    has_desc = copy['desc'].notna().to_numpy()
    for i in range(N):
        has_desc = np.random.permutation(has_desc)
        sim_w_desc_mean = copy[has_desc]['int_rate'].mean()
        sim_wo_desc_mean = copy[~has_desc]['int_rate'].mean()
        results[i] =  (sim_w_desc_mean - sim_wo_desc_mean)

    return np.mean(results >= stat)
        

    
def missingness_mechanism():
    # My p value was for 5000 repititions was 0.0182. This is much smaller than
    # 0.05, the accepted value for the threshold to reject the null hypothesis.
    # This indicates that random chance alone cannot explain the observed 
    # discrepancy between rates with and without descriptions. As such, it is
    # possible that the interest rates column may shed some insight on the 
    # missingness of "description".

    return 2

    
def other_missingness():
    # The other column with missing values is 'mths_since_last_delinq', or 
    # presumably "Months Since Last Delinquency". We can immediately rule out 
    # Missing by Design because no other column determines it. The most logical
    # answer is Missing Not at Random because it is possible for a person to 
    # have simply not have had a delinquency in the past. However, we do note 
    # that by scanning the rows, individuals with no deliquency seem to have
    # higher FICO scores. Nonetheless, MNAR is the best answer here.
    return 2


# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


def tax_owed(income, brackets):
    lowers = np.array([tup[1] for tup in brackets])
    rates = np.array([tup[0] for tup in brackets])

    return np.sum(np.maximum(income-lowers, 0)*np.diff(rates, prepend=0))


# ---------------------------------------------------------------------
# QUESTION 6
# ---------------------------------------------------------------------


def clean_state_taxes(state_taxes_raw): 
    state_taxes_raw = state_taxes_raw.dropna(how='all')
    mask = state_taxes_raw['State'].str.contains('\(').fillna(False)
    state_taxes_raw.loc[mask, 'State'] = np.nan
    state_taxes_raw = state_taxes_raw.ffill()
    state_taxes_raw['Rate'] = state_taxes_raw['Rate'].apply(lambda x : 0.00 if x == 'none' else round(float(x.strip('%'))/100, 2))
    state_taxes_raw['Lower Limit'] = state_taxes_raw['Lower Limit'].apply(lambda x : int(x.strip('$').replace(',', '')))

    return state_taxes_raw

# ---------------------------------------------------------------------
# QUESTION 7
# ---------------------------------------------------------------------


def state_brackets(state_taxes):
    return (
        state_taxes
        .groupby('State')
        .apply(
            lambda df : list(zip(df['Rate'], df['Lower Limit']))
        )
        .to_frame('bracket_list')
    )
    
def combine_loans_and_state_taxes(loans, state_taxes):
    # Start by loading in the JSON file.
    # state_mapping is a dictionary; use it!
    import json
    state_mapping_path = Path('data') / 'state_mapping.json'
    with open(state_mapping_path, 'r') as f:
        state_mapping = json.load(f)
        
    # Now it's your turn:

    tax_brackets = state_brackets(state_taxes)
    tax_brackets.index = tax_brackets.index.map(state_mapping)

    return (
        loans
        .merge(
            tax_brackets,
            left_on = 'addr_state',
            right_index = True
        )
        .rename(columns = {'addr_state' : 'State'})
    )


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

    df = loans_with_state_taxes.copy()

    df['federal_tax_owed'] = (
        df['annual_inc']
        .apply(
            lambda income : tax_owed(income, FEDERAL_BRACKETS)
        )
    )

    df['state_tax_owed'] = (
        df
        .apply(
            lambda row : tax_owed(row['annual_inc'], row['bracket_list']),
            axis=1
        )
    )

    df['disposable_income'] = df['annual_inc'] - df['federal_tax_owed'] - df['state_tax_owed']

    return df


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
