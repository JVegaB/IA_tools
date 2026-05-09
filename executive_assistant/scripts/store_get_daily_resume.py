import os
import sys
from datetime import datetime


def main():
    # 1. Fallback al directorio Home (~), igual que daily_resume.py, si la variable no está definida
    daily_resumes_path = os.environ.get("DAILY_RESUMES_PATH", os.path.expanduser("~"))

    # 2. Preparar rutas con guiones bajos (YYYY_MM_DD)
    today = datetime.now()
    target_dir = os.path.join(daily_resumes_path, today.strftime("%Y_%m_%d"))

    # 3. Definir la ruta del archivo procesado
    filepath = os.path.join(target_dir, "processed_summary.txt")

    # 4. Verificar si el archivo existe
    if os.path.isfile(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                # end="" evita un salto de línea extra que pueda romper el parseo del JSON
                print(f.read(), end="") 
        except Exception as e:
            print(f"Error: No se pudo leer el archivo. Detalles: {e}")
            sys.exit(1)
    else:
        # Imprimimos el error exactamente como lo espera el wrapper para detener la ejecución
        print("Error: No se ha generado el resumen procesado de hoy. Ejecuta /summary review primero.")
        sys.exit(1)


if __name__ == "__main__":
    main()
