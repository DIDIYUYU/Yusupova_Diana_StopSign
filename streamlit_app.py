import streamlit as st
import cv2
import numpy as np
from PIL import Image
#1
st.title("🚦 Обнаружение стоп-знака")

uploaded_file = st.file_uploader("Загрузите изображение", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(file_bytes, 1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    stop_data = cv2.CascadeClassifier('stop_data.xml')
    found = stop_data.detectMultiScale(img_gray, minSize=(20, 20))

    if len(found) == 0:
        st.warning("Стоп-знак не найден.")
    else:
        for (x, y, width, height) in found:
            cv2.rectangle(img_rgb, (x, y), (x + width, y + height), (0, 255, 0), 3)

        st.success(f"Найдено стоп-знаков: {len(found)}")
        st.image(img_rgb, caption="Результат", use_column_width=True)
