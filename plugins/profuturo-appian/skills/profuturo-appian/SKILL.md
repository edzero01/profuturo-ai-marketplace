---
name: profuturo-appian
description: Construir y revisar appian de Profuturo desde P4; coordina roles, aplica
  lineamientos y conserva evidencia y pendientes.
---

# Construcción appian Profuturo

Lee [el contrato P4–P5](../../references/handoff.md), [las fuentes y su estado](../../references/sources.json) y `../../contracts/catalog.json`.

Elige el responsable según objeto y tarea:

- `profuturo-appian-coordinador`: Coordinar construcción Appian desde P4 y reanudar tareas con evidencias.
- `profuturo-appian-arquitectura`: Inspeccionar y diseñar reutilización y dependencias de objetos Appian.
- `profuturo-appian-datos-seguridad`: Construir Record Types, relaciones y permisos Appian desde P4.
- `profuturo-appian-reglas-procesos`: Construir reglas, decisiones y procesos Appian con recuperación.
- `profuturo-appian-interfaces-ux`: Construir interfaces SAIL y Sites con roles y branding trazables.
- `profuturo-appian-integracion`: Construir integraciones y Web APIs Appian con contratos y fallos.
- `profuturo-appian-calidad-operacion`: Revisar Appian de forma independiente con evidencia por objeto.

El agente principal coordina `agents/` si la plataforma soporta delegación. Empieza por coordinador, valida el plan y trabaja solo sobre tareas con entradas disponibles. No inventes datos de negocio, APIs, UUID, framework ni aprobaciones. Una ausencia de conexión deja pendiente la acción dependiente; conserva el resto del avance.
