from typing import Any, Callable, Sequence

type Data = dict[str, Sequence[Any]]
type Preprocessor = Callable[[Data], Data]
type Tasks = dict[str, Preprocessor]


def process_data(preprocessors: Tasks, data: Data) -> Data:
    # preprocessors is a dict like {task_name: task_fn}
    for task_name, task_fn in preprocessors.items():
        print(f"Executing {task_name}")
        data = task_fn(data)
    return data


def uppercase_keys(dictionary: Data) -> Data:
    return {key.upper(): value for key, value in dictionary.items()}


def remove_long_values(dictionary: Data) -> Data:
    return {key: value for key, value in dictionary.items() if len(value) <= 5}


data: Data = {
    "india": [32, 12, 11, 20, 45, 12, 45],
    "spain": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "bolivia": [0, -1, 2],
}

tasks: Tasks = {"uppercase": uppercase_keys, "remove long": remove_long_values}

processed_data: Data = process_data(tasks, data)
print(processed_data)
