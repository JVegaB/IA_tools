# AI tools & skills

Repositorio central de **herramientas, flujos y skills** reutilizables para asistentes de IA (p. ej. Cursor, agentes con reglas explícitas). Cada carpeta es un **módulo autocontenido** con convenciones estables para que el modelo (o tú) lo referencie con `@ruta/al/modulo`.

## Contenido

| Módulo | Descripción |
|--------|-------------|
| [`executive_assistant/`](./executive_assistant/) | Asistente orientado a agenda, seguimiento y comunicación. |
| [`gitlab_assistant/`](./gitlab_assistant/) | Integración con GitLab vía `glab`, triage de MR/issues y reglas de menor privilegio. |

*(Añade aquí nuevas filas al incorporar módulos.)*

## Estructura sugerida por módulo

Cada asistente puede organizarse como prefieras; un patrón que escala bien:

```text
<nombre>_assistant/
├── docs/
│   └── README.md          # Documentación humana del módulo
├── rules/                 # Reglas de comportamiento (markdown)
├── workflows/             # Pasos por comando o tarea
├── scripts/               # Automatización opcional (CLI, APIs)
└── identity.md            # Rol y límites del asistente (opcional)
```

## Uso en el IDE / agente

1. Clona o enlaza este repo en tu workspace (submódulo, copia, o extra_addons-style según tu flujo).
2. En reglas del proyecto (p. ej. .cursorrules) referencia el módulo con rutas explícitas, por ejemplo:
  - @gitlab_assistant/rules/reviewer.md
  - @gitlab_assistant/workflows/triage.md
3. Mantén un solo lugar como fuente de verdad por módulo; evita duplicar el mismo skill en varios repos sin versión.

## Principios
- Menor privilegio: los skills no deben pedir al agente acciones destructivas o privilegiadas salvo que el módulo lo documente y tú lo aceptes.
- Sin secretos en el repo: tokens, .env y credenciales fuera del control de versiones; los scripts asumen auth ya configurada en el entorno (glab, APIs, etc.).
- Documentar el contrato: qué comandos dispara el usuario, qué hace el agente y qué queda manual.
