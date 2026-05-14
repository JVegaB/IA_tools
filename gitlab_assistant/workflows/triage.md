# Workflow: Triage de GitLab

Este flujo sirve para revisar mi carga de trabajo actual en el repositorio que tengo abierto.

1. **Obtener Lista:** Ejecuta `python3 ./.custom_agents/gitlab_assistant/scripts/list_my_work.py`.
2. **Análisis Inicial:** Muestra en el chat un resumen estructurado (Issues vs MRs).
3. **Profundizar:** Pregúntame: *"¿Qué ID quieres que revisemos a detalle?"*.
4. **Extraer Contexto:** Cuando te dé el ID (ej. MR 45), ejecuta inmediatamente `python3 ./.custom_agents/gitlab_assistant/scripts/view_context.py` (y `python3 ./.custom_agents/gitlab_assistant/scripts/view_mr_diff.py` si es un MR) para leer todo el hilo.
5. **Reporte de Pendientes:** Enumera los comentarios pendientes usando las Reglas de Clasificación (Respuestas Directas, Acciones Manuales, Cambios de Código).
   - Usa `@.custom_agents/gitlab_assistant/rules/reviewer.md` como criterio obligatorio de clasificación.
   - Si del triage sale trabajo accionable de implementación o respuesta, puedes apoyarte internamente en `@.custom_agents/gitlab_assistant/workflows/resolve_feedback.md` para ordenar el cierre del ciclo, pero **sin** tratarlo como un comando separado para el usuario.
6. **Auto-Log obligatorio:** Al terminar el reporte del paso 5, ejecuta el script de minutas documentando:
   - El MR/Issue analizado y su estado general (abierto, bloqueado, en revisión).
   - La clasificación de cada comentario pendiente (tipo, autor, prioridad si la tiene).
   - Los items que ya están resueltos vs. los que aún requieren acción.
   - El siguiente paso recomendado para el usuario.
   ```
   python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "[repo]: Triage MR/Issue #ID — ..."
   ```
