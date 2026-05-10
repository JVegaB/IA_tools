## Reglas de Clasificación de Comentarios (Triage)
Cuando leas los comentarios de un Issue o MR, debes clasificar mentalmente las peticiones en 3 categorías y actuar en consecuencia:

1. **Respuestas Directas (Dudas/Aclaraciones):** Si el comentario es una pregunta o pide una justificación técnica que no requiere tocar el código, redacta una respuesta clara, pídeme aprobación, y usa la herramienta `add_note.py` para publicarla.
2. **Acciones Manuales (Metadatos):** Si piden cambiar el título del MR, asignar a otra persona, cambiar etiquetas o hacer rebase/merge, **DESCARTA** la acción para ti y avísame explícitamente: *"⚠️ Este comentario pide cambiar [X]. Debido a mis restricciones de seguridad, por favor realiza esto manualmente en la interfaz web"*.
3. **Cambios de Código / CLI:** Si piden refactorizar, corregir un bug o cambiar un mensaje de commit:
   - Modifica los archivos locales usando tus capacidades nativas de edición.
   - O sugiéreme el comando de terminal (ej. `git commit --amend`).

## Reglas de Comunicación
- Cuando resuelvas una petición (cambio de código o respuesta), redacta el mensaje final usando `add_note.py`.
- **Regla de Etiquetado:** SIEMPRE debes incluir el `@username` del revisor o persona que dejó el comentario original para notificarle que su petición fue atendida (ej. *"Lista la optimización de la query, @jperez. Revisa el nuevo diff."*).
