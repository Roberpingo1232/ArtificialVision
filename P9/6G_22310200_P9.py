import cv2
import numpy as np

# Carga las imágenes
template = cv2.imread('opencv-template-for-matching.jpg', 0)
image = cv2.imread('opencv-template-matching-python-tutorial.jpg')

# Convertimos la imagen principal a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Obtenemos el tamaño del template
t_width, t_height = template.shape[::-1]

# Realizamos la búsqueda del template en la imagen en gris
result = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)

# Definimos el umbral de detección
threshold_value = 0.85

# Buscamos los puntos donde el resultado es mayor o igual al umbral
locations = np.where(result >= threshold_value)

# Dibujamos rectángulos en las regiones detectadas y además añadimos un pequeño círculo en el centro
for pt in zip(*locations[::-1]):
    top_left = pt
    bottom_right = (pt[0] + t_width, pt[1] + t_height)
    center = (pt[0] + t_width // 2, pt[1] + t_height // 2)

    # Rectángulo en azul
    cv2.rectangle(image, top_left, bottom_right, (255, 0, 0), 3)

    # Círculo rojo en el centro del rectángulo
    cv2.circle(image, center, 10, (0, 0, 255), -1)

# Mostramos la imagen resultante
cv2.imshow('Template Matching', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
