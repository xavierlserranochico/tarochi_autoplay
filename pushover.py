from config import *
import requests
import time


@staticmethod
def send_message(message, url, priority=1, ttl=86400, sound="incoming"):
    try:
       # Prepare data for the POST request
        data = {
            "token": TOKEN,
            "user": USER,
            "priority": priority,   
            "message": message,
            "url": url,
            "ttl": ttl,
            "sound": sound
        }

        # Send request to Pushover API
        response = requests.post(PUSHOVER_URL, data=data)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Optionally, print the response content
            # print(response.text)
            return   
        else:
            # Print a message if the request was unsuccessful
            print(f"Failed to send message. Status code: {response.status_code}")
            requests.post(PUSHOVER_URL, data=ERROR_MESSAGE)
            pass
    except requests.exceptions.RequestException as e:
        # Print an error message if an exception occurs during the request
        requests.post(PUSHOVER_URL, data=ERROR_MESSAGE)
        print(f"An error occurred sending Message: {e}")   