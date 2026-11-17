# Controles de construcción ETL MITAFO

Propuesta de controles derivados del documento fuente; no son una rúbrica
corporativa aprobada adicional. Cada revisión conserva estado, evidencia y pendiente.

| ID | Control verificable | Fuente |
| --- | --- | --- |
| DBX-01 | Oracle identificado como origen/destino; Databricks como motor | 1.2 y 2.1 |
| DBX-02 | Framework CGRLS_0010 identificado por versión/revisión verificadas | 2.2 y 2.3 |
| DBX-03 | Uso comprobado de gestores nativos, sin sustituciones ad hoc | 2.2 y 2.7 |
| DBX-04 | Siete parámetros de servicio conservados y validados | 3.1 |
| DBX-05 | Stage de origen trazado sin inventar cobertura | 2.7 y 3 |
| DBX-06 | Dependencias y condiciones completas, sin referencias inexistentes/ciclos | 3 y 4.3 |
| DBX-07 | SQL OCI/DELTA externo y parámetros tipados mediante framework | 3.2 |
| DBX-08 | Nombres de workflow, task, notebook, SQL y Delta trazables | 3.6 |
| DBX-09 | Aislamiento por folio y retención explícita de cada Delta | 2.1 y 3.6.6 |
| DBX-10 | Limpieza por notebook/folio con excepción de movimientos revisada | 2.1 y 4.2 |
| DBX-11 | Callback completo, incluyendo parámetros nulos | 3.3 y 3.4 |
| DBX-12 | Errores, logging y recuperación usando componentes del framework | 2.1 y 2.2 |
| DBX-13 | Entorno parametrizado y credenciales fuera del contrato/código | 2.1 y 2.6 |
| DBX-14 | Prueba unitaria de cada notebook con resultado esperado | 4.1 |
| DBX-15 | Prueba funcional y comparación exacta de registros/valores en migraciones | 4.1 y 4.2 |
| DBX-16 | Invocación y callback verificados con servicios reales | 4.1 y 4.2 |
| DBX-17 | Limpieza y concurrencia verificadas respetando retención/folios | 4.1 |
| DBX-18 | Rendimiento comparado, revisión y pendientes visibles antes de aceptar | 4.2 y 4.3 |

Los controles DBX-01 a DBX-13 combinan revisión de contrato y código; los controles
de entorno no se satisfacen con pruebas sintéticas. Una aprobación necesita evidencia
real y un responsable identificable; no se asigna automáticamente desde el generador.
