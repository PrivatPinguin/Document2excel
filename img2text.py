import cv2
import pytesseract
import numpy as np


# NOTE! download and install Tesseract and and to Systemvariables :
pytesseract.pytesseract.tesseract_cmd = "D:\\Program Files\\Tesseract-OCR\\tesseract.exe"


def get_text(image):
    # read image
    if type(image) == str:   

        image = cv2.imread(image)


        # convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        #remove pixel noise from image using morphological opening and closing 
        kernel = np.ones((1, 1), np.uint8)
        opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

        # apply Blur to smooth out the edges
        blur = cv2.GaussianBlur(closing, (5,5), sigmaX=1, sigmaY=1) # blur image

        # white background and black text
        thresh = cv2.bitwise_not(blur)
        
        # Morph open to remove noise and invert image
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        invert = 255 - opening

	# create countour list
        contours, hierarchy = cv2.findContours(invert, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # open empty file
        file = open("text_from_image.txt", "w", encoding="utf-8")

        # loop through contours
        len_countours = len(contours)-1
        for counter,cnt in enumerate(contours):
        
            # get bounding rectangle
            x, y, w, h = cv2.boundingRect(cnt)
            # draw rectangle
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # crop image
            crop = image[y:y + h, x:x + w]
            # apply threshold
            ret, crop_thresh = cv2.threshold(crop, 127, 255, cv2.THRESH_BINARY)
            # apply OCR
            text = pytesseract.image_to_string(crop_thresh, lang='deu')
            print(counter, 'of', len_countours, text)            
            file.write(str(text))
            if counter == len_countours:
                file.close()
                return 
