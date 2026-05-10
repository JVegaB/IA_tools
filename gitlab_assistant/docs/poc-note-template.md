# Plantilla: comentario POC (asistencia IA)

Texto opcional para publicar en un MR o issue cuando quieras **coordinar** sin presentar el mensaje como dictamen oficial. Ajusta menciones y fechas según el hilo.

Copia desde la línea siguiente (incluye el aviso).

---

**Aviso:** este mensaje es una **POC** (prueba de concepto) generada con **asistencia automatizada por IA**; no sustituye criterio humano ni decisiones oficiales del equipo. Puede contener imprecisiones.

---

Hola @usuario1 @usuario2

[… cuerpo del mensaje …]

Quedo atento a feedback; de nuevo, esto es solo **POC de mensaje asistido por IA** para agilizar la coordinación, no un dictamen técnico.

---

## Cómo publicarlo

Ver [scripts.md](scripts.md) (sección mensajes multilínea) o usar:

```bash
cat mensaje.md | glab mr note create <id>
```
