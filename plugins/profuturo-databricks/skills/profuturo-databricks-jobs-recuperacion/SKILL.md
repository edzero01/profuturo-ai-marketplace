---
name: profuturo-databricks-jobs-recuperacion
description: Construir workflows y recuperación Databricks sin omitir condiciones.
---

# Construir workflows y recuperación Databricks sin omitir condiciones.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Construye notebooks y DAG de jobs desde dependencias y condiciones P4. Verifica referencias, ausencia de ciclos y límites del framework antes de reemplazar cada stub. Parametriza ambiente y secretos; no fijes cluster, catálogo o raíz a partir de una muestra. Implementa logging, callback, reinicio/reproceso e idempotencia por folio. Prueba fallos intermedios y recuperación sin duplicar salidas, y limpieza respetando retención. La concurrencia/Singleton requiere prueba real con versión/runtime y recursos registrados; un archivo workflow no demuestra despliegue.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
