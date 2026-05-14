import sys
import json
import subprocess
from datetime import datetime

def fetch_timesheets(start_date, end_date):
    # 1. Validación estricta del formato de fechas
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("❌ Error: Las fechas deben tener el formato estricto YYYY-MM-DD.")
        sys.exit(1)

    # 2. Construcción del dominio y campos
    # Se extraen las líneas del rango de fechas. Si necesitas filtrar por el usuario 
    # exacto, odoo-mcp usualmente respeta el contexto del token (UID actual).
    domain = f"[('date', '>=', '{start_date}'), ('date', '<=', '{end_date}')]"
    fields = "['name', 'task_id', 'unit_amount', 'date', 'project_id', 'user_id']"

    try:
        # 3. Llamada al orquestador odoo-mcp
        result = subprocess.run([
            'odoo-mcp', 'search-read',
            '-p', 'vauxoo',                   # Perfil configurado
            '-m', 'account.analytic.line',    # Modelo de timesheets
            '-d', domain,                     # Rango de fechas
            '-f', fields                      # Campos requeridos para el reporte
        ], capture_output=True, text=True, check=True)
        
        # Devolvemos el JSON crudo a la terminal para que el Agente IA lo parsee
        print(result.stdout.strip())
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al ejecutar odoo-mcp CLI.\n Detalles: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error interno en la sincronización: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Uso: python3 fetch_timesheet_lines_date_range.py <start_date> <end_date>")
        print("Ejemplo: python3 fetch_timesheet_lines_date_range.py 2026-05-01 2026-05-14")
        sys.exit(1)

    fetch_timesheets(sys.argv[1], sys.argv[2])
