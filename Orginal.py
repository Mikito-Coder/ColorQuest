import cv2 
#Imports Library Computer Vison 2

from PIL import Image

from utils import get_limits
#Imports fumction from other python file 

cap = cv2.VideoCapture(0)

Blue =  [0,0,255] # Color blue in BGR 
Yellow = [0,255,255]
# Opens default camera with the value 0 
while True:
    ret, frame = cap.read()
    #Reads the ret and frame which is a boolean and the matrix(array) values for the video in BGR format 

    hsvImage =  cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Converts BGR to HSV format using a library from cv2.

    lowerLimit, upperLimit = get_limits(Yellow)
    #Gets the upper and lower Hue limits for the color Blue using my algotithm in utils.py.

    mask =  cv2.inRange(hsvImage, lowerLimit, upperLimit)
    #Frame is dark but when an object with the color Blue is put in the webcam/frame it highlights the object.

    mask_ = Image.fromarray(mask)
    #Get the array of where my mask(color Yellow) is in my image 

    bbox = mask_.getbbox()
    #Makes a bounding box around our object using pillow 

    if bbox is not None:
        x1, y1, x2, y2 = bbox

        cv2.rectangle(frame, (x1,y1), (x2,y2), [0,255,0], 5)
    # print(bbox)
    if not ret:
        print("Failed to grab frame")
        break
    # Checks for if the Ret is true which indicates there is a webcam if it isn't it breaks the code and orints an error message.
    
    # print(ret)
    # print(frame)

    cv2.imshow("Kiitan's frame", frame)


    # cv2.imshow("Kiitan's frame",frame)
    # Opens my Frame with my default webcam[0] and names it Kiitan's frame

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    #Initializes the letter q to break the code and close the camera while the frame is active.
cap.release()

cv2.destroyAllWindows()


# HOW TO OPEN MY WEBCAM WITH FRAME AND QUIT QUIT Q
# import cv2 

# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()

    

#     if not ret:
#         print("Failed to grab frame")
#         break
#     # print(ret)
#     # print(frame)
#     cv2.imshow("Kiitan's frame",frame)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()

# cv2.destroyAllWindows()