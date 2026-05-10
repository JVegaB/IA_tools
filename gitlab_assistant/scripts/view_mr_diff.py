import sys
import subprocess

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 view_mr_diff.py <id>")
        sys.exit(1)

    mr_id = sys.argv[1]

    cmd = ['glab', 'mr', 'diff', mr_id]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al obtener el diff del MR {mr_id}:")
        print(e.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
