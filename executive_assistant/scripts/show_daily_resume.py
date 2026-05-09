import os
import glob
from datetime import datetime


def main():
    # 1. Fallback al directorio Home (~), igual que daily_resume.py, si la variable no está definida
    daily_resumes_path = os.environ.get("DAILY_RESUMES_PATH", os.path.expanduser("~"))

    # 2. Preparar rutas con guiones bajos (YYYY_MM_DD)
    today = datetime.now()
    target_dir = os.path.join(daily_resumes_path, today.strftime("%Y_%m_%d"))

    # 3. Verificar si el directorio existe
    if os.path.isdir(target_dir):
        # 4. Buscar todos los archivos log_* de hoy y ordenarlos cronológicamente
        log_files = sorted(glob.glob(os.path.join(target_dir, "log_*.txt")))
        
        if log_files:
            # 5. Concatenar y mostrar el contenido (simulando el 'cat' de Bash)
            for file_path in log_files:
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        # end="" evita agregar saltos de línea adicionales que no estén en el archivo
                        print(f.read(), end="") 
                except Exception:
                    pass # Ignoramos errores de lectura individuales igual que el 2>/dev/null
            
            # Un salto de línea final por limpieza en la terminal
            print() 
        else:
            print("No se encontraron logs para el día de hoy.")
    else:
        print("Aún no hay directorio de logs para el día de hoy.")


if __name__ == "__main__":
    # Al no recibir argumentos de sys.argv, simplemente invocamos la función principal
    main()