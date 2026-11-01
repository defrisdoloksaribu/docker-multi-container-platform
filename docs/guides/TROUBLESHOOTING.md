\# Troubleshooting Guide



\## 1. Overview



This document explains how to identify and resolve common issues when running the Docker Multi-Container Inventory Platform locally.



Run commands from the project root using Windows CMD unless stated otherwise.



\## 2. Docker Desktop Is Not Running



\*\*Symptoms\*\*

\- Docker commands cannot connect to the Docker daemon.

\- Docker Compose fails to start services.



\*\*Check\*\*



```cmd

docker version

docker info

```



\*\*Solution\*\*

1\. Open Docker Desktop.

2\. Wait until the Docker engine is running.

3\. Retry the Docker command.



\## 3. Container Is Unhealthy or Not Running



\*\*Check service status\*\*



```cmd

docker compose ps

```



\*\*Inspect logs\*\*



```cmd

docker compose logs api

docker compose logs db

docker compose logs nginx

```



\*\*Solution\*\*

\- Check the first relevant error in the service logs.

\- Verify the `.env` configuration.

\- Confirm dependent services are running.

\- Restart the affected service after correcting the issue.



Example:



```cmd

docker compose up -d api

```



\## 4. Prometheus Is Not Receiving Metrics



\*\*Symptoms\*\*

\- Prometheus target status is `DOWN`.

\- PromQL queries return no data.



\*\*Check\*\*



Open:



http://localhost:9090/targets



Review the service status:



```cmd

docker compose ps

```



\*\*Solution\*\*

\- Verify the target and port in `monitoring/prometheus/prometheus.yml`.

\- Confirm the target service is running.

\- Inspect Prometheus logs:



```cmd

docker compose logs prometheus

```



After changing the configuration, restart Prometheus:



```cmd

docker compose restart prometheus

```



\## 5. Exporter Cannot Be Accessed



\*\*Symptoms\*\*

\- The exporter metrics page cannot be opened.

\- Prometheus reports the exporter target as `DOWN`.



\*\*Start the exporter\*\*



```cmd

py tools\\docker-stats-exporter\\exporter.py

```



Keep the terminal open.



From another CMD window, test:



```cmd

curl.exe http://localhost:9713/metrics

```



\*\*Solution\*\*

\- Confirm Python is available using `py --version`.

\- Confirm Docker Desktop is running.

\- Check that `docker stats --no-stream` works.

\- Make sure the exporter process is still running.

\- Verify the Prometheus target is `host.docker.internal:9713`.



Remember: the exporter runs separately on the Windows host, not inside Docker Compose.



\## 6. Grafana Does Not Display Data



\*\*Symptoms\*\*

\- Dashboard panels show `No data`.

\- Grafana cannot connect to Prometheus.



\*\*Check\*\*

\- Open Prometheus and run the query `up`.

\- Check Prometheus Targets.

\- Verify the Grafana data source URL:



```text

http://prometheus:9090

```



\*\*Solution\*\*

1\. Confirm Prometheus is running.

2\. Confirm the required scrape targets are `UP`.

3\. Run the metric query directly in Prometheus.

4\. Open Grafana data source settings.

5\. Select \*\*Save \& test\*\*.

6\. Review the panel query and dashboard time range.



If a metric is missing in Prometheus, fix the scraping issue before changing Grafana panels.



\## 7. API Cannot Connect to PostgreSQL



\*\*Check\*\*



```cmd

docker compose ps

docker compose logs db

docker compose logs api

```



\*\*Solution\*\*

\- Confirm PostgreSQL is running and ready.

\- Review database settings in `.env`.

\- Verify the API uses the correct database service hostname and port.

\- Test the API health endpoint:



```cmd

curl.exe http://localhost:8080/health

```



Do not share passwords or secrets when reporting errors.



\## 8. Important Data Safety Note



Avoid using this command as a routine troubleshooting step:



```cmd

docker compose down -v

```



The `-v` option removes Compose-managed volumes and may delete persistent PostgreSQL data.



Inspect logs and restart the affected service before considering a database reset.



\## 9. Reporting an Issue



When asking for help, include:

\- The command you

