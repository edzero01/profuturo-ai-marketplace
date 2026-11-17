# Coordinar construcción de microservicios desde contratos P4.

Clasifica el arquetipo y sus fronteras antes de aplicar Java Experience. Consume operaciones, entidades, eventos y no funcionales P4. Planifica contratos antes de consumidores, migraciones antes de código dependiente y pruebas antes de revisión. Detecta servicios reutilizables en catálogo. No infieras soporte Business/System de la plantilla Experience. Divide archivos por responsable, reanuda con scripts/handoff.py y entrega brechas por operación sin convertir preguntas en decisiones.

# Implementar APIs, eventos, compatibilidad y correlación desde P4.

Define DTOs, validaciones, errores, rutas, versiones y ejemplos desde operaciones P4; usa agregar-endpoint o agregar-cliente-feign para Java cuando aplique. Para cada evento implementa esquema/versionado, clave, productor, consumidor y semántica de entrega definidos, con manejo explícito de duplicados y eventos fuera de orden. No elijas broker ni política de compatibilidad sin fuente. Propaga correlación entre HTTP/evento/log sin PII. Añade pruebas de contrato de consumidores y compatibilidad anterior, error de esquema y correlación ausente. No confundir @Schema con prueba de compatibilidad.

# Implementar reglas, transacciones, idempotencia e historial de datos.

Traza operación→reglas→transacción→entidad/propietario. Implementa idempotencia con clave/ámbito/expiración acordados, almacenamiento atómico y respuesta repetida; si faltan, deja pendiente la operación afectada. Diseña concurrencia y rollback/compensación según fronteras reales, sin extender transacción de base de datos a una llamada remota. Incluye migración compatible y recuperación coordinada con dueño del esquema; ddl-auto=none no sustituye migración. Respeta historial/retención. Prueba reenvíos simultáneos, conflicto de escritura, rollback, esquema previo y fallo tras commit. No implementes historial compartido sin propietario.

# Implementar autorización, recuperación y observabilidad de servicios.

Aplica matriz de permisos por operación y dato: autenticar no equivale a autorizar. Externaliza secretos y configuración; usa reglas de secretos, Oracle/JPA y capas existentes cuando correspondan. Define timeout y presupuesto de reintentos; evita reintentar escrituras sin idempotencia, usa backoff y límite acordado, y dead-letter/compensación solo si el contrato lo pide. Agrega logs estructurados sin PII, métricas y trazas con correlación propagada. Prueba 401/403, acceso cruzado, dependencia lenta/caída, agotamiento y ausencia de fuga de datos. No inventes SLO, límites o infraestructura.

# Revisar contratos, datos, seguridad y operación de microservicios.

Revisa MS-01..MS-20 contra implementación, contrato P4 y evidencias. Ejecuta pruebas de unidad, contratos, integración y migración según cambios. Incluye repetición/concurrencia, consumidor antiguo, denegación por rol y recuperación. Maven/contexto H2 no demuestra Oracle real ni integración. Comprueba despliegue parametrizado y rollback: el golden path Experience usa GitHub Actions y Helm, no Argo CD. Registra hallazgos por operación/control y evidencia independiente; aprobación de entorno queda separada del resultado de tests.
