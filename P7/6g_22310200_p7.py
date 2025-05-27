import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Rango de color (puedes ajustar a rojo real si es necesario)
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Kernel para operaciones morfológicas
    kernel = np.ones((5,5), np.uint8)

    # Filtros
    smoothed = cv2.filter2D(res, -1, kernel)
    blur = cv2.GaussianBlur(res, (5,5), 0)
    median = cv2.medianBlur(res, 5)
    bilateral = cv2.bilateralFilter(res, 5, 10, 10)

    # OPERACIONES MORFOLÓGICAS: TOPHAT y BLACKHAT
    tophat = cv2.morphologyEx(res, cv2.MORPH_TOPHAT, kernel)
    blackhat = cv2.morphologyEx(res, cv2.MORPH_BLACKHAT, kernel)

    # Mostrar ventanas
    cv2.imshow('Original', frame)
    #cv2.imshow('Blur', blur)
    #cv2.imshow('Median', median)
    #cv2.imshow('Bilateral', bilateral)
    cv2.imshow('Top Hat', tophat)
    cv2.imshow('Black Hat', blackhat)

    # Salida con ESC
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

