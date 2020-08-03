import os
from pathlib import Path
from slack import WebClient
from slack.errors import SlackApiError


class SlackPost(object):

    def __init__(self):
        self.slack_token = os.getenv('TOKEN')
        self.path = Path(os.path.abspath(os.path.dirname(__file__))).parent

    def send_message(self, message=None):
        try:
            if message:
                client = WebClient(token=self.slack_token)
                client.chat_postMessage(channel="G0170NVNXPX",
                                        text=message)
                return
            client = WebClient(token=self.slack_token)
            client.chat_postMessage(channel="G0170NVNXPX",
                                    text="Task finished! :tada:")
            client.files_upload(
              channels="G0170NVNXPX",
              file="{}/static/details.log".format(self.path),
              title="Log details")
        except SlackApiError as e:
            assert e.response["error"]
