import cv2
import pytesseract
import numpy as np

def GetTextFromImage(image_array):
    # Проверим, что переданный массив имеет нужную форму (3 канала)
    if len(image_array.shape) != 3 or image_array.shape[2] != 3:
        raise ValueError("Массив должен быть изображением с 3 каналами (RGB)")

    # Изменение размера изображения для улучшения OCR
    original_height, original_width = image_array.shape[:2]
    image = cv2.resize(image_array, (int(original_width * 1.2), int(original_height * 1.12)), interpolation=cv2.INTER_LINEAR)

    # Распознаем текст с указанием возможных языков
    custom_config = r'--oem 3 --psm 3 -l rus+eng'
    text = pytesseract.image_to_string(image, config=custom_config)

    return text
