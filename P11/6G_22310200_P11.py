import numpy as np
import cv2
import matplotlib.pyplot as plt

# ============================================
# OBJETIVO 1: Comparación de imágenes con ORB
# ============================================

# # Cargar la primera imagen en escala de grises (plantilla)
# img1 = cv2.imread('opencv-feature-matching-template.jpg', 0)

# # Cargar la segunda imagen donde se buscará la plantilla
# img2 = cv2.imread('opencv-feature-matching-image.jpg', 0)

# # Crear el detector ORB
# orb = cv2.ORB_create()

# # Detectar puntos clave y descriptores
# kp1, des1 = orb.detectAndCompute(img1, None)
# kp2, des2 = orb.detectAndCompute(img2, None)

# # Emparejar los descriptores usando fuerza bruta con Hamming
# bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# matches = bf.match(des1, des2)

# # Ordenar coincidencias por distancia (mejor coincidencia = menor distancia)
# matches = sorted(matches, key=lambda x: x.distance)

# # Dibujar las 10 mejores coincidencias
# img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

# # Mostrar imagen resultante
# plt.imshow(img3)
# plt.title("Emparejamiento de características con ORB")
# plt.axis('off')
# plt.show()


# ===============================================
# OBJETIVO 2: Extracción de fondo por movimiento
# ===============================================

# Captura de video desde webcam
cap = cv2.VideoCapture(0)

# Leer los dos primeros frames para iniciar comparación
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Calcular diferencia absoluta entre los dos frames
    diff = cv2.absdiff(frame1, frame2)

    # Convertir a escala de grises
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # Aplicar desenfoque para eliminar ruido
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Umbralizar para obtener regiones de cambio (movimiento)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)

    # Dilatar para hacer más visibles los contornos
    dilated = cv2.dilate(thresh, None, iterations=3)

    # Encontrar contornos (zonas en movimiento)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar rectángulos en zonas con movimiento
    for contour in contours:
        if cv2.contourArea(contour) < 700:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Mostrar los resultados
    cv2.imshow("Video original", frame1)
    cv2.imshow("Movimiento detectado", dilated)

    # Actualizar los frames para la siguiente iteración
    frame1 = frame2
    ret, frame2 = cap.read()

    # Salir con tecla ESC
    if cv2.waitKey(30) & 0xFF == 27:
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
