import sys
import subprocess

def main():
    if len(sys.argv) < 3:
        print("Uso: python3 view_context.py <issue|mr> <id>")
        sys.exit(1)

    item_type = sys.argv[1].lower()
    item_id = sys.argv[2]

    # Validación estricta de parámetros
    if item_type not in ['issue', 'mr']:
        print("❌ Error: El tipo debe ser estrictamente 'issue' o 'mr'.")
        sys.exit(1)

    cmd = ['glab', item_type, 'view', item_id, '--comments']
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al obtener contexto de {item_type.upper()} {item_id}:")
        print(e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
