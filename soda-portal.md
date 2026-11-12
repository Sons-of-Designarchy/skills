# Soda Portal — timeline y board del cliente

**Trigger:** `/soda-portal <slug>` o "regenera el timeline de <cliente>", "actualiza el portal de <cliente>".

## Regla
La fuente de verdad son las **fases en ClickUp** (lista PROJECTS del cliente, tareas con `start` y `due`, ligadas al epic). `quotes/<slug>/project.json` es la exportación; `timeline.html` se genera. Nunca editar fechas a mano en el HTML.

## Pasos
1. Leer con el MCP de ClickUp las tareas de la lista `projectsList` del cliente (ver `project.json` → `clickup`). Fases = tag `fase`; hitos del cliente = tag `hito`. Tomar `start_date`, `due_date`, nombre.
2. Actualizar `quotes/<slug>/project.json`: `phases` (label, sub, who `soda`|`client`, start, end), `milestones` (date, what, who, row, big), `launch`, `softLaunch`. Si una fase cambió de fecha en ClickUp, cambia aquí; si no está en ClickUp, no va.
3. `node portal/build-timeline.mjs <slug>` → escribe `quotes/<slug>/entregables/timeline.html`. "Hoy" se calcula; `--today YYYY-MM-DD` solo para probar.
4. Revisar a 1280 (patrón `/screens` o Chrome headless). Las semanas salen del lunes de `start`; el ancho se ajusta al número de días hábiles hasta `launch`.
5. Mandar al cliente como Artifact de claude.ai (como se hizo con Prudence) o deploy a Netlify (`soda-quote.md`, deploy). Commit en rama, nunca en main.

## Nuevo cliente
Copiar `quotes/prudence/project.json`, cambiar slug, cliente, epic, lista, fechas. Las fases en ClickUp se crean al ganar (soda-quote.md, paso 5) con `start`/`due` y tag `fase`.

## Pendiente (Gerente 2)
Board de revisión: Artifact con base de datos donde el cliente aprueba o pide cambios por entregable; el skill lee y mueve la subtarea a `in client review` / `listo para entregar`.

## Archivos
- `portal/build-timeline.mjs` — generador
- `portal/timeline.template.html` — plantilla (diseño del timeline de Prudence con placeholders)
- `quotes/<slug>/project.json` — exportación de ClickUp
- `quotes/<slug>/entregables/timeline.html` — salida
