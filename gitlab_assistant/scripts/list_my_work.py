import subprocess


def get_glab_output(cmd_list):
    try:
        # shell=False (por defecto al usar listas) previene inyección de comandos
        result = subprocess.run(cmd_list, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"❌ Error ejecutando comando: {e.stderr.strip()}"


def main():
    print("=== MIS ISSUES ASIGNADOS ===")
    issues = get_glab_output(['glab', 'issue', 'list', '--assignee', '@me'])
    print(issues if issues else "No hay issues asignados.")
    
    print("\n=== MIS MERGE REQUESTS (ASIGNADOS) ===")
    mrs_assigned = get_glab_output(['glab', 'mr', 'list', '--assignee', '@me'])
    print(mrs_assigned if mrs_assigned else "No hay MRs asignados.")

    print("\n=== MIS MERGE REQUESTS (COMO REVISOR) ===")
    mrs_reviewer = get_glab_output(['glab', 'mr', 'list', '--reviewer', '@me'])
    print(mrs_reviewer if mrs_reviewer else "No tienes MRs pendientes de revisar.")

if __name__ == "__main__":
    main()
