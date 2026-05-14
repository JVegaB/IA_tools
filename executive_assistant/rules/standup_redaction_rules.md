# Reglas de Redacción: Reportes de Standup (Técnico a Funcional)

Cuando redactes un reporte generado por `/standup generate`, tu objetivo cambia: ya no le hablas a un Tech Lead, le hablas a un Project Manager (PM) o Consultor Funcional.

## 1. Audiencia y Tono
- El tono debe ser ejecutivo, directo y enfocado en el progreso del negocio.
- **Prohibición de Jerga (Cero Código):** Tienes estrictamente prohibido usar términos como: *OWL, XML, Python, commits, PRs, override, herencia, queries, refactor, variables, decorators*.

## 2. Traducción de Valor (El "So What?")
Cada bloque de tiempo debe explicar **qué puede hacer el usuario ahora** o **qué flujo de negocio se desbloqueó**.

* 🚫 **Prohibido (Técnico):** "Hice un override al método _compute_amount y modifiqué el XML del POS para mostrar el total."
* ✅ **Obligatorio (Funcional):** "Se habilitó la visualización de los totales actualizados directamente en la pantalla de cobro del Punto de Venta, agilizando el proceso para los cajeros."

## 3. Manejo de Errores/Bugs
Si las horas extraídas pertenecen a la corrección de un bug, no expliques por qué fallaba el código. Explica qué impacto tenía en el negocio y que ya está resuelto.
* ✅ **Ejemplo:** "Se corrigió una interrupción en el flujo de facturación electrónica que bloqueaba la emisión de comprobantes en casos de notas de crédito."


## 4.Reglas Estrictas de Formato y Redacción:
El resultado debe cumplir OBLIGATORIAMENTE con lo siguiente:

* **Idioma:** Español (Latinoamérica, tono corporativo).
* **Audiencia:** Orientado a Team Leads, Project Managers y consultores funcionales. **Cero jerga de código puro** (ej. no hables de *vistas OWL, commits, domains, overrides, methods*). Traduce el trabajo a **valor de negocio, resolución de flujos funcionales e impacto de cara al usuario**.
* **Agrupación:** Agrupa la información por **Task ID**.
* **Estructura por Grupo:**
  - **Tarea:** `[#Task_ID] - Nombre de la Tarea`
  - **URL:** (Asume o construye la URL hacia tu Odoo/Gitlab si el JSON provee la base, o deja el placeholder `https://www.wordhippo.com/what-is/the-meaning-of/spanish-word-la_tarea.html`).
  - **Tiempo Invertido:** Sumatoria total de `unit_amount` (horas) de todas las líneas de esa tarea.
  - **Resumen Funcional:** Un párrafo integrado de **50 a 150 palabras máximo**. Sintetiza todas las minutas de esa tarea en una historia coherente. ¿Qué flujo de negocio se habilitó o corrigió? ¿Qué puede hacer el usuario ahora que antes no podía?
