---
name: profuturo-databricks-datos-sql
description: Construir SQL y transformaciones MITAFO con conciliación y retención.
---

# Construir SQL y transformaciones MITAFO con conciliación y retención.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Consume mappings, esquemas y reglas P4 por tarea. Externaliza SQL OCI/DELTA y conserva marcadores #PARAM#; usa sustitución y tipos a través de las APIs verificadas del framework. Traza entradas, salidas, rechazados y transformaciones hasta stage/regla fuente. Define nombres de tablas por contrato, aislamiento por folio y retención individual. Las compartidas pueden durar hasta cierre; no borres movimientos por una regla genérica de cero residuos. Prueba nulos, tipos, esquema, duplicados, cifras y registros exactos en migración. Entrega SQL, mapping, consultas de conciliación y pendientes sin credenciales.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
