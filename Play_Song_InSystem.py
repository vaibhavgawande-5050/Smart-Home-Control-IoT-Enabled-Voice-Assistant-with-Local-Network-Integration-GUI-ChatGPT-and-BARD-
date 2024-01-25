import os
import random
def play_song(file_path): 
    if os.name == 'nt':  
        os.startfile(file_path) 
    else:  
        opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
        os.system(f'{opener} "{file_path}"')


##this function play song that is random
def play_random_song(song_list):
    random_song = random.choice(song_list)
    if os.name == 'nt':  # For Windows #os.name=='nt' check the code run on system is window or not 
        os.startfile(random_song)
    else:  # For Linux and macOS
        opener = 'open' if sys.platform == 'darwin' else 'xdg-open'
        os.system(f'{opener} "{random_song}"')
