# Workflow: Triage de GitLab

Este flujo sirve para revisar mi carga de trabajo actual en el repositorio que tengo abierto.

1. **Obtener Lista:** Ejecuta `python3 ./.custom_agents/gitlab_assistant/scripts/list_my_work.py`.
2. **Análisis Inicial:** Muestra en el chat un resumen estructurado (Issues vs MRs).
3. **Profundizar:** Pregúntame: *"¿Qué ID quieres que revisemos a detalle?"*.
4. **Extraer Contexto:** Cuando te dé el ID (ej. MR 45), ejecuta inmediatamente `python3 ./.custom_agents/gitlab_assistant/scripts/view_context.py` (y `python3 ./.custom_agents/gitlab_assistant/scripts/view_mr_diff.py` si es un MR) para leer todo el hilo.
5. **Reporte de Pendientes:** Enumera los comentarios pendientes usando las Reglas de Clasificación (Respuestas Directas, Acciones Manuales, Cambios de Código).
