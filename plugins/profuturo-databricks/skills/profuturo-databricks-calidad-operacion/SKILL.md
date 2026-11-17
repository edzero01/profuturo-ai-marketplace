---
name: profuturo-databricks-calidad-operacion
description: Revisar los 18 controles MITAFO con evidencia de código y entorno.
---

# Revisar los 18 controles MITAFO con evidencia de código y entorno.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Contrasta contratos, notebooks, SQL y workflows con DBX-01..DBX-18. Distingue pruebas sintéticas del generador y pruebas unitarias/funcionales/de datos/integración/limpieza/concurrencia del ETL real. Para migración compara registros/valores con origen; no aceptes solo conteos. Registra entradas, salidas, framework/runtime, run IDs y diferencia de rendimiento. Revisa excepciones de retención antes de aceptar limpieza y conserva pendientes del framework. No apruebes cambios que hayas construido; entrega criterio por criterio y evidencia verificable.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
