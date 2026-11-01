# Docker Multi-Container Inventory Platform

**A practical DevOps project for containerized application deployment, persistent storage, CI, and monitoring.**

[![CI](https://github.com/defrisdoloksaribu/docker-multi-container-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/defrisdoloksaribu/docker-multi-container-platform/actions/workflows/ci.yml)
![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana&logoColor=white)

**Author:** Defris Doloksaribu  
**Focus:** DevOps · Docker · CI · Monitoring  
**Repository:** [github.com/defrisdoloksaribu/docker-multi-container-platform](https://github.com/defrisdoloksaribu/docker-multi-container-platform)

---

## Overview

Project ini membangun aplikasi inventory berbasis **Docker Compose**. FastAPI menyediakan REST API, PostgreSQL menyimpan data secara persisten, dan Nginx menjadi reverse proxy.

Monitoring dilakukan menggunakan **Prometheus, cAdvisor, Grafana**, serta custom **Python Docker Stats Exporter**. GitHub Actions menjalankan automated tests dan Docker image build.

## Architecture

```text
                    CLIENT
                       |
                 NGINX :8080
                       |
                  FASTAPI
                       |
                POSTGRESQL 17
                 (data volume)

   cAdvisor -------------------+
                               |
   Docker Stats Exporter ------+--> PROMETHEUS :9090
   (Windows host :9713)        |          |
                               |       GRAFANA :3000
                               |
   GitHub Actions --> Tests --> Docker Image Build
```

**Enam Compose services:** `api`, `db`, `nginx`, `cadvisor`, `prometheus`, dan `grafana`.

Custom Docker Stats Exporter berjalan terpisah pada Windows host, bukan sebagai Compose service.

## Tech Stack

| Area | Technology |
|---|---|
| Application | Python, FastAPI |
| Database | PostgreSQL 17 |
| Container | Docker, Docker Compose |
| Reverse proxy | Nginx |
| Monitoring | Prometheus, cAdvisor, Grafana |
| Custom metrics | Python Docker Stats Exporter |
| CI | GitHub Actions |
| Testing | pytest |

## Run Locally

**Requirements:** Docker Desktop (Linux containers), Git, and Python 3 for the custom exporter.

```cmd
git clone https://github.com/defrisdoloksaribu/docker-multi-container-platform.git
cd docker-multi-container-platform
copy .env.example .env
```

Atur credentials di file `.env`, kemudian jalankan:

```cmd
docker compose up --build -d
docker compose ps
```

Jalankan exporter dari CMD kedua:

```cmd
py tools\docker-stats-exporter\exporter.py
```

Biarkan proses exporter tetap berjalan saat ingin melihat custom metrics.

## Access the Platform

| Component | Address |
|---|---|
| Inventory API | http://localhost:8080 |
| API health | http://localhost:8080/health |
| Inventory items | http://localhost:8080/items |
| Prometheus | http://localhost:9090 |
| Prometheus targets | http://localhost:9090/targets |
| Grafana | http://localhost:3000 |
| Exporter metrics | http://localhost:9713/metrics |

Contoh memeriksa API dari Windows CMD:

```cmd
curl.exe http://localhost:8080/health
curl.exe http://localhost:8080/items
```

Grafana menggunakan Prometheus sebagai data source melalui alamat internal `http://prometheus:9090`. Login menggunakan credentials dari `.env`.

## Monitoring Metrics

Custom exporter menyediakan:

- `docker_container_cpu_percent`
- `docker_container_memory_usage_bytes`
- `docker_container_memory_limit_bytes`
- `docker_container_up`

Contoh PromQL:

```promql
up{job="cadvisor"}
up{job="docker-stats-exporter"}
docker_container_cpu_percent
docker_container_memory_usage_bytes
docker_container_up
```

**Catatan:** Exporter membaca `docker stats --no-stream`. Container yang berhenti dapat tidak muncul pada output metrics. Exporter harus tetap dijalankan secara manual pada Windows host.

## CI and Validation

GitHub Actions menjalankan workflow pada `push` dan `pull_request` ke branch `main`:

1. Checkout source code.
2. Setup Python.
3. Install development dependencies.
4. Run pytest.
5. Build Docker image.

Pengujian lokal yang pernah tercatat: **3 passed**. Periksa tab **Actions** di GitHub untuk status workflow terbaru.

Pengujian project juga mencakup API health check, container monitoring, manual API restart, dan database persistence setelah container database dibuat ulang dengan named volume tetap dipertahankan.

**Batasan yang perlu diketahui:** API recovery yang diuji adalah manual restart, bukan automatic self-healing. Workflow saat ini melakukan testing dan image build, belum automatic deployment.

## Screenshots

Lihat [docs/screenshots](docs/screenshots/) untuk bukti tampilan API, container, Prometheus, Grafana, dan CI.

## Documentation

| Document | What it covers |
|---|---|
| [Architecture](docs/architecture/ARCHITECTURE.md) | Desain sistem dan komunikasi service |
| [Installation](docs/guides/INSTALLATION.md) | Setup dan menjalankan project |
| [Monitoring](docs/guides/MONITORING.md) | Prometheus, Grafana, dan exporter |
| [Testing](docs/guides/TESTING.md) | Skenario pengujian |
| [Troubleshooting](docs/guides/TROUBLESHOOTING.md) | Masalah umum dan solusinya |
| [Project report](docs/laporan/README.md) | Laporan proyek |
| [Screenshot guide](docs/screenshots/README.md) | Daftar bukti implementasi |

## Current Limitations and Next Steps

- Deployment masih berjalan pada local Docker Compose.
- Custom exporter perlu dijalankan terpisah pada host.
- Automatic deployment, production alerting, dan automated database backup belum diimplementasikan atau diverifikasi.
- Pengembangan berikutnya: integration tests, backup and restore, alert rules, serta peningkatan container security.

---

**Defris Doloksaribu** · [GitHub](https://github.com/defrisdoloksaribu)

*Hands-on DevOps portfolio project focused on containerization, CI automation, persistent storage, and infrastructure monitoring.*
