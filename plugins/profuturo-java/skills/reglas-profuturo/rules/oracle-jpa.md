# Regla: acceso a datos Oracle con JPA

**Categoría:** datos · **Aplica a:** servicios con `spring-boot-starter-data-jpa` sobre Oracle 19c

1. Nombres de tabla y columna en mayúsculas en `@Table(name = "...")` y `@Column(name = "...")`, igual que en Oracle.
2. Prefiere métodos derivados de Spring Data (`findByCampo`) o JPQL. Usa `nativeQuery = true` solo cuando haga falta una función o hint propio de Oracle, y documenta por qué en un comentario.
3. Siempre parámetros enlazados (`:param` con `@Param`). Nunca concatenes valores en una consulta.
4. Nunca `SELECT *` en consultas nativas: lista las columnas que mapea la entidad.
5. Las consultas que pueden devolver muchos registros reciben `Pageable` y regresan `Page` o `Slice`.
6. Columnas `CHAR(n)`: Oracle rellena con espacios a la derecha. Compara y devuelve esos valores con `trim()` en el service, o usa `VARCHAR2` si el modelo lo permite.
7. Cada cambio de entidad se refleja en `src/main/resources/data.sql` (perfil local) en el mismo commit, para que el test de contexto siga pasando.
8. No uses `spring.jpa.hibernate.ddl-auto` distinto de `none` fuera del perfil `local`: el esquema de Oracle lo gestiona el equipo de base de datos.

**Por qué:** la migración a Oracle 19c y la coexistencia con bases legadas hacen que los esquemas los controle un equipo distinto. Las consultas portables y parametrizadas reducen el riesgo de romper otras aplicaciones que comparten esas tablas.
