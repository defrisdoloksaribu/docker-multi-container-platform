\# Monitoring Guide



\## 1. Overview



The platform uses Prometheus, cAdvisor, Grafana, and a custom Docker Stats Exporter to monitor container resource usage.



Each component has a different responsibility: collecting metrics, storing time-series data, and visualizing monitoring information.



\## 2. Monitoring Architecture



```mermaid

flowchart TD

&#x20;   Cad\[cAdvisor]

&#x20;   Exporter\[Docker Stats Exporter]

&#x20;   Prom\[Prometheus]

&#x20;   Grafana\[Grafana Dashboard]



&#x20;   Cad -->|Container metrics| Prom

&#x20;   Exporter -->|Custom Docker metrics| Prom

&#x20;   Prom -->|PromQL queries| Grafana

```



\## 3. Prometheus Scraping



Prometheus periodically collects metrics from configured targets.



The project's Prometheus configuration is located at:



```text

monitoring/prometheus/prometheus.yml

```



The configured targets include:



| Job | Target | Purpose |

|---|---|---|

| prometheus | prometheus:9090 | Prometheus self-monitoring |

| cadvisor | cadvisor:8080 | Container resource metrics |

| docker-stats-exporter | host.docker.internal:9713 | Custom Docker statistics |



Open the Prometheus Targets page:



http://localhost:9090/targets



A target with state `UP` indicates that Prometheus can successfully scrape that endpoint.



\## 4. cAdvisor Metrics



cAdvisor collects resource usage information from running containers.



Examples of monitored resources include:



\- CPU usage

\- Memory usage

\- Container-level resource statistics



These metrics are scraped by Prometheus and can be queried through its expression browser.



\## 5. Custom Docker Stats Exporter



The project includes a custom Python exporter:



```text

tools/docker-stats-exporter/exporter.py

```



The exporter runs separately on the Windows host:



```cmd

py tools\\docker-stats-exporter\\exporter.py

```



Its metrics endpoint is:



http://localhost:9713/metrics



The exporter uses Docker CLI statistics to expose custom metrics:



| Metric | Description |

|---|---|

| `docker\_container\_cpu\_percent` | CPU usage percentage |

| `docker\_container\_memory\_usage\_bytes` | Container memory usage in bytes |

| `docker\_container\_memory\_limit\_bytes` | Container memory limit in bytes |

| `docker\_container\_up` | Running container status reported by the exporter |



\*\*Important limitation:\*\* The exporter reads the containers returned by `docker stats --no-stream`. Stopped containers may disappear from its output rather than appear with a value of zero. The exporter also requires its Python process to remain running.



\## 6. PromQL Queries



Open Prometheus at:



http://localhost:9090



Try these queries:



\### Container Status



```promql

docker\_container\_up

```



\### Container CPU Usage



```promql

docker\_container\_cpu\_percent

```



\### Container Memory Usage



```promql

docker\_container\_memory\_usage\_bytes

```



\### Container Memory Limit



```promql

docker\_container\_memory\_limit\_bytes

```



The results depend on whether the exporter is running and Prometheus has successfully scraped its endpoint.



\## 7. Grafana Dashboard



Open Grafana:



http://localhost:3000



The dashboard is named:



\*\*Docker Multi-Container Monitoring\*\*



It includes these panels:



1\. Container Memory Usage

2\. Container Status

3\. Container CPU Usage (%)



Grafana uses Prometheus as its data source.



The configured Prometheus URL inside the Docker Compose network is:



```text

http://prometheus:9090

```



After adding or updating panels, save the dashboard to preserve the configuration.



\## 8. Monitoring Workflow



1\. Start Docker Desktop.

2\. Start the Compose services.

3\. Start the custom Docker Stats Exporter in a separate terminal.

4\. Verify Prometheus targets at `/targets`.

5\. Run PromQL queries to check metric availability.

6\. Open Grafana and review the dashboard panels.



\## 9. Monitoring Limitations



\- The exporter depends on a separate Python process on the Windows host.

\- Stopped containers are not guaranteed to appear in exporter metrics.

\- Monitoring is configured for a local development environment.

\- Production alerting and long-term monitoring infrastructure are not included.



