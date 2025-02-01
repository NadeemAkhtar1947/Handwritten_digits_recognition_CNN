# 🖋️ Handwritten Digit Recognition using CNN

This project is a **Handwritten Digit Recognition** system built using a Convolutional Neural Network (CNN) trained on the MNIST dataset. It allows users to draw a digit on a canvas, and the model predicts the digit in real-time. The project is deployed using **Streamlit** for an interactive web interface.

---

## 🚀 Features

- **Interactive Canvas**: Draw digits (0-9) on a canvas using your mouse or touchpad.
- **Real-Time Prediction**: The trained CNN model predicts the digit instantly.
- **User-Friendly Interface**: Built with Streamlit for a seamless user experience.
- **Deployable**: Easily deployable on platforms like Streamlit Cloud, Heroku, or locally.

---

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **TensorFlow/Keras**: For building and training the CNN model.
- **Streamlit**: For creating the web interface.
- **NumPy**: For numerical computations.
- **PIL (Pillow)**: For image processing.
- **Streamlit-Drawable-Canvas**: For the interactive drawing canvas.

---

## 📂 Repository Structure

handwritten-digit-recognition/
├── app.py # Streamlit application code
├── mnist_model.h5 # Trained CNN model
├── README.md # Project documentation
├── requirements.txt # Python dependencies
└── images/ # Screenshots or assets (optional)

---

## 🏃‍♂️ How to Run Locally

### Step 1: Clone the Repository
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/NadeemAkhtar1947/handwritten-digit-recognition.git
cd handwritten-digit-recognition

### Step 2: Install Dependencies
Install the required Python packages using pip:
pip install -r requirements.txt

Step 3: Run the Streamlit App
Start the Streamlit application by running:
streamlit run app.py

Step 4: Open in Browser
The app will open automatically in your default browser. If not, navigate to:

🖼️ Screenshots
App Screenshot (Replace with your actual screenshot)

🎯 How to Use
Draw a Digit: Use your mouse or touchpad to draw a digit (0-9) on the canvas.

Predict: Click the "Predict Now" button.

View Result: The predicted digit will be displayed below the canvas.
