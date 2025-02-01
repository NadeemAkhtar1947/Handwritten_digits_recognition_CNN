import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas


# Set Streamlit page configuration as the first command
st.set_page_config(page_title="Handwritten Digit Recognition", layout="wide")

# Add a Markdown component to display the greeting

links_row = "<a href='https://www.linkedin.com/in/nadeem-akhtar-/' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/linkedin.png' width='30'></a>" \
            " | " \
            "<a href='https://github.com/NadeemAkhtar1947' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/github.png' width='30'></a>" \
            " | " \
            "<a href='https://www.kaggle.com/mdnadeemakhtar/code' target='_blank'>" \
            "<img src='https://www.kaggle.com/static/images/site-logo.png' width='30'></a>" \
            " | " \
            "<a href='https://nsde.netlify.app/' target='_blank'>" \
            "<img src='https://img.icons8.com/color/48/000000/globe--v1.png' width='30'></a>"

# Display the links row using Markdown
st.markdown(links_row, unsafe_allow_html=True)

# Load the trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("mnist_model.h5")

model = load_model()

# Function to predict digit
def predictDigit(image):
    image = ImageOps.grayscale(image)  # Convert to grayscale
    img = image.resize((28, 28))  # Resize to match MNIST input shape
    img = np.array(img, dtype='float32') / 255.0  # Normalize
    img = img.reshape((1, 28, 28, 1))  # Reshape for model input
    pred = model.predict(img)
    return np.argmax(pred[0])  # Get the predicted digit

# Streamlit UI
st.header("📝 Handwritten Digit Recognition")
st.subheader("🖌️ Draw a digit on the canvas and click 'Predict Now'")

# Canvas settings
stroke_width = st.slider("✏️ Select Stroke Width", 1, 30, 15)
stroke_color = "#FFFFFF"  # White stroke
bg_color = "#000000"  # Black background

# Create canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=200,
    width=200,
    key="canvas",
)

# Predict button
if st.button("🚀 Predict Now"):
    if canvas_result.image_data is not None:
        input_numpy_array = np.array(canvas_result.image_data)
        input_image = Image.fromarray(input_numpy_array.astype('uint8'), 'RGBA').convert('L')
        result = predictDigit(input_image)
        st.success(f"🎯 **Predicted Digit: {result}**")
    else:
        st.warning("⚠️ Please draw a digit on the canvas.")

# Sidebar
st.sidebar.title("ℹ️ About")
st.sidebar.info("🤖 **Handwritten Digit Recognition** using a CNN model trained on the MNIST dataset.")
st.sidebar.markdown("📌 **How it Works?**\n1. Draw a digit (0-9) on the canvas.\n2. Click **'Predict Now'**.\n3. The model will predict the digit.")
st.sidebar.text("👨‍💻 Created by Nadeem")

