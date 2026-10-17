---
name: agregar-endpoint
description: Procedimiento para agregar un endpoint REST a un microservicio Spring Boot de Profuturo respetando capas, OpenAPI, pruebas y GitOps. Úsala cuando el usuario pida exponer una operación, endpoint, ruta o API nueva.
when_to_use: '"agrega un endpoint", "expón una operación para…", "necesito un GET/POST que…", "nueva ruta en el servicio".'
argument-hint: "[descripción de la operación]"
---

# Agregar un endpoint

Sigue los pasos en orden. Antes de empezar, carga la skill `reglas-profuturo` y lee la regla de capas.

## 0. Antes de escribir código

- Si el MCP `backstage` está disponible, busca en el catálogo (`catalog.query-catalog-entities`) si otro servicio ya expone esta operación. Si existe, propón consumirlo con la skill `agregar-cliente-feign` en lugar de duplicarlo.
- Confirma con el usuario el verbo HTTP, la ruta, la entrada y la salida si no están claros.

## 1. DTOs en `beans`

- Un DTO de respuesta y, si aplica, uno de petición. Usa `@Data @Builder @NoArgsConstructor @AllArgsConstructor`.
- Documenta la clase y cada campo con `@Schema(description = ..., example = ...)`.
- Valida la entrada con `jakarta.validation` (`@NotNull`, `@NotBlank`, `@Size`, `@Pattern`).

## 2. Service

- Agrega el método a la interfaz en `services` y su implementación en `services.impl`.
- `@Transactional(readOnly = true)` si solo lee; `@Transactional` si escribe.
- Si necesita datos: repositorio en `repositories` (regla Oracle/JPA). Si necesita otro servicio: cliente Feign (skill `agregar-cliente-feign`).
- Lanza excepciones de `exceptions` para errores de negocio, no devuelvas `null`.

## 3. Controller

- Agrega el método al controller existente del servicio, salvo que el recurso sea claramente distinto.
- La ruta es relativa: el context-path `/<servicio>` ya lo agrega Spring.
- `@Valid` en el `@RequestBody`. Devuelve `ResponseEntity<Dto>`.
- `@Operation(summary = ...)` y `@ApiResponses` con los códigos que de verdad puede devolver (200/201, 400, 404, 500).

## 4. Datos locales

- Si el endpoint lee de una tabla nueva o columnas nuevas, actualiza la entidad y `src/main/resources/data.sql` para que el perfil `local` tenga datos de ejemplo.

## 5. Pruebas

- Agrega una prueba con `@WebMvcTest` del controller y `@MockBean` del service, que cubra el caso exitoso y una validación fallida.
- Corre `mvn test`.

## 6. Verificación local y PR

```bash
mvn spring-boot:run -Dspring-boot.run.profiles=local
curl -s http://localhost:8080/<servicio>/<ruta>
```

- Revisa que aparezca en Swagger: `http://localhost:8080/<servicio>/open-api/swagger-ui.html`.
- Crea una rama, haz commit y abre un pull request a `main`. No hagas push directo a `main`: el merge dispara el CI que publica la imagen y Argo CD despliega en dev.
