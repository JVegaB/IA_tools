# Reglas: Documentación de Merge Requests

Este archivo define cómo debe redactarse o mejorarse la **descripción de un MR** cuando el usuario pida `/gla documentate <link al MR>`.

## Objetivo

Transforma una descripción pobre, corta o desordenada en una narrativa de revisión que explique claramente:

1. **qué problema existía**
2. **por qué importaba**
3. **qué solución se implementó**
4. **qué archivos cambiaron**
5. **cómo se validó**

La meta no es “llenar secciones”, sino dejar un MR que pueda revisarse con contexto suficiente **sin abrir inmediatamente el diff**.

## Principios obligatorios

1. **Preserva la información útil existente**
   - No borres enlaces a tickets, capturas, caveats, pasos manuales o notas de validación que ya estén en la descripción.
   - Si la descripción actual ya contiene contenido valioso, **reorganízalo y expándelo**; no lo sustituyas por un resumen más corto.

2. **No inventes nada**
   - No inventes validaciones, screenshots, riesgos, decisiones de arquitectura ni impactos de negocio.
   - Si algo no fue ejecutado, márcalo como pendiente o simplemente no lo afirmes.

3. **La descripción final debe ser autocontenida**
   - Debe explicar el contexto funcional y técnico del cambio.
   - Debe conectar el diff con el problema que resuelve.
   - Debe dejar claro el comportamiento antes y después cuando eso aporte valor.

4. **No menciones IA**
   - Nunca expliques que la descripción fue redactada, asistida o mejorada por IA.
   - Nunca uses disclaimers de automatización en la descripción del MR.

5. **Respeta Zero-Trust**
   - Puedes actualizar el **body/description** del MR.
   - No cambies título, etiquetas, milestones, merge state o reviewers como parte de este flujo, salvo instrucción explícita del usuario y solo si las reglas del workspace lo permiten.

## Plantilla por defecto

Usa esta estructura salvo que la descripción actual ya tenga otra equivalente mejor:

```md
## Tickets

<links o referencias de tickets>

---

## Problem

<explicación del problema o limitación>

### Impact of the bug
o
### Impact of the limitation

- ...

---

## Solution

<explicación de la solución>

### Why the fix lives in ...
o
### Why the change spans ...

| Option / Layer | Why |
|---|---|
| ... | ... |

---

## Changes

| File | What changed |
|---|---|
| ... | ... |

---

## Before / After

**Before** — ...

**After** — ...

---

## Test plan

- [x] ...
- [ ] ...
```

## Reglas de contenido por sección

### `## Tickets`
- Conserva todos los links relevantes que ya existan.
- Si la descripción actual ya trae el ticket correcto, mantenlo arriba.
- No inventes números de tarea.

### `## Problem`
- Explica el comportamiento actual o la limitación previa.
- Debe mencionar el endpoint, flujo o capa afectada cuando sea relevante.
- Si es un bug, describe el síntoma observable.
- Si es una mejora, describe la limitación del contrato actual o del flujo existente.

### `### Impact of the bug / limitation`
- Usa `bug` si el cambio corrige una falla.
- Usa `limitation` si el cambio amplía o mejora comportamiento válido pero insuficiente.
- Lista consecuencias reales: UX, integraciones, rango funcional, mantenibilidad, etc.

### `## Solution`
- Explica la estrategia general y el comportamiento final.
- Debe dejar claro qué sigue siendo compatible y qué cambia.
- Menciona defaults, backward compatibility, normalización de datos o decisiones relevantes si forman parte del cambio.

### Tabla explicativa bajo `Solution`
- Añádela cuando el cambio toque varias capas, helpers o decisiones de arquitectura.
- El objetivo es explicar **por qué** cada capa se tocó, no repetir el diff.
- Para bugfixes centralizados, puede usar formato tipo:
  - `Why the fix lives in ...`
- Para mejoras transversales, puede usar:
  - `Why the change spans ...`

### `## Changes`
- Usa tabla por archivo si el diff es pequeño o mediano.
- Resume el cambio de cada archivo en lenguaje de revisión, no como lista mecánica de líneas editadas.

### `## Before / After`
- Inclúyela cuando ayude a visualizar el cambio de contrato o comportamiento.
- Puede usar ejemplos de payload, respuesta, flujo o escenario.
- Si no aporta claridad, puedes omitirla.

### `## Test plan`
- Separa claramente lo ejecutado (`[x]`) de lo no ejecutado (`[ ]`).
- Prefiere comandos reales, pruebas agregadas y verificación funcional concreta.
- Si no se pudo correr la suite completa, dilo explícitamente.

## Tono esperado

- Profesional, directo y útil para reviewer técnico.
- Más cercano a una **explicación de diseño** que a un changelog.
- Evita bullets genéricos como “updated code”, “fixed issue”, “added support”.
- Prioriza causalidad:
  - problema
  - impacto
  - decisión
  - resultado

## Cuando el usuario dé un MR de ejemplo

Si el usuario proporciona otro MR como modelo:

1. **Lee solo su descripción** salvo que el usuario pida explícitamente analizar también el diff o comentarios.
2. Copia la **estructura y el nivel de detalle**, no el contenido.
3. Reescribe el MR objetivo con esa misma disciplina narrativa.
