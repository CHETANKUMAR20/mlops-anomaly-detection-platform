import random
import time
import requests

API_URL = "http://127.0.0.1:8000/predict"

def generate_log():

    # 80% normal traffic
    if random.random() < 0.8:
        cpu = random.randint(25, 40)
        memory = random.randint(35, 50)
        response_time = random.randint(90, 150)
    else:
        # 20% anomaly spike
        cpu = random.randint(80, 100)
        memory = random.randint(85, 100)
        response_time = random.randint(700, 1200)

    return {
        "cpu": cpu,
        "memory": memory,
        "response_time": response_time
    }

def send_log():

    while True:
        log = generate_log()

        try:
            response = requests.post(API_URL, json=log)
            print(f"Sent: {log} | Result: {response.json()['prediction']}")
        except Exception as e:
            print("Error sending log:", e)

        time.sleep(2)

if __name__ == "__main__":
    send_log()
