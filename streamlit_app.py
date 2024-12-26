import streamlit as st
from main import *
import numpy as np
# streamlit_app.py
import streamlit as st
from PIL import Image
import numpy as np
from main import process_image  # Импортируем функцию из main.py

# Заголовок приложения
st.title("Обнаружение дорожного знака СТОП")

# Описание
st.write("Загрузите изображение, и приложение обработает его с помощью нейронной сети.")

# Кнопка для загрузки изображения
uploaded_file = st.file_uploader("Выберите изображение...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Открываем изображение
    image = Image.open(uploaded_file)
    image_array = np.array(image)  # Преобразуем в numpy array

    # Отображаем оригинальное изображение
    st.image(image, caption="Оригинальное изображение", use_container_width=True)

    # Кнопка для обработки изображения
    if st.button("Обработать изображение"):
        # Обрабатываем изображение с помощью функции из main.py
        processed_image = process_image(image_array)

        # Отображаем обработанное изображение
        st.image(processed_image, caption="Обработанное изображение", use_container_width=True)
