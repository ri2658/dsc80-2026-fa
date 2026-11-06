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
        ...
    
    def probability(self, words):
        ...
        
    def sample(self, M):
        ...


# ---------------------------------------------------------------------
# QUESTION 4
# ---------------------------------------------------------------------


class UnigramLM(object):
    
    def __init__(self, tokens):
        self.mdl = self.train(tokens)
    
    def train(self, tokens):
        ...
    
    def probability(self, words):
        ...
        
    def sample(self, M):
        ...


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
        ...
        
    def train(self, ngrams):
        ...
    
    def probability(self, words):
        ...
    

    def sample(self, M):
        ...
