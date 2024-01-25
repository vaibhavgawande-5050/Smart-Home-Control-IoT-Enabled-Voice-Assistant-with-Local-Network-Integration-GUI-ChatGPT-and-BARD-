import tkinter as tk
import requests

esp8266_ip = "192.168.137.13"

def control_relay(action):
    url = f"http://{esp8266_ip}/{action.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Relay {action.capitalize()} successful")
    else:
        print(f"Failed to control Relay {action}")


def create_button(frame, action, label):
    button = tk.Button(frame, text=label, command=lambda: control_relay(action))
    button.pack(side=tk.LEFT, padx=5)


def exit_program(root):
    root.destroy()


def Gui_call():
    root = tk.Tk()
    root.title("Light Controls")

    frame_red = tk.Frame(root)
    frame_red.pack(pady=10)
    create_button(frame_red, "redlighton", "Red Light On")
    create_button(frame_red, "redlightoff", "Red Light Off")

    frame_green = tk.Frame(root)
    frame_green.pack(pady=10)
    create_button(frame_green, "greenlighton", "Green Light On")
    create_button(frame_green, "greenlightoff", "Green Light Off")

    frame_yellow = tk.Frame(root)
    frame_yellow.pack(pady=10)
    create_button(frame_yellow, "bulbon", "bulb On")
    create_button(frame_yellow, "bulboff", "bulb off")

    exit_button = tk.Button(root, text="Exit", command=lambda: exit_program(root))
    exit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    Gui_call()
    