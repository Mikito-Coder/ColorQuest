# Import necessary libraries
import numpy as np
import cv2

def get_limits(color):
    # Convert the input BGR color to a NumPy array of type uint8
    c = np.uint8([[color]])  # BGR values
    
    # Convert the BGR color to HSV color space
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)
    
    # Extract the hue value from the HSV representation
    hue = hsvC[0][0][0]  # Get the hue value
    
    # Handle red hue wrap-around by checking hue value boundaries
    if hue >= 165:  # Upper limit for divided red hue
        # Define lower and upper limits for the color range, adjusting for hue wrap-around
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([180, 255, 255], dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        # Adjust limits for lower end of red hue spectrum
        lowerLimit = np.array([0, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        # For non-red hues, define a standard range around the hue value
        lowerLimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        upperLimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    
    # Return the calculated lower and upper HSV limits
    return lowerLimit, upperLimit
