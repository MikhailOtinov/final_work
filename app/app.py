def main() -> None:
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
            case "/show":
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
- Если хотите посмотреть все заметки, введите /show
- Если хотите посмотреть заметку, введите /show_note''')
    main()
