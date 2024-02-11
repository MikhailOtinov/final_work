import json
import time
from datetime import datetime


def open_file(
    data_path: str,
) -> list[dict]:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data["data"]


def save_file(
    data_path: str,
    data: list[dict],
) -> None:
    data = {"data": data}
    with open(data_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def find_all_id_title(
    by: str,
    data_path: str,
) -> list[str]|list[int]:
    data = open_file(
        data_path=data_path
    )
    if by == "id":
        return [note["id"] for note in data]
    return [note["title"] for note in data]


def show_all_notes(
    data_path: str,
    by_date: bool,
) -> list[dict]:
    data = open_file(
        data_path=data_path
    )
    if by_date:
        date = input("Введите дату в формате дд.мм.гггг: ")
        data = [notes for notes in data if notes["created_date"] == date]
    return data


def show_one_note(
    data_path: str,
    find_by: str,
) -> dict | None:
    data = open_file(
        data_path=data_path
    )
    if find_by == "id":
        ids = find_all_id_title(
            by="id",
            data_path=data_path
        )
        print(f"Существующие id: {ids}")
        id_ = input("Введите id: ")
        if id_.isdigit():
            for note in data:
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
        for note in data:
            if note["title"] == title_:
                return note
        # Если цикл завершился и мы здесь, значит заметка не найдена
        print("Заметка не найдена")
    else:
        print("Неверный параметр поиска")


def add_note(
    data_path: str,
) -> None:
    data = open_file(
        data_path=data_path
    )

    id_ = max([note["id"] for note in data]) + 1
    title = input("Название заметки: ")
    titles = [note["title"] for note in data]
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
    data.append(new_note)

    save_file(
        data_path=data_path,
        data=data,
    )
    print("Заметка добавлена")


def edit_note(
    data_path: str,
    find_by: str,
) -> None:
    data = open_file(
        data_path=data_path
    )

    if find_by == "id":
        ids = find_all_id_title(
            by="id",
            data_path=data_path
        )
        print(f"Существующие id: {ids}")
        id_ = input("Введите id: ")
        if id_.isdigit():
            note_found = False
            for note in data:
                if note.get("id") == int(id_):
                    note_found = True
                    edit = input("Введите, что вы хотите редактировать (title/body): ")
                    if edit in ("title", "body"):
                        note[edit] = input("Новый текст: ")
                        note["edit_date"] = datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
                        save_file(
                            data_path=data_path,
                            data=data,
                        )
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
        for note in data:
            if note.get("title") == title_:
                note_found = True
                edit = input("Введите, что вы хотите редактировать (title/body): ")
                if edit in ("title", "body"):
                    note[edit] = input("Новый текст: ")
                    note["edit_date"] = datetime.fromtimestamp(time.time()).strftime("%d.%m.%Y")
                    save_file(
                        data_path=data_path,
                        data=data,
                    )
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
    data = open_file(
        data_path=data_path
    )

    if find_by == "id":
        ids = find_all_id_title(
            by="id",
            data_path=data_path
        )
        print(f"Существующие id: {ids}")
        id_ = input("Введите id: ")
        if id_.isdigit():
            note_found = False
            for note in data:
                if note.get("id") == int(id_):
                    note_found = True
                    data.remove(note)
                    save_file(
                        data_path=data_path,
                        data=data,
                    )
                    print("Заметка удалена")
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
        for note in data:
            if note.get("title") == title_:
                note_found = True
                data.remove(note)
                save_file(
                    data_path=data_path,
                    data=data,
                )
                print("Заметка удалена")
        if not note_found:
            print("Заметка не найдена")
