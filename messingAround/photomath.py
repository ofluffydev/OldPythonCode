import cv2
import pytesseract

# Load the image
img = cv2.imread('screenshot.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

# Find contours in the image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Loop over the contours
for contour in contours:
    # Get the bounding rectangle
    (x, y, w, h) = cv2.boundingRect(contour)

    # Check if the aspect ratio and area match text
    if w / h > 1.9 and w > 10 and h > 5:
        # Crop the text region and recognize it using Tesseract
        roi = img[y:y+h, x:x+w]
        text = pytesseract.image_to_string(roi, lang='eng', config='--psm 6')
        print(text)
