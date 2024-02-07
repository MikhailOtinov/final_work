import json


def show_all_notes(
    data_path: str,
) -> dict:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["data"]


import json

def show_one_note(
    data_path: str,
    find_by: str,
) -> dict | None:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if find_by == "id":
        id_ = input("Введите id: ")
        if id_.isdigit():
            for note in data["data"]:
                if note["id"] == int(id_):
                    return note
            # Если цикл завершился и мы здесь, значит заметка не найдена
            print("Заметка не найдена")
        else:
            print("Неверный формат id")
    elif find_by == "title":
        title_ = input("Введите title: ")
        for note in data["data"]:
            if note["title"] == title_:
                return note
        # Если цикл завершился и мы здесь, значит заметка не найдена
        print("Заметка не найдена")
    else:
        print("Неверный параметр поиска")
