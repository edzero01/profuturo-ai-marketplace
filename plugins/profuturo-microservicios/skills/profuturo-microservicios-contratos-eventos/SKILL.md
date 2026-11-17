---
name: profuturo-microservicios-contratos-eventos
description: Implementar APIs, eventos, compatibilidad y correlación desde P4.
---

# Implementar APIs, eventos, compatibilidad y correlación desde P4.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Define DTOs, validaciones, errores, rutas, versiones y ejemplos desde operaciones P4; usa agregar-endpoint o agregar-cliente-feign para Java cuando aplique. Para cada evento implementa esquema/versionado, clave, productor, consumidor y semántica de entrega definidos, con manejo explícito de duplicados y eventos fuera de orden. No elijas broker ni política de compatibilidad sin fuente. Propaga correlación entre HTTP/evento/log sin PII. Añade pruebas de contrato de consumidores y compatibilidad anterior, error de esquema y correlación ausente. No confundir @Schema con prueba de compatibilidad.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
