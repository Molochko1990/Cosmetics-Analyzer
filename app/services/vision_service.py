import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


def GetTextFromImage(image_bytes):
    nparr = np.frombuffer(image_bytes.read(), np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if image is None:
        raise ValueError("Не удалось прочитать изображение")
    original_height, original_width = image.shape[:2]
    image = cv2.resize(image, (int(original_width * 1.2), int(original_height * 1.12)), interpolation=cv2.INTER_LINEAR)
    language = 1
    if language == 0:
        custom_config = r'--oem 3 --psm 3 -l rus --user-words user-words.txt'
        return pytesseract.image_to_string(image, config=custom_config)
    else:
        custom_config = r'--oem 3 --psm 3 -l eng --user-words user-words.txt'
        return pytesseract.image_to_string(image, config=custom_config)
