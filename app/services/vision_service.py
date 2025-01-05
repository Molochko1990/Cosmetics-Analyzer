import cv2
import pytesseract
import numpy as np


def GetTextFromImage(image_bytes):
    nparr = np.frombuffer(image_bytes.read(), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Не удалось прочитать изображение")

    # Изменение размера изображения для улучшения OCR
    original_height, original_width = image.shape[:2]
    image = cv2.resize(image, (int(original_width * 1.2), int(original_height * 1.12)), interpolation=cv2.INTER_LINEAR)

    # Распознаем текст с указанием возможных языков
    custom_config = r'--oem 3 --psm 3 -l rus+eng'
    text = pytesseract.image_to_string(image, config=custom_config)

    return text
