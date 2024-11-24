import numpy as np
import streamlit as st
from PIL import Image
from tensorflow.keras.models import load_model
from source.solution import solution  # Import fungsi dari solution.py

def show_animal_dashboard():
    # Class names for animal classification
    class_names = [
        "antelope", "badger", "bat", "bear", "bee", "beetle", "bison", "boar", "butterfly", "cat",
        "caterpillar", "chimpanzee", "cockroach", "cow", "coyote", "crab", "crow", "deer", "dog",
        "dolphin", "donkey", "dragonfly", "duck", "eagle", "elephant", "flamingo", "fly", "fox",
        "goat", "goldfish", "goose", "gorilla", "grasshopper", "hamster", "hare", "hedgehog",
        "hippopotamus", "hornbill", "horse", "hummingbird", "hyena", "jellyfish", "kangaroo", "koala",
        "ladybugs", "leopard", "lion", "lizard", "lobster", "mosquito", "moth", "mouse", "octopus",
        "okapi", "orangutan", "otter", "owl", "ox", "oyster", "panda", "parrot", "pelecaniformes",
        "penguin", "pig", "pigeon", "porcupine", "possum", "raccoon", "rat", "reindeer", "rhinoceros",
        "sandpiper", "seahorse", "seal", "shark", "sheep", "snake", "sparrow", "squid", "squirrel",
        "starfish", "swan", "tiger", "turkey", "turtle", "whale", "wolf", "wombat", "woodpecker", "zebra"
    ]

    # Load the trained animal classification model
    model_path = './model/model.h5'
    model = load_model(model_path)

    # Function to preprocess the uploaded image
    def preprocess_image(image):
        image = image.resize((180, 180))  # Resize image to 180x180 (model input size)
        image = np.array(image) / 255.0   # Normalize pixel values to the range [0, 1]
        return np.expand_dims(image, axis=0)  # Add batch dimension

    # Title and description
    st.title("🐾 Animal Classifier Dashboard")
    st.markdown(
        """
        <div style="text-align: center;">
            <h3>🌟 Klasifikasi Hewan Menggunakan CNN 🌟</h3>
            <p>Unggah gambar hewan untuk mendapatkan prediksi jenis hewan, informasi,beserta skor kepercayaan.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    treshold = 0.3
    
    # Upload image
    uploaded_file = st.file_uploader("Pilih file gambar hewan:", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("Klasifikasi Gambar"):
        with st.spinner("🔄 Sedang mengklasifikasi... Harap tunggu..."):
            # Preprocess the image
            processed_image = preprocess_image(image)

            # Predict the class
            predictions = model.predict(processed_image)
            predicted_index = np.argmax(predictions)
            predicted_animal = class_names[predicted_index]
            confidence = predictions[0][predicted_index] * 100

            # Handle different confidence levels
            if confidence < 30.0:
                st.warning(
                    "⚠ **Skor kepercayaan terlalu rendah** (kurang dari 30%). Belum ada data klasifikasi yang akurat untuk gambar ini. "
                    "Silakan coba dengan gambar lain."
                )
            elif confidence < 70.0:
                st.markdown(
                    f"""
                    <div style="border: 3px solid #FFD700; padding: 15px; border-radius: 10px; background-color: #FFF8DC;">
                        <h4>🔍 Prediksi Hewan: <strong>{predicted_animal.capitalize()}</strong></h4>
                        <p>Skor Kepercayaan: {confidence:.2f}%</p>
                    </div>
                    <br>
                    """,
                    unsafe_allow_html=True
                )
                st.warning(
                    "⚠ Skor kepercayaan rendah (30% ≤ confidence < 70%). Hasil mungkin tidak akurat. Silakan unggah gambar yang lebih jelas."
                )
            else:
                st.markdown(
                    f"""
                    <div style="border: 3px solid #AED4FF; padding: 15px; border-radius: 10px; background-color: #C6E7FF;">
                        <h4>🔍 Prediksi Hewan: <strong>{predicted_animal.capitalize()}</strong></h4>
                        <p>Skor Kepercayaan: {confidence:.2f}%</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # Show additional solution information
                solution(predicted_animal)  # Call solution function to display animal details

    else:
        st.info("📁 Harap unggah gambar untuk memulai klasifikasi.")