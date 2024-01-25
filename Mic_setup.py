import pyttsx3
import speech_recognition as sr
import time
# from googletrans import Translator



def say(text): 
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#take voice input from mic
def Take_Command(): 
     r=sr.Recognizer() 
     with sr.Microphone() as source:
       r.pause_threshold=0.5
       print("listening..")
       audio=r.listen(source,timeout=12,phrase_time_limit=8)
      
       try:
          #   say("recognizing sir ...")
          #   print("Listening......")
            r.adjust_for_ambient_noise(source, duration=1)
            query=r.recognize_google(audio,language="en-in")
            print(f"User said:{query}")
            if not query:
               query=None
       except sr.UnknownValueError:
            print("sorry i am unable to understand ")
            say("sorry i am unable to understand")

       except sr.RequestError:
            print(" sorry, i  am unable to access the speech ")
            say(" sorry, i  am unable to access the speech")
            
     return query

def listen():
    while True:
          try:
             query=Take_Command()

             if query is not None:
                  return query
          except KeyboardInterrupt:
             print("Program terminated by user.")
             break
          except Exception as e:
             print(f"An error occurred: {e}")

        # Pause for 1 second before listening again
          print("Waiting for 1 second before  listening again...")
          time.sleep(1)

# if __name__ == "__main__":
    # print(listen())
