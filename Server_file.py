

import socket
import threading
from datetime import datetime

def encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char
    return encrypted

def decrypt(text, shift):
    return encrypt(text, -shift)

user_credentials = {}


try:
    with open('user_credentials.txt', 'r') as f:
        for line in f:
            if line.strip() and ':' in line:
                parts = line.strip().split(':')
                if len(parts) == 3:
                    username, password, role = parts
                    user_credentials[username] = {'password': password, 'role': role}
except FileNotFoundError:
    pass

def register_user(username, password, role):
    encrypted_password = encrypt(password, 3)
    user_credentials[username] = {'password': encrypted_password, 'role': role}
    with open('user_credentials.txt', 'a') as f:
        f.write(f"{username}:{encrypted_password}:{role}\n")
    log_activity(username, "Registered")

def authenticate_user(username, password):
    if username in user_credentials:
        encrypted_password = user_credentials[username]['password']
        if encrypted_password == encrypt(password, 3):
            log_activity(username, "Authenticated")
            return user_credentials[username]['role']
    return None

def log_activity(username, action):
    with open('activity_log.txt', 'a') as f:
        f.write(f"{datetime.now()}: {username} - {action}\n")


def save_quiz_score(username, score_text):
    with open('quiz_scores.txt', 'a') as f:
        f.write(f"{username}:{score_text}\n")
    log_activity(username, f"Completed quiz - Score: {score_text}")


def get_all_scores():
    try:
        with open('quiz_scores.txt', 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "No quiz scores recorded yet."

def handle_client(client_socket):
    try:
        while True:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            parts = data.split('|')
            action = parts[0].strip()

            if action == 'REGISTER' and len(parts) == 4:
                username, password, role = parts[1], parts[2], parts[3]
                register_user(username, password, role)
                client_socket.send(b"User registered successfully.")

            elif action == 'LOGIN' and len(parts) == 3:
                username, password = parts[1], parts[2]
                user_role = authenticate_user(username, password)
                if user_role:
                    client_socket.send(f"Welcome back, {username}!|{user_role}".encode('utf-8'))
                else:
                    client_socket.send(b"Authentication failed.")

            elif action == 'CIVILWAR' and len(parts) == 2:
                username = parts[1]
                log_activity(username, "Viewed Civil War Document")
                client_socket.send(b"Activity logged: Viewed Civil War Document")

            elif action == 'QUIZ' and len(parts) == 2:
                username = parts[1]
                log_activity(username, "Started Quiz")
                client_socket.send(b"Activity logged: Started Quiz")

            elif action == 'SCORE' and len(parts) == 3:
                username, score = parts[1], parts[2]
                save_quiz_score(username, score)
                client_socket.send(b"Score saved successfully.")

            elif action == 'VIEW_GRADES' and len(parts) == 2:
                username = parts[1]
                if user_credentials[username]['role'] == 'educator':
                    scores = get_all_scores()
                    client_socket.send(scores.encode())
                else:
                    client_socket.send(b"Unauthorized. Only educators can view grades.")

            else:
                client_socket.send(b"Invalid action or parameters.")
    except Exception as e:
        print("Error handling client:", e)
    finally:
        client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('localhost', 7001))
    server.listen()
    print("Server is running and waiting for connections...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connected to {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    main()
