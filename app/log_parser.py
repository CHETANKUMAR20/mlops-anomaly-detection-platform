import pandas as pd

def parse_logs(file_path):
    data = []

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            
            cpu = int(parts[1].split("=")[1])
            mem = int(parts[2].split("=")[1])
            response = int(parts[3].split("=")[1])

            data.append([cpu, mem, response])

    df = pd.DataFrame(data, columns=["cpu", "memory", "response_time"])
    return df
