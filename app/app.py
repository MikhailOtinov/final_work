import pandas as pd
import time
import os


def chech_file(
    path: str
) -> str:
    columns = [
        "id",
        "title",
        "body",
        "create_date",
        "edit_date",
    ]
    data_path = f"{path}/notes.json"
    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.exists(data_path):
        with open(data_path, "w", encoding="utf-8"):
            pass

    return data_path


def main() -> None:
    data_path = chech_file(
        path="./final_work/data",
    )
    while True:
        command = input("command: ")
        match command:
            case "/exit":
                print("До встречи!")
                break
            case "/add":
                ...
            case "/edit":
                ...
            case "/delete":
                ...
            case "/show_all":
                ...
            case "/show_note":
                ...
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
