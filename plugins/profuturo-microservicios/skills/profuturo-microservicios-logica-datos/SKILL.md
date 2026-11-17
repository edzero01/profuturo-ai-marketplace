---
name: profuturo-microservicios-logica-datos
description: Implementar reglas, transacciones, idempotencia e historial de datos.
---

# Implementar reglas, transacciones, idempotencia e historial de datos.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Traza operación→reglas→transacción→entidad/propietario. Implementa idempotencia con clave/ámbito/expiración acordados, almacenamiento atómico y respuesta repetida; si faltan, deja pendiente la operación afectada. Diseña concurrencia y rollback/compensación según fronteras reales, sin extender transacción de base de datos a una llamada remota. Incluye migración compatible y recuperación coordinada con dueño del esquema; ddl-auto=none no sustituye migración. Respeta historial/retención. Prueba reenvíos simultáneos, conflicto de escritura, rollback, esquema previo y fallo tras commit. No implementes historial compartido sin propietario.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
