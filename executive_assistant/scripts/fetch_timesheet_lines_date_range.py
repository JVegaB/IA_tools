import sys
import json
import subprocess
from datetime import datetime

PROFILE = "vauxoo"
TARGET_PERSON_NAME = "Javier Vega"


def run_search_read(model, domain, fields):
    result = subprocess.run([
        'odoo-mcp', 'search-read',
        '-p', PROFILE,
        '-m', model,
        '-d', domain,
        '-f', fields,
    ], capture_output=True, text=True, check=True)

    output = result.stdout.strip()
    return json.loads(output) if output else []


def pick_target_record(records, target_name):
    target_name_lower = target_name.lower()

    exact_matches = [
        record for record in records
        if record.get("name", "").lower() == target_name_lower
    ]
    if exact_matches:
        return exact_matches[0]

    prefix_matches = [
        record for record in records
        if record.get("name", "").lower().startswith(target_name_lower)
    ]
    if prefix_matches:
        return prefix_matches[0]

    contains_matches = [
        record for record in records
        if target_name_lower in record.get("name", "").lower()
    ]
    if contains_matches:
        return contains_matches[0]

    return None


def resolve_target_identities():
    identities = []

    user_domain = f"[('name', 'ilike', '{TARGET_PERSON_NAME}')]"
    user_fields = "id,name"
    users = run_search_read('res.users', user_domain, user_fields)
    user_record = pick_target_record(users, TARGET_PERSON_NAME)
    if user_record:
        identities.append(("user_id", user_record["id"], user_record["name"]))

    employee_domain = f"[('name', 'ilike', '{TARGET_PERSON_NAME}')]"
    employee_fields = "id,name,user_id"
    employees = run_search_read('hr.employee', employee_domain, employee_fields)
    employee_record = pick_target_record(employees, TARGET_PERSON_NAME)
    if employee_record:
        identities.append(("employee_id", employee_record["id"], employee_record["name"]))

    if identities:
        return identities

    raise ValueError(
        f"No se encontro un usuario o empleado que coincida con '{TARGET_PERSON_NAME}'."
    )


def fetch_timesheets(start_date, end_date):
    # 1. Validación estricta del formato de fechas
    try:
        datetime.strptime(start_date, "%Y-%m-%d")
        datetime.strptime(end_date, "%Y-%m-%d")
    except ValueError:
        print("❌ Error: Las fechas deben tener el formato estricto YYYY-MM-DD.")
        sys.exit(1)

    # 2. Resolución del usuario/empleado y construcción del dominio
    identities = resolve_target_identities()
    # El CLI espera una lista separada por comas, no un literal de Python.
    fields = "name,task_id,unit_amount,date,project_id,user_id"

    try:
        # 3. Llamada al orquestador odoo-mcp usando el primer identificador que
        # realmente tenga líneas asociadas.
        result = []
        for domain_field, target_id, _target_name in identities:
            domain = (
                f"[('{domain_field}', '=', {target_id}), "
                f"('date', '>=', '{start_date}'), "
                f"('date', '<=', '{end_date}')]"
            )
            result = run_search_read('account.analytic.line', domain, fields)
            if result:
                break

        # Devolvemos el JSON crudo a la terminal para que el Agente IA lo parsee
        print(json.dumps(result, ensure_ascii=False, indent=2))

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
