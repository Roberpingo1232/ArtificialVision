import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # --- Rango para ROJO ---
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    res_red = cv2.bitwise_and(frame, frame, mask=mask_red)

    # --- Rango para VERDE ---
    lower_green = np.array([36, 50, 70])
    upper_green = np.array([89, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    res_green = cv2.bitwise_and(frame, frame, mask=mask_green)

    # --- Rango para AZUL ---
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    res_blue = cv2.bitwise_and(frame, frame, mask=mask_blue)

    # Mostrar todo
    cv2.imshow('Original', frame)
    cv2.imshow('Red', res_red)
    cv2.imshow('Green', res_green)
    cv2.imshow('Blue', res_blue)

    # Salir con ESC
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

