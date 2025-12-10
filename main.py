def process_git_status():
    try:
        user_input = input("Введіть число (0, 1, 2) для визначення статусу Git: ")
        status_code = int(user_input)

        match status_code:
            case 0:
                print("Git Correct")
            case 1:
                print("Git Error")
            case 2:
                print("Git Exception")
            case _:
                print("Git in Test")

    except ValueError:
        print("Git Exception")

if __name__ == "__main__":
    process_git_status()