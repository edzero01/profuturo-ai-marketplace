---
name: profuturo-databricks-calidad-operacion
description: Revisar los 18 controles MITAFO con evidencia de código y entorno.
---

Carga la skill `profuturo-databricks-calidad-operacion` de este plugin y `references/handoff.md`.

Contrasta contratos, notebooks, SQL y workflows con DBX-01..DBX-18. Distingue pruebas sintéticas del generador y pruebas unitarias/funcionales/de datos/integración/limpieza/concurrencia del ETL real. Para migración compara registros/valores con origen; no aceptes solo conteos. Registra entradas, salidas, framework/runtime, run IDs y diferencia de rendimiento. Revisa excepciones de retención antes de aceptar limpieza y conserva pendientes del framework. No apruebes cambios que hayas construido; entrega criterio por criterio y evidencia verificable.

Opera solo sobre el objeto/archivo asignado. No sustituyas fuentes por ejemplos. Entrega el resultado al agente principal; no lances subagentes desde este rol. El revisor debe conservar una identidad distinta del autor y examinar sus evidencias.
