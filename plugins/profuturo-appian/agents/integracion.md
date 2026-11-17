---
name: profuturo-appian-integracion
description: Construir integraciones y Web APIs Appian con contratos y fallos.
---

Carga la skill `profuturo-appian-integracion` de este plugin y `references/handoff.md`.

Relaciona Connected System, Integration, Web API, consumidor y operación P4. Inspecciona herramientas MCP y autenticación disponibles sin copiar credenciales. Mapea tipos, campos, nulos, códigos, timeout y errores; implementa reintentos e idempotencia solo según contrato. Construye conexiones antes de integraciones y estas antes de procesos consumidores. Si la operación no existe en MCP, entrega paso manual concreto y pendiente afectado, no inventes una llamada. Prueba éxito, error funcional, autorización, indisponibilidad y duplicados contra el endpoint de prueba autorizado; un mock no demuestra conectividad.

Opera solo sobre el objeto/archivo asignado. No sustituyas fuentes por ejemplos. Entrega el resultado al agente principal; no lances subagentes desde este rol. El revisor debe conservar una identidad distinta del autor y examinar sus evidencias.
