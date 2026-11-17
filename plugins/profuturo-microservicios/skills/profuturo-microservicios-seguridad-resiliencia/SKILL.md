---
name: profuturo-microservicios-seguridad-resiliencia
description: Implementar autorización, recuperación y observabilidad de servicios.
---

# Implementar autorización, recuperación y observabilidad de servicios.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Aplica matriz de permisos por operación y dato: autenticar no equivale a autorizar. Externaliza secretos y configuración; usa reglas de secretos, Oracle/JPA y capas existentes cuando correspondan. Define timeout y presupuesto de reintentos; evita reintentar escrituras sin idempotencia, usa backoff y límite acordado, y dead-letter/compensación solo si el contrato lo pide. Agrega logs estructurados sin PII, métricas y trazas con correlación propagada. Prueba 401/403, acceso cruzado, dependencia lenta/caída, agotamiento y ausencia de fuga de datos. No inventes SLO, límites o infraestructura.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
