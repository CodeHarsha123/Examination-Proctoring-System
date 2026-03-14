import cv2
import numpy as np

def detect_mobile(frame):
    # Basic detection based on finding rectangular contours with phone-like aspect ratios
    # This is a heuristic approach since we cannot load heavy YOLO models easily here without weights
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Minimum area to be considered
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
            
            # Check if it has 4 corners (rectangle)
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(approx)
                aspect_ratio = float(w) / h
                
                # Phones usually have aspect ratios between 1.5 and 2.5 (vertical or horizontal)
                if 0.4 < aspect_ratio < 0.7 or 1.5 < aspect_ratio < 2.5:
                     # Filter out very large/small objects (like the screen itself or small buttons)
                    if area < 50000: 
                        return True
                        
    return False
