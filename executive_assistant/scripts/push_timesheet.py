import sys
import json
import subprocess


def push_timesheets(timesheets):
    try:
        created_responses = []
        
        for ts in timesheets:
            # Convertir el diccionario actual a un string JSON válido 
            # para el parámetro -v de la CLI de odoo-mcp
            values_json = json.dumps(ts)
            
            # Ejecutar el comando nativo de odoo-mcp-multi
            result = subprocess.run([
                'odoo-mcp', 'create',
                '-p', 'vauxoo',                   # Usamos el perfil que ya autenticaste
                '-m', 'account.analytic.line',    # Modelo de timesheets
                '-v', values_json                 # Valores JSON
            ], capture_output=True, text=True, check=True)
            
            # La CLI devuelve JSON por defecto para facilitar composición
            created_responses.append(result.stdout.strip())
            
        print(f"✅ Éxito! Se subieron {len(created_responses)} registros a Odoo.")
        for r in created_responses:
            print(f"- Output ORM: {r}")
            
    except subprocess.CalledProcessError as e:
        # Si Odoo rechaza el push (ej. tarea cerrada, campo faltante)
        print(f"❌ Error al ejecutar odoo-mcp CLI.\n Detalles del ORM: {e.stderr}")
        sys.exit(1)

    except Exception as e:
        print(f"❌ Error interno en la sincronización: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Error: No se proporcionó el payload JSON.")
        sys.exit(1)

    try:
        # Parsear el arreglo de timesheets que armó la IA
        timesheets = json.loads(sys.argv[1])

    except json.JSONDecodeError:

        print("❌ Error: El payload entregado por la IA no es un JSON válido.")
        sys.exit(1)
    
    push_timesheets(timesheets)