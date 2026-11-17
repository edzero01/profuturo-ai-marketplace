---
name: profuturo-appian-datos-seguridad
description: Construir Record Types, relaciones y permisos Appian desde P4.
---

# Construir Record Types, relaciones y permisos Appian desde P4.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Lee referencias técnicas de datos y seguridad en skills/appian-referencia solo para los objetos afectados. Inspecciona esquema, identificador, relaciones y sincronización; no impongas nombres o cardinalidades que contradigan P4. Crea dependencias antes de relacionarlas y vuelve a consultar UUID y asociaciones. Configura grupos, permisos de objeto y de registros separadamente. Prueba lectura/escritura con rol autorizado y denegado, nulos, huérfanos, vistas, filtros, acciones y eventos. El autor no aprueba su propia matriz de permisos. Entrega inventario de campos/relaciones, UUID y evidencia por rol.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
