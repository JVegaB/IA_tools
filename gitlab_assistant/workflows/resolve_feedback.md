# Workflow: Resolución de Feedback

Este flujo se activa cuando estamos listos para atender un MR o Issue específico.

1. **Aplicar Código:** Si hay cambios técnicos pendientes, realiza las ediciones en los archivos locales.
2. **Confirmación Local:** Avísame qué archivos editaste y pídeme que los revise. 
3. **Commit (Opcional):** Si acordamos cambiar un mensaje de commit, usa la terminal para hacer `git commit --amend -m "..."`. (Recuerda: NO HAGAS PUSH).
4. **Cierre de Ciclo:** Una vez que yo confirme que hice el `push` manual o que los cambios locales están listos, genera un resumen de los cambios aplicados.
5. **Notificación Remota:** Ejecuta `python3 ./.custom_agents/gitlab_assistant/scripts/add_note.py` publicando ese resumen en el Issue/MR y etiquetando obligatoriamente a los involucrados.
