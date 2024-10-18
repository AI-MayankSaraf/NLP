# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 18:55:36 2024

@author: Hp
"""

import streamlit as st
from nltk import *
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk

# Download NLTK data (only needed for the first time)
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')
#nltk.download('maxent_ne_chunker')
#nltk.download('words')
#nltk.download('stopwords')

# Streamlit app
st.title("NLTK Text Processing App")

# Input text area
user_input = st.text_area("Enter text for processing", "Type your text here...")

# Tokenization
if st.checkbox("Show Tokenization"):
    words = word_tokenize(user_input)
    sentences = sent_tokenize(user_input)
    st.write("Words:", words)
    st.write("Sentences:", sentences)

# Part-of-Speech (POS) Tagging
if st.checkbox("Show Part-of-Speech Tagging"):
    words = word_tokenize(user_input)
    pos_tags = pos_tag(words)
    st.write(pos_tags)

# Named Entity Recognition (NER)
if st.checkbox("Show Named Entity Recognition"):
    words = word_tokenize(user_input)
    pos_tags = pos_tag(words)
    named_entities = ne_chunk(pos_tags)
    st.write(named_entities)

# Stopwords Removal
if st.checkbox("Show Stopwords Removal"):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(user_input)
    filtered_words = [word for word in words if word.lower() not in stop_words]
    st.write("Filtered Words:", filtered_words)
