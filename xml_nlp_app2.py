import streamlit as st
import xml.etree.ElementTree as ET
import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
from nltk import ne_chunk, pos_tag
from nltk.tree import Tree 


# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('words')
 
import subprocess
import importlib.util 
# Check if the model is installed, and install if necessary
model_name = "en_core_web_sm"
if not importlib.util.find_spec(model_name):
    subprocess.run(["python", "-m", "spacy", "download", model_name])

# Load spaCy model for NER
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 2000000  # Adjust as needed

# Function to parse XML content from uploaded files
def parse_xml_files(uploaded_files, tag_name=None):
    texts = []
    for uploaded_file in uploaded_files:
        try:
            tree = ET.parse(uploaded_file)
            root = tree.getroot()
            for elem in root.iter(tag_name) if tag_name else root.iter():
                if elem.text:
                    texts.append(elem.text.strip())
        except Exception as e:
            st.warning(f"Could not parse {uploaded_file.name}: {e}")
    return " ".join(texts)

# NLP processing with Named Entity Recognition and word frequency
def process_text(text):
    # Tokenize and clean text
    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Named Entity Recognition
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Word frequency
    word_freq = Counter(filtered_words)
    return word_freq, entities

# Generate Word Cloud
def generate_wordcloud(word_freq):
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(word_freq)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)

# Topic Modeling with Gensim's LDA
def topic_modeling(texts, num_topics=3):
    # Tokenize and remove stopwords for each document
    texts_tokenized = [[word for word in word_tokenize(text.lower()) if word.isalnum() and word not in stopwords.words('english')]
                       for text in texts]
    
    # Prepare dictionary and corpus
    dictionary = Dictionary(texts_tokenized)
    corpus = [dictionary.doc2bow(text) for text in texts_tokenized]
    
    # Train LDA model
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15)
    topics = lda_model.print_topics(num_words=5)
    return topics

# Streamlit app interface
def main():
    st.title("XML Processing + NLP Technique")

    # Allow users to upload multiple XML files
    uploaded_files = st.file_uploader("Upload XML Files", type="xml", accept_multiple_files=True)
    tag_name = st.text_input("Specify XML Tag to Extract Text From (optional)")
    num_topics = st.slider("Number of Topics for Topic Modeling", 2, 10, 3)

    if uploaded_files:
        st.write("Processing uploaded XML files...")
        combined_text = parse_xml_files(uploaded_files, tag_name)
        
        if combined_text:
            # NLP Processing
            st.write("Applying NLP processing...")
            word_freq, entities = process_text(combined_text)
            
            # Display Word Frequency
            st.subheader("Most Common Words")
            st.write(word_freq.most_common(10))
            
            # Generate Word Cloud
            st.subheader("Word Cloud")
            generate_wordcloud(word_freq)
            
            # Named Entity Recognition
            st.subheader("Named Entities")
            st.write(entities)
            
            # Topic Modeling
            st.subheader("Topic Modeling")
            # Split combined text for topic modeling
            topics = topic_modeling([combined_text], num_topics=num_topics)
            for idx, topic in enumerate(topics):
                st.write(f"Topic {idx+1}: {topic}")

if __name__ == "__main__":
    main()
