def process_data(preprocessors, data):
    # preprocessors is a dict like {task_name: task_fn}
    for task_name, task_fn in preprocessors.items():
        print(f"Executing {task_name}")
        data = task_fn(data)
    return data


def uppercase_keys(dictionary):
    return {key.upper(): value for key, value in dictionary.items()}


def remove_long_values(dictionary):
    return {key: value for key, value in dictionary.items() if len(value) <= 5}


data = {
    "india": [32, 12, 11, 20, 45, 12, 45],
    "spain": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "bolivia": [0, -1, 2],
}

tasks = {"uppercase": uppercase_keys, "remove long": remove_long_values}

processed_data = process_data(tasks, data)
print(processed_data)
