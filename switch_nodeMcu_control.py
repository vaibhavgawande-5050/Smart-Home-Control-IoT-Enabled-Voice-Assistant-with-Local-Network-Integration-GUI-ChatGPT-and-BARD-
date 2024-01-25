import requests

# Update with your ESP8266 IP address
esp8266_ip = "192.168.137.13"

def control_relay(action):
    url = f"http://{esp8266_ip}/{action.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Relay  {action.capitalize()} successful")
        return (f"Relay  {action.capitalize()} successful")

    else:
        print(f"Failed to control Relay {action}")

# action="redlighton"
# action="redlightoff"
# action="greenlighton"
# action="greenlightoff"
# action="bulblighton"
# action="bulblightoff"
# query=input("give your input here:")
def keyword_patterns(query):
    if any(keyword.lower() in query.lower() for keyword in ["turn on red light", "on red light", "red light on","activate red light","Illuminate red light","Switch on red light",
    "Enable red light","Engage red light","Power up red light","Start red light","Activate the red signal","Initiate red light","red light acivate","red light illuminate","red light start"]):
        action="redlighton"
        control_relay(action)

    if any(keyword.lower() in query.lower() for keyword in  [
        "Turn off red light","Turn of red light",
        "Off red light","of red light",
        "Red light off","red light of",
        "Deactivate red light",
        "Extinguish red light",
        "Switch off red light","switch of red light",
        "Disable red light",
        "Disengage red light",
        "Power down red light",
        "Stop red light",
        "Deactivate the red signal",
        "Terminate red light",
        "Red light deactivate",
        "Red light extinguish","Red light stop"

    ]):
        action="redlightoff"
        control_relay(action)


    if any(keyword.lower() in query.lower() for keyword in[
        "Turn on bulb",
        "On bulb",
        "bulb on",
        "Activate bulb",
        "Illuminate bulb",
        "Switch on bulb",
        "Enable bulb",
        "Engage bulb",
        "Power up bulb",
        "Start bulb",
        "Activate the bulb",
        "Initiate bulb",
        "bulb acivate",
        "bulb illuminate",
        "bulb start"
    ]):
        action="bulbon"
        control_relay(action)

    if any(keyword.lower() in query.lower() for keyword in [
        "Turn off bulb","turn of bulb",
        "Off bulb","of bulb",
        "bulb off","bulb of"
        "Deactivate bulb",
        "Extinguish bulb",
        "Switch off bulb","switch of bulb"
        "Disable bulb",
        "Disengage bulb",
        "Power down bulb",
        "Stop bulb",
        "Deactivate the bulb",
        "Terminate bulb",
        "bulb deactivate",
        "bulb extinguish",
        "bulb stop"
    ]): 
        action="bulboff"
        control_relay(action)          

    if any(keyword.lower() in query.lower() for keyword in [
        "Turn on green light",
        "On green light",
        "Green light on",
        "Activate green light",
        "Illuminate green light",
        "Switch on green light",
        "Enable green light",
        "Engage green light",
        "Power up green light",
        "Start green light",
        "Activate the green signal",
        "Initiate green light",
        "Green light acivate",
        "Green light illuminate",
        "Green light start"
    ]):
        action="greenlighton"
        control_relay(action)
    if any(keyword.lower() in query.lower() for keyword in [
        "Turn off green light","turn of green light",
        "Off green light","of green light",
        "Green light off","green light of",
        "Deactivate green light",
        "Extinguish green light",
        "Switch off green light","switch of green light"
        "Disable green light",
        "Disengage green light",
        "Power down green light",
        "Stop green light",
        "Deactivate the green signal",
        "Terminate green light",
        "Green light deactivate",
        "Green light extinguish",
        "Green light stop"
    ]):
        action="greenlightoff"
        control_relay(action) 

    if any(keyword.lower() in query.lower() for keyword in [
        "Turn on all lights",
        "On all lights",
        "All lights on",
        "Activate all lights",
        "Illuminate all lights",
        "Switch on all lights",
        "Enable all lights",
        "Engage all lights",
        "Power up all lights",
        "Start all lights",
        "Activate the all signal",
        "Initiate all lights",
        "All lights activate",
        "All lights illuminate",
        "All lights start"
    ]):
        action="greenlighton"
        control_relay(action)
        action="bulblighton"
        control_relay(action)
        action="redlighton"
        control_relay(action)
                                
    # List of phrases for turning off all lights
    all_lights_phrases_stop = [
        "Turn off all lights", "turn of all lights",
        "Off all lights","of all lights",
        "All lights off","all lights of"
        "Deactivate all lights",
        "Extinguish all lights",
        "Switch off all lights","switch of all lights"
        "Disable all lights",
        "Disengage all lights",
        "Power down all lights",
        "Stop all lights",
        "Deactivate the all signal",
        "Terminate all lights",
        "All lights deactivate",
        "All lights extinguish",
        "All lights stop"
    ]

    # Check if any of the phrases for turning off all lights are present in the query
    if any(keyword.lower() in query.lower() for keyword in all_lights_phrases_stop):
        # Set actions for turning off each color light
        action_green = "greenlightoff"
        action_bulb = "bulblightoff"
        action_red = "redlightoff"
        
        # Perform actions for turning off each color light
        control_relay(action_green)
        control_relay(action_bulb)
        control_relay(action_red)

    # List of phrases for turning on all light
    all_light_phrases_on = [
        "Turn on all light",
        "On all light",
        "All light on",
        "Activate all light",
        "Illuminate all light",
        "Switch on all light",
        "Enable all light",
        "Engage all light",
        "Power up all light",
        "Start all light",
        "Activate the all signal",
        "Initiate all light",
        "All light activate",
        "All light illuminate",
        "All light start"
    ]

    # List of phrases for turning off all light
    all_light_phrases_off = [
        "Turn off all light","turn of all light",
        "Off all light","of all light",
        "All light off","all light of"
        "Deactivate all light",
        "Extinguish all light",
        "Switch off all light",
        "Disable all light",
        "Disengage all light",
        "Power down all light",
        "Stop all light",
        "Deactivate the all signal",
        "Terminate all light",
        "All light deactivate",
        "All light extinguish",
        "All light stop"
    ]

    # Check if any of the phrases for turning on all light are present in the query
    if any(keyword.lower() in query.lower() for keyword in all_light_phrases_on):
        # Set actions for turning on each color light
        action_green = "greenlighton"
        action_bulb = "bulblighton"
        action_red = "redlighton"
        
        # Perform actions for turning on each color light
        control_relay(action_green)
        control_relay(action_bulb)
        control_relay(action_red)

    # Check if any of the phrases for turning off all light are present in the query
    elif any(keyword.lower() in query.lower() for keyword in all_light_phrases_off):
        # Set actions for turning off each color light
        action_green = "greenlightoff"
        action_bulb = "bulblightoff"
        action_red = "redlightoff"
        
        # Perform actions for turning off each color light
        control_relay(action_green)
        control_relay(action_bulb)
        control_relay(action_red)


    # List of phrases for turning on any two lights in one query
    turn_on_two_lights_phrases = [
        "Turn on red and green lights","turn on green and red lights",
        "Turn on red and green light","turn on green and red light",
        "Turn on red and bulb lights","turn on bulb and red lights",
        "Turn on red and bulb light","turn on bulb and red light",
        "Turn on green and bulb lights","turn on bulb and green lights",
        "Turn on green and bulb light","turn on green and red light",
        "Turn on red and green lights","turn on green and red lights",
        "Turn on red and green light","turn on green and red light",
        "Activate bulb and red lights",
        "Switch on green and bulb lights",
        "Enable red and green lights",
        "Start bulb and green lights",
        "Illuminate red and bulb lights",
        "Engage green and red lights",
        "Power up bulb and green lights",
        "Activate the green and bulb signal",
        "Initiate red and green lights",
        "Turn on all lights",
        "Activate all the lights",
        "Switch on all lighting elements",
        "Enable all colored lights",
        "Start all signal lights"
    ]

    # Example query
    # query = "Activate bulb and red lights"

    # Check if any of the phrases for turning on any two lights are present in the query
    for keyword in turn_on_two_lights_phrases:
        if all(keyword_part.lower() in query.lower() for keyword_part in keyword.split(" and ")):
            # Set actions for turning on the corresponding lights
            actions = []
            if "red" in query.lower():
                actions.append("redlighton")
            if "green" in query.lower():
                actions.append("greenlighton")
            if "bulb" in query.lower():
                actions.append("bulblighton")
            
            # Perform actions for turning on the lights
            for action in actions:
                control_relay(action)
            break



