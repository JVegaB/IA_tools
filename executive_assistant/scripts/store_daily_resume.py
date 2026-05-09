import sys
import os
from datetime import datetime


def main(text_to_save):
    # 1. Fallback al directorio Home (~), igual que daily_resume.py, si la variable no está definida
    daily_resumes_path = os.environ.get("DAILY_RESUMES_PATH", os.path.expanduser("~"))

    # 2. Preparar rutas con guiones bajos (YYYY_MM_DD)
    today = datetime.now()
    target_dir = os.path.join(daily_resumes_path, today.strftime("%Y_%m_%d"))

    # 3. Crear la carpeta del día si no existe
    os.makedirs(target_dir, exist_ok=True)

    # 4. Definir la ruta del archivo final
    filepath = os.path.join(target_dir, "processed_summary.txt")

    # 5. Guardar el texto (que ahora será un JSON validado) en el archivo
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text_to_save)

    print("Resumen diario listo y guardado en memoria.")


if __name__ == "__main__":
    # Validar que se haya pasado texto como argumento (mimifica el if [ -z "$1" ])
    if len(sys.argv) < 2 or not sys.argv[1].strip():
        print("Error: No se proporcionó texto para guardar.")
        sys.exit(1)

    payload = sys.argv[1]
    
    main(payload)