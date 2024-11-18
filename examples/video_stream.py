import os
import sys
import cv2
from datetime import datetime

# Ajusta la ruta para importar PlateRecognition
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from process.main import PlateRecognition

# Crear una carpeta para guardar las capturas si no existe
os.makedirs('captures', exist_ok=True)

processor = PlateRecognition()

# Configuración de la cámara
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Ancho de la cámara
cap.set(4, 720)   # Altura de la cámara

if __name__ == "__main__":
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        vehicle_image, license_plate, info = processor.process_vehicular_plate(frame, True, True)

        # Si la placa fue identificada, guardar una captura
        if license_plate:
            # Generar un nombre único para la captura usando la fecha y hora actuales
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            capture_filename = f'captures/capture_{license_plate}_{timestamp}.png'
            
            # Guardar la imagen capturada
            cv2.imwrite(capture_filename, vehicle_image)
            print(f'Captura guardada: {capture_filename}')

        print(f'License plate: {license_plate} \nInfo: {info}')
        cv2.imshow('result_process', vehicle_image)
        t = cv2.waitKey(5)
        if t == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
