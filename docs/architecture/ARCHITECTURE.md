\# System Architecture



\## 1. Overview



Docker Multi-Container Inventory Platform is a containerized application designed to demonstrate how multiple services communicate within a Docker Compose environment.



The platform uses FastAPI as the backend API, PostgreSQL as the database, and Nginx as a reverse proxy. Monitoring is provided through Prometheus, cAdvisor, Grafana, and a custom Python Docker Stats Exporter.



\## 2. System Architecture



```mermaid

flowchart TD

&#x20;   User\[Client / Browser]

&#x20;   Nginx\[Nginx Reverse Proxy]

&#x20;   API\[FastAPI Application]

&#x20;   DB\[(PostgreSQL Database)]



&#x20;   Prom\[Prometheus]

&#x20;   Cad\[cAdvisor]

&#x20;   Exporter\[Docker Stats Exporter]

&#x20;   Grafana\[Grafana Dashboard]



&#x20;   User -->|HTTP :8080| Nginx

&#x20;   Nginx -->|Proxy Request| API

&#x20;   API -->|SQL Connection| DB



&#x20;   Prom -->|Scrape :8080| Cad

&#x20;   Prom -->|Scrape :9713| Exporter

&#x20;   Grafana -->|Query :9090| Prom

```



\## 3. Container Components



| Service | Responsibility |

|---|---|

| API | Handles inventory operations using FastAPI |

| Database | Stores inventory data using PostgreSQL |

| Nginx | Acts as reverse proxy for API requests |

| cAdvisor | Collects container resource metrics |

| Prometheus | Scrapes and stores monitoring metrics |

| Grafana | Displays monitoring dashboards |



The custom Docker Stats Exporter runs separately on the Windows host. It is not a Docker Compose service.



\## 4. Communication Flow



1\. Client sends an HTTP request to Nginx through port `8080`.

2\. Nginx forwards the request to the FastAPI application.

3\. FastAPI communicates with PostgreSQL to read or update inventory data.

4\. cAdvisor collects container resource metrics.

5\. Prometheus scrapes metrics from cAdvisor and the custom exporter.

6\. Grafana queries Prometheus and visualizes the collected metrics.



\## 5. Network and Port Mapping



| Component | Port | Purpose |

|---|---:|---|

| Nginx | 8080 | External API access |

| FastAPI | 8000 | Internal application port |

| PostgreSQL | 5432 | Database connection |

| Prometheus | 9090 | Metrics and query interface |

| Grafana | 3000 | Monitoring dashboard |

| cAdvisor | 8080 | Container metrics endpoint |

| Docker Stats Exporter | 9713 | Custom Docker metrics endpoint |



Note: Some ports are used internally between containers. External accessibility depends on the Docker Compose port configuration.



\## 6. Docker Volumes



Docker volumes provide persistent storage for data that must remain available when containers are recreated.



The PostgreSQL data volume is used to preserve inventory records beyond the lifecycle of the database container.



This allows the database container to be recreated without intentionally deleting its stored data, as long as the associated volume is retained.



\## 7. Architecture Notes



\- Services communicate through the Docker Compose network.

\- Nginx provides a single entry point for API access.

\- Prometheus is responsible for metrics collection.

\- Grafana is used for metrics visualization.

\- The custom exporter depends on a Python process running on the Windows host.

\- This project is designed for local development and learning, not yet as a production deployment.



