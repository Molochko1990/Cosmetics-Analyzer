from ultralytics import YOLO
from pathlib import Path
from PIL import  Image
import numpy as np
import cv2
import io


def CropImageByPackaging(inp):
    model_path = Path(__file__).resolve().parent / 'PackageFinder.pt'
    model = YOLO(str(model_path))
    image_stream = io.BytesIO(inp)
    image = Image.open(image_stream)
    inputPhoto = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    img = inputPhoto
    imgresult = inputPhoto

    results = model(img)

    r = results[0]

    boxes = r.boxes.xyxy # [x_min, y_min, x_max, y_max] в пикселях

    classes = r.boxes.cls.tolist() # Список номеров классов

    confidences = r.boxes.conf.tolist() # Список вероятностей для каждого обнаружения

    for box, cls, conf in zip(boxes, classes, confidences):
        box = box.cpu().numpy()
        x_min, y_min, x_max, y_max = box.astype(int)
        cropped_image = imgresult[y_min:y_max, x_min:x_max]
    return cropped_image
