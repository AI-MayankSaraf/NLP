import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Title of the Streamlit app
st.title("Fantastic Word Cloud Generator")

# Text input for the user
text_input = st.text_area("Enter the text for the word cloud", height=200)

# Additional options for customization
st.sidebar.header("Word Cloud Settings")
max_words = st.sidebar.slider("Max number of words", 10, 200, 100)
background_color = st.sidebar.color_picker("Background color", "#ffffff")
colormap = st.sidebar.selectbox(
    "Colormap",
    options=["viridis", "plasma", "inferno", "magma", "cividis", "Blues", "Reds", "Greens", "Purples", "cool", "hot"],
    index=0
)

# Upload an image for the mask
mask_image = st.sidebar.file_uploader("Upload a mask image (PNG format)", type=["png"])

# Button to generate word cloud
if st.button("Generate Word Cloud"):
    if text_input:
        # Set up the mask
        mask = None
        if mask_image is not None:
            # Load the uploaded image and convert it to grayscale
            mask = np.array(Image.open(mask_image))

        # Generate word cloud
        wordcloud = WordCloud(
            max_words=max_words,
            background_color=background_color,
            colormap=colormap,
            mask=mask,
            contour_width=1,  # Optional: adds a border around the shape
            contour_color='black',  # Optional: color for the border
            width=800,
            height=400
        ).generate(text_input)

        # Display the word cloud using Matplotlib
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("Please enter some text to generate the word cloud.")
