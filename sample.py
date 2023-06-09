from sys import breakpointhook
import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("Python Webcam App")

img_counter = 0


while True:
    ret, frame = cam.read()
    if(not ret):
        print("Failed to grab frame!")
        break
    cv2.imshow("Image", frame)

    k = cv2.waitKey(1)

    if(k%256==27):
        print("Escape hit!")
        break

    elif k%256==32:
        img_name = "opencv2_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("Screenshot taken!")
        img_counter+=1

cam.release()

cam.destroyAllWindows()







