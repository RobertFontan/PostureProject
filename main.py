import cv2
import numpy as np


def get_coordinates(event, x, y, flags, param): # function to get coordinates of mouse click
    if event == cv2.EVENT_LBUTTONDOWN: # if left mouse button is clicked
        print('x:', x, 'y:', y) # print coordinates of mouse click
# initializing the camera
cap = cv2.VideoCapture(0)



while True:
    ret, frame = cap.read() # frame is image data

    # frame metadata CHANGE IN CASE OF DIFFERENT CAMERA
    # print('height, width, channels', frame.shape[0], frame.shape[1], frame.shape[2]) # height, width, channel

    # height width channels
    # 480, 640, 3

    if not ret: # ret is a boolean if frame was read 
        break

# y 175 keep head below
    cv2.line(frame, (0,270), (640,270), (255,0,0), 5)


    cv2.imshow('window', frame) # display the frame in window names webcam
    cv2.setMouseCallback('window', get_coordinates, frame) # set mouse callback function to get coordinates
                         
                         #lambda x,y,z,w: print(x,y,z,w))


    if cv2.waitKey(1) & 0xFF == ord('q'): # if q is pressed quit the 
        break

cap.release() # release the camera
cv2.destroyAllWindows() # close all windows

# detect my facial features 