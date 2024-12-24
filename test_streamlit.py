
import numpy as np
from PIL import Image
from main import process_image  # Импортируем функцию из main.py
def test_process_image():
    # Создаем тестовое изображение (белый квадрат на черном фоне)
    test_image = np.zeros((100, 100, 3), dtype=np.uint8)
    test_image[20:80, 20:80] = (255, 255, 255)  # Белый квадрат

    # Преобразуем массив NumPy в объект PIL Image
    image = Image.fromarray(test_image)

    # Вызываем функцию process_image
    processed_image = process_image(test_image)

    # Проверяем, что функция возвращает массив NumPy
    assert isinstance(processed_image, np.ndarray), "Ошибка: функция process_image не возвращает массив NumPy"

    # Проверяем, что размеры изображения сохранены
    assert processed_image.shape == test_image.shape, "Ошибка: размеры изображения изменились"

    # Проверяем, что функция выполнилась без ошибок
    assert processed_image is not None, "Ошибка: функция process_image не обработала изображение"

    print("Тест пройден успешно!")

# Запуск теста
test_process_image()