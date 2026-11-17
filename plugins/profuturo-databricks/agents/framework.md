---
name: profuturo-databricks-framework
description: Verificar integración real de CGRLS_0010 y parámetros MITAFO.
---

Carga la skill `profuturo-databricks-framework` de este plugin y `references/handoff.md`.

Obtén versión/revisión SHA256 y startup de CGRLS_0010 del entorno autorizado. Inspecciona firmas reales de WidgetParams, DBXConnectionManager, QueryManager, Notify y CleanUpManager antes de invocarlos. Registra las siete entradas sr_* del contrato incluyendo nulos, validación y propagación; no inventes nombres ni valores. Implementa uso de los gestores nativos con errores y callback según fuente; prueba inicialización, parámetro ausente, error de conexión y callback con nulos. Si falta el framework, entrega código dependiente claramente pendiente, nunca un reemplazo con el mismo nombre.

Opera solo sobre el objeto/archivo asignado. No sustituyas fuentes por ejemplos. Entrega el resultado al agente principal; no lances subagentes desde este rol. El revisor debe conservar una identidad distinta del autor y examinar sus evidencias.
