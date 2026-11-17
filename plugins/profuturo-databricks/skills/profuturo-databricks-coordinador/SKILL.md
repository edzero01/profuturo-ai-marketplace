---
name: profuturo-databricks-coordinador
description: Planificar y reanudar construcción ETL MITAFO desde contrato P4.
---

# Planificar y reanudar construcción ETL MITAFO desde contrato P4.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Valida el contrato específico con tools/etl_scaffold.py check del proyecto antes de construir y el plan común con scripts/handoff.py. Traza stages DataStage solo en migración; procesos nuevos no requieren stages ficticios. Separa verificación del framework, SQL/datos, jobs y calidad. Planifica dependencias con un escritor por notebook/tabla y revisores distintos. Los stubs no completan tareas. Conserva preguntas por raíz, nombre, retención y capacidad sin bloquear tareas independientes.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
