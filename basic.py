# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:23:12 2024

@author: Hp
"""

from nltk.tokenize import word_tokenize
s = '''Good muffins cost $3.88\nin New York.  Please buy me two of them.\n\nThanks.'''
result = word_tokenize(s)  
print(result)
print()

from nltk.tokenize import wordpunct_tokenize
s = '''Good muffins cost $3.88\nin New York.  Please buy me two of them.\n\nThanks.'''
result = wordpunct_tokenize(s)  
print(result)
print()

from nltk.tokenize import sent_tokenize, word_tokenize
result = sent_tokenize(s) 
print(result)
print()
print([word_tokenize(t) for t in sent_tokenize(s)])
print()

from nltk.tokenize import WhitespaceTokenizer
result = list(WhitespaceTokenizer().span_tokenize(s))
print(result)
print()

