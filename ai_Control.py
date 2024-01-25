
from bardapi import BardCookies 
def Powerfull_ai(query):
    
  cookie_dict={
    "__Secure-1PSID": "fAiR34Cnqx_Zm5DkGwXh7t5AElPL1uoVrJ4b3NpVz0PBY8VYm_etjp9XJyLxZ0AJKn2gCw.",
    "__Secure-1PSIDTS": "sidts-CjIBPVxjStkx3tDJmV95Vi1cYWSp0m71mpu93m6V6pvMxssl_xPiwIcHRpoZTH0ub08tRRAA",
    "__Secure-1PSIDCC": "ABTWhQFShg_4ZldPP0HRtzGSgxZ1ir4m9dUNbgQoAHSUDK8xupXnXc1Gdx_wxR_uitmxRz2OK21O"
}

  bard=BardCookies(cookie_dict=cookie_dict)

  while True:
     try:
        reply=bard.get_answer(query)['content']
        return reply
           
     except :
        print("Cookie values may have changed. Please update them.")

# query=input("input:")
# print(Powerfull_ai(query))

from openai import OpenAI
from configuration import api_key
# from Voice_Mic_setup import say
import os

chatstr=""
# this function pass query to open ai API
def chat(query): 
  global chatstr 
  # chatstr+=f"Nachiket:{query}\n Vihaan:" #this line is where we given user names
  chatstr=f"Nachiket:{query}\n Vihaan:" #this line is where we given user names
  # print(chatstr)
  Api_key = api_key
  client = OpenAI(api_key=Api_key)

  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "My name is Vihaan, created by a team led by Nachiket (team nachiket) from Amrutvahini College of Engineering. I am a virtual voice assistant, designed to provide short and fast responses. I prioritize brevity unless asked for a detailed explanation or in the case of programming questions"},
      {"role": "user", "content": chatstr}
  ]
  )

  response= (completion.choices[0].message.content)
  # print(response)
  return response




  # with open(f"Openai/{''.join(chatstr.split('intelligence')[1:]).strip()}.txt","w") as f:
  #       f.write(chatstr)



# # 
# def ai(prompt): 
#   openai.api_key =api_key
#   text=f"OpenAi response for prompt:{prompt} \n   *************************************\n \n" 
#   response = openai.Completion.create( 
#   model="gpt-3.5-turbo",  
#   prompt=prompt,
#   temperature=1,
#   max_tokens=256,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0
# ) #todo: wrap below statement in try-except may be it through a error
#   try:
#     print(response["choices"][0]["text"])
#     say(response["choices"][0]["text"])
#     text+=response["choices"][0]["text"]
#     if not os.path.exists("Openai"):
#         os.mkdir("Openai")   
  
#   except Exception:
#       print("this error is occur in ai function")

#   with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt","w") as f:
#         f.write(text)
