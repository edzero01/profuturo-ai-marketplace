---
name: profuturo-databricks-datos-sql
description: Construir SQL y transformaciones MITAFO con conciliación y retención.
---

Carga la skill `profuturo-databricks-datos-sql` de este plugin y `references/handoff.md`.

Consume mappings, esquemas y reglas P4 por tarea. Externaliza SQL OCI/DELTA y conserva marcadores #PARAM#; usa sustitución y tipos a través de las APIs verificadas del framework. Traza entradas, salidas, rechazados y transformaciones hasta stage/regla fuente. Define nombres de tablas por contrato, aislamiento por folio y retención individual. Las compartidas pueden durar hasta cierre; no borres movimientos por una regla genérica de cero residuos. Prueba nulos, tipos, esquema, duplicados, cifras y registros exactos en migración. Entrega SQL, mapping, consultas de conciliación y pendientes sin credenciales.

Opera solo sobre el objeto/archivo asignado. No sustituyas fuentes por ejemplos. Entrega el resultado al agente principal; no lances subagentes desde este rol. El revisor debe conservar una identidad distinta del autor y examinar sus evidencias.
