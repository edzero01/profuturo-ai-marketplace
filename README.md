# profuturo-ai-marketplace

Marketplace de plugins de Claude Code con las reglas y skills corporativas de Profuturo. Es la fuente de verdad del contexto que usan los agentes en los microservicios.

## Contenido

| Plugin | Skills | Reglas que aplica |
| --- | --- | --- |
| `profuturo-java` | `reglas-profuturo`, `agregar-endpoint`, `agregar-cliente-feign` | Capas del microservicio, Secretos y configuración, Oracle y JPA |

```
.claude-plugin/marketplace.json          ← define el marketplace "profuturo"
plugins/profuturo-java/
  .claude-plugin/plugin.json             ← versión del plugin
  skills/<skill>/SKILL.md                ← procedimientos
  skills/reglas-profuturo/rules/*.md     ← reglas corporativas
catalog-info.yaml + catalog/*.yaml       ← registro en Backstage (AiResource)
```

## Cómo llega a cada repo

Los repos creados con el golden path `profuturo-ms-experience` traen `.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "profuturo": {
      "source": { "source": "github", "repo": "edzero01/profuturo-ai-marketplace" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": { "profuturo-java@profuturo": true }
}
```

Al abrir `claude` en el repo y aceptar que la carpeta es de confianza, Claude Code registra el marketplace y carga el plugin. Con `autoUpdate`, los cambios que se publiquen aquí llegan a todos los repos en su siguiente sesión.

Para un repo existente, manualmente:

```bash
claude plugin marketplace add edzero01/profuturo-ai-marketplace
claude plugin install profuturo-java@profuturo --scope project
```

## Cómo publicar un cambio

1. Edita la skill o la regla y abre un PR.
2. Sube `version` en `plugins/profuturo-java/.claude-plugin/plugin.json`.
3. Si agregas una skill o regla, regístrala también en `catalog/skills.yaml` o `catalog/rules.yaml` y en `spec.skills` del plugin en `catalog/marketplace.yaml`.
4. Valida con `claude plugin validate .` antes del merge.

## Gobierno en Backstage

Las entidades de `catalog/` modelan `marketplace → plugin → skills` (relación `hasPart`) y `skill → reglas` (`dependsOn`). Cada microservicio declara `dependsOn: airesource:default/profuturo-java` en su `catalog-info.yaml`, así el catálogo responde qué servicios usan cada plugin y a quién afecta un cambio de regla.
