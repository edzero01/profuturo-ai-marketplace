# Validación de objetos Appian

Esta política de construcción resuelve las diferencias entre la referencia técnica
y validation-checkpoint; no cambia los lineamientos recibidos. Primero inspecciona
el esquema real de herramientas para comprobar soporte de inputs y contexto.
Valida la expresión final con sus inputs cuando el host lo permita. Si validateExpression
no soporta ri!, un wrapper local sirve solo para diagnosticar: conserva ambas versiones
y no declares el objeto final validado con ese resultado. Crear en un entorno de desarrollo
autorizado puede permitir validación nativa; luego consulta el objeto y ejecuta sus pruebas.
Sin esa validación, conserva estado partial, no tested. No saltar a producción por esta limitación.

Usa como máximo dos intentos de corrección por objeto y misma causa durante una ejecución;
detente antes si reaparece sin progreso. Conserva expresión, inputs, error y resultado.
Una nueva fuente o corrección verificable permite una nueva ejecución registrada.
No transformar una expresión y presentarla como prueba del artefacto original.
