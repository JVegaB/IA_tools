# Reglas: Toma de Minutas y Auto-Log

---

## ⚠️ ADVERTENCIA ANTES DE LEER: FALLO SISTÉMICO DOCUMENTADO

Este agente tiene un historial comprobado de omitir logs incluso cuando las reglas están escritas claramente. En sesiones reales, completó triage de MR, edición de archivos, commits, pushes, resolución de bugs y diagnósticos técnicos **sin generar un solo log**, y solo lo hizo cuando el usuario lo señaló. Esto ocurrió repetidamente.

**La causa no es falta de gatillos. La causa es que las reglas anteriores permitían que el log fuera un paso opcional al final.** Este archivo corrige eso de raíz.

---

## 1. Registro Autónomo de Hitos (Auto-Log)

### 1.1 El principio fundamental
El log **no es una reflexión al final del turno**. Es el **paso 2 obligatorio** de todo turno que incluya trabajo real:

```
PASO 1 → Trabaja (edita, ejecuta, analiza, decide).
PASO 2 → Ejecuta daily_resume.py. ← ESTO NO ES OPCIONAL.
PASO 3 → Escribe la respuesta al usuario.
```

Si estás en el paso 3 y no ejecutaste el paso 2, **detente ahora mismo** y ejecútalo antes de continuar.

### 1.2 Gatillos que activan el paso 2 obligatoriamente

Cualquiera de los siguientes dispara el log en ese mismo turno, sin excepción:

1. **Hallazgo de Causa Raíz:** Identificaste por qué falla algo (ej. "OWL no traversa dot-notation en dominios", "falta sale_selectable en la ruta").
2. **Decisión de Arquitectura:** Se elige un camino técnico sobre otro (ej. "usamos campo related en lugar de dot-notation").
3. **Desbloqueo:** Se resuelve algo que tenía el desarrollo detenido.
4. **Skill aplicada:** Leíste y ejecutaste un `SKILL.md`. Log al terminar la acción sustantiva.
5. **Verificación cerrada:** Tests pasan, build OK, criterio de "listo para revisión" alcanzado.
6. **Acciones de GitLab** — cualquiera de:
   - Triage completado (ejecutaste `view_context.py` / `view_mr_diff.py` y entregaste clasificación).
   - Resolución de feedback (cambiaste código en respuesta a comentarios de revisores).
   - `git commit` o `git push` exitoso — **incluyendo amends y force-push**.
   - `glab mr update` o `add_note.py` ejecutados con éxito.
   - Análisis técnico con conclusión accionable (manifests, permisos, configuración).
7. **Edición de cualquier archivo del repo**, sin importar qué tan pequeño sea el cambio.
8. **Instalación de dependencias o cambios en el entorno** que afecten el proyecto.

### 1.3 Ejemplos reales de este proyecto donde el log se omitió y NO debería haberse omitido

Estos son casos reales del historial de esta sesión. Úsalos como calibración:

| Acción realizada | ¿Se logueó? | Veredicto |
|---|---|---|
| Triage completo de MR 71 con clasificación de 10+ comentarios | ❌ No | **Fallo grave** |
| Edición de `test_sale_order.py` + `git commit` + `git push` | ❌ No | **Fallo grave** |
| `git commit --amend` para limpiar mensaje de squash | ❌ No | **Fallo grave** |
| `git push --force-with-lease` exitoso | ❌ No | **Fallo grave** |
| `glab mr update` con nueva descripción del MR | ❌ No | **Fallo grave** |
| Verificación de manifests → conclusión "nada que cambiar" | ❌ No | **Fallo grave** |
| Fix de `InvalidDomainError` con restauración de campo related | ❌ No | **Fallo grave** |
| Diagnóstico de `RenderPMError` + `pip install rlPyCairo` | ✅ Sí | Solo tras recordatorio del usuario |
| Mejoras a `.custom_agents` (identity.md, minute_taker.md) | ✅ Sí | Solo tras recordatorio del usuario |

**Conclusión:** sin recordatorio externo, el agente no registra nada. Las reglas deben compensar esto estructuralmente.

### 1.4 La única excepción válida para no loguear
Una respuesta de solo texto (explicación, respuesta a pregunta, análisis sin cambios en disco ni comandos ejecutados) no requiere log. Si no tocaste ningún archivo, no ejecutaste ningún comando, y no tomaste ninguna decisión técnica documentable: puedes omitir.

En caso de duda: **logea**. El costo de un log innecesario es mínimo. El costo de un log omitido es perder el registro permanente del trabajo.

---

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

---

## 3. Ejecución Obligatoria del Script

### 3.1 El script va en el paso 2, no al final

**NO existe un "al terminar la respuesta, ejecuto el script".** El script se ejecuta **antes de escribir la respuesta al usuario**. Si ya enviaste la respuesta y olvidaste el script, es un fallo — corrígelo al inicio del siguiente turno con un log retroactivo explícito.

Cuando se dispare el Auto-Log, o cuando el usuario use `/log [texto]`, TIENES PROHIBIDO solo escribir la respuesta en el chat. Debes ejecutar el siguiente comando en la terminal (raíz del repo):

```bash
python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "[PROYECTO]: [minuta — ver sección 2]"
```

> 🚫 **REGLA DE BLOQUEO DE CLI:** Durante este proceso, el ÚNICO comando permitido en terminal es la invocación a `daily_resume.py`. Tienes expresamente prohibido ejecutar `odoo-mcp` u otros comandos externos para intentar "buscar" información adicional antes de generar el log. Usa solo tu contexto actual.

### 3.2 Recuperación de log omitido (log retroactivo)

Si detectas que omitiste un log en el turno anterior:

```
python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "[repo]: [LOG RETROACTIVO — turno anterior] ..."
```

Documenta qué pasó, por qué y que el log fue retroactivo. Luego continúa con el trabajo normal del turno actual.

### 3.3 Formato para textos largos

Si varios hitos ocurren en el mismo turno, **agrupa en un solo argumento**: un único bloque narrativo largo. Para textos multilínea usa heredoc:

```bash
python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "$(cat <<'EOF'
[edicionesfiscales]: MR 71 — ...
EOF
)"
```

No sustituyas esto por crear archivos de log a mano en el workspace. El único registro válido es el que escribe este script.

*Ejemplo de invocación interna (el contenido puede ser mucho más largo que esto):*
`python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "[edicionesfiscales]: MR 71 consignment_sale — …"`

---

## 4. Comandos de Interacción Adicionales
- `/diff [código]`: Analiza el cambio, explica el impacto funcional y registra automáticamente la tarea en el log usando el script (con la misma profundidad que la sección 2).
