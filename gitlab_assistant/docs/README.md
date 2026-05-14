# Asistente de GitLab

Documentación del paquete **gitlab_assistant**: reglas, flujos y scripts para que el agente en Cursor te ayude con GitLab **sin** operaciones de privilegio elevado en el remoto (merge, push, etiquetas, etc.).

## Principios (zero-trust)

- El asistente actúa como revisor y enlace con GitLab bajo **menor privilegio**.
- **Prohibido** para el agente: `git push`, fusionar MRs, cambiar etiquetas, títulos o milestones en el remoto.
- **Permitido** (vía `glab` y scripts): listar trabajo, leer contexto de issues/MR, ver diffs y **publicar comentarios** con `add_note.py` cuando tú lo pidas.

La identidad resumida vive en [`../identity.md`](../identity.md). La integración con Cursor suele declararse en `.cursorrules` del repositorio (por ejemplo `/gla triage` o `/gla documentate`).

## Requisitos

| Requisito | Notas |
|-----------|--------|
| **Python 3** | Los scripts usan la biblioteca estándar y `subprocess`. |
| **[GitLab CLI `glab`](https://gitlab.com/gitlab-org/cli)** | Autenticado contra tu instancia (`glab auth login`). |
| **Repo Git** | Con remoto que `glab` reconozca (mismo proyecto que el MR/issue). |

### `glab` instalado como Snap

En entornos restringidos (p. ej. sandbox de CI o herramientas sin permisos completos), `glab` puede fallar con errores de `snap-confine` o permisos sobre `~/snap`. Ejecuta los scripts **fuera del sandbox** o con permisos equivalentes a una sesión de usuario normal.

## Comandos en el chat (Cursor)

| Comando | Acción del agente |
|---------|-------------------|
| `/gla triage` | Lee [`../rules/reviewer.md`](../rules/reviewer.md) y sigue [`../workflows/triage.md`](../workflows/triage.md). |
| `/gla documentate <link al MR>` | Lee [`../rules/mr_documentation.md`](../rules/mr_documentation.md) y sigue [`../workflows/documentate_mr.md`](../workflows/documentate_mr.md). |

*Si cambias el prefijo público del paquete, alínialo también en `.cursorrules` para que siga apuntando a estos mismos archivos.*

## Estructura del paquete

```text
.custom_agents/gitlab_assistant/
├── docs/
│   └── README.md          ← este archivo
├── identity.md
├── rules/
│   ├── reviewer.md        # Clasificación de comentarios y comunicación
│   └── mr_documentation.md
├── workflows/
│   ├── triage.md          # Revisión de carga de trabajo
│   ├── documentate_mr.md
│   └── resolve_feedback.md # Guía interna de cierre de ciclo; no comando expuesto
└── scripts/
    ├── list_my_work.py
    ├── view_context.py
    ├── view_mr_diff.py
    └── add_note.py
```

## Scripts (referencia rápida)

Ejecutar desde la **raíz del repositorio** de trabajo (donde vive `.custom_agents/`):

| Script | Uso | Descripción |
|--------|-----|----------------|
| `list_my_work.py` | `python3 ./.custom_agents/gitlab_assistant/scripts/list_my_work.py` | Issues asignados a ti, MRs asignados y MRs donde eres revisor. |
| `view_context.py` | `python3 ./.custom_agents/gitlab_assistant/scripts/view_context.py <issue\|mr> <id>` | Descripción y comentarios del ítem (`glab issue view` / `glab mr view --comments`). |
| `view_mr_diff.py` | `python3 ./.custom_agents/gitlab_assistant/scripts/view_mr_diff.py <id>` | Diff del MR (`glab mr diff`). |
| `add_note.py` | `python3 ./.custom_agents/gitlab_assistant/scripts/add_note.py <issue\|mr> <id> "<mensaje>"` | Publica una nota en el issue o MR. Para textos largos o multilínea, usa `glab mr note create` / `glab issue note create` con entrada por stdin (ver [referencia de scripts](scripts.md)). |

## Flujos (resumen)

- **Triage:** lista tu trabajo → resumen en chat → profundizar por ID → contexto + diff si es MR → clasificar comentarios pendientes según `reviewer.md`. Detalle: [`../workflows/triage.md`](../workflows/triage.md).
- **Documentar MR:** leer descripción + diff → preservar información útil → reescribir body con plantilla estructurada → verificar en GitLab. Detalle: [`../workflows/documentate_mr.md`](../workflows/documentate_mr.md).
- **Resolver feedback (referencia interna):** `resolve_feedback.md` se conserva como guía operativa para ordenar cambios y notas cuando el triage detecte trabajo accionable, pero ya no se expone como comando de chat.

## Clasificación de comentarios

Al leer hilos de un MR/issue, el asistente debe clasificar peticiones según [`../rules/reviewer.md`](../rules/reviewer.md):

1. **Respuesta directa** (duda, justificación): redactar respuesta y, si aplica, publicar con `add_note.py` / `glab`.
2. **Acción manual** (título, etiquetas, merge, rebase remoto): indicar que debe hacerse en la web; el agente no lo ejecuta.
3. **Código / terminal local:** editar en el workspace; `git commit`/`amend` solo si acordado; **sin push**. Si el triage detecta este caso, puede consultarse `../workflows/resolve_feedback.md` como guía interna.

## Enlaces útiles

- [Referencia detallada de scripts](scripts.md)
- [Plantilla de comentario POC (IA)](poc-note-template.md) — texto opcional para coordinación en MRs, con aviso de mensaje asistido por IA.

## Mantenimiento

Si cambias rutas de scripts o comandos `/gla`, actualiza este `README.md`, `scripts.md` y `.cursorrules` para que sigan coincidiendo.
