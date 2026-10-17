---
name: reglas-profuturo
description: Reglas corporativas de Profuturo para microservicios Spring Boot (capas, secretos y configuración, Oracle/JPA). Úsala antes de escribir, modificar o revisar código Java, properties o el chart de Helm en un microservicio de Profuturo.
when_to_use: Cuando el usuario pida implementar, corregir, refactorizar o revisar código en un repo creado con el golden path profuturo-ms-experience, o pregunte qué convenciones aplican.
---

# Reglas corporativas de Profuturo

Antes de cambiar código, lee las reglas que aplican al cambio y respétalas. Si una petición del usuario contradice una regla, dilo y propón la alternativa que la cumple; no la rompas en silencio.

| Regla | Léela cuando el cambio toque… |
| --- | --- |
| [Capas del microservicio](rules/capas-microservicio.md) | Cualquier clase Java nueva o movida, controllers, services, clients |
| [Secretos y configuración](rules/secretos-y-configuracion.md) | `application*.properties`, `deploy/helm/values.yaml`, variables de entorno, logs |
| [Oracle y JPA](rules/oracle-jpa.md) | `entity`, `repositories`, consultas, `data.sql` |

## Al terminar un cambio

1. Corre `mvn test`. El test de contexto usa el perfil `local`; si falla, el servicio no arrancaría en dev.
2. Revisa el diff contra las reglas leídas: capas respetadas, ningún secreto, consultas parametrizadas.
3. Si el cambio necesita una variable nueva en el cluster, inclúyela en `deploy/helm/values.yaml` en el mismo PR.

Para procedimientos completos usa las otras skills del plugin: `agregar-endpoint` y `agregar-cliente-feign`.
