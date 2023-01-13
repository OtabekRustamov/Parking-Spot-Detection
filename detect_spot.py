import cv2
import pickle

rectW, rectH = 107, 48
try:
    with open('parking_position', 'rb') as f:
        car_position = pickle.load(f)
except:
    car_position = []


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        car_position.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(car_position):
            x1, y1 = pos
            if x1 < x < x1 + rectH and y1 < y < y1 + rectW:
                car_position.pop(i)

    with open('parking_position', 'wb') as f:
        pickle.dump(car_position, f)


while True:
    img = cv2.imread('img.png')
    # cv2.rectangle(img, (50, 350), (157, 540), (0, 0, 255), 2)
    for pos in car_position:
        cv2.rectangle(img,pos,(pos[0]+rectW,pos[1]+rectH),(0,0,255),2)
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image",mouseClick)
    cv2.imshow('Image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
