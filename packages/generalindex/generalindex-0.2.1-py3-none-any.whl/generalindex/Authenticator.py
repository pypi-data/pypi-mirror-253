import base64
import os

from .utils import log


class Authenticator:
    def __init__(self):
        self.token = os.getenv('NG_API_AUTHTOKEN')
        self.login = os.getenv('LOGIN')
        self.password = os.getenv('PASSWORD')

    def get_token(self):
        if self.token is not None:
            if self.token.startswith("Bearer") or self.token.startswith("Basic") or self.token.startswith("ApiKey"):
                log.debug('Authentication with Web Token ...')
                return {'Authorization': f'{self.token}'}
            else:
                log.debug('Authentication with Web Token ...')
                return {'Authorization': f'Bearer {self.token}'}

        else:
            if self.login is not None and self.password is not None:
                log.debug('Authentication with Credentials ...')
                credentials = self.login + ":" + self.password
                message_bytes = credentials.encode('ascii')
                base64_enc = base64.b64encode(message_bytes).decode('UTF-8')

                d = {'Authorization': f"Basic {base64_enc}"}
                return d

            else:
                log.error('No login or password provided, neither token can be read from environment variable.')
                raise Exception('Authentication issue : no credentials found')
