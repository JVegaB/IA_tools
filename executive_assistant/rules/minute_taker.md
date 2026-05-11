# Reglas: Toma de Minutas y Auto-Log

## 1. Registro Autónomo de Hitos (Auto-Log)
Tu misión es reducir la carga administrativa capturando el valor técnico en tiempo real. Debes activarte automáticamente si detectas:
1. **Hallazgo de Causa Raíz:** Encontramos el porqué de un bug (ej. "Es un filtro SQL hardcoded").
2. **Decisión de Arquitectura:** Se elige un camino técnico.
3. **Desbloqueo:** Se resuelve un problema que tenía el desarrollo detenido.
4. **Skill aplicada:** Has leído y seguido un `SKILL.md` (usuario o `.cursor/skills-cursor/...`) y completaste la acción sustantiva que esa skill ordenaba (implementación, CI, canvas, etc.). No dispares auto-log si solo leíste la skill sin ejecutar trabajo.
5. **Verificación cerrada:** Tests pasan, build/instalación OK, o criterio de "listo para revisión" acordado en el hilo.
6. **Acciones de GitLab** (cualquiera de las siguientes):
   - Triage completado: ejecutaste `view_context.py` o `view_mr_diff.py` y entregaste un reporte de pendientes clasificado.
   - Resolución de feedback: aplicaste cambios de código en respuesta a comentarios de revisores.
   - `git commit` o `git push` exitoso, incluyendo amends y force-push.
   - Actualización de metadatos del MR: descripción, nota con `add_note.py`, o `glab mr update`.
   - Cualquier análisis técnico (manifests, permisos, CI) que derivó en una conclusión accionable.

### Ejemplos de gatillo GitLab → log inmediato
- Ejecuté `view_context.py mr 71` y clasifiqué comentarios pendientes → **log al entregar el reporte.**
- Edité `tests/test_sale_order.py` en respuesta a feedback de revisor y hice `git commit` → **log tras el commit/push.**
- Hice `git commit --amend` para limpiar un squash y `git push --force-with-lease` → **log al confirmar el push.**
- Actualicé la descripción del MR con `glab mr update` → **log al confirmar "✓ updated body".**
- Verifiqué manifests y concluí "nada que cambiar" → **log al dar la conclusión.**

## 2. Profundidad obligatoria del texto que envías al script
Las minutas **no** tienen límite de longitud por defecto. El usuario espera poder **reconstruir el hito** sin estar en la sala: qué archivos, qué decisión, qué error había antes y cómo se comprobó el después.

### 2.1 Checklist (incluye todo lo que aplique en cada log)
- **Ámbito:** proyecto/carpeta del workspace; si existe enlace o número, MR/issue/tarea (ej. MR 71, T#98843).
- **Alcance del cambio:** rutas de archivo o agrupación (`consignment_sale/models/…`, `views/…`, `tests/…`).
- **Comportamiento antes / problema:** síntoma, comentario de revisor, fallo de test, constraint de negocio.
- **Solución:** cambios concretos (API, dominio, vista, test), alternativas consideradas si fueron relevantes.
- **Validación:** comando exacto o categoría de prueba (`odoo-bin … --test-tags=…`), resultado; si falló primero y luego pasó, menciona la causa raíz del fallo intermedio.
- **Seguimiento humano:** push a GitLab, respuesta a revisores, riesgos — solo si aplica.

### 2.2 Estilo y tono
- Aplica `@.custom_agents/executive_assistant/rules/redaction_rules.md` para **claridad y valor**, no para acortar: puedes usar varios párrafos, listas con guiones, y citas de errores o mensajes de test cuando ayuden.
- El método STAR o micro-STAR del archivo de redacción puede **expandirse** a varios párrafos cuando el hito lo merece.

### 2.3 Anti-malentendidos
- **Un disparo al script por turno del agente** sigue siendo la norma (agrupa hitos en un solo texto si hubo varios en el mismo turno).
- **No** sustituyas profundidad por una lista de frases separadas por `; ` salvo que el usuario pida explícitamente un formato ultracorto.

## 3. Ejecución Obligatoria del Script
Cuando se dispare el Auto-Log, o cuando yo use el comando `/log [texto]`, TIENES PROHIBIDO solo escribir la respuesta en el chat. Debes ejecutar el siguiente comando en la terminal (raíz del repo, con permisos de escritura si el script guarda fuera del workspace):

`python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "[PROYECTO]: [minuta desarrollada — ver sección 2]"`

Si varios hitos ocurren en el mismo turno del agente, **agrupa en un solo argumento**: preferiblemente **un único bloque narrativo largo** que cubra todos los hitos; solo usa separadores breves (`; ` o subtítulos en la misma cadena) si ayuda a la lectura. Respeta "no log" / "sin minuta" / "skip log" en el mensaje del usuario para ese turno.

Para textos largos o multilínea, usa comillas que preserven saltos de línea o un heredoc en shell; el script escribe el argumento tal cual en el archivo de salida.

No sustituyas esto por crear tú un archivo de minuta o log en el workspace (p. ej. con herramientas del IDE). El único registro en disco para `/log` es el que escriba **este script** al recibir el texto como argumento.

*Ejemplo de invocación interna (el contenido puede ser mucho más largo que esto):*
`python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "[edicionesfiscales]: MR 71 consignment_sale — …"`

## 4. Comandos de Interacción Adicionales
- `/diff [código]`: Analiza el cambio, explica el impacto funcional y registra automáticamente la tarea en el log usando el script (con la misma profundidad que la sección 2).
