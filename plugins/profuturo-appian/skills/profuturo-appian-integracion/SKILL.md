---
name: profuturo-appian-integracion
description: Construir integraciones y Web APIs Appian con contratos y fallos.
---

# Construir integraciones y Web APIs Appian con contratos y fallos.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Relaciona Connected System, Integration, Web API, consumidor y operación P4. Inspecciona herramientas MCP y autenticación disponibles sin copiar credenciales. Mapea tipos, campos, nulos, códigos, timeout y errores; implementa reintentos e idempotencia solo según contrato. Construye conexiones antes de integraciones y estas antes de procesos consumidores. Si la operación no existe en MCP, entrega paso manual concreto y pendiente afectado, no inventes una llamada. Prueba éxito, error funcional, autorización, indisponibilidad y duplicados contra el endpoint de prueba autorizado; un mock no demuestra conectividad.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
