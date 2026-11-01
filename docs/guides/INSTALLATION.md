\# Installation Guide



\## 1. Overview



This guide explains how to install and run the Docker Multi-Container Inventory Platform on a Windows machine using Docker Desktop and Docker Compose.



\## 2. Software Prerequisites



Pastikan software berikut sudah tersedia:



| Software | Purpose |

|---|---|

| Git | Clone the project repository |

| Docker Desktop | Run Docker containers |

| Docker Compose | Manage multi-container services |

| Python 3 | Run the custom Docker Stats Exporter |

| Web Browser | Access API, Prometheus, and Grafana |



Verify the installation:



```cmd

git --version

docker --version

docker compose version

py --version

```



\## 3. Clone Repository



Open CMD and run:



```cmd

git clone https://github.com/defrisdoloksaribu/docker-multi-container-platform.git

cd docker-multi-container-platform

```



\## 4. Environment Configuration



Copy the example environment file:



```cmd

copy .env.example .env

```



Open `.env` and adjust the configuration if required.



Keep credentials private. Do not commit real passwords or secrets to GitHub.



\## 5. Start Docker Compose Services



Make sure Docker Desktop is running.



Build and start the services:



```cmd

docker compose up --build -d

```



Check the container status:



```cmd

docker compose ps

```



View service logs:



```cmd

docker compose logs

```



To stop the services:



```cmd

docker compose down

```



\## 6. Run Docker Stats Exporter



The custom Docker Stats Exporter runs separately on the Windows host. It is not included as a Docker Compose service.



Open another CMD window, navigate to the project directory, and run:



```cmd

py tools\\docker-stats-exporter\\exporter.py

```



Keep this terminal open while monitoring the exporter.



Open the metrics endpoint:



```text

http://localhost:9713/metrics

```



The exporter reads Docker container statistics and exposes metrics for Prometheus.



\## 7. Verify Installation



Check the API health endpoint:



```cmd

curl.exe http://localhost:8080/health

```



Expected response:



```json

{

&#x20; "status": "healthy",

&#x20; "database": "connected"

}

```



Check the monitoring interfaces:



| Service | URL |

|---|---|

| API | http://localhost:8080 |

| Prometheus | http://localhost:9090 |

| Prometheus Targets | http://localhost:9090/targets |

| Grafana | http://localhost:3000 |

| Docker Stats Exporter | http://localhost:9713/metrics |



Make sure the Prometheus targets show the expected scrape status and Grafana can access the Prometheus data source.



\## 8. Shutdown



Stop and remove the Compose containers:



```cmd

docker compose down

```



To also remove named volumes, use:



```cmd

docker compose down -v

```



\*\*Warning:\*\* The `-v` option removes Compose-managed volumes and can delete persistent database data. Use it only when you intentionally want to reset the database.



\## 9. Notes



\- Docker Desktop must remain running while the platform is active.

\- The custom exporter must be started separately.

\- The exporter terminal must remain open to continue exposing metrics.

\- This installation guide describes a local development environment.



