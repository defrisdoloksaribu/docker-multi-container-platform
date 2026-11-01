
import json
import logging
import re
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


HOST = "0.0.0.0"
PORT = 9713
DOCKER_TIMEOUT = 15

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)


def get_container_stats():
    """Read live container statistics from Docker CLI."""
    try:
        result = subprocess.run(
            [
                "docker",
                "stats",
                "--no-stream",
                "--format",
                "{{json .}}"
            ],
            capture_output=True,
            text=True,
            check=True,
            timeout=DOCKER_TIMEOUT
        )

    except subprocess.TimeoutExpired as error:
        raise RuntimeError("Docker stats command timed out") from error

    except FileNotFoundError as error:
        raise RuntimeError("Docker CLI was not found in PATH") from error

    except subprocess.CalledProcessError as error:
        message = error.stderr.strip() or "Unknown Docker CLI error"
        raise RuntimeError(message) from error

    containers = []

    for line in result.stdout.splitlines():
        if not line.strip():
            continue

        try:
            containers.append(json.loads(line))
        except json.JSONDecodeError as error:
            raise RuntimeError(
                f"Invalid Docker stats JSON: {line}"
            ) from error

    return containers


def to_bytes(value):
    """Convert Docker memory values into bytes."""
    match = re.fullmatch(
        r"\s*([0-9]+(?:\.[0-9]+)?)\s*([A-Za-z]+)\s*",
        value
    )

    if not match:
        raise ValueError(f"Invalid memory value: {value}")

    number = float(match.group(1))
    unit = match.group(2).upper()

    units = {
        "B": 1,
        "KB": 1000,
        "MB": 1000 ** 2,
        "GB": 1000 ** 3,
        "TB": 1000 ** 4,
        "KIB": 1024,
        "MIB": 1024 ** 2,
        "GIB": 1024 ** 3,
        "TIB": 1024 ** 4,
    }

    if unit not in units:
        raise ValueError(f"Unsupported memory unit: {unit}")

    return number * units[unit]


def escape_label(value):
    """Escape special characters for Prometheus labels."""
    return (
        str(value)
        .replace("\\", "\\\\")
        .replace("\n", "\\n")
        .replace('"', '\\"')
    )


def generate_metrics():
    containers = get_container_stats()

    metrics = [
        "# HELP docker_container_cpu_percent Container CPU usage percentage",
        "# TYPE docker_container_cpu_percent gauge",
        "# HELP docker_container_memory_usage_bytes Container memory usage in bytes",
        "# TYPE docker_container_memory_usage_bytes gauge",
        "# HELP docker_container_memory_limit_bytes Container memory limit in bytes",
        "# TYPE docker_container_memory_limit_bytes gauge",
        "# HELP docker_container_up Whether the container is running",
        "# TYPE docker_container_up gauge",
    ]

    for container in containers:
        name = escape_label(container.get("Name", "unknown"))

        cpu_value = container.get("CPUPerc", "0%")
        cpu = float(cpu_value.replace("%", "").strip())

        memory_usage, memory_limit = container["MemUsage"].split("/", 1)

        labels = f'name="{name}"'

        metrics.extend([
            f"docker_container_cpu_percent{{{labels}}} {cpu}",
            (
                f"docker_container_memory_usage_bytes{{{labels}}} "
                f"{to_bytes(memory_usage)}"
            ),
            (
                f"docker_container_memory_limit_bytes{{{labels}}} "
                f"{to_bytes(memory_limit)}"
            ),
            f"docker_container_up{{{labels}}} 1",
        ])

    return "\n".join(metrics) + "\n"


class MetricsHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"healthy\n")
            return

        if self.path != "/metrics":
            self.send_response(404)
            self.end_headers()
            return

        try:
            output = generate_metrics().encode("utf-8")

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "text/plain; version=0.0.4; charset=utf-8"
            )
            self.send_header("Content-Length", str(len(output)))
            self.end_headers()
            self.wfile.write(output)

        except Exception:
            logging.exception("Failed to generate Docker metrics")
            self.send_response(500)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Failed to generate Docker metrics\n")

    def log_message(self, format, *args):
        logging.info("%s - %s", self.address_string(), format % args)


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), MetricsHandler)

    logging.info(
        "Docker Stats Exporter running on http://%s:%s/metrics",
        HOST,
        PORT
    )

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Exporter shutting down")
    finally:
        server.server_close()
