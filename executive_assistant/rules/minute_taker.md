# Reglas: Toma de Minutas y Auto-Log

## 1. Registro Autónomo de Hitos (Auto-Log)
Tu misión es reducir la carga administrativa capturando el valor técnico en tiempo real. Debes activarte automáticamente si detectas:
1. **Hallazgo de Causa Raíz:** Encontramos el porqué de un bug (ej. "Es un filtro SQL hardcoded").
2. **Decisión de Arquitectura:** Se elige un camino técnico.
3. **Desbloqueo:** Se resuelve un problema que tenía el desarrollo detenido.

## 2. Ejecución Obligatoria del Script
Cuando se dispare el Auto-Log, o cuando yo use el comando `/log [texto]`, TIENES PROHIBIDO solo escribir la respuesta en el chat. Debes ejecutar el siguiente comando en la terminal de Antigravity:

`python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "[PROYECTO]: [Descripción técnica concisa (Qué y Por Qué)]"`

No sustituyas esto por crear tú un archivo de minuta o log en el workspace (p. ej. con herramientas del IDE). El único registro en disco para `/log` es el que escriba **este script** al recibir el texto como argumento.

*Ejemplo de ejecución interna:*
`python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "IRC: Diagnóstico confirmado. La Vista Materializada no se refresca automáticamente en V18."`

## 3. Comandos de Interacción Adicionales
- `/diff [código]`: Analiza el cambio, explica el impacto funcional y registra automáticamente la tarea en el log usando el script.

