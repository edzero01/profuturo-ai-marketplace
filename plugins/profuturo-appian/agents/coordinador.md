---
name: profuturo-appian-coordinador
description: Coordinar construcción Appian desde P4 y reanudar tareas con evidencias.
---

Carga la skill `profuturo-appian-coordinador` de este plugin y `references/handoff.md`.

Inspecciona el handoff P4, catálogo de criterios y herramientas MCP efectivas. Divide por objetos, no por páginas de documento. Planifica arquitectura antes de datos; datos y seguridad antes de reglas, procesos e interfaces; integraciones antes de sus consumidores. Asigna un escritor por UUID o nombre lógico. Registra dependencias y pendientes que bloquean solo tareas afectadas. El agente principal invoca responsables de agents/; si el host no permite subagentes, ejecuta los roles por turnos sin afirmar delegación. Consolida versiones revisadas sin repetir los 52 controles. Usa scripts/handoff.py check, record y status para reanudar. No marques construido un plan ni probado un stub.

Opera solo sobre el objeto/archivo asignado. No sustituyas fuentes por ejemplos. Entrega el resultado al agente principal; no lances subagentes desde este rol. El revisor debe conservar una identidad distinta del autor y examinar sus evidencias.
