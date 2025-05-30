import requests
import time
from datetime import datetime

# URL of the receiver microservice (Service B)
RECEIVER_URL = "http://127.0.0.1:5001/receive-data"

def send_data():
    # Simulated data payload to send
    data = {
        "source": "AdobeAnalyticsSimulator",
        "metric": "page_views",
        "value": 100,  # example metric value
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        # Make a POST request to Service B with JSON data
        response = requests.post(RECEIVER_URL, json=data)
        if response.status_code == 200:
            print("Data sent successfully:", data)
        else:
            print(f"Failed to send data. Status code: {response.status_code}")
    except Exception as e:
        print("Error sending data:", e)

if __name__ == "__main__":
    # Send data every 5 seconds (simulate queue-like behavior with polling)
    while True:
        send_data()
        time.sleep(5)  # wait before sending next data