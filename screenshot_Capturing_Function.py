import os
from PIL import ImageGrab
from datetime import datetime

def take_screenshot():
    directory="screenshots"
    file_prefix="Screenshot_capture"
    # Get the current directory where the script is located
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the directory
    directory_path = os.path.join(current_directory, directory)

    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    # Generate a unique filename using a timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{file_prefix}_{timestamp}.png"

    # Construct the full path to the file
    file_path = os.path.join(directory_path, file_name)

    # Capture screenshot
    screenshot = ImageGrab.grab()

    # Save the screenshot to the specified file
    screenshot.save(file_path, "PNG")

    print(f"Screenshot saved to {file_path}")

# Check if the script is being run directly

# 