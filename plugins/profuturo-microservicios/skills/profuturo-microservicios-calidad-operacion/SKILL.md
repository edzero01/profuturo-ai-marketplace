---
name: profuturo-microservicios-calidad-operacion
description: Revisar contratos, datos, seguridad y operación de microservicios.
---

# Revisar contratos, datos, seguridad y operación de microservicios.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Revisa MS-01..MS-20 contra implementación, contrato P4 y evidencias. Ejecuta pruebas de unidad, contratos, integración y migración según cambios. Incluye repetición/concurrencia, consumidor antiguo, denegación por rol y recuperación. Maven/contexto H2 no demuestra Oracle real ni integración. Comprueba despliegue parametrizado y rollback: el golden path Experience usa GitHub Actions y Helm, no Argo CD. Registra hallazgos por operación/control y evidencia independiente; aprobación de entorno queda separada del resultado de tests.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
