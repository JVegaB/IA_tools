# Referencia de scripts

Todos los scripts invocan **`glab`**. La autenticación y el proyecto remoto activo dependen de tu configuración local de GitLab CLI.

## Convención de rutas

En esta documentación se asume que ejecutas comandos desde la **raíz del repositorio Git** donde está instalado el asistente, por ejemplo:

```bash
cd /ruta/al/repo
python3 ./.custom_agents/gitlab_assistant/scripts/<script>.py ...
```

## `list_my_work.py`

Lista en tres bloques:

1. Issues con `--assignee @me`
2. MRs con `--assignee @me`
3. MRs con `--reviewer @me`

Sin argumentos.

## `view_context.py`

**Uso:** `python3 .../view_context.py <issue|mr> <id>`

- `issue` / `mr` en minúsculas.
- `id` numérico (ej. `363`).

Internamente: `glab issue view` o `glab mr view <id> --comments`.

## `view_mr_diff.py`

**Uso:** `python3 .../view_mr_diff.py <id>`

Equivale a `glab mr diff <id>`. Los diffs grandes conviene canalizar a un paginador: `... | less -R`.

## `add_note.py`

**Uso:** `python3 .../add_note.py <issue|mr> <id> "<mensaje>"`

- El mensaje debe ir en **una sola cadena** de argumento; comillas anidadas y saltos de línea en shell pueden ser incómodos.

### Mensajes largos o multilínea

Opción recomendada: **stdin** con `glab` (misma API que usa el agente en práctica):

```bash
# MR
cat mi_comentario.md | glab mr note create <id>

# Issue (sintaxis puede variar según versión de glab; comprobar con glab issue note create --help)
```

Tras crear la nota, `glab` suele imprimir la URL con ancla `#note_<id>`.

### Otro repositorio

Si el MR está en otro proyecto, añade el flag de repo de `glab`, por ejemplo `-R grupo/subgrupo/proyecto`.
