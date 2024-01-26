"""
Starts slack app for Liten and handles events.
"""

import re
import logging
import uuid
import requests

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

import litenai as tenai

class SlackConfig:
    """ 
    Slack config class
    """
    def __init__(self) -> None:
        self.config = tenai.Config()
        self.slack_bot_name = "Liten"
        # Get reused config values
        self.slack_bot_token = self.config.get_config(tenai.Config.SLACK_BOT_TOKEN)
        self.slack_app_token = self.config.get_config(tenai.Config.SLACK_APP_TOKEN)
        self.logger = tenai.Logger("slackapp").logger

class SlackMessage:
    """ 
    Slack message class
    """
    def __init__(self, body, logger) -> None:
        """ 
        Initialize Slack message. Throws exception if any key is missing.
        """
        self._body = body
        self._logger = logger
        self._event = body["event"]
        self._ts = self._event["ts"]
        self._channel = self._event["channel"]
        self._session = self._event["channel"]
        self._user = self._event["user"]
        self._text = self._event["text"]
        self._prompt = self._text
        self._users = []
        self._if_liten_mentioned = False
        self._files = None
        if "files" in self._event.keys():
            self._files = self._event["files"]
        self._parse_text()

    def _parse_text(self):
        """
        Replace all the IDs with the user-name in text
        """
        start = str(re.escape("<@"))
        end = str(re.escape(">"))
        self._users = re.findall(start+"(.*)"+end, self._text)
        
        for user in self._users:
            user_info = app.client.users_info(user=user)
            user_name = user_info['user']['real_name']
            if user_name == config.slack_bot_name:
                self._if_liten_mentioned = True
            self._prompt = self._prompt.replace(f"<@{user}>", f"{user_name}")
        user_info = app.client.users_info(user=self._user)
        user_name = user_info['user']['real_name']
        self._prompt = f"{user_name}: {self._prompt}"

    @property
    def files(self):
        """ 
        Return files property
        """
        return self._files
    
    @property
    def event(self):
        """ 
        Return event property
        """
        return self._event

    @property
    def ts(self):
        """ 
        Return ts property
        """
        return self._ts

    @property
    def user(self):
        """ 
        Return user property
        """
        return self._user
    
    @property
    def text(self):
        """ 
        Return text property
        """
        return self._text
    
    @property
    def prompt(self):
        """
        Return prompt property
        """
        return self._prompt
    
    @property
    def session(self):
        """ 
        Return session property
        """
        return self._session
    
    @property
    def channel(self):
        """ 
        Return channel property
        """
        return self._channel
    
    def channel_type(self):
        """ 
        Return channel_type property
        """
        if 'channel_type' in self._event.keys():
            return self._event['channel_type']
        else:
            return "error_unknown_channel_type"
    
    def if_liten_mentioned(self):
        """ 
        Return if_liten_mentioned property
        """
        return self._if_liten_mentioned
    
    def append_message(self):
        """
        Reply to the message
        """
        # Append the prompt to Liten session
        session_response = tenai.LitenAPI.create_session(self._session, {})
        if session_response[1] != 200:
            self._logger.error(f"Error creating session '{session_response[0]}' body: {self._body}")    
        else:
            response = tenai.LitenAPI.append_user_message(self._session, self._prompt)
            if response[1] != 200:
                self._logger.error(f"Error appending message '{response}' prompt: {self._prompt}")
            else:
                self._logger.info(f"Appended message to session: {self._prompt}")
    
    def reply_message(self):
        """ 
        Reply to the message
        """
        response = ""
        session_response = tenai.LitenAPI.create_session(self._session, {})
        if session_response[1] != 200:
            response = session_response[0]
        else:
            # Send the prompt to Liten
            prompt_response = tenai.LitenAPI.send(self._session, self._prompt)
            if prompt_response[1] != 200:
                response = prompt_response[0]
            else:
                # Respond to the user in the Slack thread
                response = f"<@{self._user}> {prompt_response[0]}"
        return response


config = SlackConfig()
app = App(token = config.slack_bot_token)

def download_file(file_info) -> None:
    """ 
    Download the file TBD Current download is not correct, not downloading the file but some meta info. Need to fix it.
    """
    config.logger.info(f"Downloading file: {file_info}")
    file_url = file_info["url_private"]
    table_name = file_info['name'].split(".")[0].strip()
    file_name = '/tmp/'+ table_name + uuid.uuid4().hex[0:6].upper() + '.csv'
    config.logger.info(f"Downloading file: {file_url} to {file_name} as table {table_name}")
    r = requests.get(file_url, headers={"Authorization" : f"Bearer {config.slack_bot_token}"})
    r.raise_for_status()
    file_data = r.content   # get binary content
    # save file to disk
    with open(file_name , 'w+b') as f:
        f.write(bytearray(file_data))
    config.logger.info(f"Saved {file_name} downloaded from {file_url}")
    return "Read file " + file_info['name'] + " as table " + table_name + ". "

def download_files(files):
    """ 
    Download the files
    """
    response = "Reading files. "
    config.logger.info(f"Downloading files: {files}")
    for file_info in files:
        try:
            response += download_file(file_info=file_info)
        except Exception as exc:
            config.logger.error(f"Error downloading file '{exc} file_info: {file_info}")
            response +=f"Error uploading file with exception {exc}"
    return response

@app.event("app_mention")
def mention_handler(body, say, logger=config.logger):
    """ 
    Handles the app-mention event. Create a new session if one does not exist.
    """
    try:
        logger.info(f"Event app_mention: {body}")
        msg = SlackMessage(body=body, logger=logger)
        if msg.files:
            response = download_files(msg.files)
            say(text=response, thread_ts = msg.ts)
        else:
            say(text=msg.reply_message(), thread_ts = msg.ts)
    except Exception as e:
        logger.error(f"Event app_mention: Error'{e}' for message body: {body}")
        say(text="Error reading message", thread_ts = msg.ts)

@app.event("message")
def handle_message_events(body, logger=config.logger):
    """ 
    Handles the message event
    """
    try:
        logger.info(f"Event message: {body}")
        msg = SlackMessage(body=body, logger=logger)
        # If files are shared, read it
        # Ignore if Liten is mentioned, app_mention event should handle it
        if not msg.if_liten_mentioned():
            if msg.channel_type() == "im":
                if msg.files:
                    response = download_files(msg.files)
                    app.client.chat_postMessage(channel=msg.channel, text=response)
                else:
                    response = msg.reply_message()
                    app.client.chat_postMessage(channel=msg.channel, text=response)
            else:
                msg.append_message()
    except Exception as exc:
        logger.error(f"Event message: Error '{exc}' for body: {body}")
        app.client.chat_postMessage(channel=msg.channel, text="Error reading message")

@app.event("app_home_opened")
def handle_app_home_opened_events(body, logger=config.logger):
    """ 
    Handles the app_home_opened event
    """
    logger.info(f"App Event app_home_opened: {body}")

if __name__ == "__main__":
    handler = SocketModeHandler(app=app, 
                                app_token=config.slack_app_token,
                                logger=config.logger)
    handler.start()