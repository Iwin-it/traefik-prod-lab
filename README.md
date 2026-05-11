# Traefik Production Lab

Учебный проект reverse proxy на Traefik перед переходом к Kubernetes.


# Архитектура

```text
Client
  ↓ 
Traefik
  ↓
app /api / admin / prometheus/ grafana

# Домены

https://app.local
https://app.local/api
https://admin.local
https://traefik.local/dashboard/
https://prometheus.local
https://grafana.local

# Запуск dev
docker compose --env-file .env.dev up -d

# Остановка 
docker compose --env-file .env.dev down

# Пересоздание 
docker compose --env-file .env.dev up -d --force-recreate

# Проверка
docker compose --env-file .env.dev ps
docker logs traefik --tail=100

# Проверка API
curl -k https://app.local/app.local/api/health
curl -k https://app.local/app.local/api

# Проверка Traefik metrics
curl -k -u admin:Password123 https://traefik.local/metrics

# Важные концепции
Router      → правило входящего запроса
Service     → куда отправить запрос
Middleware  → что сделать с запросом
EntryPoint  → порт входа :80 / :443
TLS         → HTTPS
Provider    → откуда Traefik берёт конфиг

# Связь с 
Docker container  → Pod
Docker Compose    → Deployment
Docker network    → Kubernetes Service
Traefik labels    → Ingress / IngressRoute
.env              → ConfigMap / Secret
Healthcheck       → Readiness/Liveness Probe
Prometheus        → Monitoring
Grafana           → Dashboards

```text
