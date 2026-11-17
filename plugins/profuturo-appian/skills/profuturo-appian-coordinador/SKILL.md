---
name: profuturo-appian-coordinador
description: Coordinar construcción Appian desde P4 y reanudar tareas con evidencias.
---

# Coordinar construcción Appian desde P4 y reanudar tareas con evidencias.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Inspecciona el handoff P4, catálogo de criterios y herramientas MCP efectivas. Divide por objetos, no por páginas de documento. Planifica arquitectura antes de datos; datos y seguridad antes de reglas, procesos e interfaces; integraciones antes de sus consumidores. Asigna un escritor por UUID o nombre lógico. Registra dependencias y pendientes que bloquean solo tareas afectadas. El agente principal invoca responsables de agents/; si el host no permite subagentes, ejecuta los roles por turnos sin afirmar delegación. Consolida versiones revisadas sin repetir los 52 controles. Usa scripts/handoff.py check, record y status para reanudar. No marques construido un plan ni probado un stub.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
