import datetime
from tmdb_Movie_Series import *
from my_Speedtest import *
from gmail import *
from open_Apps import *
# from open_Apps import open_application
from Mic_setup import listen ,say
from ai_Control import *
from system_Control import *
win_ops=WindowOpt()
sys_ops=SystemTasks()
tab_ops=TabOpt()
from screenshot_Capturing_Function import take_screenshot
from browser_Control import *
from button_GUI_For_Nodemcu import Gui_call





print("Vihaan:a intelligent Assistant.......")

def main_function(query):
 if __name__ == '__main__':

        print("*******X*************X*******************X**************X********")
        # while True:
        
        # print("listening....")
        
        # say("I am listening")   #uncommnet it later on
        # query=Take_Command()
        # query=input("give your input here: ")
        keywords = ["song", "music", "play song", "play music", "open youtube", "youtube"]
        formatted_query = query.lower().strip().replace(" ", "")
        
        
        weather_keywords = ["weather", "temperature", "rain", "humidity", "forecast", "wind speed", "UV index", "air quality", "atmospheric pressure"]
        formatted_query1 = query.lower().strip().replace(" ", "")

        site_Call(query)
        print(query)


        if any(keyword.lower() in query.lower() for keyword in ["stop", "exit","break","quite"]):
            import sys
            print("closing my prompt......")
            say("closing my prompt......")
            sys.exit()
        elif any(keyword.lower() in query.lower() for keyword in ["open youtube","youtube open"]):
            webbrowser.open("https://www.youtube.com/")
            
        elif any(keyword in formatted_query for keyword in keywords):
              from youtube_Control import Youtube_call
              print("opening youtube....")
              Youtube_call(query)
              return "opening youtube"


        elif any(keyword in formatted_query1 for keyword in weather_keywords):
            from ai_Control import Powerfull_ai
            reply=Powerfull_ai(query)
            print(reply)
            return (reply)
            

        elif "date" in query.lower():
               current_date = datetime.date.today()
               print("today date is "+str(current_date))
               return ("today date is "+str(current_date))
        elif "time" in query.lower():
                # Get the current time
                current_time = datetime.datetime.now()

                # Format the time to display only the hour and minute
                time_str1 = current_time.strftime("%I ")
                time_str2 = current_time.strftime("%M")
                print(f"current time is {time_str1} hour and {time_str2} minute")
                return (f"current time is {time_str1} hour and {time_str2} minute")
                # Print the formatted time
                # print(f"current time is {time_str1} hour and {time_str2} minute")
        elif "firefox" in query.lower():
            say("opening firefox as per your request......")
            application_path =r"C:\Program Files\Mozilla Firefox\firefox.exe"
            open_application(application_path)
            return "opening firefox as per your request"
        elif "open brave" in query.lower():
            say("opening brave browser  for you sir......")
            # application_path =r"C:\ProgramFiles\BraveSoftware\Brave-Browser\Application\brave.exe"
            application_path=r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
            open_application(application_path)
            return " opening brave browser..."
    
        elif "visual studio".strip() in query.lower() or "vs code".strip() in query.lower():
            say("Opening Visual Studio Code for you, sir...")
            application_path = r"C:\Users\vaibh\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            open_application(application_path)
            return " opening vs code "

        elif "vmware" in query.lower():
            say("opening vmware for you sir......")
            application_path =r"C:\Program Files (x86)\VMware\VMware Workstation\vmware.exe"
            open_application(application_path)
            return " opening vmware "
      
        elif "microsoftedge" in query.lower():
            say("opening microsoftegde ......")
            application_path =r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
            open_application(application_path)
            return "opening microdoft edge "
        elif "chrome" in query.lower():
            say("opening crome ......")
            application_path =r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            open_application(application_path)
            return "opening crome "
        elif "vlc" in query.lower():
            say("opening vlc ......")
            application_path =r"C:\Program Files\VideoLAN\VLC\vlc.exe"
            open_application(application_path)
            return "opening vlc "
        # elif "reset".lower() in query.lower():
            # chatstr=" "
        # elif "ok vihaan".lower() in query.lower():
        #     from ai_Control import ai
        #     output=ai(prompt=query)
        #     print(output)
        #     return output
        elif "wikipedia".lower() in query.lower():
            result=Search_Wiki(query)
            print(result)
            return (result)
            # say(result)
        elif any(keyword.lower() in query.lower() for keyword in ["map", "distance", "how to go"]):
          get_map(query)
          return "opening map"
        elif "google".lower() in query.lower():
              google_search(query)
              return "opening google "
        elif any(keyword.lower() in query.lower() for keyword in ["movie", "movies", "film","films"]):
           response=get_popular_movies()
           if isinstance(response, str):
                lines = response.split('\n')[:3]
                print('\n'.join(lines))
                return ('\n'.join(lines))
           else:
                print("Response is not a string. Unable to extract lines.")          
                return ("Response is not a string. Unable to extract lines.")          
        elif any(keyword.lower() in query.lower() for keyword in ["series", "tv series"]):
           response=get_popular_tvseries()
           print(response)
           return response
        elif any(keyword.lower() in query.lower() for keyword in ["speedtest", "check speed","speed"]):
            from my_Speedtest import get_speedtest
            print ("speedtest usually take time,please wait little")
            say("speedtest usually take time,please wait little")
            print("processing...")
            response=get_speedtest()
            print(response)
            return (response)
            # say(response)
        elif any(keyword.lower() in query.lower() for keyword in ["gmail", "mail","email"]):
            say("Type the receiver id : ")
            receiver_id = input()
            while not check_email(receiver_id):
                say("Invalid email id\nType reciever id again : ")
                receiver_id = input()
            # say("Tell the subject of email")
            say("Tell the subject of email")
            # subject = record()
            subject = input("sub=")
            say("tell the body of email")
            # body = record()
            body = input("body=")
            success = send_email(receiver_id, subject, body)
            if success:
                say('Email sent successfully')
            else:
                say("Error occurred while sending email")
            done = True
        elif any(keyword.lower() in query.lower() for keyword in ["gui","button","buttons","graphical user interface"]):
             print("opening gui for light control.......")
             say("opening gui for light control.......")
             Gui_call()
             return "opening gui for light control"
        elif any(keyword.lower() in query.lower() for keyword in ["switch", "lights","light","turn on","turn of","turn off"]):
             print("working with lights")
             from switch_nodeMcu_control import keyword_patterns 
             keyword_patterns(query) #update ip
             return "IOT Function Activated"

        elif any(keyword.lower() in query.lower() for keyword in ["image generate", "generate image","generate","generator","generat"]):
              from image_Generation import generate_image
              text1=("Image generation is lengty process it took some time ,wait just a bit ...")
              print(text1)
              say(text1)
              text1=generate_image(query)
              return text1
        elif any(keyword.lower() in query.lower() for keyword in ["get system stats", "system info","system stat","system statistics","system statistic","system information","system stat","system"]):
            from system_Control import get_Call
            print(print("getting system stats and system info.."))
            info1,info2=get_Call()
            return info1, info2
        elif any(keyword.lower() in query.lower() for keyword in ["open app", "open apps"]):
            from open_Apps import open_app
            completed = open_app(query)
            if completed:
                done = True
        elif any(keyword.lower() in query.lower() for keyword in ["note", "notes"]):
            say("what would you like to take down?")
            note = listen()
            take_note(note)
            done = True
        elif any(keyword.lower() in query.lower() for keyword in [ "select"]):
            sys_ops.select()
            done=True
        elif "copy".lower() in query.lower():
            sys_ops.copy()
            done = True
        elif "paste".lower() in query.lower():
            sys_ops.paste()
            done = True
        elif "delete".lower() in query.lower():
            sys_ops.delete()
            done = True
        elif "new".lower() in query.lower() in query:
            sys_ops.new_file()
            done = True
        elif  "switch".lower() in query and "tab".lower() in query.lower():
            tab_ops.switchTab()
            done = True
        elif  "close".lower() in query.lower() and "tab" in query.lower():
            tab_ops.closeTab()
            done = True
        elif "new" in query.lower() and "tab".lower() in query:
            tab_ops.newTab()
            done = True       
        elif "close" in query.lower():
            win_ops.closeWindow()
            done = True
        elif "switch" in query.lower():
            win_ops.switchWindow()
            done = True
        elif "minimize" in query.lower():
            win_ops.minimizeWindow()
            done = True
        elif "maximize" in query.lower():
            win_ops.maximizeWindow()
            done = True
        elif "screenshot" in query.lower() or "screenshots" in query.lower():
             take_screenshot()
             return "screenshot capture and store in screenshot directory"
        elif "ip" in query.lower():
              ip = get_ip()
              if ip:
                print(ip)
                say(ip)
                return ip
        elif any(keyword.lower() in query.lower() for keyword in ["tell me","how","who","where","why","what","hey ai","ai"," ai ","ai "," ai","artificial","inteligence","intelligence"]):
          say("wait just a little bit i am thinking")
          response=chat(query)
          print(response)
          return response
        elif any(keyword.lower() in query.lower() for keyword in ["hi","helo","hello","bihar","bihan","banke","bihari","banake","how are you","ok vihaan","ok vihan","vihaan","vihan"]):
          say("wait just a little bit i am thinking")
          response=chat(query)
          print(response)
          return response
        

import tkinter as tk
from tkinter import PhotoImage, Text, Entry, Button
from PIL import Image, ImageTk  # Import Pillow library for PNG image handling

# from vihaan_backend1 import *

root = tk.Tk()
root.title("Vihaan: A Voice-Assistant")
root.iconbitmap(r'modules\vihaan.ico')
root.configure(highlightbackground="black", highlightthickness=5)
# Set window size to full screen
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()
root.geometry(f"{window_width}x{window_height}+0+0")
# Background Image
# bg_image = PhotoImage(file=r"modules\output.gif")
bg_image = PhotoImage(file=r"C:\Users\vaibh\OneDrive\Desktop\images\background.gif")
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Header Label
label = tk.Label(root, text="VihaaN GUI", font=("Helvetica", 16, "bold"), bg="white")
# label.pack(fill=tk.BOTH, expand=True)
# label.pack(relx=0.6)
label.place(relx=0.16, rely=0.04, anchor="center")


label_width = label.winfo_reqwidth()
window_width = label_width + 20
x = (root.winfo_screenwidth() - window_width) // 2
y = 10
label.place(x=x, y=y)

# Mic Button
mic_image = PhotoImage(file=r"C:\Users\vaibh\OneDrive\Desktop\images\mic.gif")
listening = False

# def start_voice_assistant():
#     global listening
#     text = f"Vihaan:-- Listening..\n"
#     update_output(text)
#     if not listening:
#         listening = True
#         dialogue_label.config(text="Listening...")
#         # Additional code for voice assistant functionality can be added here
     
#         query=Take_Command()
#         output=main_function(query)
#         text1 = f"User:--  {query}\n"
#         text2 = f"Vihaan:--  {output}\n"

#         # Update the output in the Text widget
#         update_output(text1)
#         update_output(text2)
#         update_output("\n")
#         print(text1)
#         print(text2)
#         print()

#     else:
#         # listening = False
#         dialogue_label.config(text="")
# Dialogue Label

is_listening=False
def start_voice_assistant():
    global is_listening
    if not is_listening:
        
        is_listening = True
        # Additional code for voice assistant functionality can be added here
        update_output("Vihaan:Listening.....\n")
        root.update_idletasks()
        dialogue_label.config(text="Listening...", fg="red")
        root.update_idletasks()  
        say("I am listening")
        print()
        root.update_idletasks()  
        query = listen()
        dialogue_label.config(text="", fg="white")
        root.update_idletasks()  
        update_output("Vihaan:Processing your input\n\n")
        root.update_idletasks()  
        say("Processing your input")
        print()
        root.update_idletasks()  
        output = main_function(query)

        user_text = f"User:--  {query}\n"
        vihaan_text = f"Vihaan:--  {output}\n"

        # Update the output in the Text widget
        update_output(user_text)
        root.update_idletasks()  
        update_output(vihaan_text)
        root.update_idletasks()  
        update_output("\n")
        root.update_idletasks()  
        print(user_text)
        print(vihaan_text)
        say(output)
    else:
        # Provide feedback to the user if attempting to start listening while already listening
        is_listening = False
        label.config(text="")
        root.update_idletasks()
        

    # Reset the listening status after processing the command
    # listening = False
    # dialogue_label.config(text="")

button = tk.Button(root, image=mic_image, command=start_voice_assistant, borderwidth=0)
button.place(relx=0.62, rely=0.30, anchor="center")

# Dialogue Label
dialogue_label = tk.Label(root, text="", font=("Arial", 14), borderwidth=1, fg="black")
dialogue_label.place(relx=0.62, rely=0.37, anchor="center")

# User Input Entry
entry = Entry(root, width=60, font=("Arial", 14), bd=3, relief="solid")
entry.place(relx=0.64, rely=0.5, anchor="center", relwidth=0.65)


# Submit Button
def input_info(event=None):
    query = entry.get().strip()  # Get the input and remove leading/trailing whitespaces
    if query:  # Check if the input is not empty
        # entry.config(bg="yellow")
        # output=main_function(query)
        text1 = f"User:--  {query}\n"
        update_output(text1)
        root.update_idletasks()  
        update_output("Vihaan:Processing your input\n\n")
        root.update_idletasks()  
        say("Processing your input")
        print()
        print(query)
        output=main_function(query)
        print(output)
        # Additional code for processing user input and generating output
        openai_output = "hello this is output from open ai"
        text2 = f"Vihaan:--  {output}\n"

        # Update the output in the Text widget
        update_output(text2)
        root.update_idletasks()  

        update_output("\n")
        print(text1)
        print(text2)
        say(output)
        root.update_idletasks()  
        print()

        # Clear the input box
        entry.delete(0, 'end')

        # Clear the "Input is empty!" message if it was displayed
        # dialogue_label.config(text="")
    else:
        # Display feedback when the input is empty
        # dialogue_label.config(text="Input is empty!")
        pass

# ...


submit_button = Button(root, text="Submit", command=input_info, width=20, bd=3, height=2, relief="solid", activebackground="red", activeforeground="white")
submit_button.place(relx=0.62, rely=0.57, anchor="center")

# Bind the <Return> key to the input_info function

entry.bind("<Return>", input_info)

# Output Text Widget   
output_text = Text(root, bg="black", fg="white", font=("Arial", 14), wrap="word")
output_text.place(relx=0.32, rely=0.62, relwidth=0.65, relheight=0.32)


exit_image = Image.open(r"C:\Users\vaibh\OneDrive\Desktop\images\EXITupdated.gif")
exit_image = exit_image.resize((120, 70), Image.LANCZOS)
exit_image = ImageTk.PhotoImage(exit_image)

def exit_program():
    root.destroy()

exit_button = Button(root, image=exit_image, command=exit_program, borderwidth=0,bd=2 ,bg="black", relief="solid")
exit_button.place(relx=0.93, rely=0.125, anchor="center")

# Stop Button (Same Size as Exit Button)
stop_image = Image.open(r"C:\Users\vaibh\OneDrive\Desktop\images\stopupdated1.gif")
stop_image = stop_image.resize((120, 70), Image.LANCZOS)
stop_image = ImageTk.PhotoImage(stop_image)

def stop_listening():
    global listening
    listening = False
    # dialogue_label.config(text="Listening stopped...")

stop_button = Button(root, image=stop_image, command=stop_listening, borderwidth=0,bd=2,bg="black", relief="solid")
stop_button.place(relx=0.93, rely=0.275, anchor="center")

# Clear Button
clear_image = Image.open(r"C:\Users\vaibh\OneDrive\Desktop\images\clearupdated.gif")  # Replace with the actual image for the clear button
clear_image = clear_image.resize((120, 70), Image.LANCZOS)
clear_image = ImageTk.PhotoImage(clear_image)

def clear_output():
    output_text.delete("1.0", tk.END)

clear_button = Button(root, image=clear_image, command=clear_output, borderwidth=0, bd=2, bg="black", relief="solid")
clear_button.place(relx=0.93, rely=0.425, anchor="center")


def update_output(output):
    output_text.insert("end",output)
    
    
    # Scroll to the end of the Text widget
    output_text.yview(tk.END)

def auto_trigger():
    say("welcome to vihhan world")

# Create the button
button = tk.Button(root, text="Auto Trigger Button", command=auto_trigger)


# Schedule the auto_trigger function to be called after 3000 milliseconds (3 seconds)
root.after(1000, auto_trigger)

root.mainloop()

