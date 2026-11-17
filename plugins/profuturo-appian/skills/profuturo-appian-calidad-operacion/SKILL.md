---
name: profuturo-appian-calidad-operacion
description: Revisar Appian de forma independiente con evidencia por objeto.
---

# Revisar Appian de forma independiente con evidencia por objeto.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Selecciona criterios aplicables desde contracts/catalog.json y revisa el diff de objetos, Used By/Depends On y evidencias del autor. Comprueba permisos con un evaluador distinto del constructor. Ejecuta pruebas positivas/negativas, volumen representativo cuando exista, paginación, paquete y configuración por ambiente. Vincula cada hallazgo a criterio, UUID, prueba y responsable. No aceptes un UUID solo por formato ni una captura antigua como estado actual. Entrega revisión, pendientes de operación y criterios no aplicables razonados; la aprobación requiere responsable y recibo externos a esta revisión.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
