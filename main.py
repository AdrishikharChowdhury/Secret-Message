from utils import menu

def main():
    exit_program = False
    current_message = ""
    while not exit_program:
        exit_program, current_message = menu(current_message)

if __name__ == "__main__":
    main()
