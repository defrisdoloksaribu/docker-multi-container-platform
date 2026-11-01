\# Testing and Validation



\## 1. Overview



This document describes the testing and validation activities performed on the Docker Multi-Container Inventory Platform.



Testing covers API functionality, container health, resource monitoring, service recovery, database persistence, and the GitHub Actions CI workflow.



\## 2. API Testing



The API is accessed through the Nginx reverse proxy.



\*\*Health check\*\*



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



\*\*Retrieve inventory items\*\*



```cmd

curl.exe http://localhost:8080/items

```



\*\*Create an inventory item\*\*



```cmd

curl.exe -X POST http://localhost:8080/items -H "Content-Type: application/json" -d "{\\"name\\":\\"Mouse\\",\\"quantity\\":5}"

```



Verify the result by requesting the inventory list again.



\## 3. Container Health Checks



Check the status of all Compose services:



```cmd

docker compose ps

```



Check the logs of a specific service:



```cmd

docker compose logs api

docker compose logs db

```



Services should be running, and services with configured health checks should report a healthy status.



\## 4. CPU and Memory Monitoring



The project uses cAdvisor and the custom Docker Stats Exporter to expose container resource metrics.



Check the custom exporter endpoint:



```text

http://localhost:9713/metrics

```



Example PromQL queries:



```promql

docker\_container\_cpu\_percent

```



```promql

docker\_container\_memory\_usage\_bytes

```



Review the corresponding CPU and memory panels in the Grafana dashboard.



\## 5. API Recovery Test



This test checks whether the API service can be manually restarted after being stopped.



Stop the API container:



```cmd

docker compose kill api

```



Restart the API service:



```cmd

docker compose up -d api

```



Verify its status:



```cmd

docker compose ps api

```



Test the health endpoint again:



```cmd

curl.exe http://localhost:8080/health

```



\*\*Expected result:\*\* The API service starts again and the health endpoint responds successfully.



Note: This is a manual recovery test. It does not demonstrate automatic application recovery.



\## 6. Database Persistence Test



This test checks whether inventory records remain available after the database container is recreated.



First, check the current inventory:



```cmd

curl.exe http://localhost:8080/items

```



Recreate the database container:



```cmd

docker compose up -d --force-recreate db

```



Wait until the database is ready, then check the API health endpoint:



```cmd

curl.exe http://localhost:8080/health

```



Retrieve the inventory again:



```cmd

curl.exe http://localhost:8080/items

```



\*\*Expected result:\*\* Previously stored inventory records remain available because database data is stored in a persistent Docker volume.



\## 7. GitHub Actions CI



The project uses GitHub Actions to automate basic validation whenever changes are pushed or a pull request is created for the configured branch.



The CI workflow performs:



1\. Repository checkout.

2\. Python environment setup.

3\. Development dependency installation.

4\. Automated test execution using pytest.

5\. Docker image build.



Workflow location:



```text

.github/workflows/ci.yml

```



Check the actual execution result in the repository's \*\*Actions\*\* tab.



A successful workflow indicates that the configured CI jobs completed without errors.



\## 8. Test Evidence



Store screenshots of actual test results in:



```text

docs/screenshots/

```



Recommended evidence:



| Screenshot | Evidence |

|---|---|

| API health check | API and database connection |

| Docker Compose status | Running containers |

| Grafana dashboard | CPU, memory, and container status |

| Prometheus targets | Metrics scraping status |

| API recovery | API works after manual restart |

| Database persistence | Inventory records remain after DB recreation |

| GitHub Actions | CI workflow result |



Only include screenshots of tests that have actually been performed.



\## 9. Testing Limitations



\- API recovery is performed manually.

\- The exporter must run separately on the Windows host.

\- CI validates tests and builds the Docker image; it does not deploy the application.

\- Test results may vary depending on the local Docker environment.



