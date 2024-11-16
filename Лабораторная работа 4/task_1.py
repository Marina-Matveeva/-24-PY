# TODO решите задачу
import json

FILENAME = "input.json"

def task() -> float:
    with open(FILENAME) as f:
        json_data = json.load(f)
    list_value = [item["score"]*item["weight"] for item in json_data]
    return round(sum(list_value), 3)

if __name__ == "__main__":
    print(task())