import os
import logging
from thor.maestro.baton import JobManager

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
log = logging.getLogger(__name__)

# TODO: Should Incident Manager inherit Job manager?
class IncidentManager(JobManager):
    def __init__(self, slack_url="https://hooks.slack.com/services", **kwargs):
        self.slack_url = slack_url
        if len(kwargs):
            # pass everything else to parent
            super().__init__(**kwargs)
        else:
            # use parent default
            super().__init__()

    def notify_owner(self, owner_username, channel_name, text_type, text_message):
        """This function notifies owners by sending them a slack notification."""
        # The function should assemble the payload like the curl command below:
        # curl -X POST --data-urlencode "payload={\"channel\":
        # \"#thor-notifications-testing\", \"username\": \"thor-release-notifications\",
        # \"text\": \"This should be working now :white_check_mark:\",
        # \"icon_emoji\": \":thor2:\"}" https://hooks.slack.com/services/<secret>/<secret>
        log.info(f"notifying owner: {owner_username}")


if __name__ == "__main__":
    jjm = JenkinsJobManager()
    owner_username = ""
    channel_name = ""
    text_type = ""
    text_message = ""

    jjm.notify_owner(owner_username)
