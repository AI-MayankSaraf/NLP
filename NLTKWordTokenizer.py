# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:23:12 2024

@author: Hp
"""
from nltk.tokenize import word_tokenize
s1 = "On a $50,000 mortgage of 30 years at 8 percent, the monthly payment would be $366.88."
print(word_tokenize(s1))
##['On', 'a', '$', '50,000', 'mortgage', 'of', '30', 'years', 'at', '8', 'percent', ',', 'the', 'monthly', 'payment', 'would', 'be', '$', '366.88', '.']
s2 = "\"We beat some pretty good teams to get here,\" Slocum said."
print(word_tokenize(s2))
#['``', 'We', 'beat', 'some', 'pretty', 'good', 'teams', 'to', 'get', 'here', ',', "''", 'Slocum', 'said', '.']
s3 = "Well, we couldn't have this predictable, cliche-ridden, \"Touched by an Angel\" (a show creator John Masius worked on)) wanna-be if she didn't."
print(word_tokenize(s3))
#['Well', ',', 'we', 'could', "n't", 'have', 'this', 'predictable', ',', 'cliche-ridden', ',', '``', 'Touched', 'by', 'an', 'Angel', "''", '(', 'a', 'show', 'creator', 'John', 'Masius', 'worked', 'on', '))', 'wanna-be', 'if', 'she', 'did', "n't", '.']
s4 = "I cannot cannot work under these conditions!"
print(word_tokenize(s4))
#['I', 'can', 'not', 'can', 'not', 'work', 'under', 'these', 'conditions', '!']
s5 = "The company spent $30,000,000 last year."
print(word_tokenize(s5))
#['The', 'company', 'spent', '$', '30,000,000', 'last', 'year', '.']
s6 = "The company spent 40.75% of its income last year."
print(word_tokenize(s6))
#['The', 'company', 'spent', '40.75', '%', 'of', 'its', 'income', 'last', 'year', '.']
s7 = "He arrived at 3:00 pm."
print(word_tokenize(s7))
#['He', 'arrived', 'at', '3:00', 'pm', '.']
s8 = "I bought these items: books, pencils, and pens."
print(word_tokenize(s8))
#['I', 'bought', 'these', 'items', ':', 'books', ',', 'pencils', ',', 'and', 'pens', '.']
s9 = "Though there were 150, 100 of them were old."
print(word_tokenize(s9))
#['Though', 'there', 'were', '150', ',', '100', 'of', 'them', 'were', 'old', '.']
s10 = "There were 300,000, but that wasn't enough."
print(word_tokenize(s10))
#['There', 'were', '300,000', ',', 'but', 'that', 'was', "n't", 'enough', '.']
s11 = "It's more'n enough."
print(word_tokenize(s11))
#['It', "'s", 'more', "'n", 'enough', '.']

