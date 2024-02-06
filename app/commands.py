import json


def show_all_notes(
    data_path: str
) -> dict:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["data"]
