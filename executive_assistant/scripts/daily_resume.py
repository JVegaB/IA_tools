import sys
import os
from datetime import datetime


def main(text_to_save):
    # 1. Fallback al directorio Home si la variable no está definida
    daily_resumes_path = os.environ.get("DAILY_RESUMES_PATH", os.path.expanduser("~"))

    # 2. Preparar rutas con guiones bajos (YYYY_MM_DD)
    today = datetime.now()
    target_dir = os.path.join(daily_resumes_path, today.strftime("%Y_%m_%d"))

    # 3. Crear la carpeta del día si no existe
    os.makedirs(target_dir, exist_ok=True)

    # 4. Crear un nombre de archivo único basado en timestamp
    # En Python usamos %f para microsegundos, lo cual cumple el mismo propósito que %N en bash
    filename = f"log_{today.strftime('%H%M%S_%f')}.txt"
    filepath = os.path.join(target_dir, filename)

    # 6. Guardar el texto multilinea en el archivo
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text_to_save)

    # Confirmación para el agente o para ti si lo corres manual
    print(f"Guardado exitosamente en: {filepath}")


if __name__ == "__main__":

    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("Error: No se proporcionó texto para guardar.")
        sys.exit(1)

    text_to_save = sys.argv[1]

    main(text_to_save)
