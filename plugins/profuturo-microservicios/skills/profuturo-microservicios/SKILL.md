---
name: profuturo-microservicios
description: Construir y revisar microservicios de Profuturo desde P4; coordina roles,
  aplica lineamientos y conserva evidencia y pendientes.
---

# Construcción microservicios Profuturo

Lee [el contrato P4–P5](../../references/handoff.md), [las fuentes y su estado](../../references/sources.json) y `../../contracts/catalog.json`.

Elige el responsable según objeto y tarea:

- `profuturo-microservicios-coordinador`: Coordinar construcción de microservicios desde contratos P4.
- `profuturo-microservicios-contratos-eventos`: Implementar APIs, eventos, compatibilidad y correlación desde P4.
- `profuturo-microservicios-logica-datos`: Implementar reglas, transacciones, idempotencia e historial de datos.
- `profuturo-microservicios-seguridad-resiliencia`: Implementar autorización, recuperación y observabilidad de servicios.
- `profuturo-microservicios-calidad-operacion`: Revisar contratos, datos, seguridad y operación de microservicios.

El agente principal coordina `agents/` si la plataforma soporta delegación. Empieza por coordinador, valida el plan y trabaja solo sobre tareas con entradas disponibles. No inventes datos de negocio, APIs, UUID, framework ni aprobaciones. Una ausencia de conexión deja pendiente la acción dependiente; conserva el resto del avance.

Para Java Experience conserva `reglas-profuturo`, `agregar-endpoint` y `agregar-cliente-feign`. Para eventos, versionado, idempotencia, concurrencia y operación usa [la guía ampliada](../../references/microservicios.md) y los roles específicos. No extrapoles el arquetipo Java a otros stacks sin definición P4.
