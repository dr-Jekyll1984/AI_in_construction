import json


def task() -> float:
    file = "input_for_task_1.json"
    with open(file) as f:
        json_data = json.load(f)

    sum_val = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_val, 3)


print(task())

