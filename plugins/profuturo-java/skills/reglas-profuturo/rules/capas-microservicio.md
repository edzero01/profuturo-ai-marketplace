# Regla: capas del microservicio

**Categoría:** arquitectura · **Aplica a:** microservicios Spring Boot generados con el golden path `profuturo-ms-experience`

Todo el código vive bajo el paquete base del servicio y respeta esta separación:

| Paquete | Responsabilidad | No debe |
| --- | --- | --- |
| `controllers` | Recibir la petición, validar la entrada (`@Valid`), delegar al service y armar la respuesta HTTP | Tener lógica de negocio, usar repositorios o clientes directamente |
| `services` + `services.impl` | Lógica de negocio. Siempre interfaz + implementación | Conocer detalles HTTP (`ResponseEntity`, `HttpServletRequest`) |
| `clients` | Interfaces `@FeignClient` hacia las capas Business y System | Contener lógica; solo declaran la llamada |
| `repositories` | Acceso a datos con Spring Data | Exponerse fuera de los services |
| `entity` | Entidades JPA mapeadas a Oracle | Salir en la API |
| `beans` | DTOs de entrada y salida, documentados con `@Schema` | Llevar anotaciones JPA |
| `exceptions` | Excepciones propias del dominio | — |
| `config` / `commons` | Configuración (OpenAPI, beans técnicos) y constantes | — |
| `local` | Stubs para el perfil `local` (`@Profile("local")`) | Usarse fuera del perfil local |

Reglas concretas:

1. Inyección por constructor con `@RequiredArgsConstructor` y campos `private final`. Nada de `@Autowired` en campos.
2. Los controllers devuelven DTOs de `beans`, nunca entidades.
3. Cada endpoint lleva `@Operation` y `@ApiResponses` de springdoc con los códigos reales que puede devolver.
4. Transacciones en el service: `@Transactional` para escritura, `@Transactional(readOnly = true)` para lectura.
5. Las llamadas a otros microservicios pasan por un cliente de `clients`, nunca con `RestTemplate` o `WebClient` sueltos.

**Por qué:** la capa Experience orquesta servicios Business y System. Mantener las capas separadas permite cambiar un backend (por ejemplo, de WAS a un microservicio) sin tocar el contrato que consumen los canales.
