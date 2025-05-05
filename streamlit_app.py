import streamlit as st
import requests
from PIL import Image
import numpy as np
import io

# Настройки API
API_URL = "https://proekt-dianayusupova.amvera.io/detect"

st.title("Обнаружение дорожного знака СТОП")
st.write("Загрузите изображение для обнаружения знака СТОП через API")

uploaded_file = st.file_uploader("Выберите изображение...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Показываем оригинальное изображение
    image = Image.open(uploaded_file)
    st.image(image, caption="Оригинальное изображение", use_container_width=True)

    if st.button("Обнаружить знак СТОП"):
        try:
            # Отправляем файл на API
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            response = requests.post(API_URL, files=files)

            if response.status_code == 200:
                result = response.json()
                if result["success"]:
                    # Декодируем полученное изображение
                    processed_image = Image.open(io.BytesIO(result["image"]))
                    st.image(processed_image, caption="Результат обработки", use_container_width=True)
                else:
                    st.error(f"Ошибка API: {result.get('error', 'Неизвестная ошибка')}")
            else:
                st.error(f"Ошибка сервера: {response.status_code}")

        except requests.exceptions.RequestException as e:
            st.error(f"Ошибка соединения с API: {str(e)}")
        except Exception as e:
            st.error(f"Произошла ошибка: {str(e)}")

# Добавляем пояснение работы системы
st.markdown("""
**Примечание:** 
- Изображение отправляется на сервер API для обработки
- Используется каскадный классификатор Haar для обнаружения знаков
- Результат возвращается с выделенными областями обнаружения
""")