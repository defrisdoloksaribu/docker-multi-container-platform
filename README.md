\# Docker Multi-Container Inventory Platform



A containerized inventory management REST API built with Docker Compose, FastAPI, PostgreSQL, and Nginx.



\## Overview



This project demonstrates how to deploy and manage a multi-container application using a reverse proxy, application service, and relational database.



\## Architecture



```text

Client

&#x20; |

&#x20; v

Nginx Reverse Proxy :8080

&#x20; |

&#x20; v

FastAPI Application :8000

&#x20; |

&#x20; v

PostgreSQL Database :5432

```



\## Technology Stack



\- \*\*Docker \& Docker Compose\*\* — containerization and service orchestration

\- \*\*Nginx\*\* — reverse proxy

\- \*\*FastAPI\*\* — REST API

\- \*\*PostgreSQL\*\* — persistent relational database

\- \*\*Python\*\* — application development



\## Features



\- Multi-container orchestration

\- Container health checks

\- PostgreSQL persistent volume

\- Separate frontend and internal backend networks

\- Environment-based database configuration

\- Non-root application container

\- Inventory creation and retrieval API



\## Getting Started



\### Prerequisites



\- Docker Desktop

\- Docker Compose

\- Git



\### Installation



1\. Clone the repository:



&#x20;  ```bash

&#x20;  git clone https://github.com/defrisdoloksaribu/docker-multi-container-platform.git

&#x20;  cd docker-multi-container-platform

&#x20;  ```



2\. Create a local `.env` file from the example:



&#x20;  ```bash

&#x20;  copy .env.example .env

&#x20;  ```



3\. Edit `.env` and set a strong local database password.



4\. Start the application:



&#x20;  ```bash

&#x20;  docker compose up --build -d

&#x20;  ```



5\. Check container health:



&#x20;  ```bash

&#x20;  docker compose ps

&#x20;  ```



\## API Endpoints



| Method | Endpoint | Description |

|---|---|---|

| GET | `/health` | Check API and database connectivity |

| GET | `/items` | Retrieve inventory items |

| POST | `/items` | Create an inventory item |



\### Example Requests



Health check:



```bash

curl http://localhost:8080/health

```



Create an item:



```bash

curl -X POST http://localhost:8080/items -H "Content-Type: application/json" -d "{\\"name\\":\\"Keyboard\\",\\"quantity\\":10}"

```



Retrieve inventory:



```bash

curl http://localhost:8080/items

```



\## Persistence Test



PostgreSQL uses a named Docker volume to retain inventory data across database container restarts.



```bash

docker compose restart db

docker compose ps

curl http://localhost:8080/items

```



\## Security Considerations



\- Database credentials are configured through environment variables.

\- The `.env` file is excluded from version control.

\- PostgreSQL is not published directly to the host.

\- The application runs as a non-root user.

\- The database network is internal to the Docker environment.



\## Cleanup



Stop the services without deleting the database volume:



```bash

docker compose down

```



\## Author



\*\*Defris Doloksaribu\*\*



GitHub: \[defrisdoloksaribu](https://github.com/defrisdoloksaribu)



