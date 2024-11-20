import cv2
import numpy as np
from datetime import datetime

print("""
\t######################### Ai Dev Surya #########################
\t							         
\t          This program is made by Suryansh Sharma             
\t       Visit my Blog:   https://aidevsurya.blogspot.com       
\t       Visit my Github: https://github.com/aidevsurya         
\t								 
\t   Press 'c' to Capture and Save your Beautiful Sketch        
\t   Press 'q' to Exit					         
\t								 
\t################################################################
""")

# Our sketch generating function
def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray, (5,5), 0)
    
    # Extract edges
    canny_edges = cv2.Canny(img_gray_blur, 20, 50)
    
    # Do an invert binarize the image 
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask


# Initialize webcam, cap is the object provided by VideoCapture
# It contains a boolean indicating if it was sucessful (ret)
# It also contains the images collected from the webcam (frame)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))
    if cv2.waitKey(1) == ord('c'): # Space Key
        time = str(datetime.now()).split(" ")[0] + "_" + str(datetime.now()).split(" ")[1].split(".")[0].replace(":","-")
        print("Image Saved: ",time)
        cv2.imwrite(f"Sketch_{time}.png",sketch(frame))
    if cv2.waitKey(1) == ord('q'): # Q Key
        break
        
# Release camera and close windows
cap.release()
cv2.destroyAllWindows()      