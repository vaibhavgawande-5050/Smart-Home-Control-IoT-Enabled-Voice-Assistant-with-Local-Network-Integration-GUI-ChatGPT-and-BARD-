import subprocess
import AppOpener
import time
from random import randint



def open_application(application_path): 
            try:
                subprocess.Popen(application_path)
                print(f"Successfully opened {application_path}")
            except FileNotFoundError:
                print(f"Application not found at {application_path}")
            except Exception as e:
                print(f"Error occurred: {str(e)}")




def app_path(app):
    app_paths = {'access': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\ACCICONS.exe',
                 'powerpoint': r'C:\Program Files\Microsoft Office\root\Office16',
                 'word': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.exe',
                 'excel': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.exe',
                 'outlook': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\OUTLOOK.exe',
                 'onenote': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\ONENOTE.exe',
                 'publisher': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\MSPUB.exe',
                 'sharepoint': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\GROOVE.exe',
                 'infopath designer': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\INFOPATH.exe',
                 'infopath filler': 'C:\\Program Files (x86)\\Microsoft Office\\Office14\\INFOPATH.exe'}
    try:
        return app_paths[app]
    except KeyError:
        return None


def open_app(query):
    ms_office = ('access', 'powerpoint', 'word', 'excel', 'outlook', 'onenote', 'publisher', 'sharepoint', 'infopath designer',
                 'infopath filler')
    for app in ms_office:
        if app in query:
            path = app_path(app)
            subprocess.Popen(path)
            return True
    AppOpener.run(query[5:])
    return True

from system_Control import SystemTasks

def take_note(note):
    open_app("open notepad")
    time.sleep(0.2)
    sys_task = SystemTasks()
    sys_task.write(note)
    sys_task.save(f'note_{randint(1, 100)}')