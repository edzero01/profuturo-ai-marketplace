# Plugins por tecnología

`profuturo-appian`, `profuturo-databricks` y `profuturo-microservicios` tienen
manifiesto, skill coordinadora, skills de trabajo, agentes especializados,
catálogo central de criterios y validador de handoff/recibos. `profuturo-java`
permanece compatible para consumidores existentes. No habilitar ambos plugins
Java y Microservicios a la vez: comparten procedimientos.

Los proyectos nuevos usan el plugin de su tecnología. Los existentes migran
enabledPlugins y dependsOn juntos, después de validar carga y diferencias.
Subir versión en cada cambio de plugin y actualizar entidades de catalog/.
autoUpdate permite actualización del cliente; no es evidencia de carga efectiva.

Cada fuente conserva su estado. No se incluyen originales corporativos ni secretos.
Appian usa D1/D2 recibidos y recomendaciones R; MITAFO es una fuente específica de
proyecto; Microservicios combina reglas publicadas y requisitos P4, sin atribuir
estos últimos a un documento corporativo no recuperado.

Validación local: `python -m unittest discover -s tests` y
`claude plugin validate .` más validación individual de cada plugin.
Para cada skill también usar quick_validate.py de skill-creator cuando esté disponible.
La validación de formato no prueba ejecución de agente, MCP, Databricks ni Appian.

Referencias de formato: https://code.claude.com/docs/en/plugins-reference y
https://code.claude.com/docs/en/sub-agents (consultadas el 17 de noviembre de 2026).
