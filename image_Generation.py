import io
from dotenv import load_dotenv
import os
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

from configuration import Dreamstudio_key
DREAMSTUDIO = Dreamstudio_key

def generate_image(text):
    from Mic_setup import say
    query=text
    query=query.replace("generate","")
    query=query.replace("image","")
    query=query.replace("of","")
    text1=(f"generating image of{query}")
    print(text1)
    say(text1)
    
    stability_api = client.StabilityInference(
        key=DREAMSTUDIO,
        verbose=True,
    )

    # the object returned is a python generator
    answers = stability_api.generate(
        prompt=text,
        seed=95456, # if provided, specifying a random seed makes results deterministic
    )

    # iterating over the generator produces the api response
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                print("WARNING: Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
                return
            elif artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.show()
    return text1
    
# query=input("input:")

