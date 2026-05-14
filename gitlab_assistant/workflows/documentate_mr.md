# Workflow: Documentar un Merge Request

Este flujo se activa cuando el usuario pide:

`/gla documentate <link al MR>`

El objetivo es **mejorar la descripción del MR** para que quede lista para revisión humana, usando la plantilla y reglas de `@.custom_agents/gitlab_assistant/rules/mr_documentation.md`.

## Pasos

1. **Leer la regla de documentación**
   - Lee primero `@.custom_agents/gitlab_assistant/rules/mr_documentation.md`.

2. **Resolver el MR objetivo**
   - Si el usuario dio una URL completa, extrae el ID del MR.
   - Si el enlace es ambiguo o no corresponde a un MR, detente y pide aclaración.

3. **Leer el estado actual del MR**
   - Ejecuta `glab mr view <id>` para leer la descripción actual.
   - Ejecuta `glab mr view <id> --comments` si necesitas contexto adicional del hilo.
   - Ejecuta `glab mr diff <id>` para entender el alcance real del cambio.

4. **Preservar lo que ya sirve**
   - Identifica y conserva:
     - links de tickets
     - screenshots o evidencias
     - notas de validación
     - caveats útiles
     - cualquier bloque que aporte contexto real
   - Reorganiza y expande; no empobrezcas la descripción.

5. **Redactar la nueva descripción**
   - Usa la estructura definida en `mr_documentation.md`.
   - Elige entre `Impact of the bug` o `Impact of the limitation` según corresponda.
   - Añade tabla explicativa bajo `Solution` cuando el cambio toque varias capas o helpers.
   - Añade `Before / After` si ayuda a visualizar el cambio.
   - En `Test plan`, separa claramente validación ejecutada vs pendiente.

6. **Actualizar el MR**
   - Ejecuta `glab mr update <id> --description "..."`.
   - Está permitido actualizar el **body** del MR en este flujo.
   - No cambies título, labels, milestones o reviewers como parte de este comando.

7. **Verificación**
   - Relee el MR con `glab mr view <id>` para confirmar que el body quedó publicado como se esperaba.
   - Si detectas warnings de metadata (por ejemplo, formato del task ID en el título), repórtalos como **Acción Manual**; no los resuelvas cambiando el título.

8. **Respuesta al usuario**
   - Resume qué se mejoró en la descripción.
   - Señala cualquier pendiente manual detectado en el hilo.

9. **Auto-Log obligatorio**
   - Inmediatamente después de actualizar el MR o completar el análisis del hilo, ejecuta:
   - `python3 ./.custom_agents/executive_assistant/scripts/daily_resume.py "[repo]: Documentación MR #ID — ..."`
   - La minuta debe incluir:
     - MR atendido
     - estructura aplicada
     - información preservada
     - cambios principales en el body
     - validación hecha con `glab mr view`
     - pendientes manuales si los hubo

## Resultado esperado

Un MR con descripción:

- clara para reviewers
- consistente con el diff real
- rica en contexto funcional y técnico
- explícita en su validación
- sin perder la información valiosa que ya tenía
