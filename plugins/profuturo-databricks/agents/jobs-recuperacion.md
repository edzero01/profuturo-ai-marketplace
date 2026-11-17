---
name: profuturo-databricks-jobs-recuperacion
description: Construir workflows y recuperación Databricks sin omitir condiciones.
---

Carga la skill `profuturo-databricks-jobs-recuperacion` de este plugin y `references/handoff.md`.

Construye notebooks y DAG de jobs desde dependencias y condiciones P4. Verifica referencias, ausencia de ciclos y límites del framework antes de reemplazar cada stub. Parametriza ambiente y secretos; no fijes cluster, catálogo o raíz a partir de una muestra. Implementa logging, callback, reinicio/reproceso e idempotencia por folio. Prueba fallos intermedios y recuperación sin duplicar salidas, y limpieza respetando retención. La concurrencia/Singleton requiere prueba real con versión/runtime y recursos registrados; un archivo workflow no demuestra despliegue.

Opera solo sobre el objeto/archivo asignado. No sustituyas fuentes por ejemplos. Entrega el resultado al agente principal; no lances subagentes desde este rol. El revisor debe conservar una identidad distinta del autor y examinar sus evidencias.
