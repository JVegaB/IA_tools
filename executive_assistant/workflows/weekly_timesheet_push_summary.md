# Workflow: Gestión Diaria de Timesheets (Push to Odoo)

Este flujo obtiene un resumen previamente generado usando la herramienta de lectura local, para después inyectarlo en el ERP a través de nuestro orquestador en Python.

1. **Recuperación:** Ejecuta `python3 ./.custom_agents/executive_assistant/scripts/store_get_daily_resume.py` para extraer de disco el resumen previamente aprobado.
2. **Validación:** Si el script devuelve un error, detén el proceso e infórmame. No intentes continuar.
3. **Ejecución de Carga (Push):** Si se recupera el texto con éxito, es necesario utilizar ese texto resultante (el cual debe ser un formato JSON válido) y pasarlo como argumento al script de subida.
   - **Script a ejecutar:** `./.custom_agents/executive_assistant/scripts/push_timesheet.py`
   - **Ejemplo de uso** (mandando un texto que representa un JSON):
     `python3 ./.custom_agents/executive_assistant/scripts/push_timesheet.py '[{"name": "Optimizacion de queries", "task_id": 123, "unit_amount": 1.5}]'`
   *(Nota: Usa comillas simples `'` para envolver el argumento JSON en la terminal de bash y evitar conflictos con las comillas dobles internas).*
4. **Confirmación:** Lee la salida del script. Avísame cuando la carga haya finalizado exitosamente mostrando los IDs, o repórtame exactamente el error si hubo algún problema con el ORM de Odoo.
