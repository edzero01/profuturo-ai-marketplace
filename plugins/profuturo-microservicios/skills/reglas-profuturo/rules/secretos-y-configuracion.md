# Regla: secretos y configuración

**Categoría:** seguridad · **Aplica a:** todo repositorio de microservicio

1. Ninguna credencial, token, contraseña o cadena de conexión real se escribe en el repositorio: ni en `application*.properties`, ni en `values.yaml`, ni en código, ni en tests.
2. Los valores por ambiente se leen de variables de entorno con un default inocuo para local: `spring.datasource.url=${DB_URL:jdbc:oracle:thin:@//localhost:1521/XEPDB1}`.
3. En Kubernetes, los secretos llegan como `env` con `valueFrom.secretKeyRef` en `deploy/helm/values.yaml`. El Secret lo crea plataforma; el chart solo lo referencia.
4. Las URLs de otros servicios siguen el patrón `application.client.<nombre>.url=${<NOMBRE>_CLIENT_URL:http://localhost:8081}`.
5. El perfil `local` (H2 + stubs) es el único lugar donde se permiten valores fijos, y solo valores de prueba.
6. No se registran en logs datos personales del trabajador (CURP, NSS, saldos, cuentas). Si hace falta trazar, se registra el identificador de la operación.

**Por qué:** Profuturo administra información financiera y personal de trabajadores. Un secreto en Git queda en el historial aunque se borre después, y los repos se clonan en muchas máquinas.
