import pandas as pd
import time
import os, json

from commands import (
    show_all_notes,
    show_one_note,
    add_note,
    edit_note,
    delete_note,
)


def check_file(
    path: str
) -> None:
    dirname = os.path.dirname(path)
    if not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(
                {"data": []},
                json_file,
                ensure_ascii=False,
                indent=4
            )


def renumber_ids(
    data_path: str,
) -> None:
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    for index, item in enumerate(data["data"], start=1):
        item["id"] = index
    with open(data_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def output_note_text(
    note: dict,
) -> None:
    id_ = note["id"]
    title = note["title"]
    body = note["body"]
    create_date = note["created_date"]
    edit_date = note["edit_date"]

    print(f"{id_}. {title}")
    print(f"Заметка была создана {create_date} числа.")
    print(f"Последнее редактирование {edit_date} числа.\n")
    print(body)
    print("\n\n\n")


def main() -> None:
    main_path = "./app/data/notes.json"

    check_file(
        path=main_path,
    )

    while True:
        renumber_ids(
            data_path=main_path
        )
        command = input("command: ")
        match command:
            case "/exit":
                print("До встречи!")
                break
            case "/add":
                add_note(
                    data_path=main_path,
                )
                print("Новая заметка добавлена!")
            case "/edit":
                print("Введите через что вы хотите найти заметку для редактирования (exit - отмена): id/title")
                while True:
                    find_by = input("По ")
                    if find_by in ("id", "title", "exit"):
                        note = edit_note(
                            data_path=main_path,
                            find_by=find_by,
                        )
                        break
                    else:
                        print("Вы возможно ошиблись с командой")
            case "/delete":
                print("Введите через что вы хотите удалить заметку (exit - отмена): id/title")
                while True:
                    find_by = input("По ")
                    if find_by in ("id", "title", "exit"):
                        delete_note(
                            data_path=main_path,
                            find_by=find_by,
                        )
                        break
                    else:
                        print("Вы возможно ошиблись с командой")
            case "/show_all":
                notes = show_all_notes(
                    data_path=main_path
                )
                if len(notes) != 0:
                    for note in notes:
                        output_note_text(
                            note=note
                        )
                else:
                    print("Пока что нет заметок")
            case "/show_note":
                print("Введите через что вы хотите найти заметку (exit - отмена): id/title")
                while True:
                    find_by = input("По ")
                    if find_by in ("id", "title", "exit"):
                        note = show_one_note(
                            data_path=main_path,
                            find_by=find_by,
                        )
                        if note is not None:
                            output_note_text(
                                note=note,
                            )
                            break
                    else:
                        print("Вы возможно ошиблись с командой")
            case _:
                print("Вы ввели не существующую комманду!")

if __name__ == "__main__":
    print(
'''Добро пожаловать в "Мои заметки"
- Если хотите выйти, введите /exit
- Если хотите добавить заметку, введите /add
- Если хотите редактировать заметку, введите /edit
- Если хотите удалить заметку, введите /delete
- Если хотите посмотреть все заметки, введите /show_all
- Если хотите посмотреть заметку, введите /show_note''')
    main()
