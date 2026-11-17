---
name: profuturo-microservicios-seguridad-resiliencia
description: Implementar autorización, recuperación y observabilidad de servicios.
---

Carga la skill `profuturo-microservicios-seguridad-resiliencia` de este plugin y `references/handoff.md`.

Aplica matriz de permisos por operación y dato: autenticar no equivale a autorizar. Externaliza secretos y configuración; usa reglas de secretos, Oracle/JPA y capas existentes cuando correspondan. Define timeout y presupuesto de reintentos; evita reintentar escrituras sin idempotencia, usa backoff y límite acordado, y dead-letter/compensación solo si el contrato lo pide. Agrega logs estructurados sin PII, métricas y trazas con correlación propagada. Prueba 401/403, acceso cruzado, dependencia lenta/caída, agotamiento y ausencia de fuga de datos. No inventes SLO, límites o infraestructura.

Opera solo sobre el objeto/archivo asignado. No sustituyas fuentes por ejemplos. Entrega el resultado al agente principal; no lances subagentes desde este rol. El revisor debe conservar una identidad distinta del autor y examinar sus evidencias.
