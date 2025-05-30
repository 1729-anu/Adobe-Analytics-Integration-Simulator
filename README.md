# Adobe Analytics Style Data Integration Simulator

## Overview
This project simulates a simplified data integration between two microservices, inspired by Adobe Analytics and AdCloud integration.

- **Service A**: Simulates Adobe Analytics, sending metric data periodically via REST API.
- **Service B**: Simulates AdCloud, receiving and storing the data in an SQLite database.

## Tech Stack
- Python 3
- Flask (for REST API server)
- Requests (for HTTP client)
- SQLite (local database)

## How to Run

1. Clone the repository.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the receiver service (Service B):

```bash
python service_b.py
```

4. In a new terminal, start the sender service (Service A):

```bash
python service_a.py
```

5. Service A will send data every 5 seconds to Service B, which stores it in `analytics_data.db`.

## Verify Data
You can inspect the SQLite database using any SQLite viewer or CLI tool:

```bash
sqlite3 analytics_data.db
sqlite> SELECT * FROM logs;
```

## Notes
- This is a basic simulator to demonstrate REST API data exchange, error handling, and persistence.
- The services run locally; in a real scenario, they would be deployed on different servers or containers.
