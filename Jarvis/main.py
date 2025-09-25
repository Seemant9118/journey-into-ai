from listen_for_wake_word_fn import listen_for_wake_word
from speak_fn import speak
from listen_for_cmd_fn import listen_for_command
from handling_cmd_fn import handle_command

if __name__ == "__main__":
    print("Initializing Jarvis...")
    if listen_for_wake_word():
        while True:
            command = listen_for_command()
            handle_command(command)