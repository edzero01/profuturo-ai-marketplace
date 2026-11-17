---
name: profuturo-databricks
description: Construir y revisar databricks de Profuturo desde P4; coordina roles,
  aplica lineamientos y conserva evidencia y pendientes.
---

# Construcción databricks Profuturo

Lee [el contrato P4–P5](../../references/handoff.md), [las fuentes y su estado](../../references/sources.json) y `../../contracts/catalog.json`.

Elige el responsable según objeto y tarea:

- `profuturo-databricks-coordinador`: Planificar y reanudar construcción ETL MITAFO desde contrato P4.
- `profuturo-databricks-framework`: Verificar integración real de CGRLS_0010 y parámetros MITAFO.
- `profuturo-databricks-datos-sql`: Construir SQL y transformaciones MITAFO con conciliación y retención.
- `profuturo-databricks-jobs-recuperacion`: Construir workflows y recuperación Databricks sin omitir condiciones.
- `profuturo-databricks-calidad-operacion`: Revisar los 18 controles MITAFO con evidencia de código y entorno.

El agente principal coordina `agents/` si la plataforma soporta delegación. Empieza por coordinador, valida el plan y trabaja solo sobre tareas con entradas disponibles. No inventes datos de negocio, APIs, UUID, framework ni aprobaciones. Una ausencia de conexión deja pendiente la acción dependiente; conserva el resto del avance.

Lee [los 18 controles MITAFO](../../references/etl-mitafo.md). El generador y el contrato ETL específico viven en el proyecto creado por profuturo-databricks-etl; no sustituyas CGRLS_0010 ni ejecutes un workflow solo por estar generado.
