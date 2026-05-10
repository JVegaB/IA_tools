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

#### Cursor

1. Navega hasta el workspace deseado.
2. Ejecuta la descarga de agentes.

```sh
curl -s "https://raw.githubusercontent.com/JVegaB/IA_tools/refs/heads/master/setup_agents.sh" | bash
```

3. Inicia un nuevo chat dentro del workspace preparado.

## Principios
- Menor privilegio: los skills no deben pedir al agente acciones destructivas o privilegiadas salvo que el módulo lo documente y tú lo aceptes.
- Sin secretos en el repo: tokens, .env y credenciales fuera del control de versiones; los scripts asumen auth ya configurada en el entorno (glab, APIs, etc.).
- Documentar el contrato: qué comandos dispara el usuario, qué hace el agente y qué queda manual.
