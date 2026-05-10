import sys
import subprocess

def main():
    if len(sys.argv) < 4:
        print("Uso: python3 add_note.py <issue|mr> <id> \"texto del comentario\"")
        sys.exit(1)

    item_type = sys.argv[1].lower()
    item_id = sys.argv[2]
    comment_text = sys.argv[3]

    if item_type not in ['issue', 'mr']:
        print("❌ Error: El tipo debe ser 'issue' o 'mr'.")
        sys.exit(1)

    if not comment_text.strip():
        print("❌ Error: El comentario no puede estar vacío.")
        sys.exit(1)

    cmd = ['glab', item_type, 'note', item_id, '-m', comment_text]
    
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"✅ Éxito: Comentario publicado en el {item_type.upper()} {item_id}.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error de glab al publicar el comentario en {item_type.upper()} {item_id}:")
        print(e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
