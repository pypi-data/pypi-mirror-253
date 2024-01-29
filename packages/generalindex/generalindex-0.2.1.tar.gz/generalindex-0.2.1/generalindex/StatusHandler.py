import os
import time

from deprecated import deprecated

from .utils import log
from .HTTPCaller import HTTPCaller


@deprecated(version='0.1.20', reason="You should use trip-task-util package instead")
class StatusHandler:
    '''
    Allows to send statuses to the Status Page of the NorthGravity Application.
    Each status type has a color and a corresponding message.
    - INFO: Blue
    - ERROR: Red
    - WARNING: Orange
    '''

    def __init__(self):
        self.caller = HTTPCaller()

        self.job_id = os.environ.get('JOBID')
        self.eid = os.environ.get('EID')
        self.component_name = os.environ.get('NG_COMPONENT_NAME')
        self.group_name = os.environ.get('NG_STATUS_GROUP_NAME', '')

    def send_status(self, status, message):
        # Set the api call for the status connected to the new log event
        log.debug(f'Send status with status {status} and message {message}')

        payload = {'jobId': self.job_id,
                   'eId': self.eid,
                   'status': status,
                   'message': message,
                   'className': 'python',
                   'groupName': self.group_name,
                   'componentName': self.component_name,
                   'time': time.strftime('%Y-%m-%dT%H:%M:%S'),
                   }

        r = self.caller.post(path="/status", payload=payload, headers={'X-KH-E-ID': self.eid})

        log.debug(f'URL: {r.url} \nHeaders: {r.request.headers} \nPayload: {payload}')

        if r.status_code > 201:
            log.info("Sending status response was: " + str(r.status_code) + " and text " + str(r.text))
            log.info("Sending status response was: " + str(r.status_code) + " and text " + str(r.text))

        return

    def running(self, message):
        self.send_status('RUNNING', message)

    @deprecated(version='0.1.5', reason="You should use running(message) or error(message) function instead.")
    def info(self, message):
        self.send_status('RUNNING', message)

    def error(self, message):
        self.send_status('ERROR', message)

    def warn(self, message):
        self.send_status('WARN', message)
