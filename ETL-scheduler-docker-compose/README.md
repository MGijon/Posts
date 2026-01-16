# ETL Orchestrator Benchmarking Project

This project aims to evaluate and compare various lightweight (and heavyweight) orchestrators to determine the best fit for an MVP transition from Docker Compose to k3s. We measure resource consumption (CPU/RAM) and observability ease for each candidate.

## 📋 Methodology

To ensure accurate results, we follow a strict "Clean Slate" protocol between tests:

* **Reset Environment**: Remove all containers, networks, and volumes.
* **Execution**: Start the specific orchestrator stack.
* **Benchmark**: Run the 5-minute resource capture script.
* **Analyze**: Review logs and generated CSV data.


```bash
# Clean slate command
docker system prune -a --volumes -f
```

## 🚀 Orchestrator Execution Matrix

| Orquestrator | Execute scheduler | Observation method | 
| :----------: | :---------------: | :----------------: | 
| Ofelia | ```docker-compose -f ofelia-test.yml up -d``` | ```docker logs -f ofelia_scheduler``` |
| Supervisord | ```docker-compose -f supervisor-test.yml up -d``` | ```docker logs -f supervisor_etl``` |
| Cronicle | ```docker-compose -f cronicle-test.yml up -d``` | Web UI at ```http://localhost:8081``` |
| Airflow | ```docker-compose -f airflow-test.yml up -d``` | Web UI at ```http://localhost:8080``` |
| Kestra | ```docker-compose -f kestra-test.yml up -d``` | Web UI at ```http://localhost:8082``` |
| Dagster | ```docker-compose -f dagster-test.yml up -d``` | Web UI at ```http://localhost:3000``` |

## 📉 Benchmarking Workflow

1. Initialize Stack
Choose an orchestrator and bring it up in detached mode.

```bash
docker-compose -f [filename].yml up -d
```

2. Run Automated Capture
Execute the benchmark script. Ensure the stack runs for at least 5 minutes to capture multiple cron fires.


```bash
chmod +x benchmark.sh
./benchmark.sh results_[orchestrator].csv
```

3. Cleanup
Bash

```bash
docker-compose -f [filename].yml down
```

## 📊 Results Summary



### Key Performance Indicators (KPIs)

Cooming soon...

* **Idle Footprint**: Critical for MVP hosting on a cheap VPS.
* **Scheduling Latency**: Time between "Cron time" and "Job start."
* **Audit Trail**: Ease of finding logs for a job that failed 10 iterations ago.