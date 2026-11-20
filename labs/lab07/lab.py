# lab.py


import pandas as pd
import numpy as np
np.set_printoptions(legacy='1.21')
import os
import re


# ---------------------------------------------------------------------
# QUESTION 1
# ---------------------------------------------------------------------


def match_1(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_1("abcde]")
    False
    >>> match_1("ab[cde")
    False
    >>> match_1("a[cd]")
    False
    >>> match_1("ab[cd]")
    True
    >>> match_1("1ab[cd]") # Including a substring ("ab[cd]") that satisfies the pattern does not qualify as a match.
    False
    >>> match_1("ab[cd]ef")
    True
    >>> match_1("1b[#d] _")
    True
    """
    pattern = r'^.{2}\[.{2}\].*'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_2(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_2("(123) 456-7890")
    False
    >>> match_2("858-456-7890")
    False
    >>> match_2("(858)45-7890")
    False
    >>> match_2("(858) 456-7890")
    True
    >>> match_2("(858)456-789")
    False
    >>> match_2("(858)456-7890")
    False
    >>> match_2("a(858) 456-7890")
    False
    >>> match_2("(858) 456-7890b")
    False
    """
    pattern = r'^\(858\)\s\d{3}-\d{4}$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_3(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_3("qwertsd?")
    True
    >>> match_3("qw?ertsd?")
    True
    >>> match_3("ab c?")
    False
    >>> match_3("ab   c ?")
    True
    >>> match_3(" asdfqwes ?")
    False
    >>> match_3(" adfqwes ?")
    True
    >>> match_3(" adf!qes ?")
    False
    >>> match_3(" adf!qe? ")
    False
    """
    pattern = r'^[\w\s\?]{5,9}\?$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_4(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_4("$$AaaaaBbbbc")
    True
    >>> match_4("$!@#$aABc")
    True
    >>> match_4("$a$aABc")
    False
    >>> match_4("$iiuABc")
    False
    >>> match_4("123$$$Abc")
    False
    >>> match_4("$$Abc")
    True
    >>> match_4("$qw345t$AAAc")
    False
    >>> match_4("$s$Bca")
    False
    >>> match_4("$!@$")
    False
    """
    pattern = r'^\$[^abc\$]*\$[aA]+[bB]+[cC]+$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_5(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_5("dsc80.py")
    True
    >>> match_5("dsc80py")
    False
    >>> match_5("dsc80..py")
    False
    >>> match_5("dsc80+.py")
    False
    """
    pattern = r'^[a-zA-Z_]\w*\.py$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_6(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_6("aab_cbb_bc")
    False
    >>> match_6("aab_cbbbc")
    True
    >>> match_6("aab_Abbbc")
    False
    >>> match_6("abcdef")
    False
    >>> match_6("ABCDEF_ABCD")
    False
    """
    pattern = r'^[a-z]+_[a-z]+$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_7(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_7("_abc_")
    True
    >>> match_7("abd")
    False
    >>> match_7("bcd")
    False
    >>> match_7("_ncde")
    False
    """
    pattern = r'^_.*_$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None



def match_8(string):
    """
    DO NOT EDIT THE DOCSTRING!
    >>> match_8("ASJDKLFK10ASDO")
    False
    >>> match_8("ASJDKLFK0ASDo!!!!!!! !!!!!!!!!")
    True
    >>> match_8("JKLSDNM01IDKSL")
    False
    >>> match_8("ASDKJLdsi0SKLl")
    False
    >>> match_8("ASDJKL9380JKAL")
    True
    """
    pattern = r'^[^O^i^1]{1,}$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None



def match_9(string):
    '''
    DO NOT EDIT THE DOCSTRING!
    >>> match_9('NY-32-NYC-1232')
    True
    >>> match_9('ca-23-SAN-1231')
    False
    >>> match_9('MA-36-BOS-5465')
    False
    >>> match_9('CA-56-LAX-7895')
    True
    >>> match_9('NY-32-LAX-0000') # If the state is NY, the city can be any 3 letter code, including LAX or SAN!
    True
    >>> match_9('TX-32-SAN-4491')
    False
    '''
    pattern = r'^((CA-\d{2}-(SAN|LAX))|(NY-\d{2}-[A-Z]{3}))-\d{4}$'

    # Do not edit following code
    prog = re.compile(pattern)
    return prog.search(string) is not None


def match_10(string):

    '''
    DO NOT EDIT THE DOCSTRING!
    >>> match_10('ABCdef')
    ['bcd']
    >>> match_10(' DEFaabc !g ')
    ['def', 'bcg']
    >>> match_10('Come ti chiami?')
    ['com', 'eti', 'chi']
    >>> match_10('and')
    []
    >>> match_10('Ab..DEF')
    ['bde']
    
    '''
    string = string.lower()
    string = re.sub(r'[\Wa]', '', string)

    return re.findall(r'...', string)


# ---------------------------------------------------------------------
# QUESTION 2
# ---------------------------------------------------------------------


def extract_personal(s):
    email_pattern = r'\w+@\w+(?:\.\w+)+'
    ssn_pattern = r'\d{3}-\d{2}-\d{4}'
    bitcoin_pattern = r'\w{26,}'
    street_pattern = r'\d+(?: \w+)+'

    tup = (
        re.findall(email_pattern , s),
        re.findall(ssn_pattern, s),
        re.findall(bitcoin_pattern, s),
        re.findall(street_pattern, s)
    )

    return tup


# ---------------------------------------------------------------------
# QUESTION 3
# ---------------------------------------------------------------------


def hashtag_list(tweet_text):

    return tweet_text.transform(lambda tweet : re.findall(r'\#(\S+)', tweet))

def most_common_hashtag(tweet_lists):
    most_common = tweet_lists.explode().value_counts().index[0]

    return tweet_lists.transform(lambda hastag_list : most_common if len(hastag_list) > 0 else np.nan)


def create_features(tweets):
    tweets = tweets.copy(   )

    def clean(text):
        text = re.sub(r'\#(\S+)', ' ', text)
        text = re.sub(r'@\w+', ' ', text)
        text = re.sub(r'https?://\S+', ' ', text)
        text = re.sub(r'\bRT\b', ' ', text)
        text = re.sub(r'[^a-zA-Z0-9\s]', ' ', text)
        text = text.lower()
        text = re.sub(r'\s+', ' ', text).strip()

        return text

    tweet_text = tweets['text']

    tweets['num_hashtags'] = hashtag_list(tweet_text).apply(lambda tweet_list : len(tweet_list))
    tweets['common_hashtag'] = most_common_hashtag(hashtag_list(tweet_text))
    tweets['num_tags'] = tweet_text.transform(lambda tweet : len(re.findall(r'@\w+', tweet)))
    tweets['num_links'] = tweet_text.transform(lambda tweet : len(re.findall(r'https?://\S+', tweet)))
    tweets['is_retweet'] = tweet_text.transform(lambda tweet : bool(re.findall(r'\bRT\b', tweet)))
    tweets['text'] = tweet_text.transform(lambda tweet : clean(tweet))

    return tweets
