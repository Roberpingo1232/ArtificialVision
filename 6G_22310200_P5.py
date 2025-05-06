import numpy as np
import matplotlib
import cv2

img = cv2.imread('bookpage.jpg')
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval1, thresh_binary = cv2.threshold(grayscaled, 127, 255, cv2.THRESH_BINARY)
retval2, thresh_binary_inv = cv2.threshold(grayscaled, 127, 255, cv2.THRESH_BINARY_INV)
retval3, thresh_trunc = cv2.threshold(grayscaled, 127, 255, cv2.THRESH_TRUNC)
retval4, thresh_tozero = cv2.threshold(grayscaled, 127, 255, cv2.THRESH_TOZERO)
retval5, thresh_tozero_inv = cv2.threshold(grayscaled, 127, 255, cv2.THRESH_TOZERO_INV)

adaptive_mean = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                      cv2.THRESH_BINARY, 115, 1)
adaptive_gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                      cv2.THRESH_BINARY, 115, 1)

retval6, otsu = cv2.threshold(grayscaled, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('Original', img)
cv2.imshow('THRESH_BINARY', thresh_binary)
cv2.imshow('THRESH_BINARY_INV', thresh_binary_inv)
cv2.imshow('THRESH_TRUNC', thresh_trunc)
cv2.imshow('THRESH_TOZERO', thresh_tozero)
cv2.imshow('THRESH_TOZERO_INV', thresh_tozero_inv)
cv2.imshow('ADAPTIVE_MEAN', adaptive_mean)
cv2.imshow('ADAPTIVE_GAUSSIAN', adaptive_gaus)
cv2.imshow('OTSU', otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
