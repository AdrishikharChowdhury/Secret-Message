import getpass
from paragraph import encoder_paragraph, decoder_paragraph

def menu(current_message=""):
    print("\n=== Menu ===")
    print("1. Encode a paragraph")
    print("2. Decode a paragraph")
    print("3. Show the message")
    print("4. Exit")

    try:
        choice = int(input("\nEnter your option: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return False, current_message

    match choice:
        case 1:
            message = getpass.getpass("Enter the message to encode: ")
            current_message = encoder_paragraph(message)
            print("Message encoded successfully.")
        case 2:
            message = getpass.getpass("Enter the message to decode: ")
            current_message = decoder_paragraph(message)
            print("Message decoded successfully.")
        case 3:
            print(f"The current message is:\n{current_message}")
        case 4:
            print("Thank you for using this program!")
            return True, current_message
        case _:
            print("Invalid Choice!!")

    return False, current_message