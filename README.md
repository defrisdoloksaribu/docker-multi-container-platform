# Docker Multi-Container Inventory Platform

<<<<<<< HEAD
**A containerized inventory platform built with Docker, FastAPI, PostgreSQL, Nginx, and an integrated monitoring stack.**
=======
**A containerized inventory platform with automated testing, persistent storage, reverse proxy, and infrastructure monitoring.**
>>>>>>> f656763 (docs: improve project documentation and README)

[![CI](https://github.com/defrisdoloksaribu/docker-multi-container-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/defrisdoloksaribu/docker-multi-container-platform/actions/workflows/ci.yml)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?logo=docker&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-4169E1?logo=postgresql&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-E6522C?logo=prometheus&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-F46800?logo=grafana&logoColor=white)

**Author:** Defris Doloksaribu  
**Project Category:** DevOps / Containerization / Infrastructure Monitoring  
**Repository:** [GitHub](https://github.com/defrisdoloksaribu/docker-multi-container-platform)

---

## 1. Project Overview

<<<<<<< HEAD
Docker Multi-Container Inventory Platform merupakan proyek portfolio untuk membangun dan mengelola aplikasi inventory menggunakan **Docker multi-container architecture**.

Aplikasi menggunakan FastAPI sebagai REST API, PostgreSQL sebagai persistent database, dan Nginx sebagai reverse proxy. Seluruh application services dikelola menggunakan Docker Compose.

Untuk infrastructure monitoring, proyek ini mengintegrasikan Prometheus, cAdvisor, Grafana, serta custom Python-based Docker Stats Exporter untuk mengumpulkan informasi CPU, memory, dan container status.

Selain itu, GitHub Actions digunakan untuk menjalankan automated testing dan Docker image build melalui CI workflow.
=======
Docker Multi-Container Inventory Platform merupakan proyek portofolio untuk mempraktikkan workflow DevOps melalui aplikasi inventory berbasis container.

Platform ini mengintegrasikan FastAPI sebagai backend REST API, PostgreSQL sebagai persistent database, dan Nginx sebagai reverse proxy. Untuk infrastructure monitoring, project ini menggunakan Prometheus, cAdvisor, Grafana, serta custom Python Docker Stats Exporter.

Docker Compose digunakan untuk mengelola multi-container services, sedangkan GitHub Actions menjalankan automated testing dan Docker image build melalui CI pipeline.

Project ini berfokus pada praktik **containerization, service communication, CI automation, database persistence, dan infrastructure monitoring** sebagai bagian dari persiapan internship di bidang DevOps.
>>>>>>> f656763 (docs: improve project documentation and README)

Project ini berfokus pada penerapan practical DevOps workflow, mulai dari application containerization, service management, monitoring, hingga continuous integration.

<<<<<<< HEAD
## 2. Key Features

- **Multi-Container Management** — Mengelola enam application dan monitoring services menggunakan Docker Compose.
- **REST API** — Menyediakan endpoint untuk inventory management dan application health check.
- **Persistent Database** — Menggunakan PostgreSQL dengan Docker named volume.
- **Reverse Proxy** — Mengatur application traffic menggunakan Nginx.
- **Health Checks** — Memeriksa kondisi service yang memiliki health check.
- **Automated Testing** — Menjalankan unit tests menggunakan pytest.
- **Continuous Integration** — Mengotomatisasi testing dan Docker image build melalui GitHub Actions.
- **Infrastructure Monitoring** — Menggunakan Prometheus dan cAdvisor untuk metric collection.
- **Custom Metrics Exporter** — Mengumpulkan CPU, memory, dan status container menggunakan Python.
- **Grafana Dashboard** — Menampilkan container status dan resource utilization.
- **Recovery Testing** — Menguji API recovery melalui manual container restart.

## 3. System Architecture
=======
- **Multi-container management** — mengelola enam container services menggunakan Docker Compose.
- **REST API** — menyediakan endpoint untuk health check dan inventory management.
- **Persistent storage** — menyimpan PostgreSQL data menggunakan Docker named volume.
- **Reverse proxy** — meneruskan application requests melalui Nginx.
- **Health checks** — memeriksa kesiapan services yang memiliki health check configuration.
- **Automated testing** — menjalankan Python tests menggunakan pytest.
- **Continuous integration** — menjalankan testing dan Docker image build melalui GitHub Actions.
- **Container monitoring** — mengumpulkan resource metrics menggunakan cAdvisor dan Prometheus.
- **Custom Docker metrics** — menyediakan CPU, memory, dan container status metrics melalui Python exporter.
- **Grafana dashboard** — menampilkan container CPU, memory, dan status monitoring.
- **Recovery testing** — memverifikasi API setelah container dihentikan dan dijalankan kembali secara manual.

## System Architecture
>>>>>>> f656763 (docs: improve project documentation and README)

```mermaid
flowchart TB
    U["Client / User"]
    N["Nginx Reverse Proxy"]
    A["FastAPI Application"]
    D[("PostgreSQL 17<br/>Persistent Volume")]

    CA["cAdvisor"]
<<<<<<< HEAD
    E["Docker Stats Exporter<br/>Python Host Process"]
    P["Prometheus"]
    G["Grafana"]
=======
    E["Docker Stats Exporter<br/>Windows Host :9713"]
    P["Prometheus<br/>Port 9090"]
    G["Grafana<br/>Port 3000"]
>>>>>>> f656763 (docs: improve project documentation and README)

    GH["GitHub Actions"]
    T["Automated Testing"]
    B["Docker Image Build"]

    U --> N
    N --> A
    A --> D

    CA --> P
    E --> P
    P --> G

    GH --> T
    T --> B
```

### Service Components

| Service | Technology | Responsibility |
|---|---|---|
<<<<<<< HEAD
| API | FastAPI | Menangani inventory requests |
| Database | PostgreSQL 17 | Persistent data storage |
| Reverse Proxy | Nginx | Request routing |
| Container Monitoring | cAdvisor | Container resource metrics |
| Metrics Collection | Prometheus | Metrics scraping and querying |
| Visualization | Grafana | Monitoring dashboard |

**Additional component:** Docker Stats Exporter merupakan Python process yang berjalan di host Windows, bukan Docker Compose service.
=======
| `api` | Python, FastAPI | Menyediakan REST API inventory |
| `db` | PostgreSQL 17 | Menyimpan inventory data |
| `nginx` | Nginx | Menjadi reverse proxy aplikasi |
| `cadvisor` | cAdvisor | Mengumpulkan container resource metrics |
| `prometheus` | Prometheus | Scraping dan querying metrics |
| `grafana` | Grafana | Memvisualisasikan monitoring metrics |

Custom Docker Stats Exporter berjalan sebagai Python process pada Windows host, terpisah dari keenam Compose services.

Docker Compose mengelola service lifecycle, networking, health checks, restart policies, dan persistent volumes sesuai konfigurasi project.
>>>>>>> f656763 (docs: improve project documentation and README)

## 4. Technology Stack

| Category | Tools |
|---|---|
| Containerization | Docker, Docker Compose |
| Backend | Python, FastAPI |
| Database | PostgreSQL 17 |
| Reverse Proxy | Nginx |
| Monitoring | Prometheus, cAdvisor, Grafana |
<<<<<<< HEAD
| Metrics Exporter | Python |
| Testing | pytest |
| CI/CD | GitHub Actions (CI) |
=======
| Custom Metrics | Python Docker Stats Exporter |
| Testing | pytest |
| CI | GitHub Actions |
>>>>>>> f656763 (docs: improve project documentation and README)
| Version Control | Git, GitHub |

## 5. Getting Started

### Prerequisites

Pastikan software berikut sudah terinstall:

<<<<<<< HEAD
- Docker Desktop
- Git
- Python 3

Docker Desktop harus berjalan dengan Linux containers enabled.
=======
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/)
- Python 3 untuk menjalankan custom exporter

Docker Desktop harus berjalan dengan Linux containers sebelum menjalankan Docker Compose.
>>>>>>> f656763 (docs: improve project documentation and README)

### Clone Repository

```cmd
git clone https://github.com/defrisdoloksaribu/docker-multi-container-platform.git
cd docker-multi-container-platform
```

### Environment Configuration

Buat file `.env` dari template:

```cmd
copy .env.example .env
```

<<<<<<< HEAD
Sesuaikan PostgreSQL credentials dan Grafana administrator password berdasarkan konfigurasi `.env.example`.

> Security note: Jangan commit `.env`, password, token, atau credentials ke public repository.

### Start Application
=======
Buka `.env` menggunakan text editor dan sesuaikan variabel yang diperlukan, termasuk PostgreSQL credentials dan Grafana administrator password.

Jangan upload `.env`, password, token, atau secret ke repository.

### 3. Build and Start the Platform
>>>>>>> f656763 (docs: improve project documentation and README)

```cmd
docker compose up --build -d
```

<<<<<<< HEAD
Perintah ini akan build application image dan menjalankan seluruh Docker Compose services.
=======
Perintah ini membangun application image dan menjalankan Compose services di background.
>>>>>>> f656763 (docs: improve project documentation and README)

### Verify Containers

```cmd
docker compose ps
```

<<<<<<< HEAD
Pastikan semua service berjalan dan configured health checks menunjukkan status sehat.

### Start Custom Exporter

Buka CMD baru dari project directory:
=======
Pastikan services berjalan dan health checks yang tersedia mencapai status sehat.

Untuk memvalidasi konfigurasi Compose:
>>>>>>> f656763 (docs: improve project documentation and README)

```cmd
py tools\docker-stats-exporter\exporter.py
```

<<<<<<< HEAD
Biarkan proses exporter tetap berjalan selama monitoring berlangsung.
=======
### 5. Run the Custom Docker Stats Exporter

Exporter dijalankan secara terpisah pada Windows host dan bukan bagian dari Docker Compose services.

Buka CMD window baru dari project directory:

```cmd
py tools\docker-stats-exporter\exporter.py
```

Biarkan terminal tetap berjalan selama monitoring membutuhkan exporter.

### 6. Verify the API
>>>>>>> f656763 (docs: improve project documentation and README)

## 6. Application Endpoints

| Component | URL | Description |
|---|---|---|
| Inventory API | http://localhost:8080 | API access through Nginx |
| Prometheus | http://localhost:9090 | Metrics query interface |
| Prometheus Targets | http://localhost:9090/targets | Target monitoring status |
| Grafana | http://localhost:3000 | Monitoring dashboard |
| Custom Exporter | http://localhost:9713/metrics | Custom container metrics |

### API Reference

| Method | Endpoint | Function |
|---|---|---|
| GET | `/health` | Application and database health check |
| GET | `/items` | Retrieve inventory data |
| POST | `/items` | Create inventory item |

Example health check:

```cmd
curl.exe http://localhost:8080/health
```

<<<<<<< HEAD
Example response:
=======
Contoh response yang telah diverifikasi:
>>>>>>> f656763 (docs: improve project documentation and README)

```json
{
  "status": "healthy",
  "database": "connected"
}
```

<<<<<<< HEAD
## 7. Monitoring Dashboard

Monitoring stack menggunakan Prometheus sebagai metrics collection system dan Grafana sebagai visualization platform.

Dashboard utama menyediakan tiga monitoring panels:
=======
Retrieve inventory data:

```cmd
curl.exe http://localhost:8080/items
```

Contoh data hasil pengujian sebelumnya:
>>>>>>> f656763 (docs: improve project documentation and README)

1. **Container Status** — Menampilkan status container yang terdeteksi exporter.
2. **Container CPU Usage** — Menampilkan CPU utilization setiap container.
3. **Container Memory Usage** — Menampilkan penggunaan memory container.

<<<<<<< HEAD
![Grafana Monitoring Dashboard](docs/screenshots/grafana-dashboard.png)
=======
Data tersebut merupakan contoh hasil pengujian lokal, bukan data yang dijamin tersedia pada instalasi baru.
>>>>>>> f656763 (docs: improve project documentation and README)

### Example Prometheus Queries

<<<<<<< HEAD
Container status:
=======
API diakses melalui Nginx pada `http://localhost:8080`.

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Memeriksa API dan database connectivity |
| `GET` | `/items` | Mengambil inventory list |
| `POST` | `/items` | Menambahkan inventory item |

### Add an Inventory Item

Contoh request menggunakan Windows CMD:

```cmd
curl.exe -X POST http://localhost:8080/items -H "Content-Type: application/json" -d "{\"name\":\"Mouse\",\"quantity\":5}"
```

Verifikasi hasilnya dengan mengambil inventory list kembali.

## Monitoring and Observability

Platform menyediakan monitoring interfaces berikut:

| Component | URL | Purpose |
|---|---|---|
| Inventory API | [localhost:8080](http://localhost:8080) | API access through Nginx |
| Prometheus | [localhost:9090](http://localhost:9090) | Metrics query |
| Prometheus Targets | [localhost:9090/targets](http://localhost:9090/targets) | Scrape target status |
| Grafana | [localhost:3000](http://localhost:3000) | Monitoring dashboard |
| Docker Stats Exporter | [localhost:9713/metrics](http://localhost:9713/metrics) | Custom Docker metrics |

Grafana menggunakan Prometheus sebagai data source dengan internal Docker network URL:

```text
http://prometheus:9090
```

Login Grafana menggunakan credentials yang dikonfigurasi melalui environment variables.

### Custom Docker Metrics

Exporter menyediakan beberapa custom metrics:

| Metric | Description |
|---|---|
| `docker_container_cpu_percent` | Container CPU usage percentage |
| `docker_container_memory_usage_bytes` | Container memory usage |
| `docker_container_memory_limit_bytes` | Container memory limit |
| `docker_container_up` | Running container status reported by exporter |

### Prometheus Queries

Memeriksa status cAdvisor target:
>>>>>>> f656763 (docs: improve project documentation and README)

```promql
docker_container_up
```

<<<<<<< HEAD
CPU utilization:

```promql
docker_container_cpu_percent
```

Memory usage:
=======
Memeriksa custom container status:

```promql
docker_container_up
```

Memeriksa custom CPU usage:

```promql
docker_container_cpu_percent
```

Memeriksa custom memory usage:

```promql
docker_container_memory_usage_bytes
```

**Monitoring note:** Custom exporter menggunakan `docker stats --no-stream`. Stopped containers dapat menghilang dari exporter output, bukan selalu ditampilkan dengan nilai nol. Exporter juga membutuhkan Python process yang tetap berjalan pada host.

## Grafana Dashboard

Dashboard project bernama **Docker Multi-Container Monitoring**.

Dashboard ini memiliki tiga monitoring panels:

1. Container Memory Usage
2. Container Status
3. Container CPU Usage (%)

Screenshot dashboard tersedia di [`docs/screenshots/`](docs/screenshots/).
>>>>>>> f656763 (docs: improve project documentation and README)

```promql
docker_container_memory_usage_bytes
```

<<<<<<< HEAD
Exporter availability:

```promql
up{job="docker-stats-exporter"}
```

## 8. Continuous Integration
=======
GitHub Actions digunakan untuk menjalankan CI workflow ketika terjadi `push` atau `pull_request` pada branch `main`.

Workflow configuration:

```text
.github/workflows/ci.yml
```

Tahapan CI:

1. Checkout source code.
2. Setup Python environment.
3. Install development dependencies.
4. Run automated tests menggunakan pytest.
5. Build Docker image.
>>>>>>> f656763 (docs: improve project documentation and README)

GitHub Actions digunakan untuk menjalankan CI workflow pada event `push` dan `pull_request` ke branch `main`.

<<<<<<< HEAD
Workflow mencakup:

1. Source code checkout.
2. Python environment setup.
3. Development dependencies installation.
4. Automated testing menggunakan pytest.
5. Docker image build.

Run local tests:
=======
Pengujian dapat dijalankan melalui temporary Python container dari Windows CMD:
>>>>>>> f656763 (docs: improve project documentation and README)

```cmd
docker run --rm -v "%cd%:/workspace" -w /workspace python:3.12-slim sh -c "pip install --no-cache-dir -r requirements-dev.txt && python -m pytest tests"
```

<<<<<<< HEAD
Previously recorded local test result:
=======
Hasil pengujian lokal yang telah tercatat sebelumnya:
>>>>>>> f656763 (docs: improve project documentation and README)

```text
3 passed
```

<<<<<<< HEAD
Periksa GitHub Actions untuk hasil CI terbaru.

**Note:** Implementasi CI saat ini mencakup testing dan image build. Automatic deployment ke production environment belum dikonfigurasi sebagai fitur yang terverifikasi.
=======
Hasil tersebut merujuk pada eksekusi sebelumnya. Periksa GitHub Actions untuk memastikan status CI pada commit terbaru.

**Important:** Workflow ini merupakan continuous integration untuk testing dan image build. Automatic deployment belum menjadi bagian dari pipeline yang telah diverifikasi.
>>>>>>> f656763 (docs: improve project documentation and README)

## 9. Testing and Validation

Beberapa skenario pengujian yang telah dilakukan:

| Test Scenario | Validation |
|---|---|
| API Health Check | Memastikan API dan database dapat diakses |
| Container Status | Memastikan enam container terdeteksi exporter |
| Prometheus Targets | Memeriksa status target monitoring |
| CPU Monitoring | Memeriksa CPU metrics |
| Memory Monitoring | Memeriksa memory metrics |
| API Recovery | Menguji pemulihan API setelah manual restart |
| Database Persistence | Memeriksa data setelah database container dibuat ulang |
| CI Workflow | Memeriksa automated testing dan image build |

### API Recovery Test

<<<<<<< HEAD
=======
API diuji dengan menghentikan container, kemudian menjalankannya kembali secara manual:

>>>>>>> f656763 (docs: improve project documentation and README)
```cmd
docker compose kill api
docker compose up -d api
docker compose ps api
```

<<<<<<< HEAD
API kemudian diperiksa kembali menggunakan health endpoint.

Pengujian ini membuktikan manual recovery, bukan automatic self-healing tanpa intervensi.

### Database Persistence Test

=======
Setelah API dijalankan kembali, health endpoint berhasil merespons dan inventory data dapat diakses.

Pengujian ini membuktikan **manual service recovery**, bukan automatic recovery tanpa intervensi pengguna.

### Database Persistence Test

PostgreSQL container dibuat ulang tanpa menghapus named volume:

>>>>>>> f656763 (docs: improve project documentation and README)
```cmd
docker compose up -d --force-recreate db
docker compose ps
```

<<<<<<< HEAD
Setelah database sehat kembali, periksa data melalui endpoint inventory.

## 10. Documentation

Dokumentasi teknis tambahan tersedia di folder [`docs/`](docs/).
=======
Setelah database kembali siap, endpoint diperiksa:

```cmd
curl.exe http://localhost:8080/health
curl.exe http://localhost:8080/items
```

Inventory record yang telah diuji tetap tersedia setelah database container dibuat ulang selama persistent volume dipertahankan.
>>>>>>> f656763 (docs: improve project documentation and README)

| Document | Description |
|---|---|
| [System Architecture](docs/architecture/ARCHITECTURE.md) | Arsitektur sistem dan komunikasi antarservice |
| [Installation Guide](docs/guides/INSTALLATION.md) | Instalasi dan konfigurasi environment |
| [Monitoring Guide](docs/guides/MONITORING.md) | Prometheus, Grafana, dan custom exporter |
| [Testing Guide](docs/guides/TESTING.md) | Test scenarios dan validation |
| [Troubleshooting](docs/guides/TROUBLESHOOTING.md) | Masalah umum dan cara penanganan |
| [Project Screenshots](docs/screenshots/README.md) | Bukti implementasi dan hasil monitoring |
| [Project Report](docs/laporan/README.md) | Dokumentasi laporan proyek |

<<<<<<< HEAD
## 11. Known Limitations
=======
Untuk menghentikan services tanpa menghapus named volumes:
>>>>>>> f656763 (docs: improve project documentation and README)

- Project deployment masih menggunakan local Docker Compose environment.
- CI workflow berfokus pada testing dan Docker image build.
- API recovery yang diuji dilakukan secara manual.
- Custom exporter harus dijalankan secara terpisah pada host.
- Status metric exporter saat ini mencakup container yang dikembalikan oleh `docker stats`, bukan seluruh stopped containers.
- Production alerting dan notification belum diverifikasi.
- Security hardening untuk monitoring dan container access masih dapat ditingkatkan.

<<<<<<< HEAD
## 12. Future Improvements
=======
Hindari `docker compose down -v` jika database data dan monitoring data masih ingin dipertahankan.

## Documentation

Project documentation tersedia di folder [`docs/`](docs/).

### Technical Documentation

| Document | Description |
|---|---|
| [System Architecture](docs/architecture/ARCHITECTURE.md) | System design, communication flow, networking, ports, dan volumes |
| [Installation Guide](docs/guides/INSTALLATION.md) | Prerequisites, environment setup, dan deployment lokal |
| [Monitoring Guide](docs/guides/MONITORING.md) | Prometheus, cAdvisor, exporter, PromQL, dan Grafana |
| [Testing and Validation](docs/guides/TESTING.md) | API testing, recovery, persistence, dan CI |
| [Troubleshooting Guide](docs/guides/TROUBLESHOOTING.md) | Common issues dan troubleshooting steps |

### Project Report and Evidence

- [Project Report](docs/laporan/README.md)
- [Screenshot Documentation](docs/screenshots/README.md)

Screenshot digunakan sebagai evidence dari implementasi dan pengujian aktual. Setiap hasil yang belum diuji tidak boleh ditulis sebagai hasil yang sudah berhasil.
>>>>>>> f656763 (docs: improve project documentation and README)

- Menambahkan API integration tests.
- Mengimplementasikan PostgreSQL backup and restore.
- Menambahkan Prometheus alert rules dan notification.
- Meningkatkan container security.
- Menyempurnakan custom exporter untuk mendeteksi stopped containers.
- Mengembangkan deployment automation.
- Mengevaluasi Kubernetes orchestration.

<<<<<<< HEAD
## 13. Author
=======
```text
docker-multi-container-platform/
├── .github/
│   └── workflows/
│       └── ci.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── requirements.txt
├── docs/
│   ├── architecture/
│   │   └── ARCHITECTURE.md
│   ├── guides/
│   │   ├── INSTALLATION.md
│   │   ├── MONITORING.md
│   │   ├── TESTING.md
│   │   └── TROUBLESHOOTING.md
│   ├── laporan/
│   └── screenshots/
├── monitoring/
│   └── prometheus/
│       └── prometheus.yml
├── nginx/
│   └── default.conf
├── tests/
├── tools/
│   └── docker-stats-exporter/
│       └── exporter.py
├── .dockerignore
├── .env.example
├── .gitignore
├── compose.yaml
├── Dockerfile
├── README.md
├── requirements.txt
└── requirements-dev.txt
```

## Known Limitations

- Deployment masih berorientasi pada local environment menggunakan Docker Compose.
- CI menjalankan automated tests dan Docker image build; automatic deployment belum diverifikasi.
- API recovery yang diuji dilakukan secara manual.
- Custom exporter berjalan sebagai separate host process dan harus dijalankan secara terpisah.
- Stopped containers tidak dijamin muncul pada custom exporter metrics.
- Production alerting dan long-term monitoring belum termasuk implementasi saat ini.
- cAdvisor configuration perlu security review sebelum digunakan pada production environment.
- Automated database backup dan restore belum dinyatakan teruji.

## Future Improvements

- Menambahkan integration tests untuk API dan database.
- Mengimplementasikan automated PostgreSQL backup dan restore testing.
- Menambahkan Prometheus alert rules dan monitoring notifications.
- Memperkuat container security dan monitoring access control.
- Mengembangkan deployment pipeline setelah CI stabil.
- Mengevaluasi orchestration dan automated recovery lebih lanjut.

## Author
>>>>>>> f656763 (docs: improve project documentation and README)

**Defris Doloksaribu**

- GitHub: [@defrisdoloksaribu](https://github.com/defrisdoloksaribu)
- Repository: [docker-multi-container-platform](https://github.com/defrisdoloksaribu/docker-multi-container-platform)

---

*Built as a hands-on DevOps portfolio project focused on containerization, CI automation, persistent storage, and infrastructure monitoring.*
