import cv2
import matplotlib.pyplot as plt
import numpy as np

# Leer la imagen en escala de grises
img = cv2.imread('Img_P2.png', cv2.IMREAD_GRAYSCALE)

# Calcular histograma original
hist_original = cv2.calcHist([img], [0], None, [256], [0, 256])

# Ecualizar la imagen
img_eq = cv2.equalizeHist(img)

# Calcular histograma de la imagen ecualizada
hist_eq = cv2.calcHist([img_eq], [0], None, [256], [0, 256])

# Mostrar todo en una sola ventana
plt.figure(figsize=(12, 6))

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.plot(hist_original, color='black')
plt.title('Histograma Original')
plt.xlim([0, 256])

plt.subplot(2, 2, 3)
plt.imshow(img_eq, cmap='gray')
plt.title('Imagen Ecualizada')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.plot(hist_eq, color='black')
plt.title('Histograma Ecualizado')
plt.xlim([0, 256])

plt.tight_layout()
plt.show()
