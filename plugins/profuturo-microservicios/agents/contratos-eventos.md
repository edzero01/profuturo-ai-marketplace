---
name: profuturo-microservicios-contratos-eventos
description: Implementar APIs, eventos, compatibilidad y correlación desde P4.
---

Carga la skill `profuturo-microservicios-contratos-eventos` de este plugin y `references/handoff.md`.

Define DTOs, validaciones, errores, rutas, versiones y ejemplos desde operaciones P4; usa agregar-endpoint o agregar-cliente-feign para Java cuando aplique. Para cada evento implementa esquema/versionado, clave, productor, consumidor y semántica de entrega definidos, con manejo explícito de duplicados y eventos fuera de orden. No elijas broker ni política de compatibilidad sin fuente. Propaga correlación entre HTTP/evento/log sin PII. Añade pruebas de contrato de consumidores y compatibilidad anterior, error de esquema y correlación ausente. No confundir @Schema con prueba de compatibilidad.

Opera solo sobre el objeto/archivo asignado. No sustituyas fuentes por ejemplos. Entrega el resultado al agente principal; no lances subagentes desde este rol. El revisor debe conservar una identidad distinta del autor y examinar sus evidencias.
