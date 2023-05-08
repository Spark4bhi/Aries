# import the modules
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QListWidget, QListWidgetItem
import sys
import threading
import time
import webbrowser

# import functions from other python files
from events.listen import listen
from events.speak import speak
from Commands.get_weather import get_weather
from Commands.run import run_app
from Commands.search import search
from Commands.generate_text import generate_text
from Commands.open_website import open_website
from Commands.todo import add_todo, read_todo, remove_todo

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
number_words = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10
}

# the main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Aries - Your Personal Assistant")
        self.setGeometry(200, 200, 500, 400)

        self.text_label = QLabel(self)
        self.text_label.setGeometry(30, 30, 440, 100)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.text_label.setFont(font)
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setText("Say 'Help' to Get Started!")

        self.command_input = QLineEdit(self)
        self.command_input.setGeometry(30, 150, 300, 40)
        font.setPointSize(12)
        font.setBold(False)
        self.command_input.setFont(font)

        self.submit_button = QPushButton('Submit', self)
        self.submit_button.setGeometry(350, 150, 120, 40)
        self.submit_button.clicked.connect(self.submit_command)

        self.start_listening_button = QPushButton('Start Listening', self)
        self.start_listening_button.setGeometry(30, 200, 120, 40)
        self.start_listening_button.clicked.connect(self.start_listening)

        self.stop_listening_button = QPushButton('Stop Listening', self)
        self.stop_listening_button.setGeometry(170, 200, 120, 40)
        self.stop_listening_button.clicked.connect(self.stop_listening)

        self.show_chats_button = QPushButton('Show Chats', self)
        self.show_chats_button.setGeometry(310, 200, 120, 40)
        self.show_chats_button.clicked.connect(self.show_chats)

        self.chat_list_widget = QListWidget(self)
        self.chat_list_widget.setGeometry(30, 250, 440, 100)
        self.chat_list_widget.itemClicked.connect(self.select_chat)

        self.previous_chats = []

    def submit_command(self):
        command = self.command_input.text().lower()
        full_prompt = self.text_label.text() + ' ' + command
        self.previous_chats.append(full_prompt)
        self.process_command(command)

    def start_listening(self):
        self.text_label.setText("Listening...")
        self.listening_thread = threading.Thread(target=self.listen)
        self.listening_thread.start()

    def stop_listening(self):
        self.text_label.setText("Stopped Listening")
        self.listening_thread.join()

    def show_chats(self):
        self.chat_list_widget.clear()
        self.chat_list_widget.addItems(self.previous_chats)
        self.chat_list_widget.show()

    def select_chat(self, item):
        chat = item.text()
        self.command_input.setText(chat.split(' ')[-1])
        self.chat_list_widget.hide()

    def listen(self):
        while True:
            command = listen()
            self.process_command(command)

    # process the command
    def process_command(self, command):
        self.command_input.clear()
        self.text_label.setText(f"You: {command}")
        if "help" in command:
            print("Here are the commands you can use:")
            print("1. Search <query>")
            print("2. Generate text")
            print("3. Open <app name>")
            print("4. Run <website name>")
            print("5. Weather <city>")
            print("6. Add todo <todo>")
            print("7. Read todo")
            print("8. Remove todo <number>")
            print("9. Hello")
            speak("Here are the commands you can use:")
            speak("1. Search <query>")
            speak("2. Generate text")
            speak("3. Open <app name>")
            speak("4. Run <website name>")
            speak("5. Weather <city>")
            speak("6. Add todo <todo>")
            speak("7. Read todo")
            speak("8. Remove todo <number>")
            speak("9. Hello")
            self.previous_chats.append("Aries: Here are the commands you can use:")
            self.previous_chats.append("Aries: 1. Search <query>")
            self.previous_chats.append("Aries: 2. Generate text")
            self.previous_chats.append("Aries: 3. Open <app name>")
            self.previous_chats.append("Aries: 4. Run <website name>")
            self.previous_chats.append("Aries: 5. Weather <city>")
            self.previous_chats.append("Aries: 6. Add todo <todo>")
            self.previous_chats.append("Aries: 7. Read todo")
            self.previous_chats.append("Aries: 8. Remove todo <number>")
            self.previous_chats.append("Aries: 9. Hello")
        elif "search" in command:
            query = command.replace("search", "")
            print(f"Searching for {query}...")
            self.previous_chats.append(f"Aries: {query}")
            search(query)
        elif "hello" in command:
            speak("Hello, how can I assist you today?")
            self.previous_chats.append(
                "Aries: Hello, how can I assist you today?")
            print("Hello, how can I assist you today?")
        elif "weather" in command:
            city = command.replace("weather", "")
            weather = get_weather(city)
            print(weather)
            self.previous_chats.append(f"Aries: {weather}")
            speak(weather)
        elif "run" in command:
            website_name = command.replace("run", "").strip()
            link = open_website(website_name)
            print(f"Link for {website_name}: {link}")
            self.previous_chats.append(f"Aries: Link for {website_name}: {link}")
            speak(f"Here is the link for {website_name}: {link}")
            webbrowser.get(chrome_path).open(link)
        elif "open" in command:
            app_name = command.replace("open", "").strip()
            print(f"Opening {app_name}...")
            self.previous_chats.append(f"Aries: Opening {app_name}...")
            speak(f"Opening {app_name}...")
            run_app(app_name)
        elif "to do add" in command:
            task = command.replace("todo add", "").strip()
            print(f"Adding '{task}' to your todo list...")
            add_todo(task)
            speak(f"Added '{task}' to your todo list.")
            self.previous_chats.append(
                f"Aries: Added '{task}' to your todo list.")
        elif "to do read" in command:
            print("Reading todo list...")
            self.previous_chats.append("Aries: Reading todo list...")
            speak(read_todo())
        elif "to to remove" in command or "2 2 remove" in command:
            task_num_str = command.replace("to to remove", "").strip()
            task_num = number_words.get(task_num_str, None)
            if task_num is None:
                self.previous_chats.append(
                    "Aries: Sorry, I couldn't understand the task number. Please try again.")
                print("Sorry, I couldn't understand the task number. Please try again.")
            else:
                print(
                    f"Removing task number {task_num} from your todo list...")
                self.previous_chats.append(
                    f"Aries: Removing task number {task_num} from your todo list...")
                speak(remove_todo(task_num))
        elif "exit" in command:
            print("Goodbye!")
            self.previous_chats.append("Aries: Goodbye!")
            speak("Goodbye!")
            sys.exit()     
        else:
            prompt = command.replace("generate", "")
            generated_text = generate_text(prompt)
            speak(generated_text)
            self.previous_chats.append(f"Aries: {generated_text}")
            print(generated_text)

# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
