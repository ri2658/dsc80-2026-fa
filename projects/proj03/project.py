# project.py


import pandas as pd
import numpy as np
from pathlib import Path
import re
import requests
import time


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def get_book(url):
    time.sleep(0.5)

    res = requests.get(url)
    html_text = res.text

    pattern = r'\*\*\* ?START OF (?:THE|THIS) PROJECT GUTENBERG EBOOK[^\n]*?\*\*\*(.*?)\*\*\* ?END OF (?:THE|THIS) PROJECT GUTENBERG EBOOK[^\n]*?\*\*\*'

    match = re.search(pattern, html_text, re.DOTALL)

    if match:
        extracted_text = match.group(1).strip()
        return extracted_text.replace('\r\n', '\n')


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def tokenize(book_string):
    pattern = r'\n{2,}'

    text = '\x02' + re.sub(
        pattern,
        ' \x02 \x03 ',
        book_string.strip()
    ) + '\x03'

    tokens = re.findall(r'\w+|[^\w\s]', text)
    return tokens


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


class UniformLM(object):


    def __init__(self, tokens):

        self.mdl = self.train(tokens)
        
    def train(self, tokens):
        return pd.Series(pd.Series(tokens).unique()).value_counts(normalize=True)
    
    def probability(self, words):
        probs = np.array([self.mdl[word] if word in self.mdl.index else 0 for word in words])
        return float(np.prod(probs))
        
    def sample(self, M):
            mdl_dict = self.mdl.to_dict()
            return ' '.join(np.random.choice(list(mdl_dict.keys()), size=M, replace=True, p=list(mdl_dict.values())))


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


class UnigramLM(object):


    def __init__(self, tokens):
        self.mdl = self.train(tokens)
        
    def train(self, tokens):
        return pd.Series(tokens).value_counts(normalize=True)
    
    def probability(self, words):
        probs = np.array([self.mdl[word] if word in self.mdl.index else 0 for word in words])
        return float(np.prod(probs))
        
    def sample(self, M):
            mdl_dict = self.mdl.to_dict()
            return ' '.join(np.random.choice(list(mdl_dict.keys()), size=M, replace=True, p=list(mdl_dict.values())))



# ---------------------------------------------------------------------
# QUESTION 5
# ---------------------------------------------------------------------


class NGramLM(object):
    
    def __init__(self, N, tokens):
        # You don't need to edit the constructor,
        # but you should understand how it works!
        
        self.N = N

        ngrams = self.create_ngrams(tokens)

        self.ngrams = ngrams
        self.mdl = self.train(ngrams)

        if N < 2:
            raise Exception('N must be greater than 1')
        elif N == 2:
            self.prev_mdl = UnigramLM(tokens)
        else:
            self.prev_mdl = NGramLM(N-1, tokens)

    def create_ngrams(self, tokens):
        if len(tokens) == self.N:
            return tokens

        n_grams = []

        i=0
        while i+self.N <= len(tokens):
            n_grams.append(tuple(tokens[i:i+self.N]))
            i += 1

        return n_grams
        
    def train(self, ngrams):
        df = pd.DataFrame()
        df['ngram'] = pd.Series(ngrams)
        df['n1gram'] = df['ngram'].apply(lambda tup : tup[:-1])

        ngram_counts = df.groupby('ngram').transform('size')
        n1gram_counts = df.groupby('n1gram').transform('size')

        df['prob'] = ngram_counts/n1gram_counts
        df = df.drop_duplicates().sort_values('prob').reset_index(drop=True)

        return df
    
    def probability(self, words):
        ...
    

    def sample(self, M):
        ...
