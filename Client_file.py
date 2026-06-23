
import socket
import getpass


def send_request(client, request):
    client.send(request.encode())
    response = client.recv(1024).decode()
    return response

def manage_quiz_questions():
    while True:
        print("\n--- Quiz Management ---")
        print("1. View Questions")
        print("2. Add a Question")
        print("3. Delete a Question")
        print("4. Back to Main Menu")
        choice = input("Choose an option: ")

        if choice == '1':
            with open('quiz_questions.txt', 'r') as f:
                lines = f.readlines()
                for i, line in enumerate(lines, 1):
                    print(f"{i}. {line.strip()}")
        elif choice == '2':
            question = input("Enter question: ")
            correct = input("Enter correct answer: ")
            options = input("Enter options separated by ' | ' (include the correct one): ")
            with open('quiz_questions.txt', 'a') as f:
                f.write(f"{question} ({correct}) {options}\n")
            print("Question added.")
        elif choice == '3':
            with open('quiz_questions.txt', 'r') as f:
                lines = f.readlines()
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line.strip()}")
            delete_index = int(input("Enter the number of the question to delete: ")) - 1
            if 0 <= delete_index < len(lines):
                lines.pop(delete_index)
                with open('quiz_questions.txt', 'w') as f:
                    f.writelines(lines)
                print("Question deleted.")
            else:
                print("Invalid number.")
        elif choice == '4':
            break
        else:
            print("Invalid option.")




def civil_war():
    with open('civil_war.txt', 'r') as file:
        content = file.read()
    chapters = content.split("Chapter ")
    for chapter in chapters:
        if chapter.strip():
            print(f"\nChapter {chapter.strip()}")
            input("Press Enter to continue...")



def quiz_question(client, username):
    with open('quiz_questions.txt', 'r') as file:
        lines = file.readlines()

    score = 0
    total_questions = 0
    option_labels = ['A', 'B', 'C', 'D']

    for line in lines:
        if line.strip():
            parts = line.split('(')
            if len(parts) >= 2:
                question = parts[0].strip()
                answer_part = parts[1].split(')')[0].strip()
                options_string = parts[1].split(')')[1].strip()
                options = options_string.split(' | ')
                total_questions += 1

                print(f"\n{total_questions}. {question}")
                for i, option in enumerate(options):
                    print(f"{option_labels[i]}. {option.strip()}")

                user_answer = input("Your answer (enter A, B, C, D): ").upper()

                if user_answer in option_labels[:len(options)]:
                    selected_option = options[option_labels.index(user_answer)].strip()
                    if selected_option == answer_part:
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer is: {answer_part}")
                else:
                    print("Invalid option.")

    print(f"\nYour final score: {score}/{total_questions}")


    send_request(client, f'SCORE|{username}|{score}/{total_questions}')



def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 7001))

    new_user = input("Are you a new user? (yes/no): ")
    username = ""
    role = ""

    if new_user.lower() == 'yes':
        print("Please register")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        role = input("Enter role (educator/student): ").lower()
        response = send_request(client, f'REGISTER|{username}|{password}|{role}')
        print(response)

        if "successfully" in response.lower():
            print(f"Welcome to Sierra Leone's Civil War Archive, {username}!")
        else:
            client.close()
            return

    elif new_user.lower() == 'no':
        print("Please login")
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")
        response = send_request(client, f'LOGIN|{username}|{password}')
        if "|" in response:
            message, role = response.split('|')
            print(message)
        else:
            print(response)
            client.close()
            return


    while True:
        print("\nMenu:")
        print("1. View Civil War Document")
        print("2. Take Quiz")
        if role == 'educator':
            print("3. View Students' Grades")
            print("4. Manage Quiz Questions")
            print("5. Exit")
        else:
            print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            send_request(client, f'CIVILWAR|{username}')
            civil_war()
        elif choice == '2':
            send_request(client, f'QUIZ|{username}')
            quiz_question(client, username)
        elif choice == '3' and role == 'educator':
            grades = send_request(client, f'VIEW_GRADES|{username}')
            print("\n--- Student Grades ---\n")
            print(grades)

        elif choice == '4' and role == 'educator':
            manage_quiz_questions()

        elif (choice == '5' and role != 'educator') or (choice == '5' and role == 'educator'):
            print("Exiting...")
            client.close()
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
