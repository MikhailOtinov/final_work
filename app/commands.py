import json
import time
from datetime import datetime


def find_all_id_title(
    by: str,
    data_path: str,
) -> list[str]|list[int]:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    if by == "id":
        return [note["id"] for note in data["data"]]
    return [note["title"] for note in data["data"]]


def show_all_notes(
    data_path: str,
) -> dict:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["data"]


def show_one_note(
    data_path: str,
    find_by: str,
) -> dict | None:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if find_by == "id":
        ids = find_all_id_title(
            by="id",
            data_path=data_path
        )
        print(f"Существующие id: {ids}")
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
        titles = find_all_id_title(
            by="title",
            data_path=data_path
        )
        print(f"Существующие title: {titles}")
        title_ = input("Введите title: ")
        for note in data["data"]:
            if note["title"] == title_:
                return note
        # Если цикл завершился и мы здесь, значит заметка не найдена
        print("Заметка не найдена")
    else:
        print("Неверный параметр поиска")


def add_note(
    data_path: str,
) -> None:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        id_ = max([note["id"] for note in data["data"]]) + 1
        title = input("Название заметки: ")
        titles = [note["title"] for note in data["data"]]
        if title in titles:
            count_title = titles.count(title)
            title += f" ({count_title})"
        body = input("Напишите заметку: ")
        create_date = datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
        edit_date = create_date
    new_note = {
        "id": id_,
        "title": title,
        "body": body,
        "created_date": create_date,
        "edit_date": edit_date,
    }
    data["data"].append(new_note)

    with open(data_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def edit_note(
    data_path: str,
    find_by: str,
) -> None:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if find_by == "id":
        ids = find_all_id_title(
            by="id",
            data_path=data_path
        )
        print(f"Существующие id: {ids}")
        id_ = input("Введите id: ")
        if id_.isdigit():
            note_found = False
            for note in data["data"]:
                if note.get("id") == int(id_):
                    note_found = True
                    edit = input("Введите, что вы хотите редактировать (title/body): ")
                    if edit in ("title", "body"):
                        note[edit] = input("Новый текст: ")
                        note["edit_date"] = datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
                        with open(data_path, "w", encoding="utf-8") as file:
                            json.dump(data, file, ensure_ascii=False, indent=4)
                        print("Заметка отредактирована")
                        break
                    else:
                        print("Неверный параметр редактирования")
            if not note_found:
                print("Заметка не найдена")
        else:
            print("Неверный формат id")
    elif find_by == "title":
        titles = find_all_id_title(
            by="title",
            data_path=data_path
        )
        print(f"Существующие title: {titles}")
        title_ = input("Введите title: ")
        note_found = False
        for note in data["data"]:
            if note.get("title") == title_:
                note_found = True
                edit = input("Введите, что вы хотите редактировать (title/body): ")
                if edit in ("title", "body"):
                    note[edit] = input("Новый текст: ")
                    note["edit_date"] = datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
                    with open(data_path, "w", encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                    print("Заметка отредактирована")
                    break
                else:
                    print("Неверный параметр редактирования")
        if not note_found:
            print("Заметка не найдена")


def delete_note(
    data_path: str,
    find_by: str,
) -> None:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if find_by == "id":
        ids = find_all_id_title(
            by="id",
            data_path=data_path
        )
        print(f"Существующие id: {ids}")
        id_ = input("Введите id: ")
        if id_.isdigit():
            note_found = False
            for note in data["data"]:
                if note.get("id") == int(id_):
                    note_found = True
                    data["data"].remove(note)
                    with open(data_path, "w", encoding="utf-8") as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
            if not note_found:
                print("Заметка не найдена")
        else:
            print("Неверный формат id")
    elif find_by == "title":
        titles = find_all_id_title(
            by="title",
            data_path=data_path
        )
        print(f"Существующие title: {titles}")
        title_ = input("Введите title: ")
        note_found = False
        for note in data["data"]:
            if note.get("title") == title_:
                note_found = True
                data["data"].remove(note)
                with open(data_path, "w", encoding="utf-8") as file:
                    json.dump(data, file, ensure_ascii=False, indent=4)
        if not note_found:
            print("Заметка не найдена")
