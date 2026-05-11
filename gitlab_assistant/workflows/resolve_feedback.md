# Workflow: Resolución de Feedback

Este flujo se activa cuando estamos listos para atender un MR o Issue específico.

1. **Aplicar Código:** Si hay cambios técnicos pendientes, realiza las ediciones en los archivos locales.
2. **Confirmación Local:** Avísame qué archivos editaste y pídeme que los revise.
3. **Commit (Opcional):** Si acordamos cambiar un mensaje de commit, usa la terminal para hacer `git commit --amend -m "..."`. (Recuerda: NO HAGAS PUSH).
4. **Cierre de Ciclo:** Una vez que yo confirme que hice el `push` manual o que los cambios locales están listos, genera un resumen de los cambios aplicados.
5. **Notificación Remota:** Ejecuta `python3 ./.custom_agents/gitlab_assistant/scripts/add_note.py` publicando ese resumen en el Issue/MR y etiquetando obligatoriamente a los involucrados.
6. **Auto-Log obligatorio:** Inmediatamente después de cualquiera de los pasos 1–5 que haya producido un resultado verificable (archivo editado, commit, push, o nota publicada), ejecuta el script de minutas documentando:
   - El MR/Issue atendido, los comentarios del revisor que motivaron el cambio.
   - Los archivos modificados y la naturaleza del cambio (modelo, vista, test, i18n, etc.).
   - La decisión técnica tomada y alternativas descartadas si las hubo.
   - El resultado de la validación (tests, revisión manual, resultado del push).
   - El seguimiento pendiente (re-revisión del revisor, QA funcional, etc.).
   ```
   python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "[repo]: Resolución feedback MR #ID — ..."
   ```
   > **Nota:** No esperes al paso 5 para loguear. Si en el paso 1 ya editaste archivos y en el paso 3 ya hiciste commit, el log va después del commit aunque el push no haya ocurrido todavía.
