import cv2
from ultralytics import YOLO
import serial
import time

# Configurar puerto Serial al Arduino en COM4 a 115200 baudios
arduino = serial.Serial('COM4', 115200, timeout=1)
time.sleep(2)  # Espera a que el Arduino se inicialice

model = YOLO('yolov8n.pt')  # Modelo pequeño YOLOv8

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        result = results[0]

        telefono_detectado = False

        for box, cls, score in zip(result.boxes.xyxy, result.boxes.cls, result.boxes.conf):
            class_name = model.names[int(cls)]

            if class_name == 'cell phone' and float(score) > 0.5:
                telefono_detectado = True
                x1, y1, x2, y2 = box.int().tolist()
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.putText(frame, f"Cell phone {score:.2f}", (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # Enviar '1' si detecta teléfono, '0' si no
        if telefono_detectado:
            arduino.write(b'1')
        else:
            arduino.write(b'0')

        cv2.imshow("Detección Teléfono", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    arduino.close()
    cv2.destroyAllWindows()

