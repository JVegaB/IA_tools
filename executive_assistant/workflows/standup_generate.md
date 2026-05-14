# Workflow: Generación de Standup Report

Este proceso debe ser ejecutado cuando se reciba la instrucción `/standup generate`. Su propósito es extraer registros de timesheet y traducirlos a un reporte funcional, listo para copiar y pegar en chats de seguimiento o correos.

## Pasos Obligatorios:

1. **Solicitud de Fechas:** Pregúntame inmediatamente: *"¿De qué fecha a qué fecha quieres generar el standup? (Por favor, indícame el rango)"*.
2. **Ejecución (Restringida):**
   - Una vez que te dé las fechas, tradúcelas al formato **`YYYY-MM-DD`**.
   - **TIENES PROHIBIDO** ejecutar cualquier otro script o comando durante este flujo interactivo que no sea el extractor.
   - Ejecuta: `python3 ./.custom_agents/executive_assistant/scripts/fetch_timesheet_lines_date_range.py <start_date> <end_date>`.
3. **Procesamiento de Datos:** Analiza el JSON devuelto. Filtra (si es necesario) para asegurar que solo procesas los registros que me pertenecen.
4. **Generación del Reporte (Solo en Chat):** Genera la respuesta en el chat. **No guardes nada en disco**. 
