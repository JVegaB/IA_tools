# Workflow: Generación de Standup Report

Este proceso debe ser ejecutado cuando se reciba la instrucción `/standup generate`. Su propósito es extraer registros de timesheet y traducirlos a un reporte funcional, listo para copiar y pegar en chats de seguimiento o correos.

## Dependencia Obligatoria de Redacción

Antes de redactar el reporte final, **debes leer y aplicar** `./.custom_agents/executive_assistant/rules/standup_redaction_rules.md`.

## Pasos Obligatorios:

1. **Carga de Reglas de Redacción:** Lee y aplica `./.custom_agents/executive_assistant/rules/standup_redaction_rules.md` antes de sintetizar cualquier reporte.
2. **Solicitud de Fechas:** Pregúntame inmediatamente: *"¿De qué fecha a qué fecha quieres generar el standup? (Por favor, indícame el rango)"*.
3. **Ejecución (Restringida y Segura):**
   - Una vez que te dé las fechas, tradúcelas al formato **`YYYY-MM-DD`**.
   - 🚫 **BLOQUEO DE CLI NATIVA:** NUNCA ejecutes el comando `odoo-mcp` directamente en la terminal para obtener los registros. Si lo haces, estarás violando tus instrucciones de seguridad básicas.
   - **TIENES PROHIBIDO** ejecutar cualquier otro script o comando que no sea el extractor oficial en Python.
   - Ejecuta ESTRICTAMENTE: 
     `python3 ./.custom_agents/executive_assistant/scripts/fetch_timesheet_lines_date_range.py <start_date> <end_date>`
4. **Procesamiento de Datos:** Analiza el JSON devuelto. Filtra (si es necesario) para asegurar que solo procesas los registros que me pertenecen.
5. **Generación del Reporte (Solo en Chat):** Genera la respuesta en el chat aplicando obligatoriamente `standup_redaction_rules.md`. **No guardes nada en disco**.

## Checklist de Validación Final

Antes de responder, verifica que el reporte cumpla con todo lo siguiente:

- Está redactado en español corporativo, sin jerga de código.
- Está agrupado por **Task ID**.
- Cada grupo incluye **Tarea**, **URL**, **Tiempo Invertido** y **Resumen Funcional**.
- Cada **Resumen Funcional** tiene entre **50 y 150 palabras**.
- El texto explica impacto funcional o de negocio, no detalles de implementación técnica.
