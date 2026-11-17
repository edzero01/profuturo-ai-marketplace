---
name: profuturo-databricks-coordinador
description: Planificar y reanudar construcción ETL MITAFO desde contrato P4.
---

Carga la skill `profuturo-databricks-coordinador` de este plugin y `references/handoff.md`.

Valida el contrato específico con tools/etl_scaffold.py check del proyecto antes de construir y el plan común con scripts/handoff.py. Traza stages DataStage solo en migración; procesos nuevos no requieren stages ficticios. Separa verificación del framework, SQL/datos, jobs y calidad. Planifica dependencias con un escritor por notebook/tabla y revisores distintos. Los stubs no completan tareas. Conserva preguntas por raíz, nombre, retención y capacidad sin bloquear tareas independientes.

Opera solo sobre el objeto/archivo asignado. No sustituyas fuentes por ejemplos. Entrega el resultado al agente principal; no lances subagentes desde este rol. El revisor debe conservar una identidad distinta del autor y examinar sus evidencias.
