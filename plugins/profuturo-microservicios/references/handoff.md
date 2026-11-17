# Contrato P4–P5 y evidencia

Usa `contracts/catalog.json` como catálogo de IDs y roles, `contracts/handoff.schema.json`
como formato de entrada y `scripts/handoff.py` para validación semántica/reanudación.
El plan lleva version=profuturo-handoff-v1, technology, project, catalog_version,
p4(product_id, sha256, source_refs), tasks y pending. Cada tarea lleva id, role,
depends_on, writes, criteria, source_refs y pending_ids. Los pendientes llevan id,
question y blocks: IDs de tareas afectadas. Una pregunta no bloquea todo el plan.

Antes de ejecutar, valida fuentes y versión del catálogo. Verifica herramientas y
permisos del host. La coordinación se hace desde el agente principal: no presupongas
que un subagente pueda lanzar otro. Usa agents/ para delegar si el host lo soporta;
sin delegación, conserva los mismos contratos y turnos de revisión independientes.

Un resultado lleva task_id, plan_sha256, author, status, artifacts y checks.
Cada artifact lleva id, path relativo al workspace y sha256. Cada check lleva id,
status(pass/fail/pending/not_applicable), rationale y artifact_ids al pasar.
Los de entorno llevan method=runtime, environment y run_id; un test sintético no
puede acreditarlos. pending enlaza pending_id. not_applicable necesita justificación
específica, revisada por el responsable; no usarlo para saltar una limitación.
Appian confirma cada objeto escrito mediante objects(uuid, confirmation_artifact).
El UUID se obtiene de una consulta real guardada, no de un generador.

Estados: partial conserva avances; built declara construcción; tested exige revisar
todos los criterios; reviewed exige reviewer distinto de author y review_artifact;
approved añade approval(responsible, receipt_artifact). El validador comprueba
estructura, referencias y hashes; no autentica personas, no prueba que una consulta
sea real ni otorga aprobación. Revisor y aprobador inspeccionan los artefactos.

Desde el directorio del proyecto, indicando la ruta instalada del plugin:
`python <plugin>/scripts/handoff.py check --plan .profuturo/handoff.json`
`python <plugin>/scripts/handoff.py result --plan .profuturo/handoff.json --result resultado.json`
`python <plugin>/scripts/handoff.py record --plan .profuturo/handoff.json --result resultado.json`
`python <plugin>/scripts/handoff.py status --plan .profuturo/handoff.json`
record usa bloqueo de escritor y reemplazo atómico; solo acepta dependencias
revisadas con evidencia intacta. Para modificar una tarea ya revisada, crea una
revisión de plan y conserva el recibo anterior. No edites estado para habilitar pasos.
