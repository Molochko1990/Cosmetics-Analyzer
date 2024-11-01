import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def GetTextFromImage(language, imagePath):
    image = cv2.imread(imagePath)
    original_height, original_width = image.shape[:2]
    image = cv2.resize(image, (int(original_width*1.2), int(original_height*1.12)), interpolation=cv2.INTER_LINEAR)

    #cv2.imshow('Image', image)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    if language == 0:
        custom_config = r'--oem 3 --psm 3 -l rus'
        return pytesseract.image_to_string(image, config=custom_config)
    else:
        custom_config = r'--oem 3 --psm 3 -l eng --user-words user-words.txt'
        return pytesseract.image_to_string(image, config=custom_config)


#print(GetTextFromImage(1, 'Test-1.jpg'))



