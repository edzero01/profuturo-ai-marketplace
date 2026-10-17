---
name: agregar-cliente-feign
description: Procedimiento para que un microservicio de Profuturo consuma otro servicio (capa Business o System) con OpenFeign, incluyendo configuración por ambiente, stub para el perfil local y variable en Helm. Úsala cuando haya que llamar a otra API o microservicio.
when_to_use: '"consume el servicio X", "llama a la API de…", "integra con el microservicio de…", "necesito datos de otro servicio".'
argument-hint: "[nombre del servicio destino]"
---

# Agregar un cliente Feign

Antes de empezar, carga la skill `reglas-profuturo` y lee las reglas de capas y de secretos.

## 0. Identifica el servicio destino

- Si el MCP `backstage` está disponible, busca el servicio o su API en el catálogo (`catalog.query-catalog-entities`): obtén su nombre, dueño, ruta base y, si existe, su definición OpenAPI.
- Si no está en el catálogo, pide al usuario la ruta base y el contrato (entrada y salida).

En los pasos siguientes, `<nombre>` es el nombre corto del destino en kebab-case (por ejemplo `saldos`) y `<Nombre>` su versión PascalCase.

## 1. Interfaz en `clients`

```java
@FeignClient(name = "<nombre>-client", url = "${application.client.<nombre>.url}")
public interface <Nombre>Client {

    @GetMapping("/<ruta>")
    <Nombre>Response consultar(@RequestParam("id") String id);

}
```

- DTOs de respuesta del destino en `beans` (con `@Schema`).
- `@EnableFeignClients` ya está en la clase `Application`; no lo repitas.

## 2. Configuración por ambiente

En `src/main/resources/application.properties`:

```properties
application.client.<nombre>.url=${<NOMBRE>_CLIENT_URL:http://localhost:8081}
```

En `src/main/resources/application-local.properties`, apúntalo al stub:

```properties
application.client.<nombre>.url=http://localhost:${server.port}${server.servlet.context-path}/local-stub/<nombre>
```

## 3. Stub para el perfil local

En `local/LocalStubController.java` (o un controller nuevo en `local` con `@Profile("local")` y `@Hidden`), agrega un endpoint bajo `/local-stub/<nombre>/<ruta>` que devuelva una respuesta de ejemplo con la misma forma que el servicio real. Sin este stub, el perfil local y el test de contexto no reflejan el flujo.

## 4. Variable en el cluster

En `deploy/helm/values.yaml`, dentro de `env`:

```yaml
env:
  - name: <NOMBRE>_CLIENT_URL
    value: http://<servicio-destino>.<namespace>.svc.cluster.local/<ruta-base>
```

Si el destino aún no está desplegado en dev, deja `springProfile: local` y documenta la variable en el PR.

## 5. Uso desde el service

- Inyecta el cliente en el service por constructor. Nunca desde el controller.
- Traduce los errores del cliente (`FeignException`) a excepciones propias de `exceptions`.

## 6. Pruebas y PR

- Prueba unitaria del service con el cliente mockeado (`@MockBean` o Mockito).
- `mvn test`, verificación con el perfil local y pull request a `main`.
