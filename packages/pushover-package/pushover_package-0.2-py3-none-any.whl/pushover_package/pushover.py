import requests

class Pushover:
    def __init__(self, api_token):
        self.api_token = api_token
    
    def send_notification(self, message, user_key, title="", priority=0, retry=30, expire=3600):
        """
        Sends a notification to a user via Pushover.
        :param message: The message to send
        :param title: The title of the message (optional)
        :return: Response from Pushover API
        """
        url = "https://api.pushover.net/1/messages.json"
        data = {
            "token": self.api_token,
            "user": user_key,
            "message": message,
            "title": title
        }
        if priority > 0:
            data["priority"] = priority
            data["retry"] = retry
            data["expire"] = expire
            
        response = requests.post(url, data=data)
        return response