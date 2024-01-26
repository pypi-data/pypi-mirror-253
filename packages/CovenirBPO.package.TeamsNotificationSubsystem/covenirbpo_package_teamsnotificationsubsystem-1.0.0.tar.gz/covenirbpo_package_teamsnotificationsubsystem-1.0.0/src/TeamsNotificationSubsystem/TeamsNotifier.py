from os import environ
import requests
import json
import os
class TeamsNotifier:
    def __init__(self):
        self.webhook_url = environ.get('TEAMS_WEBHOOK')
        self.resources_folder = os.path.join(os.path.dirname(__file__), 'Resources')
        

    def check_environment(self):
        if self.webhook_url is None or self.webhook_url == "":
            raise Exception("TEAMS_WEBHOOK environment variable not set")


    def send_error_message(self, title, message):
        self.check_environment()

        # Load ErrorCard.json from Resources folder
        resource = os.path.join(self.resources_folder, 'ErrorCard.json')
        with open(resource, 'r') as file:
            error_card = json.load(file)

        # Customize the error card payload
        error_card['attachments'][0]['content']['body'][0]['text'] = title
        error_card['attachments'][0]['content']['body'][1]['text'] = message

        # Send the Teams notification
        payload = error_card
        response = requests.post(self.webhook_url, json=payload)
        response.raise_for_status()


    def send_warning_message(self, title, message):
        self.check_environment()

        # Load ErrorCard.json from Resources folder
        resource = os.path.join(self.resources_folder, 'WarningCard.json')
        with open(resource, 'r') as file:
            error_card = json.load(file)

        # Customize the error card payload
        error_card['attachments'][0]['content']['body'][0]['text'] = title
        error_card['attachments'][0]['content']['body'][1]['text'] = message

        # Send the Teams notification
        payload = error_card
        response = requests.post(self.webhook_url, json=payload)
        response.raise_for_status()


    def send_info_message(self, title, message):
        self.check_environment()

        # Load ErrorCard.json from Resources folder
        resource = os.path.join(self.resources_folder, 'StandardCard.json') 
        with open(resource, 'r') as file:
            error_card = json.load(file)

        # Customize the error card payload
        error_card['attachments'][0]['content']['body'][0]['text'] = title
        error_card['attachments'][0]['content']['body'][1]['text'] = message

        # Send the Teams notification
        payload = error_card
        response = requests.post(self.webhook_url, json=payload)
        response.raise_for_status()

    