#!/bin/bash
set -a
source /ELK/.env
set +a

# Caminho onde guardar o backup
BACKUP_DIR="/ELK/backup"
BACKUP_FILE="$BACKUP_DIR/kibana_backup.ndjson"

# Criar diretoria para armazenar o ficheiro do backup, se não existir
mkdir -p "$BACKUP_DIR"

# Executar exportação dos saved objects
curl -k -u elastic:$ELASTICSEARCH_PASSWORD -X POST "https://{YOUR_IP}:5601/api/saved_objects/_export" \
  -H "kbn-xsrf: true" \
  -H "Content-Type: application/json" \
  -d '{
    "type": [
      "config",
      "config-global",
      "url",
      "index-pattern",
      "action",
      "query",
      "tag",
      "graph-workspace",
      "search",
      "alert",
      "visualization",
      "event-annotation-group",
      "lens",
      "map",
      "dashboard",
      "cases",
      "metrics-data-source",
      "infrastructure-monitoring-log-view",
      "canvas-element",
      "canvas-workpad",
      "osquery-saved-query",
      "osquery-pack",
      "csp-rule-template",
      "threshold-explorer-view",
      "uptime-dynamic-settings",
      "synthetics-privates-locations",
      "synthetics-private-location",
      "synthetics-dynamic-settings",
      "links",
      "apm-indices",
      "infrastructure-ui-source",
      "inventory-view",
      "infra-custom-dashboards",
      "metrics-explorer-view",
      "apm-service-group",
      "apm-custom-dashboards"
    ],
    "includeReferencesDeep": true
  }' \
  -o "$BACKUP_FILE"
