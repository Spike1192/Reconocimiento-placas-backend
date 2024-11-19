import os
import sys
import cv2
from datetime import datetime

# Ajusta la ruta para importar PlateRecognition
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from process.main import PlateRecognition

# Crear una carpeta para guardar las capturas si no existe
os.makedirs('captures', exist_ok=True)

# Inicializar un conjunto para almacenar placas guardadas
saved_plates = set()

if __name__ == "__main__":
    processor = PlateRecognition()
    image_path = 'examples/Image2.jpg'
    vehicle_image, license_plate, info = processor.process_static_image(image_path, draw=True)

    # Verificar si la placa no está repetida
    if license_plate and license_plate not in saved_plates:
        # Agregar la placa al conjunto de placas guardadas
        saved_plates.add(license_plate)
        
        # Generar el nombre de archivo basado en la placa
        capture_filename = f'captures/{license_plate}.png'
        
        # Guardar la imagen capturada
        cv2.imwrite(capture_filename, vehicle_image)
        print(f'Captura guardada: {capture_filename}')
    else:
        if license_plate in saved_plates:
            print('La placa ya ha sido registrada previamente.')

    print(f'License plate: {license_plate} \nInfo: {info}')
    cv2.imshow('plate recognition', vehicle_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
