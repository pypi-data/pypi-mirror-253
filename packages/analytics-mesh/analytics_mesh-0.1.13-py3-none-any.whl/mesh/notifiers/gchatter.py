import os

import logging
from json import dumps
from httplib2 import Http

log = logging.getLogger(__name__)

class GChatter(object):
    def __init__(self, webhook_filename=None) -> None:
        """
        :param webhook_filename: The webhook filename pointing to a channel that you want to post a message to
        """
        self.gchatter = log
        self.env = os.environ.get("NODE_ENV", 'dev')
        self.webhook_filename = webhook_filename
        self.message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
        self.http_obj = Http()
        self.webhook = None

        try:
            with open(self.webhook_filename, 'r') as file:
                self.webhook = file.read()
        except (TypeError, FileNotFoundError) as e:
            self.gchatter.error(f'Type or file not found error, using default logger')
            if self.env not in['dev', None]:
                raise e
            
    def notify(self, message):
        if not self.webhook:
            self.gchatter.info(message)
        else:
            self.http_obj.request(uri=self.webhook,
                                method='POST',
                                headers=self.message_headers,
                                body=dumps({'text':message})
                                )
