# Workflow: Gestión Diaria de Timesheets, Generado de summary.

Este proceso debe ser ejecutado cuando se reciba la instruccion `/summary review`.

El proceso tiene como finalidad producir un texto con un formato JSON estricto. El cual contendra las entradas de timesheet (minutas), con su respectivo task ID, descripcion, y horas trabajadas.

El punto de este proceso, es que tengamos una conversacion donde afinemos detalles en los timesheets a guardar y podamos realizar cambios y/o ajustes generando un borrador. Y cuando yo lo apruebe, guardarlo con la herramienta `python3 ./.custom_agents/executive_assistant/scripts/store_daily_resume.py`.

## Convención de rutas y variable de entorno

Los scripts `daily_resume.py`, `show_daily_resume.py`, `store_daily_resume.py` y `store_get_daily_resume.py` respetan **`DAILY_RESUMES_PATH`**. Si no está definida, todos usan por defecto el **home del usuario** (`~`), bajo `~/YYYY_MM_DD/` (logs, `processed_summary.txt`, etc.). Opcionalmente puedes fijar otra base, por ejemplo:

`export DAILY_RESUMES_PATH="$HOME"`

## Sin archivos intermedios en el workspace (obligatorio para el agente)

- El borrador del JSON y las minutas **viven en la conversación** (contexto del agente), no en ficheros que el agente cree con herramientas del IDE.
- **Prohibido** para cumplir este flujo: crear en el repo archivos tipo `timesheet_summary.json`, `.timesheet_*.txt`, copias de resumen, o usar `$(cat archivo)` / redirecciones a archivo **solo para alimentar** `store_daily_resume.py`. La carga debe ser **un único primer argumento** en la línea de comandos.
- **Permitido / esperado:** que los **scripts Python de este proyecto** escriban en rutas externas al workspace cuando tú los invoques así: `python3 ./.custom_agents/executive_assistant/scripts/<script>.py "<texto>"`. El agente no “reimplementa” ese guardado; solo construye el string y lo pasa.

## Invocación de scripts (obligatorio para el agente)

- **Sí:** una sola orden del tipo `python3 ./.custom_agents/executive_assistant/scripts/<nombre>.py` con **un único argumento** string cuando el script lo requiera (mismo patrón que `daily_resume.py` y `store_daily_resume.py`).
- **No:** `python3 -c "..."`, scripts inline, `subprocess` desde otro programa, ni atajos que sustituyan al binario del repo. Así la aprobación de permisos coincide con “solo ejecuté tu programa”.

1. **Extracción:** Ejecuta silenciosamente `python3 ./.custom_agents/executive_assistant/scripts/show_daily_resume.py` (con el mismo `DAILY_RESUMES_PATH` que usaste al registrar `/log`) para obtener todos los hitos y logs del día actual.
2. **Análisis Colaborativo:** Presenta la información en el chat y pídeme que te ayude a agrupar esos logs en "Entradas de Timesheet".
3. **Estructura:** Agrupar obligatoriamente por PROYECTO.
4. **Enfoque (What/Why/How):** Describir el Problema, la Causa Técnica y la Solución Implementada. Evitar descripciones vagas.
5. **Estructuración:** Para cada entrada, debemos definir colaborativamente:
   - Idioma (ej. Inglés Técnico o Español).
   - Longitud máxima (ej. 100 palabras).
   - Link o ID de la tarea asociada (ej. ID de Odoo o GitLab).
   - Tiempo a imputar (ej. 2.5 horas).
   - Descripción técnica del trabajo (What/Why/How).
6. **Formato Estricto:** Una vez que acordemos los IDs y los tiempos, debes generar un **JSON de arrays válido** con esta estructura exacta para Odoo:
   ```json

   [
     {
       "name": "Descripción técnica (Qué/Por qué/Cómo)",
       "task_id": 8902,
       "unit_amount": 2.5
     }
   ]

  ```
7. **Guardado en Memoria:** Cuando yo apruebe la lista final, construye en tu contexto el **JSON válido** (un solo array) y ejecútalo **directamente en terminal** pasándolo como **primer y único argumento** de texto a `store_daily_resume.py`. No crees ningún archivo en el workspace para esto; el propio script escribe donde corresponda fuera del repo.

   Desde la raíz del proyecto, con el mismo `DAILY_RESUMES_PATH` que en el paso 1 si aplica:

   ```bash
   export DAILY_RESUMES_PATH="${DAILY_RESUMES_PATH:-$HOME}"
   python3 ./.custom_agents/executive_assistant/scripts/store_daily_resume.py '[{"name":"…","task_id":8902,"unit_amount":2.5}]'
   ```

   Usa **comillas simples** en bash para envolver el JSON (como en `weekly_timesheet_push_summary.md`), de modo que las comillas dobles internas del JSON no rompan el comando. Si algún `name` debe contener una comilla simple `'` que chocaría con bash, reformula el texto o escapa según bash; prioriza **JSON en una sola línea** para reducir errores.

   **Salida esperada:** mensaje de confirmación del script; el contenido lo persiste **solo** `store_daily_resume.py` bajo `$DAILY_RESUMES_PATH/YYYY_MM_DD/processed_summary.txt`.
