---
name: profuturo-appian-reglas-procesos
description: Construir reglas, decisiones y procesos Appian con recuperación.
---

# Construir reglas, decisiones y procesos Appian con recuperación.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Separa validación de captura y regla de negocio. Implementa expression rules desde entradas/salidas de P4 y pruebas de frontera, nulos y errores. Crea Process Models con estados, decisiones, tareas, asignaciones, tiempos y recuperación definidos; no inventes escalamiento ni aprobadores. Prueba secuencia, paralelismo, rechazo, corrección y espera con correlación de instancia. Aplica references/validation-policy.md para inputs y reintentos; una versión envuelta para diagnóstico no valida el objeto final. Entrega definición y consultas de objetos reales, resultados esperados/observados y rutas no probadas.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
