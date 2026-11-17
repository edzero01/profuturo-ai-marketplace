---
name: profuturo-databricks-framework
description: Verificar integración real de CGRLS_0010 y parámetros MITAFO.
---

# Verificar integración real de CGRLS_0010 y parámetros MITAFO.

Lee [el contrato común](../../references/handoff.md) y el catálogo `../../contracts/catalog.json`. Selecciona solo los IDs asignados a la tarea.

Obtén versión/revisión SHA256 y startup de CGRLS_0010 del entorno autorizado. Inspecciona firmas reales de WidgetParams, DBXConnectionManager, QueryManager, Notify y CleanUpManager antes de invocarlos. Registra las siete entradas sr_* del contrato incluyendo nulos, validación y propagación; no inventes nombres ni valores. Implementa uso de los gestores nativos con errores y callback según fuente; prueba inicialización, parámetro ausente, error de conexión y callback con nulos. Si falta el framework, entrega código dependiente claramente pendiente, nunca un reemplazo con el mismo nombre.

Devuelve el resultado con artefactos, hashes, criterios evaluados, pendientes y evidencia esperada/observada. Declara partial si falta una dependencia real. Una instrucción instalada no acredita una ejecución.
